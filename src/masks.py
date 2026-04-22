def get_mask_card_number(number_card: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX."""
    encrypted_card = []

    if len(number_card) != 16 or not number_card.isdigit():
        return "Номер карты должен содержать 16 цифр"

    encrypted_card.append(number_card[0:4])
    encrypted_card.append(" ")
    encrypted_card.append(number_card[4:6])
    encrypted_card.append("**")
    encrypted_card.append(" ")
    encrypted_card.append("****")
    encrypted_card.append(" ")
    encrypted_card.append(number_card[-4:])

    return "".join(encrypted_card)


def get_mask_account(account: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    encrypted_account = []

    if not account.isdigit() or len(account) < 4 :
        return "Номер счета должен состоять только из цифр и содержать минимум 4 цифры"

    encrypted_account.append("**")
    encrypted_account.append(account[-4:])

    return "".join(encrypted_account)
