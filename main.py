
from math import trunc
import discord
import random
import os
from keep_alive import keep_alive

client = discord.Client()
commandlist = ['$hello','$rnum','$whoami','$test','$help']

def randomnum():
    num = random.randint(0,100)
    return num

def embedmessage():
    embmsg = discord.Embed(title="TacoBot greeting!",description="Hello i am TacoBot, your multipurpose discord bot ready to fufill any task",colour=discord.Colour.green())
    embmsg.set_author(name=client.user,icon_url="https://cdn.discordapp.com/avatars/823384204183732304/68676285840eec1763141ac2abd97373.png?size=256")
    embmsg.set_thumbnail(url="https://cdn.discordapp.com/avatars/823384204183732304/68676285840eec1763141ac2abd97373.png?size=256")
    embmsg.add_field(name="Commands",value="To access a list of commands to use $help\nOne such command you can use is " + commandlist[random.randint(0,len(commandlist) - 1)],inline=True)
    embmsg.add_field(name="Support",value="If you need help with anything else please contact my creator, TheMajesticTaco#5235",inline=True)
    embmsg.set_footer(text="TacoBot created by TheMajesticTaco")
    return embmsg
    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="In Mexico, say $hello"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        print(message.author , " said: " , message.content , " in " , message.guild)

    if message.content.startswith('$hello'):
        thembed = embedmessage()
        await message.channel.send(embed=thembed)
    
    if message.content.startswith('$rnum'):
        answer = str(randomnum())
        await message.reply("Your number is: " + answer)
    
    if message.content.startswith('$whoami'):
        await message.reply("You are " , message.author, mention_author=True)
    
    if message.content.startswith('$help'):
        await message.reply('My current commands are:\n$hello\n$rnum\n$whoami\n$help',mention_author=False)
    
    if message.content.startswith('$test'):
        await message.reply('This is a just a testing command. I am alive!')
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)
        

keep_alive()
client.run(os.getenv('TOKEN'))