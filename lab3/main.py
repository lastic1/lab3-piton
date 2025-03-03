from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    dol = None  # Инициализируем переменную dol
    num_1 = None  # Инициализируем переменную num_1
    if request.method == 'POST':
        try:
            num_1 = float(request.form.get('num_1'))  # Пытаемся преобразовать ввод в число
            dol = num_1 * 58.2  # Вычисляем результат
        except (ValueError, TypeError):  # Обрабатываем ошибки, если ввод не число
            dol = "Ошибка: введите число!"

    return render_template('index.html', dol=dol, num_1=num_1)  # Передаем результат в шаблон


if __name__ == '__main__':
    app.run(debug=True)
