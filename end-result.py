import os
import discord
from time import sleep
import asyncio
import tweepy

# Setup Discord bot
discord_token = os.environ['discord_token']
client=discord.Client()

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

# Initiate Tweepy + Discord APIs
auth=tweepy.OAuthHandler(consumer_key1,consumer_secret1)
auth.set_access_token(access_token1,access_token_secret1)
api = tweepy.API(auth)

# Channel IDs
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
      print(f"{guild.name} - {guild.id}")
      insguilds = insguilds + 1
      print("Guilds: " + str(insguilds))

@client.event
async def on_message(message):
    # Ignore messages from self
    if message.author == client.user:
        return
    # Extract needed variables
    channel = str(message.channel.id)
    # Channel ID 1
    if channel == discord_channel_id1:
        api.update_status(
            message.embeds[0].description + "\n" + message.embeds[0].image.url
        )
        print('Tweet posted from channel 1')
    # Channel ID 2
    if channel ==discord_channel_id2:
        api.update_status(status=message.content)
        print('Tweet posted from channel 2')
    # Channel ID 3
    if channel ==discord_channel_id3:
        api.update_status(status=message.content)
        print('Tweet posted from channel 3')

# Initiate bot
async def main_func():
    await client.start(discord_token)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main_func())
