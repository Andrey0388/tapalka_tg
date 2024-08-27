import os
from flask import Flask, send_from_directory
import telebot
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    webAppUrl = 'https://имя-проекта.glitch.me'
    markup.add(telebot.types.InlineKeyboardButton(text='Играть', web_app=telebot.types.WebAppInfo(webAppUrl)))
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку ниже, чтобы начать игру!", reply_markup=markup)

# Flask сервер для обслуживания webapp
@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('public', 'index.html')

@app.route('/<path:path>', methods=['GET'])
def serve_file(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    # Запуск Flask в режиме отладки, если нужно
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# Запуск бота
bot.polling()
