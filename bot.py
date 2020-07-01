import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ':')

@client.event
async def on_ready():
    print('On')

client.run('NzI4MDA1MzY4ODczMjIyMTk0.Xv0GSw.MxbwM3r9PCMGMJeOALGxWTFTlm4')
