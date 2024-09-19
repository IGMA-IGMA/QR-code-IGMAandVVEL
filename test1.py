import telebot
from telebot import types
import my_token

# Ваш токен от BotFather
TOKEN = my_token.Token
bot = telebot.TeleBot(TOKEN)



def go():
    print('вызвана функция go')


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Принять', callback_data='save_data')
    markup_inline.add(item_yes)

    bot.send_message(message.chat.id, 'Сделайте выбор', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: call.data == 'save_data')
def save_btn(call):
    print(call.data)
    message = call.message
    if call.message:
        if call.data == 'save_data':
            chat_id = message.chat.id
            message_id = message.message_id
            bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                 text='Данные сохранены!')

# @bot.callback_query_handler(func=lambda call: call.data == 'YES')
# def callback_inline(call):
#     print(call)
#     if call.data == 'yes':
#         go()

bot.polling()