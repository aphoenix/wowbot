#!/opt/python3.3/bin/python

import discord
import logging
 
# Set up the logging module to output diagnostic to the console.
logging.basicConfig()
 
client = discord.Client()
client.login('andrew@aphoenix.ca', 'n0twr0ng$$3')
 
if not client.is_logged_in:
    print('Logging in to Discord failed')
    exit(1)
@client.event
def on_message(message):
    if message.content.startswith('!purge'):
        if message.author == client.user:
            print('Purging')
            if message.channel.name == 'class-colors':
                for messages in client.logs_from(message.channel):
                    client.delete_message(messages)
    if message.content.startswith('!butts'):
        client.send_message(message.channel, message.channel.name)
   
    if message.channel.name == 'class-colors':
        arservers = client.servers
        fuckyouroleids = message.author.roles
        print('pre role loop')
        randomrole = ''
        for butts in arservers:
            print('inside server loop')
            if butts.name == 'RhinoTest':
                arroles1 = butts.roles
                print('inside name if')
                for fuckyou1 in arroles1:
                    print('inside ID loop')
                    randomrole = fuckyou1
        DruidID = randomrole
        LockID = randomrole
        WarriorID = randomrole
        RogueID = randomrole
        DeathKnightID = randomrole
        HunterId = randomrole
        MageID = randomrole
        MonkID = randomrole
        PaldinID = randomrole
        PriestID = randomrole
        ShamanID = randomrole
        DemonHunterID = randomrole
        print('preloop')
        for nam in arservers:
            print('inside server loop')
            if nam.name == 'RhinoTest':
                arroles = nam.roles
                print('inside name if')
                for fuckyou in arroles:
                    print('inside ID loop')
                    if fuckyou.name == 'Druid':
                        DruidID = fuckyou
                    if fuckyou.name == 'Warlock':
                        LockID = fuckyou
                    if fuckyou.name == 'Warrior':
                        WarriorID = fuckyou
                    if fuckyou.name == 'Rogue':
                        RogueID = fuckyou
                    if fuckyou.name == 'DK':
                        DeathKnightID = fuckyou
                    if fuckyou.name == 'Hunter':
                        HunterId = fuckyou
                    if fuckyou.name == 'Mage':
                        MageID = fuckyou
                    if fuckyou.name == 'Monk':
                        MonkID = fuckyou
                    if fuckyou.name == 'Paladin':
                        PaldinID = fuckyou
                    if fuckyou.name == 'Priest':
                        PriestID = fuckyou
                    if fuckyou.name == 'Shaman':
                        ShamanID = fuckyou
                    if fuckyou.name == 'DH':
                        DemonHunterID = fuckyou
        print('outsideloop?')
        if 'druid' in message.content.lower():
            print('giving druid')
            client.replace_roles(message.author,DruidID)
        elif 'warlock' in message.content.lower():
            print('giving warlock')
            client.replace_roles(message.author,LockID)
        elif 'shaman' in message.content.lower():
            print('giving ShamanID')
            client.replace_roles(message.author,ShamanID)
        elif 'paladin' in message.content.lower():
            print('giving PaldinID')
            client.replace_roles(message.author,PaldinID)
        elif 'monk' in message.content.lower():
            print('giving MonkID')
            client.replace_roles(message.author,MonkID)
        elif 'mage' in message.content.lower():
            print('giving MageID')
            client.replace_roles(message.author,MageID)
        elif 'priest' in message.content.lower():
            print('giving PriestID')
            client.replace_roles(message.author,PriestID)
        elif 'hunter' in message.content.lower():
            print('giving HunterId')
            client.replace_roles(message.author,HunterId)
        elif 'death knight' in message.content.lower():
            print('giving DeathKnightID')
            client.replace_roles(message.author,DeathKnightID)
        elif 'rogue' in message.content.lower():
            print('giving RogueID')
            client.replace_roles(message.author,RogueID)
        elif 'warrior' in message.content.lower():
            print('giving WarriorID')
            client.replace_roles(message.author,WarriorID)
        elif 'demon hunter' in message.content.lower():
            print('giving DemonHunter')
            client.replace_roles(message.author,DemonHunterID)
       
           
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
client.run()
