# -*- coding: utf-8 -*-
import telebot
import os
from dotenv import load_dotenv
import urllib.request
import urllib.parse
import re
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import requests

load_dotenv()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
bot = telebot.TeleBot(os.getenv('TOKEN'))
print(sys.getdefaultencoding())


def yt_search(text):
    while True:
        try:
            html = urllib.request.urlopen(
                "https://www.youtube.com/results?search_query=" + urllib.parse.quote(text + " music"))
            video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())[0]
            return "https://www.youtube.com/watch?v=" + video_id + "\n"
        except requests.exceptions.ConnectionError:
            time.sleep(0.01)
            continue
        except BaseException as err:
            print(err)
            raise


def spotify_search(text):
    while True:
        try:
            return spotify.search(q=text, type='track')['tracks']['items'][0]['external_urls']['spotify'] + "\n"
        except requests.exceptions.ConnectionError:
            time.sleep(0.01)
            continue
        except BaseException as err:
            print(err)
            raise


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hello this is music search bot. Type your query and get links\n Привет, это бот поиска музыки. Напиши запрос и я выдам тебе ссылки")


@bot.message_handler(func=lambda m: True)
def get_links(message):
    search_text = message.text
    print(search_text)
    link = "The most relevant results/Наиболее подходящие результаты:\n" + yt_search(search_text) + spotify_search(
        search_text)
    print(link)
    bot.reply_to(message, link)
    # bot.reply_to(message, message.text)


bot.infinity_polling()
