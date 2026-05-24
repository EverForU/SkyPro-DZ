from src.processing import filter_by_state, sort_by_date


def test_filter_executed(transactions_dict):
    """Фильтрация по состоянию EXECUTED"""
    result = filter_by_state(transactions_dict, "EXECUTED")
    assert result == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_canceled(transactions_dict):
    """Фильтрация по состоянию CANCELED"""
    result = filter_by_state(transactions_dict, "CANCELED")
    assert result == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_descending(transactions_dict):
    """Сортировка по убыванию (по умолчанию)"""
    result = sort_by_date(transactions_dict)
    assert result == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_ascending(transactions_dict):
    """Сортировка по возрастанию"""
    result = sort_by_date(transactions_dict, reverse=False)
    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert result == expected
