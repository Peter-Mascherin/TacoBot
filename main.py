
import discord
import random
import json
import os
import requests
from keep_alive import keep_alive
from discord.ext import commands
from tacobotdatabase import TacoBotEconomy


client = commands.Bot(command_prefix="$")
database_eco = TacoBotEconomy()
commandlist = ['$hello','$rnum','$whoami','$test','$helpme','$uwu','$fact','joke','calc']
complimentlist = json.loads(open("compliments.json",encoding="utf8").read())

def getrandomfact():
    factrequest = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    factjson = json.loads(factrequest.text)
    return factjson['text']

def getrandomjoke():
    dadjokerequest = requests.get(url="https://icanhazdadjoke.com/",headers={"Accept":"application/json"})
    dadjoke = json.loads(dadjokerequest.text)
    return dadjoke['joke']

def randomnum():
    num = random.randint(0,100)
    return num

def helloembedmessage():
    embmsg = discord.Embed(title="TacoBot greeting!",description="Hello i am TacoBot, your multipurpose discord bot ready to fufill any task",colour=discord.Colour.green())
    embmsg.set_author(name=client.user,icon_url="https://cdn.discordapp.com/avatars/823384204183732304/68676285840eec1763141ac2abd97373.png?size=256")
    embmsg.set_thumbnail(url="https://cdn.discordapp.com/avatars/823384204183732304/68676285840eec1763141ac2abd97373.png?size=256")
    embmsg.add_field(name="Commands",value="To access a list of commands to use $helpme\nOne such command you can use is " + commandlist[random.randint(0,len(commandlist) - 1)],inline=True)
    embmsg.add_field(name="Support",value="If you need help with anything else please contact my creator, TheMajesticTaco#5235",inline=True)
    embmsg.set_footer(text="TacoBot created by TheMajesticTaco")
    return embmsg

def helpembedmessage():
    helpemb = discord.Embed(title="Help Screen",desscription="This is a embed help screen to show you the commands and what they do",colour=discord.Colour.blue())
    helpemb.set_author(name=client.user,icon_url="https://cdn.discordapp.com/avatars/823384204183732304/68676285840eec1763141ac2abd97373.png?size=256")
    helpemb.set_thumbnail(url="https://cdn.discordapp.com/avatars/823384204183732304/68676285840eec1763141ac2abd97373.png?size=256")
    helpemb.add_field(name="Command Name",value="$hello,$helpme,$whoami,$rnum,$test,$uwu,$fact,$joke,$calc",inline=True)
    helpemb.add_field(name="Command Description",value="to be added",inline=True)
    return helpemb
    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="In Mexico, say $hello"))
    print('We have logged in as {0.user}'.format(client))

@client.command(name="test")
async def testcommand(ctx):
    await loggingmethod(ctx)
    await ctx.message.reply("Your command works and the bot is alive")

@client.command(name="hello")
async def hellocommand(ctx):
    await loggingmethod(ctx)
    theembed = helloembedmessage()
    await ctx.message.channel.send(embed=theembed)

@client.command(name="rnum")
async def rnumcommand(ctx):
    await loggingmethod(ctx)
    answer = str(randomnum())
    await ctx.message.reply("Your number is: " + answer)

@client.command(name="whoami")
async def whoamicommand(ctx):
    await loggingmethod(ctx)
    await ctx.message.reply("You are " + str(ctx.message.author), mention_author=True)

@client.command(name="helpme")
async def helpcommand(ctx):
    await loggingmethod(ctx)
    helpembed = helpembedmessage()
    await ctx.message.reply(embed=helpembed,mention_author=True)

@client.command(name="uwu")
async def uwucommand(ctx):
    await loggingmethod(ctx)
    await ctx.message.reply(complimentlist[random.randint(0,(len(complimentlist)-1))])

@client.command(name="fact")
async def factcommand(ctx):
    await loggingmethod(ctx)
    thefact = getrandomfact()
    await ctx.message.reply(thefact)

@client.command(name="joke")
async def jokecommand(ctx):
    await loggingmethod(ctx)
    thejoke = getrandomjoke()
    await ctx.message.reply(thejoke)

@client.command(name="calc")
async def calculatorcommand(ctx,expression):
    await loggingmethod(ctx)
    try:
        resultstring = str(eval(expression))
    except:
        resultstring = "Calulation error, please check your expression to fix any errors in expression"
    await ctx.message.channel.send(expression + " = " + resultstring)

async def loggingmethod(context):
    if context.message.author == client.user:
        return
    else:
        print(context.message.author , " said: " , context.message.content , " in " , context.message.guild)

@client.command(name="check")
async def checkcommand(ctx):
    await loggingmethod(ctx)
    amount = str(database_eco.getDocuments())
    await ctx.message.reply("You have " + amount + " document(s) in the database")


@client.command(name="eco")
async def ecocommand(ctx,moderaw,money):
    await loggingmethod(ctx)
    mode = moderaw.strip().lower()
    dis_id = ctx.message.author.id
    dis_name = ctx.message.author
    if(mode == "add"):
        theresult = database_eco.addAmount(discord_id=dis_id,discord_name=dis_name,amount=money)
    await ctx.message.reply("Result of function: " + theresult)


keep_alive()
client.run(os.getenv('TOKEN'))

