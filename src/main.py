from src.widget import mask_account_card

def main() -> None:
    card = "1234567812345678"
    account = "12345678901234567890"

    print(mask_account_card(card))



if __name__ == "__main__":
    main()
