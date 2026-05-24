import pytest

from src.masks import get_date, get_mask_account, get_mask_card_number


def test_standard_card(card_result):
    """Стандартный номер карты без пробелов"""
    result = get_mask_card_number("1234567890123456")
    assert result == card_result


def test_card_with_spaces(card_result):
    """Номер карты с пробелами"""
    result = get_mask_card_number("1234 5678 9012 3456")
    assert result == card_result


def test_card_with_text(card_result):
    """Номер карты с текстом — фильтрует только цифры"""
    result = get_mask_card_number("Visa 1234567890123456 !!!")
    assert result == card_result


def test_card_with_different_format(card_result):
    """Номер карты в другом формате"""
    result = get_mask_card_number("1234-5678-9012-3456")
    assert result == card_result


def test_card_short_number():
    """Номер карты короче 16 цифр"""
    result = get_mask_card_number("123456789012")
    assert result == "Не верно введён номер карты."


def test_empty_string():
    """Пустая строка"""
    result = get_mask_card_number("")
    assert result == "Не верно введён номер карты."


@pytest.mark.parametrize(
    "info,expected",
    [
        ("Счёт 12345678901234567890", "**7890"),
        ("Счёт 15245695", "Номер счета должен состоять из 20 цифр."),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(info, expected):
    """Проверка параметризацией"""
    assert get_mask_account(info) == expected


def test_get_date():
    """Преобразование даты"""
    result = get_date("2026-04-24T02:26:18.671407")
    assert result == "24.04.2026"
