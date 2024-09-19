import telebot
from telebot import types
import my_token

# Ваш токен от BotFather
TOKEN = my_token.Token
bot = telebot.TeleBot(TOKEN)


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем инлайн-клавиатуру
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Добавляем инлайн-кнопки с callback_data
    btn1 = types.InlineKeyboardButton("Кнопка 1", callback_data="btn1")
    btn2 = types.InlineKeyboardButton("Кнопка 2", callback_data="btn2")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Нажмите на кнопку:", reply_markup=markup)


# Обработка нажатий на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "btn1":
        bot.send_message(call.message.chat.id, "Вы нажали кнопку 1")
    elif call.data == "btn2":
        bot.send_message(call.message.chat.id, "Вы нажали кнопку 2")


# Запуск бота
bot.polling(none_stop=True)
