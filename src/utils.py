import json


def read_json_file(file_path):
    """
    Читает JSON файл и возвращает список транзакций.
    Если ошибка - возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверяем, что это список
        if isinstance(data, list):
            return data
        else:
            print("Ошибка: файл содержит не список")
            return []

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {file_path} содержит неверный JSON")
        return []
    except Exception as e:
        print(f"Ошибка: {e}")
        return []