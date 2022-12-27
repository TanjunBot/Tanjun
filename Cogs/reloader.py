import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
import asyncio

dev_list = [471036610561966111, 760155365710102549, 766350321638309958, 689565769230712866, 810484550727761940]

class Reloader(commands.Cog):

    def __init__(self, client):
        self.client = client
          
    möglichkeitenArt = [
        discord.OptionChoice(name = "countingsystem", value = "countingsystem"),
        discord.OptionChoice(name = "Economy", value = "Economy"),
        discord.OptionChoice(name = "Funcommands", value = "Funcommands"),
        discord.OptionChoice(name = "Giveaway", value = "Giveaway"),
        discord.OptionChoice(name = "Levelsystem", value = "Levelsystem"),
        discord.OptionChoice(name = "Logging", value = "Logging"),
        discord.OptionChoice(name = "ModCmds", value = "ModCmds"),
        discord.OptionChoice(name = "musicbot", value = "musicbot"),
        discord.OptionChoice(name = "MusikQuiz", value = "MusikQuiz"),
        discord.OptionChoice(name = "secruitysystem", value = "secruitysystem"),
        discord.OptionChoice(name = "ServerEinrichten", value = "ServerEinrichten"),
        discord.OptionChoice(name = "Splitroles", value = "Splitroles"),
        discord.OptionChoice(name = "support", value = "support"),
        discord.OptionChoice(name = "Umfrage", value = "Umfrage"),
        discord.OptionChoice(name = "Utility", value = "Utility"),
        discord.OptionChoice(name = "Help", value = "Help"),
        discord.OptionChoice(name = "Birthday", value = "Birthday"),
        discord.OptionChoice(name = "minigames", value = "minigames")
    ]

    @slash_command(name='restart', description='Lade den gesamten Bot oder nur ein bestimmtes script neu!')
    async def restart(self, ctx, extension : Option(str, "Welchen Command möchtest du ausführen?", required = False, choices = möglichkeitenArt, default = None)):
        if not ctx.author.id in dev_list:
            await ctx.respond("Dieser Befehl ist zu heiß für dich!")
            return
        await ctx.defer()
        if extension == None:
            initial_extensions = [
                "Cogs.countingsystem",  #
                "Cogs.Economy",         #
                "Cogs.Funcommands",     
                "Cogs.Giveaway",        #
                "Cogs.Levelsystem",     #
                "Cogs.Logging",         
                "Cogs.ModCmds",         #
                "Cogs.secruitysystem",  #
                "Cogs.ServerEinrichten",#
                "Cogs.Splitroles",
                "Cogs.support",         #
                "Cogs.Umfrage",         #
                "Cogs.Utility",#
                "Cogs.Help",
                "Cogs.Birthday",#
                "Cogs.minigames",
                "Cogs.reloader"
            ]

            for extension in initial_extensions:
                self.client.reload_extension(extension)
            await ctx.respond("Ich habe den Bot erfolgreich neu gestartet! ||Bitte mache das nur, wenn es auch wirklich benötigt wird :)||")
        else:
            self.client.reload_extension(f"Cogs.{extension}")
            await ctx.respond(f"Ich habe die Extension `{extension}` erfolgreich neugeladen!")


def setup(client):
    client.add_cog(Reloader(client))