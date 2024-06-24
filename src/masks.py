def get_mask_card_number(card: str) -> str | None:
    """Функция маскировки номера карты"""
    if card.isdigit() and len(card) == 16:
        return f"{card[:4]} {card[4:6]} ** **** {card[12:16]}"
    else:
        return None


def get_mask_account(acc: str) -> str | None:
    """Функция маскировки номера счета"""
    if acc.isdigit() and len(acc) == 20:
        return f"**{acc[16:20]}"
    else:
        return None


print(get_mask_card_number(input()))
print(get_mask_card_number(input()))
