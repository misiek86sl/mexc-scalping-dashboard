from flask import Flask, render_template
from telegram import Bot
import datetime

# Dane użytkownika (Twoje!)
API_KEY = "mx0vgluPpbwYNnP3Qt"
SECRET_KEY = "f060398b48004f608b832fb850657c9d"
TELEGRAM_TOKEN = "7796564718:AAGoPnYM6spq8qdWcnsCoHntsOMgAAhfsgQ"
TELEGRAM_CHAT_ID = "5186732306"

bot = Bot(token=TELEGRAM_TOKEN)
app = Flask(__name__)

# Przykładowy status
trade_log = [
    {"pair": "BTC/USDT", "side": "BUY", "amount": "10", "leverage": "500x", "timestamp": datetime.datetime.now()},
    {"pair": "SOL/USDT", "side": "SELL", "amount": "10", "leverage": "300x", "timestamp": datetime.datetime.now()},
]

@app.route("/")
def index():
    return render_template("index.html", trades=trade_log)

@app.route("/send")
def send_notification():
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Test wiadomości z bota 🚀")
    return "Wysłano wiadomość do Telegrama"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
