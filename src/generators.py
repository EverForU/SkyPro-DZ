from typing import Iterator, Dict, Any

transactions = [
    {
        "id": 1,
        "operationAmount": {
            "amount": "100.50",
            "currency": {
                "name": "Доллар",
                "code": "USD"
            }
        },
        "description": "Покупка в магазине"
    },
    {
        "id": 2,
        "operationAmount": {
            "amount": "5000.00",
            "currency": {
                "name": "Рубль",
                "code": "RUB"
            }
        },
        "description": "Перевод другу"
    },
    {
        "id": 3,
        "operationAmount": {
            "amount": "75.20",
            "currency": {
                "name": "Доллар",
                "code": "USD"
            }
        },
        "description": "Оплата подписки"
    },
    {
        "id": 4,
        "operationAmount": {
            "amount": "200.00",
            "currency": {
                "name": "Евро",
                "code": "EUR"
            }
        },
        "description": "Билет в музей"
    }
]


def filter_by_currency(transactions_usd: list[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """Генератор по коду - USD"""
    for usd in transactions_usd:
        try:
            if usd["operationAmount"]["currency"]["code"] == currency_code:
                yield usd

        except (TypeError, KeyError, AttributeError) as error:
            print(f"Ошибка в транзакции {usd}: - {error}")
            continue





def transaction_descriptions(description: list) -> Iterator:
    """Генератор операций"""
    for operation in description:
        if "description" in operation:
            yield operation["description"]


def card_number_generator(start: int, end: int) -> Iterator:
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        card = str(number)

        while len(card) < 16:
            card = "0" + card
        result = card[0:4] + " " + card[4:8] + " " + card[8:12] + " " + card[12:16]

        yield result


if __name__ == "__main__":

    transaction = filter_by_currency(transactions, "USD")
    for x in range(2):
        print(next(transaction))

    descriptions = transaction_descriptions(transactions)
    for x in range(4):
        print(next(descriptions))

print("\nНомера карт (1-5):")
for card in card_number_generator(1, 5):
    print(card)