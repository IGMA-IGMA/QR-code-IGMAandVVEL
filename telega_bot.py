import telebot
import craft
import my_token
import creatDIR
import admin
import os

API_TOKEN = my_token.Token
bot = telebot.TeleBot(API_TOKEN)


# USER_COMMAND
@bot.message_handler(commands=["start"])
def send_welcome(message):
    Hello_text = """
    👨‍💻 **Команда IGMA and VVEL** 👨‍💻

    Мы — команда юных разработчиков, которая занимается разработкой инновационных решений для работы с QR-кодами. Наш проект нацелен на создание удобных и эффективных инструментов для генерации и распознавания QR-кодов.

    📲 **Чем мы занимаемся:**
    - **Создание QR-кодов:** Простой и быстрый способ создания уникальных QR-кодов для ваших нужд.
    - **Распознавание QR-кодов:** Мгновенное сканирование и расшифровка QR-кодов, будь то текст, ссылки или другая информация.

    Мы стремимся сделать работу с QR-кодами простой, доступной и удобной для всех. Следите за нашими обновлениями и новыми функциями!
    """
    bot.reply_to(message, Hello_text)
    admin.add_to_json("id_user.json", {str(message.chat.id): str(message.chat.username)})


@bot.message_handler(commands=["help"])
def send_help(message):
    help = """
    Бот для создания 
    """
    bot.send_message(message.chat.id, help)


# ADMIN_COMMAND
@bot.message_handler(commands=["229343"])
def ADMIN_ADD(message):
    inf_new_adm = {str(message.chat.id): str(message.chat.username)}
    admin.add_to_json("id_admin.json", inf_new_adm)
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

        with open("id_admin.json", "rb") as file_admin:
            bot.send_document(chat_id, file_admin)
        file_admin.close()

        bot.send_message(chat_id, spisok)




# USER_exp
@bot.message_handler(content_types=["text"])
def create_QR(message):
    image_path = craft.creating_QR_code(message.text, "t")
    with open(image_path, "rb") as image:
        bot.send_photo(chat_id=message.chat.id, photo=image)
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
