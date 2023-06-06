# encoding=utf-8

import telebot
from telebot.types import *

token = "6002115800:AAHyGx9OWSAt6sefksF8a-H5I0rGLUlCjxI"
bot = telebot.TeleBot(token)

# Markup
markup = ReplyKeyboardMarkup(True)

markup.row("✨Discord✨", "game")


@bot.message_handler(content_types=['text'])
def textMessage(message: Message):
    text = message.text

    if text == "start" or text == "/start":
        bot.send_message(message.chat.id,
                         f"Приветствую тебя, {message.from_user.first_name}! Я бот от которого ты можешь узнать много нового о нашем сервере. На него можно зайти по айпи d14.gamely.pro:20458 с версией 1.16.5",
                         reply_markup=markup)
    elif text == "✨Discord✨":
        bot.send_message(message.from_user.id,
                         "На наш дискорд сервер ты можешь перейти по этой ссылке https://discord.gg/Q3eKcrZaBe")
    elif text == "game":
        bot.send_message(message.from_user.id, "https://t.me/DonGriefBot/game")


bot.polling(none_stop=True)
