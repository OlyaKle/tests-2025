import unittest
from small_project import *


class TestMathOperations(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Arrange - подготовка тестовых данных
        a, b = 2, 3
        expected = 5

        # Act - выполнение тестируемого действия
        result = add(a, b)

        # Assert - проверка результата
        self.assertEqual(result, expected)

    def test_divide_by_zero(self):
        # Arrange
        a, b = 5, 0

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            divide(a, b)

        # Доп проверка текста сообщения об ошибке
        self.assertEqual(str(context.exception), "Делитель не может быть нулем")

    def test_is_prime_edge_cases(self):
        # AAA для нескольких граничных случаев
        self.assertFalse(is_prime(1))  # 1 не простое
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(17))

    def test_multiply_negative_numbers(self):
        # Arrange
        a, b = -3, -4
        expected = 12

        # Act
        result = multiply(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_subtract_zero(self):
        # Arrange
        a, b = 5, 0
        expected = 5

        # Act
        result = subtract(a, b)

        # Assert
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()