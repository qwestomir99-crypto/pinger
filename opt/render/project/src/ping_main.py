import time
import requests

MAIN_BOT_URL = "https://ansamb-sledov-bot-94wz.onrender.com/ping"
PING_INTERVAL = 60  # 1 минута

def ping_main_bot():
    while True:
        try:
            r = requests.get(MAIN_BOT_URL, timeout=30)
            print(f"[Пингер] Пинг основного бота. Статус: {r.status_code}")
        except Exception as e:
            print(f"[Пингер] Ошибка пинга: {e}")
        time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    ping_main_bot()
