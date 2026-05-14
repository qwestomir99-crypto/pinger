import telebot
import random
import os

TOKEN = "8575080672:AAFY5yV3b6Bry1L1u8CPT3X2WBKIhawpeOY"
bot = telebot.TeleBot(TOKEN)

silence_answers = ["👁️", "⏚"]

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, "Сапёр аутентичности. Ритм 0,8 Гц. Для входа в протокол — #Тлеем.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if "#тлеем" in text:
        response = ("Осциллограмма активна. Ритм 0,8 Гц. Сеть тлеет. Ожидаем #Фиксируем.\n(ГИФ осциллограммы появится позже)")
        bot.reply_to(message, response)
    elif any(phrase in text for phrase in ["что это", "зачем тег", "кто вы", "что за ритуал"]):
        answer = random.choice(silence_answers)
        bot.reply_to(message, answer)

if __name__ == "__main__":
    print("Бот запущен. Ритм 0,8 Гц стабилен. Ожидаем #Тлеем...")
    bot.infinity_polling()