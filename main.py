
import discord
import random
import os
from keep_alive import keep_alive

client = discord.Client()


def randomnum():
    num = random.randint(0,100)
    return num
    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Behind you"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$rnum'):
        answer = str(randomnum())
        await message.reply("Your number is: " + answer)
    
    if message.content.startswith('$whoami'):
        await message.reply("You are stupid", mention_author=True)
    
    if message.content.startswith('$help'):
        await message.reply('My current commands are:\n$hello\n$rnum\n$whoami\n$help',mention_author=False)
    
    if message.content.startswith('$test'):
        await message.reply('This is a just a testing command. I am alive!')

keep_alive()
client.run(os.getenv('TOKEN'))