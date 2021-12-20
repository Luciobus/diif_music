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

load_dotenv()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
bot = telebot.TeleBot(os.getenv('TOKEN'))
print(sys.getdefaultencoding())


def yt_search(text):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + urllib.parse.quote(text + " music"))
    video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())[0]
    # print(video_id)
    return "https://www.youtube.com/watch?v=" + video_id + "\n"


def spotify_search(text):
    return spotify.search(q=text, type='track')['tracks']['items'][0]['external_urls']['spotify'] + "\n"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello in Google Sheets Bot")


@bot.message_handler(func=lambda m: True)
def get_links(message):
    search_text = message.text
    print(search_text)
    link = yt_search(search_text) + spotify_search(search_text)
    print(link)
    bot.reply_to(message, link)
    # bot.reply_to(message, message.text)


bot.infinity_polling()
