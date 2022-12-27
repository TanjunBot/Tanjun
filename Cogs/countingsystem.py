import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
import json
from pathlib import Path
from pymongo import MongoClient

cluster = MongoClient("")

db = cluster["Main"]
countingcollection = db["counting"]
blacklistcollection = db["blacklist"]


class Counting(commands.Cog):

    def __init__(self, client):
        self.client = client



    @has_permissions(manage_channels=True)
    @slash_command(name='setcount', description='Sage mir, bei welcher Zahl wir grade sind!')
    async def setcount(self, ctx, progress : Option(int, "Bei welcher Zahl soll ich weiterzählen?", required = True)):
        await ctx.defer()
        m = f"Countingfortschritt erfolgreich auf `{progress}` gesetzt."
        try:
            countingcollection.update_one({"_id" : ctx.guild.id}, {"$set" : {"progress" : progress}})
        except:
            countingcollection.insert_one({"_id" : ctx.guild.id, "progress" : progress})
            m += "\nWie ich sehe hast du gar keinen Channel festgelegt. Bitte benutze den `\setcountingchannel` befehl!"

        await ctx.send(m)
    
    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if not message.guild:
            return
        
        try:
            blacklist = blacklistcollection.find_one({"_id" : message.guild.id})
            if message.channel.id in blacklist["blacklistedchannel"]:
                return
        except:
            pass
        try:
            for role in message.author.roles:
                if role.id in blacklist["blacklistedroles"]:
                    return
        except:
            pass
        
        countings = countingcollection.find_one({"_id" : message.guild.id})
        if countings == None:
            return
        channelid = countings["channel"]
        try:
            progress = countings["progress"]
        except:
            progress = 0
        
        try:
            lastcounter = countings["lastcounter"]
        except:
            lastcounter = 0
        
        if message.channel.id == channelid:
            try:
                int(message.content)
            except:
                await message.delete()
                return
            if int(message.content) == progress + 1:
                if message.author.id == lastcounter:
                    await message.delete()
                    return
                progress = int(message.content)
                lastcounter = message.author.id
                countingcollection.update_one({"_id" : message.guild.id}, {"$set" : {"channel" : channelid, "progress" : progress, "lastcounter" : lastcounter}})
                if str(message.content)[-2:] == "00":
                    await message.add_reaction("🎉")
                    await message.pin()
            else:
                await message.delete()
                return


          


def setup(client):
    client.add_cog(Counting(client))