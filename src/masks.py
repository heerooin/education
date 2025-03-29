import logging
from typing import Optional

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
log_file = "D:/Programming/pyCharm/pyCharmProjects/pythonProject1/logs/masks.log"
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card: str) -> Optional[str]:
    """Функция маскировки номера карты"""
    if card.isdigit() and len(card) == 16:
        masked_card = f"{card[:4]} {card[4:6]}** **** {card[-4:]}"
        logger.info(f"Маскировка номера карты выполнена успешно: {masked_card}")
        return masked_card
    logger.error(f"Ошибка маскировки номера карты: некорректный ввод ({card})")
    return None


def get_mask_account(acc: str) -> Optional[str]:
    """Функция маскировки номера счета"""
    if acc.isdigit() and len(acc) == 20:
        masked_acc = f"****{acc[-4:]}"
        logger.info(f"Маскировка номера счета выполнена успешно: {masked_acc}")
        return masked_acc
    logger.error(f"Ошибка маскировки номера счета: некорректный ввод ({acc})")
    return None
