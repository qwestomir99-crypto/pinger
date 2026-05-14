import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

# --- НАСТРОЙКИ: ПИНГУЕМ ОСНОВНОГО БОТА ---
MAIN_BOT_URL = "https://ansamb-sledov-bot-94wz.onrender.com/ping"
PING_INTERVAL = 60  # 1 минута

def ping_main_bot():
    while True:
        try:
            r = requests.get(MAIN_BOT_URL, timeout=30)
            print(f"[Пингер] Пинг основного бота на {MAIN_BOT_URL}. Статус: {r.status_code}")
        except Exception as e:
            print(f"[Пингер] Ошибка пинга: {e}")
        time.sleep(PING_INTERVAL)

@app.route('/')
def health():
    return "Pinger is alive", 200

if __name__ == "__main__":
    # Запускаем фоновый пинг
    threading.Thread(target=ping_main_bot, daemon=True).start()
    # Запускаем Flask-сервер для Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
