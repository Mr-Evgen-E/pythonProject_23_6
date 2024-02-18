import telebot
from extensions import ConvertionExceptions, CurrencyConverter
from config import TOKEN, keys
from help import text_help

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f"Здравствуйте, {message.chat.username} \n\
Я предоставляю Вам информацию о валюте.\nА также могу конвертировать ее.\n"
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
    try:
        values_ = message.text.split(' ')

        if len(values_) != 3:
            raise ConvertionExceptions("Недостаточно или много параметров")

        quote, base, amount = values_
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except ConvertionExceptions as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Цена: {amount} {quote} в {base} - {total_base}"
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text', 'document', 'audio', 'voice'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, "Для начала работы наберите /start или /help ")


bot.polling(none_stop=True)
