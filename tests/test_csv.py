from unittest.mock import mock_open, patch
from src.csv_and_pandas import csv_open, xlsx_open


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
