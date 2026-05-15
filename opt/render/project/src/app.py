import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

# 1. Активная часть: пингуем основной бот
def ping_main_bot():
    while True:
        try:
            # Здесь живет твой старый добрый пингер
            r = requests.get('https://ansamb-sledov-bot-94wz.onrender.com/ping')
            print(f"Пинг отправлен. Статус: {r.status_code}")
        except Exception as e:
            print(f"Ошибка пинга: {e}")
        time.sleep(60)

# 2. Пассивная часть: отвечаем на запросы для Render
@app.route('/')
def health():
    return "Pinger is alive", 200

# 3. Сердце приложения: запускаем всё вместе
if __name__ == "__main__":
    # Запускаем активный пингер в фоновом потоке
    ping_thread = threading.Thread(target=ping_main_bot)
    ping_thread.daemon = True  # Поток завершится вместе с основным приложением
    ping_thread.start()

    # Запускаем пассивный Flask-сервер
    app.run(host='0.0.0.0', port=10000)
