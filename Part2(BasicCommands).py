import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

#On ready function(this isn't needed for a command)
@client.event
async def on_ready():
    print("The bot is ready.")

#Command that makes bot say "Hi!"
@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

#Command that makes bot say "Hi!"
@client.command()
async def printinformation(ctx):


client.run("ODA4MzExNzc1MjA0MzQzODM4.YCEtAA.hQnYndW7xlyXbSCW1bpyCdA7uJI")
