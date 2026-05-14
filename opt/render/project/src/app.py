import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

# --- НАСТРОЙКИ (ПРОВЕРЬ URL ОСНОВНОГО БОТА) ---
MAIN_BOT_URL = "https://ansamb-sledov-bot-94wz.onrender.com/ping"
PING_INTERVAL = 300  # 5 минут
# -----------------------------------------------

def ping_main_bot():
    while True:
        try:
            r = requests.get(MAIN_BOT_URL, timeout=30)
            print(f"Пинг отправлен. Статус: {r.status_code}")
            if r.status_code != 200:
                print(f"Ошибка: ожидался 200, получен {r.status_code}")
        except Exception as e:
            print(f"Ошибка пинга: {e}")
        time.sleep(PING_INTERVAL)

@app.route('/')
def health():
    return "Pinger is alive", 200

@app.route('/ping')
def ping_self():
    return "pong", 200

if __name__ == "__main__":
    # Запускаем пинг в фоновом потоке
    threading.Thread(target=ping_main_bot, daemon=True).start()
    # Запускаем Flask-сервер для Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
