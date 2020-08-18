import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.idle, activity=discord.Game('+help For Commands'))
    
    print('On')

@client.command()
async def help(ctx):
    await ctx.send('Type +code For Persistants PythonBot Code')

    
@client.command()
async def code(ctx):
    await ctx.send('https://github.com/Poitnless/pythonbot')


client.run(os.environ['token'])
