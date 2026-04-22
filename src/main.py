from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    card = "1234567812345678"
    account = "12345678901234567890"

    print(get_mask_card_number(card))
    print(get_mask_account(account))


if __name__ == "__main__":
    main()
