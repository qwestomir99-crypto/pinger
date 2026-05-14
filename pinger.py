import os
import sys
import time
import threading
import requests
from flask import Flask

# Принудительно переключаемся в нужную директорию
os.chdir('/opt/render/project/src/')

app = Flask(__name__)

MAIN_BOT_URL = "https://ansamb-sledov6-bot.onrender.com/ping"
PING_INTERVAL = 300  # 5 минут

def ping_main_bot():
    while True:
        try:
            r = requests.get(MAIN_BOT_URL, timeout=30)
            print(f"Пинг отправлен. Статус: {r.status_code}")
        except Exception as e:
            print(f"Ошибка пинга: {e}")
        time.sleep(PING_INTERVAL)

@app.route('/')
def health():
    return "Pinger is alive", 200

if __name__ == "__main__":
    threading.Thread(target=ping_main_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
