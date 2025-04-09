import json
import logging
import os
import unittest
from unittest.mock import mock_open, patch

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
log_file = "../logs/utils.log"
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_file(file_path: str) -> list:
    """
    Открываем файл по указанному пути и получаем список.
    """
    try:
        logger.info(f"Попытка открыть файл: {file_path}")

        if not os.path.exists(file_path):
            logger.warning(f"Файл {file_path} не найден.")
            return []

        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно прочитан. Количество записей: {len(data)}")
                return data

            logger.warning(f"Файл {file_path} содержит некорректные данные (не список).")
            return []

    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}")
        return []


class TestOpenFile(unittest.TestCase):
    @patch("os.path.exists", return_value=False)
    def test_file_not_exists(self, mock_exists):
        """
        Тестируем случай, когда файл не существует.
        """
        result = open_file("non_existent_file.json")
        self.assertEqual(result, [])
        mock_exists.assert_called_once_with("non_existent_file.json")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
    def test_file_contains_valid_list(self, mock_file, mock_exists):
        """
        Тестируем случай, когда файл существует и содержит список.
        """
        result = open_file("valid_file.json")
        self.assertEqual(result, [{"key": "value"}])
        mock_exists.assert_called_once_with("valid_file.json")
        mock_file.assert_called_once_with("valid_file.json", encoding="utf-8")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='{invalid json}')
    @patch("json.load", side_effect=json.JSONDecodeError("Error", "", 0))
    def test_file_is_corrupted(self, mock_json_load, mock_file, mock_exists):
        """
        Тестируем случай, когда файл повреждён и не может быть прочитан.
        """
        result = open_file("corrupted_file.json")
        self.assertEqual(result, [])
        mock_exists.assert_called_once_with("corrupted_file.json")
        mock_file.assert_called_once_with("corrupted_file.json", encoding="utf-8")
        mock_json_load.assert_called_once()


if __name__ == "__main__":
    unittest.main()
