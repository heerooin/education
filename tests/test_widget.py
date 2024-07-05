import pytest
from src.widget import mask_account_card
from src.widget import get_dat


def test_mask_account_card():
    assert test_mask_account_card('Счет 73654108430135874305') == *123*4305
    assert test_mask_account_card('0') == None


def test_get_data():
    pass


