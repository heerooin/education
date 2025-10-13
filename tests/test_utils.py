from unittest.mock import mock_open, patch
from src.utils import open_file


@patch("os.path.exists", return_value=False)
def test_file_not_exists(mock_exists):
    """Тестируем случай, когда файл не существует."""
    result = open_file("non_existent_file.json")
    assert result == []
    mock_exists.assert_called_once_with("non_existent_file.json")


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
def test_file_contains_valid_list(mock_file, mock_exists):
    """Тестируем случай, когда файл существует и содержит список."""
    result = open_file("valid_file.json")
    assert result == [{"key": "value"}]
    mock_exists.assert_called_once_with("valid_file.json")
    mock_file.assert_called_once_with("valid_file.json", encoding="utf-8")
