import pytest
from src.widget import mask_account_card
from src.widget import get_data


@pytest.mark.parametrize('x, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                         ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
                                         ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(x, expected):
    assert mask_account_card(x) == expected
    assert mask_account_card(x) == expected
    assert mask_account_card(x) == expected
    assert mask_account_card('') is None
    assert mask_account_card('00') is None


@pytest.mark.parametrize('x, expected', [('2024-03-11T02:26:18.671407', '11.03.2024')])
def test_get_data(x, expected):
    assert get_data(x) == expected
