import pytest
import requests
import time


class TestCalculatorIntegration:
    """Интеграционные тесты для калькулятора"""

    BASE_URL = "http://localhost:5000"

    @classmethod
    def setup_class(cls):
        """Настройка перед всеми тестами"""
        # Ждем запуска сервера
        time.sleep(2)

    def test_calculation_flow_success(self):
        """Тест 1: Успешный поток вычислений через API"""
        # Тестируем сложение
        response = requests.post(f"{self.BASE_URL}/api/calculate", json={
            "a": 10,
            "b": 5,
            "operation": "add"
        })

        # Проверяем успешный ответ
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        data = response.json()

        # Проверяем корректность вычислений
        assert data['operation'] == 'add'
        assert data['a'] == 10.0
        assert data['b'] == 5.0
        assert data['result'] == 15.0

    def test_all_operations_integration(self):
        """Тест 2: Интеграция всех математических операций"""
        test_cases = [
            {"operation": "add", "a": 8, "b": 3, "expected": 11},
            {"operation": "subtract", "a": 8, "b": 3, "expected": 5},
            {"operation": "multiply", "a": 8, "b": 3, "expected": 24},
            {"operation": "divide", "a": 8, "b": 2, "expected": 4},
            {"operation": "power", "a": 2, "b": 3, "expected": 8}
        ]

        for case in test_cases:
            response = requests.post(f"{self.BASE_URL}/api/calculate", json={
                "a": case["a"],
                "b": case["b"],
                "operation": case["operation"]
            })

            assert response.status_code == 200
            data = response.json()
            assert data['result'] == case['expected'], f"Ошибка в операции {case['operation']}"

    def test_division_by_zero_error_flow(self):
        """Тест 3: Поток обработки ошибки деления на ноль"""
        response = requests.post(f"{self.BASE_URL}/api/calculate", json={
            "a": 10,
            "b": 0,
            "operation": "divide"
        })

        # Проверяем, что сервер корректно обрабатывает ошибку
        assert response.status_code == 400
        data = response.json()
        assert 'error' in data
        assert 'Деление на ноль' in data['error']

    def test_validation_integration(self):
        """Тест 4: Интеграция модуля валидации с API"""
        # Тест с нечисловыми входными данными
        response = requests.post(f"{self.BASE_URL}/api/calculate", json={
            "a": "не число",
            "b": 5,
            "operation": "add"
        })

        assert response.status_code == 400
        data = response.json()
        assert 'error' in data
        assert 'должны быть числами' in data['error']

        # Тест с отсутствующими параметрами
        response = requests.post(f"{self.BASE_URL}/api/calculate", json={
            "a": 5,
            # "b" отсутствует
            "operation": "add"
        })

        assert response.status_code == 400
        data = response.json()
        assert 'error' in data

    def test_invalid_operation_flow(self):
        """Тест 5: Обработка недопустимой операции"""
        response = requests.post(f"{self.BASE_URL}/api/calculate", json={
            "a": 10,
            "b": 5,
            "operation": "invalid_operation"
        })

        assert response.status_code == 400
        data = response.json()
        assert 'error' in data
        assert 'Недопустимая операция' in data['error']

if __name__ == '__main__':
    pytest.main([__file__, "-v"])