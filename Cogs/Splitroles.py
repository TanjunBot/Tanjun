import discord
from discord.ext import commands, tasks
import pymongo
import time
import json
from pathlib import Path
from pymongo import MongoClient


cluster = MongoClient("")

db = cluster["Main"]
serversettingscollection = db["serversettings"]


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
    @tasks.loop(seconds=10)
    async def splittisplit(self):
        for guild in self.client.guilds:
            try:
                serversettings = serversettingscollection.find_one({"_id" : guild.id})
                if serversettings == None:
                    serversettings = {}
            except:
                serversettings = {}

            serversettings[str(guild.id)] = serversettings

            settings = serversettings[str(guild.id)]
            try:
                settings = settings["server"]
            except:
                pass
            roles = []
            doit = False
            try:
                settings["splitroles"]
                doit = True
            except:
                doit = False
            if doit == True:
                c11 = 0
                for member in guild.members:
                    try:
                        c11 += 1
                        splitrolestodelete = []
                        splitrolestokeep = []
                        for r in settings["splitroles"]:
                            roles = settings["splitroles"][r]
                            doit2 = True
                            for role in member.roles:
                                if role.id in roles:
                                    doit2 = False

                            if doit2 == True:
                                splitrolestodelete.append(int(r))

                            if doit2 == False:
                                splitrolestokeep.append(int(r))

                        roles2 = member.roles
                        c = 0
                        for rrr in splitrolestokeep:
                            r = guild.get_role(int(rrr))
                            if not r in roles2:
                                roles2.append(r)
                        for r in roles2:
                            if r.id in splitrolestodelete:
                                roles2.pop(c)
                            c += 1
                        if roles2 != member.roles:
                            await member.edit(roles = roles2)

                    except:
                        pass
                    


    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        self.splittisplit.start()

def setup(client):
    client.add_cog(Example(client))
