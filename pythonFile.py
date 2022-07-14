# Dudas:
# 1. Por qué al hacer 'view - command palette - python:select interpreter' me ha reconocido el import? 



#!/usr/bin/env python3

import tweepy
import schedule
import random
from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


a_column=["Mami, ", "Bebé, ", "Prinsesa, ", "Mamasita, "]
b_column=["yo quiero ", "yo puedo ", "yo vine a ", "voy a "]
c_column=["encendelte ", "amalte ", "perrialte ", "jugal "]
d_column=["suave ", "lento ", "rápido ", "fuelte "]
e_column=["hasta que salga el sol ","toda la noche ", "hasta el amanesel ","todo el día "]
f_column=["sin paral.","sin compromiso.","feis to feis.", "sin miedo."]

all_columns = [a_column, b_column, c_column, d_column, e_column, f_column]



def generate_lyrics():
    

    final_str=""

    for i in range(0, 3):

        if i<2:    # Versos

            for column in all_columns:

                final_str += column[random.randint(0, len(column)-1)]


        if i == 2:    # Chorus

            for i in range (1, 4):

                final_str += all_columns[i][random.randint(0, len(a_column)-1)].capitalize()

            final_str = final_str[:-1] + '.'

        final_str += '\n'
    
    print(final_str)

    api.update_status(final_str)



def main():
    
    schedule.every(3).minutes.do(generate_lyrics)

    while True:

        schedule.run_pending()


if __name__ == "__main__":
    main()    
  