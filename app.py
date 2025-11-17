from flask import Flask, request, jsonify, render_template_string
from calculator import Calculator
from validation import validate_numbers, validate_operation

app = Flask(__name__)
calc = Calculator()

# Простая HTML форма для тестирования
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор</title>
</head>
<body>
    <h1>Простой калькулятор</h1>
    <form method="POST" action="/calculate">
        <input type="text" name="a" placeholder="Первое число" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
            <option value="power">^</option>
        </select>
        <input type="text" name="b" placeholder="Второе число" required>
        <button type="submit">Вычислить</button>
    </form>
    {% if result is not none %}
        <h2>Результат: {{ result }}</h2>
    {% endif %}
    {% if error %}
        <h2 style="color: red">Ошибка: {{ error }}</h2>
    {% endif %}
</body>
</html>
"""


@app.route('/')
def index():
    """Главная страница с формой калькулятора"""
    return render_template_string(HTML_FORM)


@app.route('/calculate', methods=['POST'])
def calculate():
    """API endpoint для вычислений"""
    # Получение данных из формы
    a = request.form.get('a')
    b = request.form.get('b')
    operation = request.form.get('operation')

    # Валидация входных данных
    is_valid, error_msg, numbers = validate_numbers(a, b)
    if not is_valid:
        return render_template_string(HTML_FORM, error=error_msg)

    if not validate_operation(operation):
        return render_template_string(HTML_FORM, error="Недопустимая операция")

    num_a, num_b = numbers

    # Выполнение математической операции
    try:
        if operation == 'add':
            result = calc.add(num_a, num_b)
        elif operation == 'subtract':
            result = calc.subtract(num_a, num_b)
        elif operation == 'multiply':
            result = calc.multiply(num_a, num_b)
        elif operation == 'divide':
            result = calc.divide(num_a, num_b)
        elif operation == 'power':
            result = calc.power(num_a, num_b)

        return render_template_string(HTML_FORM, result=result)

    except ValueError as e:
        return render_template_string(HTML_FORM, error=str(e))
    except Exception as e:
        return render_template_string(HTML_FORM, error="Внутренняя ошибка сервера")


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """JSON API endpoint для вычислений"""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Отсутствуют данные'}), 400

    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    # Валидация входных данных
    is_valid, error_msg, numbers = validate_numbers(str(a), str(b))
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    if not validate_operation(operation):
        return jsonify({'error': 'Недопустимая операция'}), 400

    num_a, num_b = numbers

    # Выполнение математической операции
    try:
        if operation == 'add':
            result = calc.add(num_a, num_b)
        elif operation == 'subtract':
            result = calc.subtract(num_a, num_b)
        elif operation == 'multiply':
            result = calc.multiply(num_a, num_b)
        elif operation == 'divide':
            result = calc.divide(num_a, num_b)
        elif operation == 'power':
            result = calc.power(num_a, num_b)

        return jsonify({
            'operation': operation,
            'a': num_a,
            'b': num_b,
            'result': result
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)