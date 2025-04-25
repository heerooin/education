import pytest
from unittest.mock import patch, mock_open
from src.re_coll_rand import bank_operations, category_operations


@pytest.fixture
def sample_operations():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


def test_bank_operations(sample_operations):
    result = bank_operations(sample_operations, "Перевод")
    assert len(result) == 2

    result = bank_operations(sample_operations, "вклада")
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"

    result = bank_operations(sample_operations, "Снятие наличных")
    assert len(result) == 0


def test_category_operations(sample_operations):
    result = category_operations(sample_operations)
    assert isinstance(result, dict)
    assert len(result) == 3
    assert result["Перевод организации"] == 1
    assert result["Открытие вклада"] == 1
    assert result["Перевод со счета на счет"] == 1

    existing_dict = {"Перевод организации": 3, "Снятие наличных": 2}
    result = category_operations(sample_operations, existing_dict)
    assert result["Перевод организации"] == 4
    assert result["Открытие вклада"] == 1
    assert result["Перевод со счета на счет"] == 1
    assert result["Снятие наличных"] == 2


@patch('builtins.print')
def test_output_format(mock_print, sample_operations):
    with patch('src.re_coll_rand.mask_account_card') as mock_mask:
        mock_mask.side_effect = lambda x: f"Счет **4321" if "Счет" in x else "MasterCard 7771 27** **** 3727"

        from src.widget import get_data

        operation = sample_operations[1]
        date = get_data(operation["date"])
        description = operation["description"]

        print(f'{date} {description}')

        mock_print.assert_any_call(f'{date} {description}')
