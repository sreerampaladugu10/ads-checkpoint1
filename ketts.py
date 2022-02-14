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

        
client.run(config.api_key)
