import key
import requests
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot(key.TOKEN)

url = 'https://www.cbr.ru/'

def parser(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    mass = soup.find_all('div', class_='col-md-2 col-xs-9 _right mono-num')
    res = [c.text for c in mass]
    return res


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item4 = telebot.types.KeyboardButton('USD')
    item5 = telebot.types.KeyboardButton('EUR')
    item6 = telebot.types.KeyboardButton('CNY')

    markup.add(item4, item5, item6)

    bot.send_message(message.chat.id, 'Добро пожаловать! Курс какой валюты хотите узнать? ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    if message.text == 'USD':   
        bot.send_message(message.chat.id, f'курс валюты: {parser(url)[0]}')
    elif message.text == 'EUR': 
        bot.send_message(message.chat.id, f'курс валюты: {parser(url)[2]}')
    elif message.text == 'CNY':
        bot.send_message(message.chat.id, f'курс валюты: {parser(url)[4]}')

bot.polling(none_stop=True)