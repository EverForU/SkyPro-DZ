from unittest.mock import patch, Mock
from src.external_api import convert_to_rubles, get_exchange_rate


def test_convert_to_rubles_rub():
    """Тест конвертации RUB (без конвертации)."""
    transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}}
    result = convert_to_rubles(transaction)
    assert result == 1000.00
    assert isinstance(result, float)


def test_convert_to_rubles_usd_without_api_key():
    """Тест конвертации USD когда нет API ключа (используется примерный курс)."""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("src.external_api.get_exchange_rate", return_value=90.0):
        result = convert_to_rubles(transaction)
        expected = 100.00 * 90.0
        assert result == expected


def test_convert_to_rubles_eur_without_api_key():
    """Тест конвертации EUR когда нет API ключа (используется примерный курс)."""
    transaction = {"operationAmount": {"amount": "50.00", "currency": {"code": "EUR"}}}

    with patch("src.external_api.get_exchange_rate", return_value=98.0):
        result = convert_to_rubles(transaction)
        expected = 50.00 * 98.0
        assert result == expected


def test_convert_to_rubles_unknown_currency():
    """Тест с неизвестной валютой (GBP)."""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "GBP"}}}

    result = convert_to_rubles(transaction)
    assert result == 100.0


def test_convert_to_rubles_no_currency_field():
    """Тест когда в транзакции нет поля currency."""
    transaction = {"operationAmount": {"amount": "100"}}

    result = convert_to_rubles(transaction)
    assert result == 100.0


def test_convert_to_rubles_empty_transaction():
    """Тест с пустой транзакцией."""
    transaction = {}

    result = convert_to_rubles(transaction)
    assert result == 0.0


def test_convert_to_rubles_string_amount():
    """Тест что сумма правильно конвертируется из строки в число."""
    transaction = {"operationAmount": {"amount": "99.99", "currency": {"code": "RUB"}}}

    result = convert_to_rubles(transaction)
    assert result == 99.99
    assert isinstance(result, float)


def test_convert_to_rubles_rounding():
    """Тест округления до 2 знаков после запятой."""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    with patch("src.external_api.get_exchange_rate", return_value=90.5555):
        result = convert_to_rubles(transaction)
        expected = 100.00 * 90.5555
        expected_rounded = round(expected, 2)
        assert result == expected_rounded


def test_convert_to_rubles_api_error_fallback():
    """Тест когда API возвращает ошибку, используется fallback курс."""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    with patch("src.external_api.get_exchange_rate", side_effect=Exception("API error")):
        result = convert_to_rubles(transaction)
        # При ошибке возвращается исходная сумма
        assert result == 100.0


def test_get_exchange_rate_no_api_key_usd():
    """Тест получения курса USD без API ключа."""
    with patch("os.getenv", return_value=None):
        with patch("src.external_api.load_dotenv"):
            result = get_exchange_rate("USD")
            assert result == 90.0


def test_get_exchange_rate_no_api_key_eur():
    """Тест получения курса EUR без API ключа."""
    with patch("os.getenv", return_value=None):
        with patch("src.external_api.load_dotenv"):
            result = get_exchange_rate("EUR")
            assert result == 98.0


def test_get_exchange_rate_with_api_key_success():
    """Тест успешного получения курса с API ключом."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": 92.75}

    with patch("requests.get", return_value=mock_response):
        with patch("os.getenv", return_value="fake_api_key_123"):
            result = get_exchange_rate("USD")
            assert result == 92.75


def test_get_exchange_rate_api_returns_failure():
    """Тест когда API возвращает success=False."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": False, "error": {"info": "Invalid API key"}}

    with patch("requests.get", return_value=mock_response):
        with patch("os.getenv", return_value="invalid_key"):
            result = get_exchange_rate("USD")
            # При ошибке API возвращается fallback курс
            assert result == 90.0


def test_get_exchange_rate_eur_with_api_fallback():
    """Тест получения курса EUR с fallback при ошибке API."""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.side_effect = Exception("Server error")

    with patch("requests.get", return_value=mock_response):
        with patch("os.getenv", return_value="fake_key"):
            result = get_exchange_rate("EUR")
            assert result == 98.0


def test_get_exchange_rate_usd_with_api_and_json_error():
    """Тест когда API возвращает некорректный JSON."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")

    with patch("requests.get", return_value=mock_response):
        with patch("os.getenv", return_value="fake_key"):
            result = get_exchange_rate("USD")
            assert result == 90.0


def test_convert_to_rubles_usd_real_api_flow():
    """Интеграционный тест: конвертация USD с моком API."""
    transaction = {"operationAmount": {"amount": "150.00", "currency": {"code": "USD"}}}

    # Мокаем get_exchange_rate чтобы вернул определённый курс
    with patch("src.external_api.get_exchange_rate", return_value=91.25):
        result = convert_to_rubles(transaction)
        expected = 150.00 * 91.25
        assert result == round(expected, 2)


def test_convert_to_rubles_eur_real_api_flow():
    """Интеграционный тест: конвертация EUR с моком API."""
    transaction = {"operationAmount": {"amount": "75.50", "currency": {"code": "EUR"}}}

    with patch("src.external_api.get_exchange_rate", return_value=99.50):
        result = convert_to_rubles(transaction)
        expected = 75.50 * 99.50
        assert result == round(expected, 2)


def test_get_exchange_rate_api_called_with_correct_params():
    """Тест что API вызывается с правильными параметрами."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": 90.0}

    with patch("requests.get", return_value=mock_response) as mock_get:
        with patch("os.getenv", return_value="test_key"):
            get_exchange_rate("USD")

            # Проверяем что запрос сделан с правильными параметрами
            mock_get.assert_called_once()
            args, kwargs = mock_get.call_args
            assert kwargs["params"]["from"] == "USD"
            assert kwargs["params"]["to"] == "RUB"
            assert kwargs["params"]["amount"] == 1
            assert kwargs["headers"]["apikey"] == "test_key"
