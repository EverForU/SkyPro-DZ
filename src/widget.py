def mask_account_card(account: str) -> str:

    encrypted_account = []

    for char in account:
        if char.isdigit():
            encrypted_account.append(char)

    if len("".join(encrypted_account)) == 20:
        return "".join(filter(str.isdigit,encrypted_account))

    elif len("".join(encrypted_account)) == 16:
        return "".join(filter(str.isdigit,encrypted_account))

    else:
        return "Не верно введён номер счёта или карты!"

    return print(encrypted_account)
    # y = "".join(x)