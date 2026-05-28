import pytest

from src.widget import get_date_main, mask_account_card


@pytest.mark.parametrize(
    "info,expected",
    [
        ("Счёт 12345678901234567890", "Счёт **7890"),
        ("Счёт 15245695", "Не верно указан номер или счёт."),
        ("12345678901234567890", "**7890"),
        ("MasterCard 9876545566991235", "MasterCard 9876 54** **** 1235"),
        ("9876545566991235", "9876 54** **** 1235"),
        ("MasterCard 9876545565", "Не верно указан номер или счёт."),
        ("MasterCard 9876 5455 65", "Не верно указан номер или счёт."),
    ],
)
def test_mask_account_card(info, expected):
    """Проверка параметризацией"""
    assert mask_account_card(info) == expected


def test_get_date_full():
    """Проверка даты в начальном формате."""
    result = get_date_main("2026-04-24T02:26:18.671407")
    assert result == "24.04.2026"


def test_get_date_slash():
    """Проверка даты через слэш"""
    result = get_date_main("2026/08/22T02:26:")
    assert result == "22.08.2026"


def test_get_date_space():
    """Проверка даты через пробел"""
    result = get_date_main("2026 08 22T02:26:18.6714")
    assert result == "22.08.2026"
