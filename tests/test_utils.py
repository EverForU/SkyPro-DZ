from unittest.mock import mock_open, patch
from src.utils import read_json_file


def test_read_json_file_success():
    """Тест успешного чтения файла."""
    mock_data = '[{"id": 1, "amount": 100}]'

    with patch('builtins.open', mock_open(read_data=mock_data)):
        result = read_json_file('any.json')

    assert len(result) == 1
    assert result[0]['id'] == 1


def test_read_json_file_not_found():
    """Тест если файл не найден."""
    with patch('builtins.open', side_effect=FileNotFoundError()):
        result = read_json_file('not_exist.json')

    assert result == []


def test_read_json_file_invalid():
    """Тест если JSON неверный."""
    with patch('builtins.open', mock_open(read_data='not json')):
        result = read_json_file('bad.json')

    assert result == []


def test_read_json_file_with_dict_instead_list():
    """Тест когда JSON содержит не список, а словарь."""
    with patch('builtins.open', mock_open(read_data='{"key": "value"}')):
        result = read_json_file('test.json')
        assert result == []