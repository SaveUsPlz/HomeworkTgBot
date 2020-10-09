import telebot

bot = telebot.TeleBot('1339112927:AAFO2IsDIdjUYSXU4I_T8hEOneu5mOiL9YM')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')

bot.polling()