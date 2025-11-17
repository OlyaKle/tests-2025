def validate_numbers(a: str, b: str) -> tuple:
    """
    Валидация и преобразование входных данных в числа
    Возвращает кортеж (валидность, сообщение об ошибке, числа)
    """
    if not a or not b:
        return False, "Оба числа должны быть указаны", (None, None)

    try:
        num_a = float(a)
        num_b = float(b)
        return True, "", (num_a, num_b)
    except ValueError:
        return False, "Оба параметра должны быть числами", (None, None)

def validate_operation(operation: str) -> bool:
    valid_operations = ['add', 'subtract', 'multiply', 'divide', 'power']
    return operation in valid_operations