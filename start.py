import feedparser
import logging
import telebot
from telebot import types
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
itembtn1 = types.KeyboardButton('Анекдоты')
itembtn2 = types.KeyboardButton('Истории')
keyboard.add(itembtn1, itembtn2)

keyEmpty = types.ReplyKeyboardMarkup(row_width=2)


@bot.message_handler(commands=["start"])
def cmd_start(m):
    bot.send_message(m.chat.id, 'Бот присылает 10 лучших анекдотов/историй из rss anekdot.ru по твоему выбору',
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def pub(m):
    if m.text == 'Анекдоты':
        f = feedparser.parse("https://www.anekdot.ru/rss/export_j.xml")
        for entry in f['entries']:
            if len(entry['description']) < 1500:
                bot.send_message(m.chat.id, entry['description'].replace('<br>', "\n"), reply_markup=keyboard,
                                 disable_web_page_preview=True)
    elif m.text == 'Истории':
        f = feedparser.parse("https://www.anekdot.ru/rss/export_o.xml")
        for entry in f['entries']:
            if len(entry['description']) < 1500:
                bot.send_message(m.chat.id, entry['description'].replace('<br>', "\n"), reply_markup=keyboard,
                                 disable_web_page_preview=True)
    else:
        bot.send_message(m.chat.id, '', reply_markup=keyboard)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
bot.polling(none_stop=True)
print('started')
