import telebot
import craft
import my_token
import creatDIR
import admin
import os

API_TOKEN = my_token.Token
bot = telebot.TeleBot(API_TOKEN)




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


@bot.message_handler(commands=["help"])
def send_help(message):
    help = """
    Бот для создания 
    """
    bot.send_message(message.chat.id, help)

@bot.message_handler(commands=["229343"])
def ADMIN_ADD(message):
    inf_new_adm = {str(message.chat.username): str(message.chat.id)}
    admin.add_to_json("id_admin.json", inf_new_adm)
    bot.send_message(message.chat.id, "Вас занесли в Root-room\nКоманды доступные вам:\t /help")




@bot.message_handler(commands=["clean_db"])
def handle_clean_db(message):
    chat_id = message.chat.id
    if str(chat_id) in ["1185507660", "1077355845", "959742702"]:
        print("Начал")
        perech = creatDIR.clean_directory("telega_db/imagesQR/images_save")
        bot.send_message(chat_id, perech)


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
    image_path = f"telega_db/imagesQR/images_open/{l+1}.jpg"
    with open(image_path, "wb") as new_file:
        new_file.write(downloaded_file)
    new_file.close()

    link, _ = craft.recognize_qr_code_and_print_link(image_path)


    bot.send_message(message.chat.id, link)

#"Olyvel": "959742702"

# Запуск бота
if __name__ == "__main__":
    creatDIR.creat_DIR_telega()
    bot.polling()
    try:
        creatDIR.delit_DIR_telega()
    except:
        creatDIR.delit_DIR_telega()


