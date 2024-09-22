import telebot
import admin
import my_token
import patern_color

# Ваш токен от BotFather
TOKEN = my_token.Token

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

RAINBOW_COLORS = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet']
selected_color = None

@bot.message_handler(commands=['reset_color_qr'])
def reset_color_qr(message):
    print(message.text)
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for color in RAINBOW_COLORS:
        markup.add(color)
    markup.add('RGB', 'HEX')
    bot.send_message(message.chat.id, "Выберите цвет или формат для QR-кода:", reply_markup=markup)
    bot.register_next_step_handler(message, process_color_qr)

# Команда для сброса цвета фона QR-кода
@bot.message_handler(commands=['reset_background_color'])
def reset_background_color_qr(message):
    print(message.text)
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for color in RAINBOW_COLORS:
        markup.add(color)
    markup.add('RGB', 'HEX')
    bot.send_message(message.chat.id, "Выберите цвет или формат для фона QR-кода:", reply_markup=markup)
    bot.register_next_step_handler(message, process_background_color_qr)

# Обработка выбора цвета или формата для QR-кода
def process_color_qr(message):
    global selected_color
    choice = message.text
    if choice in RAINBOW_COLORS:
        selected_color = choice
        bot.send_message(message.chat.id, f"Вы выбрали цвет {choice}. Цвет QR-кода установлен.")
        admin.update_setting(str(message.chat.id), "COLOR", selected_color)
    elif choice == 'RGB':
        msg = bot.send_message(message.chat.id, "Введите цвет в формате RGB (например, 255,0,0):")
        bot.register_next_step_handler(msg, handle_rgb_input, source='COLOR')
    elif choice == 'HEX':
        msg = bot.send_message(message.chat.id, "Введите цвет в формате HEX (#RRGGBB):")
        bot.register_next_step_handler(msg, handle_hex_input, source='COLOR')
    else:
        bot.send_message(message.chat.id, "Неверный выбор, попробуйте снова.")
        reset_color_qr(message)

# Обработка выбора цвета или формата для фона QR-кода
def process_background_color_qr(message):
    global selected_color
    choice = message.text
    if choice in RAINBOW_COLORS:
        selected_color = choice
        bot.send_message(message.chat.id, f"Вы выбрали цвет {choice}. Цвет фона QR-кода установлен.")
        admin.update_setting(str(message.chat.id), "BACKCOLOR", selected_color)
    elif choice == 'RGB':
        msg = bot.send_message(message.chat.id, "Введите цвет в формате RGB (например, 255,0,0):")
        bot.register_next_step_handler(msg, handle_rgb_input, source='BACKCOLOR')
    elif choice == 'HEX':
        msg = bot.send_message(message.chat.id, "Введите цвет в формате HEX (#RRGGBB):")
        bot.register_next_step_handler(msg, handle_hex_input, source='BACKCOLOR')
    else:
        bot.send_message(message.chat.id, "Неверный выбор, попробуйте снова.")
        reset_background_color_qr(message)

# Обработка ввода HEX-кода
def handle_hex_input(message, source):
    global selected_color
    hex_color = message.text
    if patern_color.validate_hex(hex_color):
        selected_color = hex_color
        bot.send_message(message.chat.id, f"Цвет {hex_color} корректен в формате HEX. Цвет {'QR-кода' if source == 'COLOR' else 'фона QR-кода'} установлен.")
        admin.update_setting(str(message.chat.id), source, selected_color)
    else:
        bot.send_message(message.chat.id, "Некорректный формат HEX. Попробуйте снова.")
        bot.register_next_step_handler(message, handle_hex_input, source)

# Обработка ввода RGB-кода
def handle_rgb_input(message, source):
    global selected_color
    rgb_color = message.text
    if patern_color.validate_rgb(rgb_color):
        selected_color = tuple(map(int, rgb_color.split(',')))
        bot.send_message(message.chat.id, f"Цвет {rgb_color} корректен в формате RGB. Цвет {'QR-кода' if source == 'COLOR' else 'фона QR-кода'} установлен.")
        admin.update_setting(str(message.chat.id), source, selected_color)
    else:
        bot.send_message(message.chat.id, "Некорректный формат RGB. Попробуйте снова.")
        bot.register_next_step_handler(message, handle_rgb_input, source)

# Запуск бота
bot.polling()
