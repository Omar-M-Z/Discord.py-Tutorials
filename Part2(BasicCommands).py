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

#Command that makes bot send information about the context of the command
@client.command()
async def sendinformation(ctx):
    #sends name of server the command is sent in
    await ctx.send(ctx.guild)
    #sends name of the user that sends the command
    await ctx.send(ctx.author)
    #sends name of the channel in which the command was sent
    await ctx.send(ctx.channel)
    
#Command that takes two arguments from user and sends them
@client.command()
async def sendarguments(ctx, arg1, arg2):
    await ctx.send(arg1)
    await ctx.send(arg2)

#Command that with name that is different from the name of the function and has aliases
@client.command(name = "helloworld", aliases = ["hiworld", "greetingsworld"])
async def examplecommand(ctx):
    await ctx.send("Hello World")

#Command that checks if user has permission to kick members from a server
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx):
    await ctx.send("You can kick members and abuse your permissions!")

client.run(<Bot Token Goes Here>)
