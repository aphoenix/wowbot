#!/opt/python3.3/bin/python

import praw
import time
import discord
import logging
import random


try:
    import creds
except:
    print "Need valid creds.py to login"
    exit()


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='error.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()
client.login(discordid, discordpw)


with open(quotes.txt) as f:
    quotes = f.readlines()
with open(helpmessage.txt) as f:
    helpmessage = f.read()
with open(roles.txt) as f:
    roles = f.readlines()

lockroles = ["Moderator", "Chat Moderator", "Twitterbot"]
cannotset = """Sorry I could not set your class because I did not
            recognize the class you chose. Type `@WoWbot help` for
            more information."""

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
    for client.user.name in message.mentions:
        if message.author.name == "aphoenix":
            if 'roles' in message.content.lower():
                for server in client.servers:
                    if server.name == 'wow':
                        wowroles = ''
                        for role in server.roles:
                            wowroles += '`'
                            wowroles += role.name
                            wowroles += '`'
                            wowroles += ': '
                            wowroles += role.id
                            wowroles += '\n'
                        client.send_message(message.channel, wowroles[1:])


        if 'help' in message.content.lower():
            client.send_message(message.channel, helpmessage)
       
            
        elif 'class' in message.content.lower():
            doit = True
            for role in message.author.roles:
                if role.name in lockroles:
                    doit = False
            if 'remove' in message.content.lower() and doit:
                client.replace_roles(message.author,client.servers[1].roles[0])
                break
            try:
                myrole = next(role for role in roles if role in message.content.lower().split())
            except:
                myrole = "unrecognized"
                doit = False
                client.send_message(message.author, cannotset)
            print('setting ' + message.author.name + ' as ' + myrole)
            for server in client.servers:
                if server.name == 'wow' and doit:
                    for role in server.roles:
                        if (myrole == role.name):
                            client.replace_roles(message.author,role)


        elif 'rickme' in message.content.lower():
            client.send_message(message.channel, random.choice(quotes))
        

client.run()
