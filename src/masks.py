def get_mask_card_number(number_card: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX."""
    encrypted_card = []

    for symbol in number_card:
        if symbol.isdigit():
            encrypted_card.append(symbol)

    if len("".join(encrypted_card)) != 16:
        return "Не верно введён номер карты."

    return f"{"".join(encrypted_card[0:4])} {"".join(encrypted_card[5:7])}** **** {"".join(encrypted_card[-4:])}"


def get_mask_account(account: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    encrypted_account = []

    for symbol in account:
        if symbol.isdigit():
            encrypted_account.append(symbol)

    if len("".join(encrypted_account)) != 20:
        return "Номер счета должен состоять 20 цифр."

    return f"**{"".join(encrypted_account[-4:])}"


def get_date(date: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ."""

    year, month, day = date[0:10].split("-")

    return f"{day}.{month}.{year}"
