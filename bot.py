import config
import telebot

from hh_parsing import parse_data
from handle_data import handel_vacancies
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['check'])
def get_vacancy(message):
    raw_data = parse_data()
    data = handel_vacancies(raw_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Показать вакансии')
    markup.add(item1)

    for text in data[:10]:
        bot.send_message(message.chat.id, text, reply_markup=markup)




if __name__ == '__main__':
     bot.infinity_polling()
