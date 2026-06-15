"""
Модуль для работы с внешним API конвертации валют.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(transaction):
    """
    Конвертирует сумму транзакции в рубли.
    """
    # Берём сумму и валюту из транзакции
    operation_amount = transaction.get('operationAmount', {})

    # Получаем сумму (она в виде строки)
    amount_str = operation_amount.get('amount', '0')
    amount = float(amount_str)  # Превращаем строку в число

    # Получаем код валюты
    currency_info = operation_amount.get('currency', {})
    currency = currency_info.get('code', 'RUB')

    # Если рубли - просто возвращаем сумму
    if currency == 'RUB':
        return amount

    # Если доллары или евро - конвертируем
    if currency in ['USD', 'EUR']:
        try:
            rate = get_exchange_rate(currency)
            result = amount * rate
            return round(result, 2)
        except:
            print(f"Не удалось сконвертировать {currency}, возвращаю исходную сумму")
            return amount

    print(f"Валюта {currency} не поддерживается")
    return amount


def get_exchange_rate(currency):
    """
    Получает курс валюты к рублю.
    """
    api_key = os.getenv('EXCHANGE_API_KEY')

    # Если нет ключа - используем примерные курсы для теста
    if not api_key:
        print("ВНИМАНИЕ: Нет API ключа, использую примерные курсы")
        if currency == 'USD':
            return 90.0
        if currency == 'EUR':
            return 98.0

    # Если ключ есть - идём в API
    url = f"https://api.apilayer.com/exchangerates_data/convert"

    params = {
        'from': currency,
        'to': 'RUB',
        'amount': 1
    }

    headers = {
        'apikey': api_key
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if data.get('success'):
            return data.get('result')
        else:
            raise Exception("API ошибка")

    except:
        print(f"Ошибка при запросе курса {currency}")
        return 90.0 if currency == 'USD' else 98.0