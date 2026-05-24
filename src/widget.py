from src.masks import get_date, get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Получает данные пользователя и шифрует карту или номер счёта"""
    if info.isdigit():
        number = info
        if len(number) == 16:
            masked = get_mask_card_number(number)

        elif len(number) == 20:
            masked = get_mask_account(number)

        else:
            return "Не верно указан номер или счёт."

        return f"{masked}"

    else:
        parts = info.rsplit(" ", 1)

        if len(parts) == 2:
            name, number = parts

        if len(number) == 16:
            masked = get_mask_card_number(number)

        elif len(number) == 20:
            masked = get_mask_account(number)

        else:
            return "Не верно указан номер или счёт."

        return f"{name} {masked}"


def get_date_main(info: str) -> str:
    return get_date(info)


def main() -> None:
    print(mask_account_card("Счёт 12345678901234567890"))
    print(mask_account_card("MasterCard 9876545566991235"))
    print(get_date_main("2026-04-24T02:26:18.671407"))


if __name__ == "__main__":
    main()
