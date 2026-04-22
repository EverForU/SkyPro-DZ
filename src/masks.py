def mask_account_card(account: str) -> str:
    """Маскирует номер банковской карты или счёта."""
    encrypted_input = []

    for char in account:
        if char.isdigit():
            encrypted_input.append(char)

    if len("".join(encrypted_input)) == 20:  # Маскирует номер счёта.

        encrypted_account = "".join(encrypted_input)
        return f"**{"".join(filter(str.isdigit, encrypted_account))[0:4]}"

    elif len("".join(encrypted_input)) == 16:  # Маскирует номер карты.
        encrypted_card = "".join(encrypted_input)
        return f"{encrypted_card[0:4]} {encrypted_card[4:6]}** **** {encrypted_card[-4:]}"

    else:  # При ошибке.
        return "Не верно введён номер счёта или карты!"


def get_date(date: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ."""

    year, month, day = date[0:10].split("-")

    return f"{day}.{month}.{year}"
