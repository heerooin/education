from src.masks import get_mask_account
from datetime import datetime


def mask_account_card(cards_number: str) -> str:
    """Функция маскировки номера карты и счета"""
    if "Счет" in cards_number:
        mask_account = f"Счет {get_mask_account(cards_number[5:])}"
        return mask_account
    if "Visa Platinum" in cards_number:
        mask_account = f"Visa Platinum {cards_number[-16:-12]} {cards_number[-12:-10]}** **** {cards_number[-4:]}"
        return mask_account
    if "Maestro" in cards_number:
        mask_account = f"Maestro {cards_number[-16:-12]} {cards_number[-12:-10]}** **** {cards_number[-4:]}"
        return mask_account
    else:
        return None


def get_data(data: str) -> str:
    """Функция возвращения даты"""
    d = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return d.strftime("%d.%m.%Y")


if __name__ == '__main__':
    print(mask_account_card("Visa Platinum 8990922113665229"))
