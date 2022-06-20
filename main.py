import requests
import telebot
import datetime
from newsapi.newsapi_client import NewsApiClient
import time
import threading

#setting up the bot
bot = telebot.TeleBot("5053564211:AAErkWczkc3a_opoTtvTPfzGpEZi4NOyyYM")

def latest():
    prev_data = None
    api = NewsApiClient(api_key='6d9c618d270046f8a902eb5917123cbc')

    while True:        
        api = NewsApiClient(api_key='6d9c618d270046f8a902eb5917123cbc')
        crypto_data =  api.get_everything(q='war', language='en', page_size=20)
        main=crypto_data['articles'][1]
        if prev_data != main:
            author = main['author']
            title = main['title']
            description = main['description']

            bot.send_message("-651098387", text=f"{main}")
            prev_data=main
            


        else:
            pass
        
        war_data =  api.get_everything(q='war', language='en', page_size=20)
        main=war_data['articles'][1]
        if prev_data != main:
            author = main['author']
            title = main['title']
            description = main['description']

            bot.send_message("-651098387", text=f"{main}")
            prev_data=main
            


        else:
            pass

        time.sleep(10)
t1 = threading.Thread(name="thread", target=latest)
t1.start()
bot.infinity_polling()