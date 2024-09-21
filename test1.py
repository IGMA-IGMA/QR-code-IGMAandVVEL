import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import my_token


# Вставьте сюда ваш токен
bot = telebot.TeleBot(my_token.Token)



# Функция для создания клавиатуры с кнопками
def create_keyboard(command):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(f'{command}_button_{i+1}') for i in range(12)]
    keyboard.add(*buttons)
    return keyboard

# Обработчик команды reset_background_color_qr
@bot.message_handler(commands=['reset_background_color_qr'])
def handle_reset_background_color_qr(message):
    keyboard = create_keyboard('reset_background_color_qr')
    bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=keyboard)

# Обработчик команды reset_color_qr
@bot.message_handler(commands=['reset_color_qr'])
def handle_reset_color_qr(message):
    keyboard = create_keyboard('reset_color_qr')
    bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=keyboard)

# Обработчик кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text.startswith('reset_background_color_qr_button_'):
        # Обработка кнопок для reset_background_color_qr
        bot.send_message(message.chat.id, f'Вы нажали: {message.text}')
    elif message.text.startswith('reset_color_qr_button_'):
        # Обработка кнопок для reset_color_qr
        bot.send_message(message.chat.id, f'Вы нажали: {message.text}')

# Запуск бота
bot.polling()
