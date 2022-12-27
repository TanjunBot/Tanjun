from logging import exception
import discord
from discord.ext import commands
from pathlib import Path
import DiscordUtils
import sys
import traceback

# Get configuration.json
from pymongo import MongoClient

cluster = MongoClient("")

db = cluster["Main"]
collection = db["prefixe"]


# Intents
intents = discord.Intents.all()
intents.members = True


bot = commands.Bot("HAHHAHAHAHAHAHA LOLLLLLLLLLLLLLLLLLLLLLLLLLLL", intents = intents)
tracker = DiscordUtils.InviteTracker(bot)

# Load cogs
initial_extensions = [
    "Cogs.countingsystem",  #
    "Cogs.Economy",         #
    "Cogs.Funcommands",     
    "Cogs.Giveaway",        #
    "Cogs.Levelsystem",     #
    "Cogs.Logging",         
    "Cogs.ModCmds",         #
    #"Cogs.musicbot",        #
    #"Cogs.MusikQuiz",       #
    "Cogs.secruitysystem",  #
    "Cogs.ServerEinrichten",  #
    "Cogs.Splitroles",
    "Cogs.support",         #
    "Cogs.Umfrage",         #
    "Cogs.Utility",#
    "Cogs.Help",
    "Cogs.Birthday",#
    "Cogs.minigames",
    #"Cogs.tmp"
    "Cogs.reloader"
]

print(initial_extensions)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(f"{extension} loaded!")
        except Exception as e:
            print(f"Failed to load extension {extension}")
            raise e

@bot.event
async def on_error(error, *args, **kwargs):
  channel = bot.get_channel(966713797056274552)
  tracebacks = ""
  try:
    for tb in traceback.format_tb(sys.exc_info()[2]):
          tracebacks += tb
  except:
      tracebacks = sys.exc_info()[2]
  m = f"**__Ich habe einen Error!__**\n\n`Error:`\n{error}\n\n`args:`\n{args}\n\n`kwargs:`\n{kwargs}\n\n`sys.exc_info type:`\n{sys.exc_info()[0]}\n\n`sys.exc_info value:`\n{sys.exc_info()[1]}\n\n`traceback:`\n{tracebacks}\n\nBitte behebe den Error :) es kann sein, dass ich neu gestartet werden muss. Benutze dazu den `/restart` befehl!"
  if len(m) <= 2000:
      await channel.send(m)
  else:
      while len(m) > 2000:
          await channel.send(m[0:2000])
          m = m[2000:]



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(f"{len(bot.guilds)} Benutzen den Bot!")
    await bot.change_presence(activity=discord.Streaming(name="Katzenbrotsalammi", url="https://www.twitch.tv/entcheneric"))
    print(discord.__version__)

bot.run("")