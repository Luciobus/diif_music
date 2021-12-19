# -*- coding: utf-8 -*-
import telebot
import os
from dotenv import load_dotenv
import urllib.request
import urllib.parse
import re
import sys

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))
print(sys.getdefaultencoding())


def yt_search(text):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + urllib.parse.quote(text))
    video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())[0]
    # print(video_id)
    return "https://www.youtube.com/watch?v=" + video_id


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello in Google Sheets Bot")


@bot.message_handler(func=lambda m: True)
def get_links(message):
    search_text = message.text
    print(search_text)
    link = yt_search(search_text)
    print(link)
    bot.reply_to(message, link)
    # bot.reply_to(message, message.text)


bot.infinity_polling()
