import os
import telebot

from hh_parsing import parse_data
from handle_data import handel_vacancies
from telebot import types

token = os.environ['token']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Бот готов к поиску вакансий')


@bot.message_handler(func=lambda message: message.text == "Показать вакансии")
def get_vacancy(message):
    raw_data = parse_data()
    data = handel_vacancies(raw_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Показать вакансии')
    markup.add(item1)

    if not data:
        bot.send_message(message.chat.id, 'Новых вакансий нет')
    else:
        for text in data[:10]:
            bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)



@bot.message_handler()
def another_answer(message):
    bot.send_message(message.chat.id, 'Неверный запрос. Нажмите кнопку "Показать вакансии"')


if __name__ == '__main__':
     bot.infinity_polling()
