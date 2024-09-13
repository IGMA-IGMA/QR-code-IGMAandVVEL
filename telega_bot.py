import telebot
import craft
import my_token
import creatDIR

API_TOKEN = my_token.Token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
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


@bot.message_handler(commands=['help'])
def send_help(message):
    opis = """
    Текст с помощью
    """
    bot.reply_to(message.text, opis)


@bot.message_handler(commands=['clean_db'])
def handle_clean_db(message):
    chat_id = message.chat.id
    if str(chat_id) in ['1185507660', '1077355845', '959742702']:
        print('Начал')
        perech = creatDIR.clean_directory('telega_db/imagesQR/images_save')
        bot.send_message(chat_id, perech)


@bot.message_handler(content_types=['text'])
def create_QR(message):
    image_path = craft.creating_QR_code(message.text, 't')

    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id=message.chat.id, photo=image)
        print(message.chat.id, message.chat.active_usernames)




# Запуск бота
if __name__ == '__main__':
    creatDIR.creat_DIR_telega()
    bot.polling()
    try:
        print('Успешно')
    except:
        print('Не успешно')
        creatDIR.delit_DIR_telega()
    creatDIR.delit_DIR_telega()
