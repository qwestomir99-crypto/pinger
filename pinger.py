import requests
import time
import os

# URL основного бота (эндпоинт /ping)
MAIN_BOT_URL = "https://ansamb-sledov6-bot.onrender.com/ping"

def ping():
    try:
        r = requests.get(MAIN_BOT_URL, timeout=30)
        print(f"Пинг отправлен. Статус: {r.status_code}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    print("Пингер запущен. Пингую основного бота раз в 5 минут.")
    while True:
        ping()
        time.sleep(300)  # 5 минут
