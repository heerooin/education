import pytest
from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize('x, expected',[('7000792289606361', '7000 79 ** **** 6361')])
def test_get_mask_card_number(x,expected):
    assert get_mask_card_number(x) == expected
    assert get_mask_card_number('0') is None
    assert get_mask_card_number('') is None


@pytest.mark.parametrize('x, expected',[('73654108430135874305', '**4305')])
def test_get_mask_account(x, expected):
    assert get_mask_account(x) == expected
    assert get_mask_account('0') is None
    assert get_mask_account('') is None
