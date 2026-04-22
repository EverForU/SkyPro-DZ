def mask_account_card(account: str) -> str:

    encrypted_account = []

    for char in account:
        if char.isdigit():
            encrypted_account.append(char)

    if len("".join(encrypted_account)) == 20:
        return "".join(filter(str.isdigit,encrypted_account))

    if len("".join(encrypted_account)) == 16:
        return "".join(filter(str.isdigit,encrypted_account))

    return print(encrypted_account)
    # y = "".join(x)