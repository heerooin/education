from unittest.mock import patch
import pandas as pd
from src.csv_and_pandas import xlsx_open


@patch("pandas.read_excel")
def test_xlsx_open_success(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([{
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации"
    }])
    result = xlsx_open("transactions_excel.xlsx")
    assert result == [{
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации"
    }]


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_xlsx_open_file_not_found(mock_read_excel):
    result = xlsx_open("transactions_excel.xlsx")
    assert result == []
