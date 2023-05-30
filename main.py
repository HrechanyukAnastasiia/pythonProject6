import telebot
bot = telebot.TeleBot("5818305501:AAFKjdRo8hLPnLH3JmTkdaQF10ZN1iGA3Cg")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello 🤞😁')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Усі кажуть " + message.text + ", а ти купи слона")
bot.polling()
