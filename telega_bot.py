import telebot
import craft
import my_token
import creatDIR
import admin
import os
import URLaddress

API_TOKEN = my_token.Token
bot = telebot.TeleBot(API_TOKEN)


# USER_COMMAND
@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id = message.chat.id
    Hello_text = """
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
                          {str(message.chat.id): [str(message.chat.username), {"COLOR": "black", "WIDTH": "290", "HEIGHT": "290"}]})
    else:
        print('Пользователь уже в BD')


@bot.message_handler(commands=["help"])
def send_help(message):
    help = """
    Бот для создания QR
    """
    bot.send_message(message.chat.id, help)


# @bot.message_handler(commands=['QR_setting'])
# def qr_setting_command(message):
#     # Отправляем сообщение с подтверждением
#     bot.send_message(message.chat.id, "Действительно хотите изменить настройки создания QR-кода? (да/нет)")
#     bot.register_next_step_handler(message, process_confirmation)
#
#
# def process_confirmation(message):
#     if message.text.lower() == 'да':
#         bot.send_message(message.chat.id,
#                          "Введите ширину и длину картинки, а затем цвет заднего фона (формат: цвет ширина длина ).")
#         bot.register_next_step_handler(message, process_dimensions)
#     elif message.text.lower() == 'нет':
#         bot.send_message(message.chat.id, "Настройки не изменены.")
#     else:
#         bot.send_message(message.chat.id, "Пожалуйста, ответьте 'да' или 'нет'.")
#         bot.register_next_step_handler(message, process_confirmation)
#
#
# def process_dimensions(message):
#     try:
#         chat_id = str(message.chat.id)
#         color, width, height = message.text.split()
#
#         admin.update_setting_user(chat_id, color, width, height)
#
#         bot.send_message(message.chat.id,
#                          f"Настройки QR-кода обновлены: ширина={width}, длина={height}.")
#     except ValueError:
#         bot.send_message(message.chat.id,
#                          "Некорректный формат. Введите ширину, длину и цвет фона (формат: ширина длина цвет).")
#         bot.register_next_step_handler(message, process_dimensions)


@bot.message_handler(commands=["reset_color_QR"])
def reset_color_QR(message):
    chat_id = message.chat.id



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
    bot.send_message(chat_id, 'Вы вызвали не существующую команду')


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
    chat_id = message.chat.id
    image_path = craft.creating_QR_code(message.text, "t")
    with open(image_path, "rb") as image:
        url_image = URLaddress.upload_image_to_fileio(image_path)
        teg_img = f""
        bot.send_photo(chat_id=chat_id, photo=image)
        bot.send_message(chat_id=chat_id, text=url_image)

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
