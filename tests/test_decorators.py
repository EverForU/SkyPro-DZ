import pytest

from src.decorators import log


def test_log_to_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5

    captured = capsys.readouterr()

    assert "Начало выполнения функции 'add'" in captured.out
    assert "Функция 'add' успешно завершена. Результат: 5" in captured.out


def test_log_to_console_exception(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "Начало выполнения функции 'divide'" in captured.out
    assert "Ошибка в функции 'divide'" in captured.out


def test_log_to_file_success(tmp_path):
    log_file = tmp_path / "test.log"

    @log(str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)

    assert result == 20

    content = log_file.read_text(encoding="utf-8")

    assert "Начало выполнения функции 'multiply'" in content
    assert "Функция 'multiply' успешно завершена. Результат: 20" in content


def test_log_to_file_exception(tmp_path):
    log_file = tmp_path / "test.log"

    @log(str(log_file))
    def fail():
        raise ValueError("test error")

    with pytest.raises(ValueError, match="test error"):
        fail()

    content = log_file.read_text(encoding="utf-8")

    assert "Начало выполнения функции 'fail'" in content
    assert "Ошибка в функции 'fail': test error" in content


def test_wraps_preserves_function_name():
    @log()
    def my_function():
        pass

    assert my_function.__name__ == "my_function"
