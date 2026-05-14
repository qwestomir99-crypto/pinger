import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

# URL самого пингера (для самопинга)
PINGER_URL = "https://bot-pinger-88an.onrender.com"
PING_INTERVAL = 60  # 1 минута — чаще, чтобы гарантированно не спать

def ping_self():
    while True:
        try:
            r = requests.get(PINGER_URL, timeout=30)
            print(f"[Пингер] Пинг отправлен на {PINGER_URL}. Статус: {r.status_code}")
        except Exception as e:
            print(f"[Пингер] Ошибка пинга: {e}")
        time.sleep(PING_INTERVAL)

@app.route('/')
def health():
    return "Pinger is alive", 200

if __name__ == "__main__":
    # Запускаем пинг в фоновом потоке
    threading.Thread(target=ping_self, daemon=True).start()
    # Запускаем Flask-сервер
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
