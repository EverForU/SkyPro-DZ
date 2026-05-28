import pytest


@pytest.fixture
def card_result():
    return "1234 56** **** 3456"


@pytest.fixture
def transactions_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_usd():
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100.50", "currency": {"name": "Доллар", "code": "USD"}},
            "description": "Покупка в магазине",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "5000.00", "currency": {"name": "Рубль", "code": "RUB"}},
            "description": "Перевод другу",
        },
        {
            "id": 3,
            "operationAmount": {"amount": "75.20", "currency": {"name": "Доллар", "code": "USD"}},
            "description": "Оплата подписки",
        },
        {
            "id": 4,
            "operationAmount": {"amount": "200.00", "currency": {"name": "Евро", "code": "EUR"}},
            "description": "Билет в музей",
        },
    ]
