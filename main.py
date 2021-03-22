import discord
import random

client = discord.Client()


def randomnum():
    num = random.randint(0,100)
    return num
    
    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$rnum'):
        answer = str(randomnum())
        await message.channel.send("Your number is: " + answer)
    
    if message.content.startswith('$whoami'):
        await message.reply("You are stupid", mention_author=True)
    
    if message.content.startswith('$help'):
        await message.reply('My current commands are:\n$hello\n$rnum\n$whoami\n$help',mention_author=False)

client.run("ODIzMzg0MjA0MTgzNzMyMzA0.YFgCTA.q1nJh_scF-kdIiNqDtIMUFGLZSA")