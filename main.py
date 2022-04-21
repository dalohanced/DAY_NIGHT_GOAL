import telebot
import time
from telebot import types
bot = telebot.TeleBot(open("key12.txt").readline())

murkup=types.ReplyKeyboardMarkup(resize_keyboard=True)

item1=types.KeyboardButton("/1")
item2=types.KeyboardButton("")
item3=types.KeyboardButton("")
item4=types.KeyboardButton("")

murkup.add(item1,item2,item3,item4)

@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id,'Привет, этот бот будет напоминать тебе о твоей цели,напиши ее мне',reply_markup=murkup)

@bot.message_handler(content_types=['text'])

@bot.message_handler(commands=['1'])
def bred(message):

    bot.send_message(message.chat.id,"Твоя цель на сегодня:",reply_markup=murkup)

    txt = message.text

    a=txt

    bot.send_message(message.chat.id,a)

bot.polling(none_stop=True, interval=0)