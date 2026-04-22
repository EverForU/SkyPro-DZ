from src.masks import get_date, mask_account_card


def main() -> None:
    card = "Maestro 7000792289606361"
    account = "Счет 73654108430135874305"

    print(mask_account_card(account))
    print(mask_account_card(card))
    print(get_date("2024-03-11T02:26:18.671407"))


if __name__ == "__main__":
    main()
