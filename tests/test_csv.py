import unittest
from unittest.mock import patch
import pandas as pd
from src import csv_and_pandas


@patch('pd.read_excel')
def test_csv_open_success(self, mock_csv_reader, mock_file):
    """Тест успешного чтения CSV"""
    mock_csv_reader.return_value = [{"id": "650703",
                                     "state": "EXECUTED",
                                     "date": "2023-09-05T11:30:32Z",
                                     "amount": "16210",
                                     "currency_name": "Sol",
                                     "currency_code": "PEN",
                                     "from": "Счет 58803664561298323391",
                                     "to": "Счет 39745660563456619397",
                                     "description": "Перевод организации"}]
    result = csv_and_pandas.csv_open("transactions.csv")
    self.assertEqual(result, [{"id": "650703",
                                     "state": "EXECUTED",
                                     "date": "2023-09-05T11:30:32Z",
                                     "amount": "16210",
                                     "currency_name": "Sol",
                                     "currency_code": "PEN",
                                     "from": "Счет 58803664561298323391",
                                     "to": "Счет 39745660563456619397",
                                     "description": "Перевод организации"}])
    mock_file.assert_called_once_with("transactions.csv", mode="r", encoding="utf-8")


@patch('pd.read_excel')
def test_xlsx_open_success(self, mock_csv_reader, mock_file):
    """Тест успешного чтения xlsx"""
    mock_read_excel.return_value = pd.DataFrame = [{"id": "650703",
                                                    "state": "EXECUTED",
                                                    "date": "2023-09-05T11:30:32Z",
                                                    "amount": "16210",
                                                    "currency_name": "Sol",
                                                    "currency_code": "PEN",
                                                    "from": "Счет 58803664561298323391",
                                                    "to": "Счет 39745660563456619397",
                                                    "description": "Перевод организации"}]
    result = csv_and_pandas.xlsx_open("transactions_excel.xlsx")
    self.assertEqual(result, [{"id": "650703",
                                     "state": "EXECUTED",
                                     "date": "2023-09-05T11:30:32Z",
                                     "amount": "16210",
                                     "currency_name": "Sol",
                                     "currency_code": "PEN",
                                     "from": "Счет 58803664561298323391",
                                     "to": "Счет 39745660563456619397",
                                     "description": "Перевод организации"}])
    mock_read_excel.assert_called_once_with("transactions_excel.xlsx", sheet_name="Sheet1", dtype=str)


@patch("os.path.exists", return_value=False)
def test_csv_open_file_not_found(self, mock_exists):
    """Тест ошибки: файл CSV не найден"""
    result = csv_and_pandas.csv_open("transactions.csv")
    self.assertEqual(result, [])


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_xlsx_open_file_not_found(self, mock_read_excel):
    """Тест ошибки: файл Excel не найден"""
    result = csv_and_pandas.xlsx_open("transactions_excel.xlsx")
    self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
