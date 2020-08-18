import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():
    print('On')

@client.command()
async def ping(ctx):
    await ctx.send('hello')

client.run('NzQ1MjExMTA3NjIyMjU2Njkw.Xzud7Q.l_FUhLO9PxpFge3ncHXTCe8qWCk')
