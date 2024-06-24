from src.masks import get_mask_account
from src.masks import get_mask_card_number
from datetime import datetime


def mask_account_card(cards_number: str) -> str:
    """Функция маскировки номера карты и счета"""
    if "Счет" in cards_number:
        mask_account = f"Счет {get_mask_account(cards_number[:])}"
        return mask_account
    else:
        card = get_mask_card_number(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], card)
        return mask_card


def get_data(data: str) -> str:
    """Функция возвращения даты"""
    d = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return d.strftime("%d.%m.%y")


if __name__=='__main__':
    print(mask_account_card("Visa Platinum 8990922113665229"))
