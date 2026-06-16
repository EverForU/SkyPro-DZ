import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

log_file_path = os.path.join("logs", "utils.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

file_handler.setFormatter(file_formatter)

utils_logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX."""
    utils_logger.debug(f"Попытка маскировки номера карты: {number_card[:4]}...")

    encrypted_card = []

    for symbol in number_card:
        if symbol.isdigit():
            encrypted_card.append(symbol)

    if len("".join(encrypted_card)) != 16:
        utils_logger.error(f"Неверная длина номера карты: {len(''.join(encrypted_card))} цифр, ожидалось 16")
        return "Не верно введён номер карты."

    masked_card = (
        f"{''.join(encrypted_card[0:4])} {''.join(encrypted_card[4:6])}** **** {''.join(encrypted_card[-4:])}"
    )
    utils_logger.info(f"Номер карты успешно замаскирован: {masked_card}")
    return masked_card


def get_mask_account(account: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    utils_logger.debug(f"Попытка маскировки номера счета: ...{account[-4:] if len(account) >= 4 else account}")

    encrypted_account = []

    for symbol in account:
        if symbol.isdigit():
            encrypted_account.append(symbol)

    if len("".join(encrypted_account)) != 20:
        utils_logger.error(f"Неверная длина номера счета: {len(''.join(encrypted_account))} цифр, ожидалось 20")
        return "Номер счета должен состоять из 20 цифр."

    masked_account = f"**{''.join(encrypted_account[-4:])}"
    utils_logger.info(f"Номер счета успешно замаскирован: {masked_account}")
    return masked_account


def get_date(date: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ."""
    utils_logger.debug(f"Попытка форматирования даты: {date}")

    try:
        date_part = date[0:10].replace(".", "-").replace("/", "-").replace(" ", "-")
        year, month, day = date_part.split("-")

        formatted_date = f"{day}.{month}.{year}"
        utils_logger.info(f"Дата успешно отформатирована: {date} -> {formatted_date}")
        return formatted_date

    except Exception as e:
        utils_logger.error(f"Ошибка при форматировании даты '{date}': {str(e)}")
        raise
