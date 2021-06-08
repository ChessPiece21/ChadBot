"Ok."

import os
import random

import discord
from discord.ext import commands

description = "Gives you Chad gifs, ok?"
bot = commands.Bot(command_prefi="/", description=description)

gifs = [
    "https://media.giphy.com/media/xT9IgrlyzJlE6ljtS0/giphy.gif",
    "https://thumbs.gfycat.com/ForcefulHopefulJapanesebeetle-max-1mb.gif",
    "https://tenor.com/MWVF.gif",
    "https://tenor.com/TKX1.gif",
    "https://tenor.com/7geU.gif",
    "https://tenor.com/GS73.gif",
    "https://media1.tenor.com/images/91fc0b7471e932b7eacdf0af056a3ee2/tenor.gif?itemid=16694978",
    "https://thumbs.gfycat.com/FluffySomberGazelle-max-1mb.gif",
    "https://nerdbot.com/wp-content/uploads/2020/06/ForcefulHopefulJapanesebeetle-size_restricted.gif",
]

@bot.event
async def on_ready():
	print("Logged in.")

@bot.command(description='Returns a random GIF of Chad saying "ok."'
async def ok(ctx):
	print("Ok.")
	await ctx.send(random.choice(gifs))

# DISCORDTOKEN ENV VAR MUST BE SET OR SERVER WILL NOT RUN
# EXPORT DISCORDTOKEN=XXXXXXXXXXXXXXX
bot.run(os.environ.get("DISCORDTOKEN"))
