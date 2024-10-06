import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import my_token
import test1
import admin

# Вставьте сюда ваш токен
bot = telebot.TeleBot(my_token.Token)


colors = ["black", "white", "red", "green", "blue", "yellow", "gray", "orange", "purple", "pink"]

# Функция для создания клавиатуры с кнопками
def create_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(color) for color in colors]  # Используем названия цветов для кнопок
    keyboard.add(*buttons)
    return keyboard

# Обработчик команды reset_background_color_qr
@bot.message_handler(commands=["reset_background_color_qr"])
def handle_reset_background_color_qr(message):
    create_keyboard()
    bot.send_message(message.chat.id, "Выберите цвет фона:", reply_markup=keyboard)

# Обработчик команды reset_color_qr
@bot.message_handler(commands=["reset_color_qr"])
def handle_reset_color_qr(message):
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, "Выберите цвет текста:", reply_markup=keyboard)

# Обработчик кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text in colors:
        if message.reply_to_message and "Выберите цвет фона:" in message.reply_to_message.text:
            bot.send_message(message.chat.id, f"Вы выбрали цвет фона: {message.text}")
        elif message.reply_to_message and "Выберите цвет текста:" in message.reply_to_message.text:
            bot.send_message(message.chat.id, f"Вы выбрали цвет текста: {message.text}")

# Запуск бота
bot.polling()