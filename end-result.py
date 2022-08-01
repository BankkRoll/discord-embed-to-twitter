import os
import discord
from time import sleep
import asyncio
import tweepy



discord_token = os.environ['discord_token']
    #here is where you will put information for your twitter developer api keys
    #this will be twitter bot 1
access_token_secret1 = os.environ['access_token_secret1']
access_token1 = os.environ['access_token1']
consumer_secret1 = os.environ['consumer_secret1']
consumer_key1 = os.environ['consumer_key1']
    #here is where you will put information for your twitter developer api keys
    #this will be twitter bot 2
access_token_secret2 = os.environ['access_token_secret2']
access_token2 = os.environ['access_token2']
consumer_secret2 = os.environ['consumer_secret2']
consumer_key2 = os.environ['consumer_key2']
    #here is where you will put information for your twitter developer api keys
    #this will be twitter bot 3
access_token_secret3 = os.environ['access_token_secret3']
access_token3 = os.environ['access_token3']
consumer_secret3 = os.environ['consumer_secret3']
consumer_key3 = os.environ['consumer_key3']

auth=tweepy.OAuthHandler(consumer_key1,consumer_secret1)
auth.set_access_token(access_token1,access_token_secret1)
api = tweepy.API(auth)
client=discord.Client()

    #here are your channels ids for each bot
discord_channel_id1='000000000000000000'
discord_channel_id2='000000000000000000'
discord_channel_id3='000000000000000000'



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    sleep(0.5)
    print("A list of all servers where the bot is on:")
    # List of all Servers the Bot is
    insguilds = 0
    for guild in client.guilds:
      print("%s - %s" % (guild.name, guild.id))
      insguilds = insguilds + 1
      print("Guilds: " + str(insguilds))



@client.event
async def on_message(message):
    if message.author != client.user and str(message.channel.id) ==discord_channel_id1 :
        img = message.embeds[0].image.url
        desc =  message.embeds[0].description 
        api.update_with_media(img, desc)
        print('Tweet posted from channel 1')
    
    if message.author != client.user and str(message.channel.id) ==discord_channel_id2 :
        api.update_status(status=message.content)
        print('Tweet posted from channel 2')
    
    if message.author != client.user and str(message.channel.id) ==discord_channel_id3 :
        api.update_status(status=message.content)
        print('Tweet posted from channel 3')
    



async def main_func():
    await client.start(discord_token)


asyncio.get_event_loop().run_until_complete(main_func())
