#!/opt/python3.3/bin/python

import time
import discord
import logging
import random


try:
    import creds
except:
    print("Need valid creds.py to login")
    exit(1)


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='error.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()
client.login(creds.discordid, creds.discordpw)
user_agent = "Aphoenix's Grand Murloc Hunt for Discord"


roles = [
      'dk',
      'druid',
      'hunter',
      'mage',
      'monk',
      'paladin',
      'priest',
      'rogue',
      'shaman',
      'warlock',
      'warrior',
      ]


for role in roles:
    print(role)


if not client.is_logged_in:
    print('Login fail')
    exit(1)


@client.event
def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('--Server List--')
    for server in client.servers:
        print(server.name)


@client.event
def on_message(message):
    print(message.channel + ': ' + message.content)


client.run()
