import unittest
from unittest.mock import mock_open, patch
from utils import open_file

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