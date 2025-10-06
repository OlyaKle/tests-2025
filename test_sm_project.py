import pytest
from small_project import add, subtract, multiply, divide, is_prime

def test_add_positive_numbers():
    # Arrange - подготовка тестовых данных
    a, b = 2, 3
    expected = 5

    # Act - выполнение тестируемого действия
    result = add(a, b)

    # Assert - проверка результата
    assert result == expected

def test_divide_by_zero():
    # Arrange
    a, b = 5, 0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        divide(a, b)

    # Проверка сообщения об ошибке
    assert str(exc_info.value) == "Делитель не может быть нулем"

# Параметризованные тесты
@pytest.mark.parametrize("number,expected", [
    (1, False),  # 1 не простое
    (2, True),  # простое
    (4, False),  # четное число
    (17, True),  # простое число
    (25, False),  # составное число
])
def test_is_prime(number, expected):
    # Act и Assert
    assert is_prime(number) == expected


def test_multiply_negative_numbers():
    # Arrange
    a, b = -3, -4
    expected = 12

    # Act
    result = multiply(a, b)

    # Assert
    assert result == expected


def test_subtract_zero():
    # Arrange
    a, b = 5, 0
    expected = 5

    # Act
    result = subtract(a, b)

    # Assert
    assert result == expected


# Фикстура для переиспользования данных
@pytest.fixture
def sample_numbers():
    return (10, 2)


def test_operations_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 12
    assert subtract(a, b) == 8
    assert multiply(a, b) == 20
    assert divide(a, b) == 5