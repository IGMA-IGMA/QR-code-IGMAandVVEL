import telebot
import craft


# Вставь сюда свой токен от BotFather
API_TOKEN = '6501255192:AAGa6lHliMwht7N4tDpP58v-4ARydruk0yk'

# Создаем экземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
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

# Обработчик команды /help
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

    # Открываем изображение в режиме чтения байтов
    with open(image_path, 'rb') as image:
        # Отправляем изображение в ответ на текстовое сообщение
        bot.send_photo(message.chat.id, image)

# Запуск бота
if __name__ == '__main__':
    bot.infinity_polling()

