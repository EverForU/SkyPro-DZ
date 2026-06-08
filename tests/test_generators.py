from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_EUR(transactions_usd):
    """Фильтрация по валюте EUR"""
    result = filter_by_currency(transactions_usd, "EUR")
    result_list = list(result)

    assert len(result_list) == 1


def test_filter_by_currency_RUB(transactions_usd):
    """Фильтрация по валюте RUB"""
    result = filter_by_currency(transactions_usd, "RUB")
    result_list = list(result)

    assert len(result_list) == 1


def test_filter_by_currency_key_error():
    """Отсутствует ключ 'operationAmount' (KeyError)"""
    transactions = [{"id": 1, "something": "else"}, {"id": 2, "operationAmount": {"currency": {"code": "USD"}}}]

    result = filter_by_currency(transactions, "USD")
    result_list = list(result)

    assert len(result_list) == 1
    assert result_list[0]["id"] == 2


def test_transaction_descriptions(transactions_usd):
    """Ожидаем возвращение итератора по операции"""
    transactions = [{"description": "Покупка"}, {"description": "Перевод"}, {"description": "Оплата"}]
    descriptions = transaction_descriptions(transactions)

    assert next(descriptions) == "Покупка"
    assert next(descriptions) == "Перевод"
    assert next(descriptions) == "Оплата"


def test_card_number_generator_ten_to_twelve():
    """Тест: генерация номеров от 5 до 10"""
    result = card_number_generator(5, 10)
    result_list = list(result)

    assert result_list[0] == "0000 0000 0000 0005"
    assert result_list[1] == "0000 0000 0000 0006"
    assert result_list[2] == "0000 0000 0000 0007"


def test_card_number_generator_big_number():
    """Тест: генерация большого номера"""
    result = card_number_generator(999999999995, 999999999999)
    result_list = list(result)

    assert result_list[0] == "0000 9999 9999 9995"
    assert result_list[1] == "0000 9999 9999 9996"
    assert result_list[2] == "0000 9999 9999 9997"
    assert result_list[3] == "0000 9999 9999 9998"
    assert result_list[4] == "0000 9999 9999 9999"


def test_card_number_generator_single_number():
    """Тест: одно число (start = end)"""
    result = card_number_generator(42, 42)
    result_list = list(result)

    assert len(result_list) == 1
    assert result_list[0] == "0000 0000 0000 0042"


def test_transaction_descriptions_empty():
    """Тест: пустой список"""
    transactions = []
    result = transaction_descriptions(transactions)
    assert list(result) == []
