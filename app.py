

from flask import Flask, request, render_template


app = Flask(__name__)

# Список уведомлень
notifications = []

# Налаштування Flask для режиму продакшену
app.config['DEBUG'] = False
app.config['TESTING'] = False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Отримуємо дані з POST запиту
        data = request.json
        # Додаємо уведомлення в список
        notifications.append(data)
        # Повертаємо підтвердження успішного отримання уведомлення
        return 'Уведомление успешно принято!'
    else:
        # Показуємо всі отримані уведомлення на головній сторінці
        return render_template("index.html", notifications=notifications)

@app.route('/notification', methods=['POST'])
def receive_notification():
    data = request.json
    message = data.get('message')
    # Тут ви можете додатково обробляти отримане сповіщення
    print("Отримано сповіщення: ", message)
    return 'Сповіщення успішно отримано!'

if __name__ == '__main__':
    # Запускаємо додаток з Gunicorn, якщо він запускається локально
    app.run()
