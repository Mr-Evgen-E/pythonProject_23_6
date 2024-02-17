import requests
import telebot
import json
from config import TOKEN
from help import text_help

bot = telebot.TeleBot(TOKEN)

keys = {
    "рубль": "RUB",
    "доллар": "USD",
    "евро": "EUR"
}

@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f"Здравствуйте, {message.chat.username} \n\
Я предоставляю Вам информацию о валюте.\nА так же могу сконвертировать ее.\n"
+ f"{text_help}")

@bot.message_handler(commands=['help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, text_help)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    quote, base, amount = message.text.split(" ")
    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}")
    text = json.loads(r.content)[keys[base]]
    bot.send_message(message, text)


@bot.message_handler(content_types=['text', 'document', 'audio', 'voice'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, "Для начала работы наберите /start или /help ")


bot.polling(none_stop=True)
