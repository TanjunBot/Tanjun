from sqlite3 import Timestamp
import discord
from discord.ext import commands, tasks
import time
import pytz
import json
from discord.commands import Option, slash_command
from discord.ui import Select, View
from discord.ext.commands import has_permissions
import datetime
from pymongo import MongoClient


cluster = MongoClient("")

db = cluster["Main"]
umfragecollection = db["umfragen"]

class Umfrage(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        self.umfragen_aktuallisieren.start()

    @tasks.loop(seconds=60)
    async def umfragen_aktuallisieren(self):
        for guild in self.client.guilds:
            try:
                try:
                    umfragen = umfragecollection.find_one({"_id" : guild.id})
                    if umfragen == None:
                        umfragen = {}
                except:
                    umfragen = {}
                umfragen[str(guild.id)] = dict(umfragen)

                for gg in umfragen[str(guild.id)]:
                    try:
                        if umfragen[str(guild.id)][str(gg)]["endet"] == False:
                            g = umfragen[str(guild.id)][str(gg)]
                            channel = self.client.get_channel(g["channel"])
                            try:
                                message = await channel.fetch_message(int(gg))
                                umfragetext = g["umfrage"]
                                timeins = g["time"]
                                Timestamp = time.time()
                                if timeins <= Timestamp:
                                    reactioncounts = []
                                    for re in message.reactions:
                                        reactioncounts.append([re.count - 1, re.emoji])
                                    reactioncounts = sorted(reactioncounts, key=lambda x: x[0] if type(x[0])==int else 999999999, reverse=True)
                                    embed = discord.Embed(title="__Umfrage beendet!__",description=f"{umfragetext}",color=0xbd24e7)
                                    ergebnisse = "** **"
                                    for rea in reactioncounts:
                                        if rea[0] == 1:
                                            ergebnisse += f"\n{rea[1]} hat {rea[0]} Stimme"
                                        else:
                                            ergebnisse += f"\n{rea[1]} hat {rea[0]} Stimmen"
                                    embed.add_field(name=f'Umfrage Ergebnisse:',value=ergebnisse,inline=False)
                                    await message.edit(embed = embed)

                                    umfragen[str(guild.id)][gg]["endet"] = True

                                umfragen[str(guild.id)][gg]["time"] = timeins
                            except:
                                umfragen[str(guild.id)][gg]["endet"] = True
                                pass

                    except:
                        pass
            except:
                raise


    @has_permissions(view_audit_log=True)
    @slash_command(name='umfrage', description='Erstelle eine Umfrage')
    async def umfrage(self, ctx, channel : Option(discord.TextChannel, "In welchen Channel soll die Umfrage erstellt werden?", required = True), dauer_der_umfrage : Option(str, "Wie lang soll die Umfrage gehen? (10h oder 12m)", required = True), emojis_mit_leerzeichen_getrennt : Option(str, "Welche Emojis soll es zur Auswahl geben?", required = True), titel_der_umfrage : Option(str, "Was soll der Titel sein?", required = True), umfrage : Option(str, "Was ist die Umfrage?", required = True)):
        await ctx.defer()
        try:
            umfragen = umfragecollection.find_one({"_id" : ctx.guild.id})
            if umfragen == None:
                umfragen = {}
        except:
            umfragen = {}
        curr_dt = datetime.datetime.now(tz=pytz.timezone("Europe/Berlin"))
        timestamp = int(round(curr_dt.timestamp()))
        dauer_der_umfrage = timestamp + int(convert(dauer_der_umfrage))

        umfragen[str(ctx.guild.id)] = dict(umfragen)
        
        
        myEmbed = discord.Embed(title=titel_der_umfrage, description=f"{umfrage} \nUmfragenende: <t:{dauer_der_umfrage}:R>",color=0xbd24e7)

        msg = await channel.send(embed = myEmbed)
        try:
            umfragen[str(ctx.guild.id)]
        except:
            umfragen[str(ctx.guild.id)] = {}
        
        umfragen[str(ctx.guild.id)][str(msg.id)] = {"endet" : False, "time" : dauer_der_umfrage, "titel" : titel_der_umfrage, "umfrage" : umfrage, "channel" : channel.id}
        for em in emojis_mit_leerzeichen_getrennt.split(" "):
            try:
                await msg.add_reaction(em)
            except:
                pass

        try:
            umfragecollection.update_one({"_id" : ctx.guild.id}, {"$set" : umfragen[str(ctx.guild.id)]}, upsert = True)
        except:
            raise

        await ctx.respond("Die Umfrage wurde erfolgreich gestartet!\n||Du kannst jederzeit mit zusätzlichen Reaktionen reagieren. Diese werden auch ausgewertet!||")


def get_zeit_übrig(timeins):
    zeitübrig = ""
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    days = timeins // seconds_in_day
    hours = (timeins - (days * seconds_in_day)) // seconds_in_hour
    minutes = (timeins - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
    if days > 1:
        zeitübrig += f"{days} Tage"
    if days == 1:
        zeitübrig += f"{days} Tag"

    if hours > 1:
        zeitübrig += f"{hours} Stunden"
    if hours == 1:
        zeitübrig += f"{hours} Stunde"

    if minutes > 1:
        zeitübrig += f"{minutes} Minuten"
    if minutes == 1:
        zeitübrig += f"{minutes} Minute"
    
    if minutes == 0 and hours == 0 and days == 0:
        zeitübrig = "Umfrage ist jeden Moment vorrüber"

    return zeitübrig

          
def convert(time):
    pos = ["s", "m", "h", "d", "w"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]



def setup(client):
    client.add_cog(Umfrage(client))