import os
import time
import threading
import requests
import Flask
from flask

from ping_main import ping_main_bot

app = Flask(__name__)

@app.route('/')
def health():
    return "Pinger is alive", 200

if __name__ == "__main__":
    # Запускаем активный пинг в фоновом потоке
    threading.Thread(target=ping_main_bot, daemon=True).start()
    # Запускаем Flask-сервер для Render
    app.run(host='0.0.0.0', port=10000)
