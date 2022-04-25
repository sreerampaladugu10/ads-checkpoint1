import discord
from discord.ext import commands
import random
import var
import config

client = commands.Bot(command_prefix="")

#lists for chat functuonality

from var import coin  
from var import answers
from var import guns
from var import agents


@client.event
async def on_ready():
    print("bot is ready")

@client.command(aliases=["this is so sad", "sed","sad","so sad"])
async def seed(ctx):
 await ctx.send("play despasito")  

@client.event
async def on_message(ctx):
    
    #guns
    if 'gun' in ctx.content:
        await ctx.channel.send(f"{random.choice(guns)}")   
    elif 'playground' in ctx.content:
        await ctx.channel.send(f"{random.choice(guns)}") 

    #general msgs    
    elif 'ketts' in ctx.content:
        await ctx.channel.send(f"{random.choice(answers)}")   
    elif 'hey' in ctx.content:
        await ctx.channel.send(f"{random.choice(answers)}")

    #coinflip    
    elif 'coinflip' in ctx.content:
        await ctx.channel.send(f"{random.choice(coin)}")   
    elif 'flip' in ctx.content:
        await ctx.channel.send(f"{random.choice(coin)}") 
                
    #agents
    elif 'agents' in ctx.content:
        await ctx.channel.send(f"{random.choice(agents)}")   
  
    #ff
    elif 'surrender' in ctx.content:
        await ctx.channel.send(f"{random.choice(agents)}") 
    
   



from datetime import datetime
from pytz import timezone
  
format = "%Y-%m-%d %I:%M:%S:%p"
  
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
  
# Convert to Asia/Kolkata time zone
indiautc = now_utc.astimezone(timezone('Asia/Kolkata'))
ind=(indiautc.strftime(format))

phutc = now_utc.astimezone(timezone('Asia/Manila'))
ph=(phutc.strftime(format))

singaporeutc = now_utc.astimezone(timezone('Asia/Singapore'))
sg=(singaporeutc.strftime(format))

scutc = now_utc.astimezone(timezone('America/New_York'))
sc=(scutc.strftime(format))



@client.event
async def on_message(message):
    if message.content == "time":
        await message.channel.send("the time in singapore is"+" "+sg+"\n"+"the time in philippines is"+" "+ph+"\n"+" "+"the time in India is"+ind+" "+"\n"+"the time in south carolina is"+" "+sc+"\n", reference=message)


client.run(config.api_key)
