import functools


def log(filename=None):
    """Декоратор для логирования выполнения функций"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            func_name = func.__name__

            start_msg = f"Начало выполнения функции '{func_name}'"

            if filename:
                # Запись в файл
                file = open(filename, "a", encoding="utf-8")
                file.write(start_msg + "\n")
            else:
                # Вывод в консоль
                print(start_msg)

            try:
                # Вызываем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение
                end_msg = f"Функция '{func_name}' успешно завершена. Результат: {result}"

                if filename:
                    file.write(end_msg + "\n")
                    file.close()
                else:
                    print(end_msg)

                return result

            except Exception as e:
                # Логируем ошибку
                error_msg = f"Ошибка в функции '{func_name}': {e}"

                if filename:
                    file.write(error_msg + "\n")
                    file.close()
                else:
                    print(error_msg)

                # Пробрасываем ошибку дальше
                raise

        return wrapper

    return decorator
