import telebot
import craft
import token


API_TOKEN = token.Token

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


@bot.message_handler(func=lambda message: True)
def send_image(message):
    # Путь к изображению, которое будет отправлено
    image_path = 'path/to/your/image.jpg'

    with open(image_path, 'rb') as image:
        bot.send_photo(message.chat.id, image)

# Запуск бота
if __name__ == '__main__':
    bot.infinity_polling()

