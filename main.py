import telebot

TOKEN = '6832851527:AAG5o94cSvqamGyd4BwHvtUYmKYxoL37N7w'

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f"Welcome, {message.chat.username}")


@bot.message_handler(content_types=['text', 'document', 'audio', 'voice'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, "Тест")

@bot.message_handler(content_types=['photo'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, "Nice meme XDD")

bot.polling(none_stop=True)