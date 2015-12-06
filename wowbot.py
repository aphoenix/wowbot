#!/opt/python3.3/bin/python

import praw
import time
import discord
import logging
import random
import re

try:
    import creds
except:
    print("Need valid creds.py to login")
    exit()


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='error.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()
client.login(creds.discordid, creds.discordpw)
user_agent = "Aphoenix's Discord / Reddit integration system."
thing_limit = 25
last_summons = time.time()

with open('quotes.txt') as f:
    quotes = f.readlines()
with open('helpmessage.txt') as f:
    helpmessage = f.read()
with open('rags.txt') as f:
    rags = f.readlines()
with open('8ball.txt') as f:
    ball = f.readlines()


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


lockroles = ["Moderator", "Chat Moderator", "Twitterbot"]
cannotset = """Sorry I could not set your class because I did not
            recognize the class you chose. Type `@WoWbot help` for
            more information."""


r = praw.Reddit(user_agent=user_agent)
r.login(creds.redditid,creds.redditpw) #replace with OAuth soon


wowsub = r.get_subreddit('WoW')


if not client.is_logged_in:
    print('Login fail')
    exit(1)


def say_reddit_submission(submission):
    saythis = submission.short_link
    client.send_message(message.channel,saythis)


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
    if message.author.id != client.user.id:
        if message.author.id == "113097494489006080":
            if '!roles' in message.content.lower():
                print(message.author.name + ': ' + message.content)
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


        if message.author.id == "77511942717046784":
            if '!butts' in message.content.lower():
                client.send_message(message.channel, '<3')


        if '!help' in message.content.lower():
            client.send_message(message.channel, helpmessage)


        elif '!class' in message.content.lower():
            print(' class is true')
            doit = True
            for role in message.author.roles:
                if role.name in lockroles:
                    doit = False
            if 'remove' in message.content.lower() and doit:
                client.replace_roles(message.author,client.servers[1].roles[0])
                print('setting ' + message.author.name + ' to have no class')
            try:
                myrole = next(role for role in roles if role in message.content.lower().split())
                print(myrole)
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
                            client.delete_message(message)


        elif '!rickme' in message.content.lower():
            client.send_message(message.channel, random.choice(quotes))


        elif '!purge' in message.content.lower():
            for server in client.servers:
                if server.name == 'wow':
                    purged = random.choice(server.members)
                    ragnarquote = random.choice(rags)
                    saythis = ragnarquote + '\n'
                    saythis += purged.name + ' has been purged.'
                    client.send_message(message.channel,saythis)


        elif '!sticky' in message.content.lower():
            if 'bottom' in message.content.lower():
                sub = wowsub.get_sticky(bottom=True)
            else:
                sub = wowsub.get_sticky()
            say_reddit_submission(sub, message)


        elif '!hot' in message.content.lower():
            sub = random_reddit_submission('hot')
            say_reddit_submission(sub, message)


        elif '!rising' in message.content.lower():
            sub = random_reddit_submission('rising')
            say_reddit_submission(sub, message)


        elif '!new' in message.content.lower():
            sub = random_reddit_submission('new')
            say_reddit_submission(sub, message)


        elif '!controversial' in message.content.lower():
            sub = random_reddit_submission('controversial')
            say_reddit_submission(sub, message)


        elif '!rickme' in message.content.lower():
            client.send_message(message.channel, random.choice(quotes))

        elif '!purge' in message.content.lower():
            for server in client.servers:
                if server.name == 'wow':
                    purged = random.choice(server.members)
                    ragnarquote = random.choice(rags)
                    saythis = ragnarquote + '\n'
                    saythis += purged.name + ' has been purged.'
                    client.send_message(message.channel,saythis)

        #elif '!choice' in message.content.lower():
        #    words = []
        #    for word in message.content.lower:
        #        if word != '!choice':
        #            words.append(word)
        #    saythis = 'I choose ' + random.choice(words) + '.'
        #    client.send_message(message.channel,saythis)


        elif '!8ball' in message.content.lower():
            question = message.content
            question = re.sub('!8ball', '', question)
            saythis = message.author.name + ' asked: _' + question + '_\n'
            saythis += 'The 8 Ball says: ' + random.choice(ball)
            client.send_message(message.channel, saythis)


        #elif '!aphoenix' in message.content.lower():
        #    global last_summons
        #    time_passed = time.time() - last_summons 
        #    print(time_passed)
        #    if time_passed > 3600:
        #        saythis = message.author.name + ' wants you in Discord'
        #        try:
        #            r.send_message('aphoenix', 'Discord Summons', saythis)
        #            client.send_message(message.channel, 'Aphoenix has been summoned.')
        #            last_summons = time.time()
        #        except:
        #            pass
        #    else:
        #        client.send_message(message.channel, 'You are doing too much aphoenix summoning.')


client.run()
