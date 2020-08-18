import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Type +help For Commands')
    
    print('On')

@client.command()
async def ping(ctx):
    await ctx.send('hello')

client.run(os.environ['token'])
