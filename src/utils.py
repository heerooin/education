import os
import json
import unittest
from unittest.mock import mock_open, patch

def open_file(file_path: str) -> list:
    """
    Открываем файл по указанному пути и получаем список
    """
    try:
        if not os.path.exists(file_path):
            return []
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError,OSError):
                pass
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
    @patch("builtins.open", new_callable=mock_open)
    def test_file_is_corrupted(self, mock_file, mock_exists):
        """
        Тестируем случай, когда файл повреждён и не может быть прочитан.
        """
        mock_file.side_effect = json.JSONDecodeError("Error", "", 0)
        result = open_file("corrupted_file.json")
        self.assertEqual(result, [])
        mock_exists.assert_called_once_with("corrupted_file.json")
        mock_file.assert_called_once_with("corrupted_file.json", encoding="utf-8")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_file_os_error(self, mock_file, mock_exists):
        """
        Тестируем случай, когда возникает ошибка при открытии файла (например, OSError).
        """
        mock_file.side_effect = OSError("Error")
        result = open_file("os_error_file.json")
        self.assertEqual(result, [])
        mock_exists.assert_called_once_with("os_error_file.json")
        mock_file.assert_called_once_with("os_error_file.json", encoding="utf-8")

if __name__ == "__main__":
    unittest.main()