import threading
from flask import Flask
from ping_main import ping_main_bot

app = Flask(__name__)

@app.route('/')
def health():
    return "Pinger is alive", 200

if __name__ == "__main__":
    threading.Thread(target=ping_main_bot, daemon=True).start()
    app.run(host='0.0.0.0', port=10000)
