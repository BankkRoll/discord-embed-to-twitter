import os
import discord
from time import sleep
import asyncio
import tweepy



discord_token = os.environ['discord_token']
access_token_secret1 = os.environ['access_token_secret']
access_token1 = os.environ['access_token']
consumer_secret1 = os.environ['consumer_secret']
consumer_key1 = os.environ['consumer_key']


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
