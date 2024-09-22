import telebot
import craft
import my_token
import creatDIR
import admin
import os
import URLaddress
import patern_color

API_TOKEN = my_token.Token
bot = telebot.TeleBot(API_TOKEN)


# USER_COMMAND
@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id = message.chat.id
    Hello_text = f"""
    Здравствуйте, {message.chat.username}
    👨‍💻 **Команда IGMA and VVEL** 👨‍💻

    Мы — команда юных разработчиков, которая занимается разработкой инновационных решений для работы с QR-кодами. Наш проект нацелен на создание удобных и эффективных инструментов для генерации и распознавания QR-кодов.

    📲 **Чем мы занимаемся:**
    - **Создание QR-кодов:** Простой и быстрый способ создания уникальных QR-кодов для ваших нужд.
    - **Распознавание QR-кодов:** Мгновенное сканирование и расшифровка QR-кодов, будь то текст, ссылки или другая информация.

    Мы стремимся сделать работу с QR-кодами простой, доступной и удобной для всех. Следите за нашими обновлениями и новыми функциями!
    """
    bot.reply_to(message, Hello_text)
    if not admin.user_in_dbUser(str(chat_id)):
        admin.add_to_json("db_user_tg/id_user.json",
                          {str(message.chat.id): [str(message.chat.username),
                                                  {"COLOR": "black", "BACKCOLOR": "white"}]})
    else:
        print("Пользователь уже в BD")


@bot.message_handler(commands=["help"])
def send_help(message):
    chat_id = message.chat.id
    help = """
    Бот для создания QR
    """
    bot.send_message(chat_id, help)


@bot.message_handler(commands=["my_setting"])
def my_setting(message):
    chat_id = message.chat.id
    setting = admin.re_setting(str(chat_id))
    re = f"""
    Ваши настройки, {message.chat.username}
    COLOR: {setting["COLOR"]}
    BACKCOLOR: {setting["BACKCOLOR"]}
    """
    bot.send_message(chat_id, re)

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



# ADMIN_COMMAND
@bot.message_handler(commands=["229343"])
def ADMIN_ADD(message):
    inf_new_adm = {str(message.chat.id): str(message.chat.username)}
    admin.add_to_json("db_user_tg/id_admin.json", inf_new_adm)
    bot.send_message(message.chat.id,
                     "Вас занесли в Root-room\nКоманды доступные вам:\n /clean_db_image_save \n /stop_bot")


@bot.message_handler(commands=["clean_db_image_save"])
def clean_db_image_save(message):
    chat_id = str(message.chat.id)
    if admin.user_is_admin(chat_id):
        perech = creatDIR.clean_directory("telega_db/imagesQR/images_save")
        bot.send_message(chat_id, perech)


@bot.message_handler(commands=["clean_db_image_open"])
def clean_db_image_open(message):
    chat_id = str(message.chat.id)
    if admin.user_is_admin(chat_id):
        perech = creatDIR.clean_directory("telega_db/imagesQR/images_save")
        bot.send_message(chat_id, perech)


@bot.message_handler(commands=["stop_bot"])
def stop_bot(message):
    chat_id = str(message.chat.id)
    if admin.user_is_admin(chat_id):
        bot.stop_bot()
    bot.send_message(chat_id, "Вы вызвали не существующую команду")


@bot.message_handler(commands=["spisok_admin"])
def sending_list_admins(message):
    chat_id = str(message.chat.id)

    if admin.user_is_admin(chat_id):
        spisok = admin.spisok_admin()

        with open("db_user_tg/id_admin.json", "rb") as file_admin:
            bot.send_document(chat_id, file_admin)
        file_admin.close()

        bot.send_message(chat_id, spisok)


# USER_exp
@bot.message_handler(content_types=["text"])
def create_QR(message):
    print(message.text)
    chat_id = message.chat.id
    setting = admin.return_setting(str(chat_id))
    COLOR = setting["COLOR"]
    BACKCOLOR = setting["BACKCOLOR"]
    image_path = craft.creating_QR_code(message.text, "t", COLOR, BACKCOLOR)
    with open(image_path, "rb") as image:
        url_image = URLaddress.upload_image_to_fileio(image_path)
        bot.send_photo(chat_id=chat_id, photo=image)
        bot.send_message(chat_id=chat_id, text=url_image)
    image.close()

    image.close()


@bot.message_handler(content_types=["photo"])
def reqognize(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    l = len(os.listdir("telega_db/imagesQR/images_open"))
    image_path = f"telega_db/imagesQR/images_open/{l + 1}.jpg"
    with open(image_path, "wb") as new_file:
        new_file.write(downloaded_file)
    new_file.close()

    link, _ = craft.recognize_qr_code_and_print_link(image_path)

    bot.send_message(message.chat.id, link)


# Запуск бота
if __name__ == "__main__":
    creatDIR.creat_DIR_telega()
    bot.polling()
    try:
        creatDIR.delit_DIR_telega()
    except:
        creatDIR.delit_DIR_telega()
