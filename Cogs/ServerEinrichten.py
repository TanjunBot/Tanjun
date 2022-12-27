import os
import json
import time
from datetime import date, datetime
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
import asyncio
from io import BytesIO
from discord.ext.commands.errors import EmojiNotFound
import pprint

import pytz
import numpy as np
import re
import DiscordUtils
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageOps
import itertools
import discord
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from pathlib import Path
from pymongo import MongoClient

from Cogs.MusikQuiz import MusikQuiz

cluster = MongoClient("")

db = cluster["Main"]
serversettingscollection = db["serversettings"]
settingmessagescollection = db["settingmessages"]
invitecounter = db["invitecount"]

eigenevcs = []

class servereinrichten(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        self.tracker = DiscordUtils.InviteTracker(self.client)

        self.werbung.start()
        
    @tasks.loop(seconds=60)
    async def werbung(self):
        timenow = datetime.now()
        zeit = timenow.strftime("%H:%M")
        print(zeit)
        if zeit == "04:00":
            await partnerembedsender(self)
        if zeit == "10:00":
            await partnerembedsender(self)
        if zeit == "16:00":
            await partnerembedsender(self)
        if zeit == "22:00":
            await partnerembedsender(self)
        tz_London = pytz.timezone('Europe/Berlin')
        now = datetime.now(tz_London)

        for guild in self.client.guilds:
            try:
                x = serversettingscollection.find_one({"_id" : guild.id})
                if x["Serverstats"]["User"] == True:
                    try:
                        vc = guild.get_channel(x["Serverstats"]["Userid"])
                        members = [member for member in guild.members if not member.bot]
                        name = ""
                        for l in vc.name:
                            try:
                                int(l)
                            except:
                                name += l
                        name += str(len(members)).strip() 

                        if not name == vc.name:
                            await vc.edit(name = name)
                    except:
                        raise
                if x["Serverstats"]["Insgesammt_User"] == True:
                    try:
                        vc = guild.get_channel(x["Serverstats"]["Insgesammt_Userid"])
                        members = guild.members
                        name = ""
                        for l in vc.name:
                            try:
                                int(l)
                            except:
                                name += l
                        name += str(len(members)).strip() 
                        if not name == vc.name:
                            await vc.edit(name = name)
                    except:
                        raise
                if x["Serverstats"]["Bots"] == True:
                    try:
                        vc = guild.get_channel(x["Serverstats"]["Botsid"])
                        members = [member for member in guild.members if member.bot]
                        name = ""
                        for l in vc.name:
                            try:
                                int(l)
                            except:
                                name += l
                        name += str(len(members)).strip() 
                        if not name == vc.name:
                            await vc.edit(name = name)
                    except:
                        raise
                if x["Serverstats"]["Userziel"] != 0:
                    try:
                        vc = guild.get_channel(x["Serverstats"]["Userzielid"])
                        members = [member for member in guild.members if not member.bot]
                        if len(members) > int(x["Serverstats"]["Userziel"]):
                            name = ""
                            for l in vc.name:
                                try:
                                    int(l)
                                except:
                                    name += l
                            if not "Erreicht!" in name:
                                name += "Erreicht!".strip() 
                            if not name == vc.name:
                                try:
                                    await vc.edit(name = name)
                                except:
                                    raise
                        else:
                            name = ""
                            for l in vc.name:
                                try:
                                    int(l)
                                except:
                                    name += l
                            name += x["Serverstats"]["Userziel"].strip() 
                            if not name == vc.name:
                                await vc.edit(name = name)
                    except:
                        raise
                if x["Serverstats"]["Datum"] == True:
                    try:
                        vc = guild.get_channel(x["Serverstats"]["Datumid"])

                        name = ""
                        for l in vc.name:
                            try:
                                int(l)
                            except:
                                if not l == ".":
                                    name += l
                        name += now.strftime("%d.%m.%Y").strip() 

                        if not name == vc.name:
                            await vc.edit(name = name)
                    except:
                        raise
            except:
                pass
        toc = time.perf_counter()


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        global eigenevcs
        if member.bot == False:
            x = serversettingscollection.find_one({"_id" : member.guild.id})
            try:
                x["tempchannel"]["tempchannel_aktiviert"]
            except:
                return
            if x["tempchannel"]["tempchannel_aktiviert"] == False:
                return
            if after.channel == None:
                after = before
            if before.channel == None:
                before = after
            vc = self.client.get_channel(x["tempchannel"]["tempchannel_id"])
            if after.channel.id == x["tempchannel"]["tempchannel_id"]:
                vc = await member.guild.create_voice_channel(f"VC von {member.name}",category=vc.category)
                await vc.set_permissions(member, manage_permissions=True, manage_channels=True)
                await member.move_to(vc)
                myEmbed = discord.Embed(description=f"Du hast soeben erfolgreich einen Eigenen Channel erstellt. Du hast Admin Rechte für den Channel bekommen, somit kannst du ganz einfach alle Einstellungen Treffen, die du willst.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Eigene Channel v 1.0 ⬝ {member}")
                await member.send(embed = myEmbed)
                eigenevcs.append(vc.id)
            if before.channel.category.id == vc.category.id:
                if before.channel.id in eigenevcs:
                    if len(before.channel.members) == 0:
                        await asyncio.sleep(10)
                        if len(before.channel.members) == 0:
                            await before.channel.delete()



    @slash_command(name = "deleteallselfroles", description = "Lösche alle selfroles")
    async def deleteallselfroles(self, ctx, sicherheitsscheck : Option(str, 'Bitte gebe "JA, ICH WILL" genau so ein.' , required = True)):
        await ctx.defer()
        if sicherheitsscheck == "JA, ICH WILL":
            if ctx.guild.owner.id == ctx.author.id:
                serversettingscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {"selfroles" : {}}})
                await ctx.respond("Alle Selfroles wurden erfolgreich gelöscht.")
            else:
                await ctx.respond("Nur der Owner des Servers darf diesen Befehl ausführen")
        else:
            await ctx.respond("Du hast en Sicherheitscheck nicht bestanden.")

    @has_permissions(view_audit_log=True)
    @slash_command(name='settings', description='Richte den Server ein.')
    async def settings(self, ctx):
        await ctx.defer()
        try:
            serversettings = serversettingscollection.find_one({"_id" : ctx.guild.id})
            if serversettings == None:
                serversettings = {}
        except:
            serversettings = {}

        serversettings[str(ctx.guild.id)] = dict(serversettings)


        try:
            settingmessages = settingmessagescollection.find_one({"_id" : ctx.guild.id})
            if settingmessages == None:
                settingmessages = {}
        except:
            settingmessages = {}

        settingmessages[str(ctx.guild.id)] = dict(settingmessages)


        embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=ctx.author.color)
        embed.add_field(name="1️⃣",value='> Logging',inline=False)
        embed.add_field(name="2️⃣",value='> Levelsystem',inline=False)
        embed.add_field(name="3️⃣",value='> Selfroles',inline=False)
        embed.add_field(name="4️⃣",value='> Serverstats',inline=False)
        embed.add_field(name="5️⃣",value='> Automatisch Werbung senden',inline=False)
        embed.add_field(name="6️⃣",value='> Splitrollen Reinigen',inline=False)
        embed.add_field(name="7️⃣",value='> Default Roles',inline=False)
        embed.add_field(name="8️⃣",value='> Temporäre Channel',inline=False)
        embed.add_field(name="9️⃣",value='> Join/Leave Message',inline=False)
        embed.add_field(name="🔟",value='> Geburstage',inline=False)
        message = await ctx.send(embed = embed)
        try:
            settingmessages[str(ctx.guild.id)]["mainsettings"]
            settingmessages[str(ctx.guild.id)]["mainsettings"].append(message.id)
        except:
            try:
                settingmessages[str(ctx.guild.id)]
                settingmessages[str(ctx.guild.id)]["mainsettings"] = [message.id]
            except:
                myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: se0.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {ctx.author}")
                await ctx.send(embed = myEmbed)
                return
        if message:
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("4️⃣")
            await message.add_reaction("5️⃣")
            await message.add_reaction("6️⃣")
            await message.add_reaction("7️⃣")
            await message.add_reaction("8️⃣")
            await message.add_reaction("9️⃣")
            await message.add_reaction("🔟")
        try:
            serversettingscollection.update_one({"_id" : ctx.guild.id}, {"$set" : serversettings[str(ctx.guild.id)]}, upsert = True)
            print("Habs geupdated!")
        except:
            serversettings[str(ctx.guild.id)]["_id"] = ctx.guild.id
            serversettingscollection.insert_one(serversettings[str(ctx.guild.id)])
            print("NEUUUUUUUUUUUUUUUUUU!")

        try:
            settingmessagescollection.update_one({"_id" : ctx.guild.id}, {"$set" : settingmessages[str(ctx.guild.id)]}, upsert = True)
        except:
            settingmessages[str(ctx.guild.id)]["_id"] = ctx.guild.id
            settingmessagescollection.insert_one(settingmessages[str(ctx.guild.id)])



    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        member = await self.client.fetch_user(payload.user_id)


        if member.bot == True:
            return
        #print(settings)

        try:
            serversettings = serversettingscollection.find_one({"_id" : payload.guild_id})
            if serversettings == None:
                serversettings = {}
        except:
            serversettings = {}

        serversettings[str(payload.guild_id)] = dict(serversettings)

        try:
            settingmessages = settingmessagescollection.find_one({"_id" : payload.guild_id})
            if settingmessages == None:
                settingmessages = {}
        except:
            settingmessages = {}

        settingmessages[str(payload.guild_id)] = dict(settingmessages)
        try:
            for selfrole in serversettings[str(payload.guild_id)]["selfroles"]:

                if payload.emoji.name == serversettings[str(payload.guild_id)]["selfroles"][selfrole]["Emojiname"].replace(" ", "") and payload.message_id == serversettings[str(payload.guild_id)]["selfroles"][selfrole]["msgid"]:


                    for g in self.client.guilds:
                        if g.id == payload.guild_id:
                            guild = g
                    member = await guild.fetch_member(payload.user_id)
                    role = get(guild.roles, id=serversettings[str(payload.guild_id)]["selfroles"][selfrole]["role"])
                    await member.remove_roles(role)
        except:
            pass
                    



    @has_permissions(kick_members=True)
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):


        if payload.member.bot == True:
            return
        
        try:
            serversettings = serversettingscollection.find_one({"_id" : payload.guild_id})
            if serversettings == None:
                serversettings = {}
        except:
            serversettings = {}

        serversettings[str(payload.guild_id)] = dict(serversettings)

        try:
            settingmessages = settingmessagescollection.find_one({"_id" : payload.guild_id})
            if settingmessages == None:
                settingmessages = {}
        except:
            settingmessages = {}

        settingmessages[str(payload.guild_id)] = dict(settingmessages)

        try:
            for selfrole in serversettings[str(payload.guild_id)]["selfroles"]:
                if payload.emoji.name == serversettings[str(payload.guild_id)]["selfroles"][selfrole]["Emojiname"].replace(" ", "") and payload.message_id == serversettings[str(payload.guild_id)]["selfroles"][selfrole]["msgid"]:
                    guild = ""
                    for g in self.client.guilds:
                        if g.id == payload.guild_id:
                            guild = g
                    role = get(guild.roles, id=serversettings[str(payload.guild_id)]["selfroles"][selfrole]["role"])
                    roles = payload.member.roles
                    roles.append(role)
                    if not payload.member.roles == roles:
                        try:
                            await payload.member.edit(roles = roles)
                        except:
                            pass
                    if serversettings[str(payload.guild_id)]["selfroles"][selfrole]["type"] == "single":

                        channel = await self.client.fetch_channel(payload.channel_id)
                        msg = await channel.fetch_message(payload.message_id)
                        guild = ""
                        msgid = msg.id

                        for reaction in msg.reactions:

                            if not str(reaction.emoji) == str(payload.emoji):

                                try:
                                    await msg.remove_reaction(reaction.emoji, payload.member)
                                except:
                                    pass
        except:
            pass
                


        if payload.member.guild_permissions.kick_members == False:
            return
    
        try:
            settingmessages[str(payload.guild_id)]
        except:
            settingmessages[str(payload.guild_id)] = {}
        try:
            settingmessages[str(payload.guild_id)]["mainsettings"]
        except:
            settingmessages[str(payload.guild_id)]["mainsettings"] = []
        if payload.message_id in settingmessages[str(payload.guild_id)]["mainsettings"]:

            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                try:
                    serversettings[str(payload.guild_id)]["logging"]
                except:
                    serversettings[str(payload.guild_id)]["logging"] = {"Logging_aktiv" : False, "Log_Channel" : None}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)
                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["logging"]["Logging_aktiv"] == True:
                    an = "aktiviert"

                embed.add_field(name="1️⃣",value=f'> Loging Deaktivieren/aktivieren (momentan: {an})',inline=False)
                try:
                    chan = await self.client.fetch_channel(serversettings[str(payload.guild_id)]["logging"]["Log_Channel"])
                    try:
                        chan = chan.mention
                    except:
                        chan = "Error! Channel could not be found anywhere! Pls make shure you dont deletet it."
                except:
                    chan = "Nicht festgelegt"
                embed.add_field(name="2️⃣",value=f'> Log Channel Ändern (momentan {chan})',inline=False)
                
                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["Logging"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["Logging"] = [message.id]
            
            if payload.emoji.name == "2️⃣":
                try:
                    serversettings[str(payload.guild_id)]["levelsys"]
                except:
                    serversettings[str(payload.guild_id)]["levelsys"] = {"Levelsystem_aktiviert" : True, "levelup_nachrichten" : True, "excluded_channel" : [], "xpmultiplyerroles" : {}, "XPrewardroles" : {}}

                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)

                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["levelsys"]["Levelsystem_aktiviert"] == True:
                    an = "aktiviert"
                embed.add_field(name="1️⃣",value=f'> Levelsystem Deaktivieren/aktivieren (momentan: {an})',inline=False)

                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["levelsys"]["levelup_nachrichten"] == True:
                    an = "aktiviert"
                embed.add_field(name="2️⃣",value=f'> Levelup Benachrichtigungen Deaktivieren/aktivieren (momentan: {an})',inline=False)

                guild = ""
                for g in self.client.guilds:
                    if g.id == payload.guild_id:
                        guild = g

                message = ""
                for ch in serversettings[str(payload.guild_id)]["levelsys"]["excluded_channel"]:
                    cha = await self.client.fetch_channel(ch)
                    try:
                        message += f'\n{cha.mention}'
                    except:
                        message += f'\nChannel konnte nicht gefunden werden.'
                embed.add_field(name="3️⃣",value=f'> Ausgeschlossene Channel ändern(momentan: {message})',inline=False)

                message = ""
                for ch in serversettings[str(payload.guild_id)]["levelsys"]["xpmultiplyerroles"]:

                    role = get(guild.roles, id=int(ch))
                    try:
                        message += f'\n{role.mention} : {serversettings[str(payload.guild_id)]["levelsys"]["xpmultiplyerroles"][ch]}'
                    except:
                        message += f'\nRolle wurde nicht gefunden. : {serversettings[str(payload.guild_id)]["levelsys"]["xpmultiplyerroles"][ch]}'
                embed.add_field(name="4️⃣",value=f'> Rollen mit XP boost ändern (momentan: {message})',inline=False)

                message = ""
                for ch in serversettings[str(payload.guild_id)]["levelsys"]["XPrewardroles"]:

                    role = get(guild.roles, id=int(ch))
                    try:
                        message += f'\n{role.mention} : {serversettings[str(payload.guild_id)]["levelsys"]["XPrewardroles"][ch]}'
                    except:
                        message += f'\nRolle wurde nicht gefunden. : {serversettings[str(payload.guild_id)]["levelsys"]["XPrewardroles"][ch]}'
                embed.add_field(name="5️⃣",value=f'> Xp reward Roles (momentan: {message})',inline=False)

                
                message = await channel.send(embed = embed)

                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                await message.add_reaction("4️⃣")
                await message.add_reaction("5️⃣")

                try:
                    settingmessages[str(payload.guild_id)]["levelsetings"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["levelsetings"] = [message.id]
            
            if payload.emoji.name == "3️⃣":
                try:
                    serversettings[str(payload.guild_id)]
                except:
                    serversettings[str(payload.guild_id)] = {}
                try:
                    serversettings[str(payload.guild_id)]["selfroles"]
                except:
                    serversettings[str(payload.guild_id)]["selfroles"] = {}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)

                embed.add_field(name="1️⃣",value=f'> Selfrole Hinzufügen (Single Type, heißt: es kann nur eine Selfrole aus der Nachricht benutzt werden. Für z.B. Geschlecht/Alter etc.)',inline=False)

                embed.add_field(name="2️⃣",value=f'> Selfrole Hinzufügen (Multy Type, heißt: es können mehrere Selfroles aus der Nachricht benutzt werden. Für z.B. Hobbys/Spiele etc.)',inline=False)

                embed.add_field(name="3️⃣",value=f'> Selfrole Entfernen',inline=False)

                message = ""

                try:
                    messageseslengths = 0
                    for se in serversettings[str(payload.guild_id)]["selfroles"]:
                        if len(message) <= 900:
                            s = serversettings[str(payload.guild_id)]["selfroles"][se]

                            guild = ""
                            for g in self.client.guilds:
                                if g.id == payload.guild_id:
                                    guild = g
                            try:
                                message += f'\n{s["name"]} : {s["type"]}, {self.client.get_emoji(s["Emojiid"])}, {guild.get_role(s["role"]).mention}, channel: {discord.utils.get(guild.channels, id=int(s["Channelid"])).mention}' 
                            except:
                                try:
                                    message += f'\n{s["name"]} : {s["type"]}, {s["Emojiname"]}, {guild.get_role(s["role"]).mention}, channel: {discord.utils.get(guild.channels, id=int(s["Channelid"])).mention}' 
                                except:
                                    try:
                                        message += f'\n{s["name"]} : {s["type"]}, {s["Emojiname"]}, Rolle Konnte nicht geladen werden., channel: {discord.utils.get(guild.channels, id=int(s["Channelid"])).mention}'
                                    except:
                                        message += f'\n{s["name"]} : {s["type"]}, {s["Emojiname"]}, Rolle Konnte nicht geladen werden., channel: Channel konnte nicht geladen werden.'
                        else:
                            messageseslengths += 1000
                            embed.add_field(name="Momentane Selfroles",value=f'> {message}',inline=False)
                            if messageseslengths >= 5000:
                                message = await channel.send(embed = embed)
                                embed = discord.Embed(description='Tanjun Einstellungen\nWOW! Du hast ganz schön viele Selfroles! Ein Embed reicht nicht aus, um alle anzuzeigen!',color=0x0000ff)
                                messageseslengths = 0
                            message = ""
                            s = serversettings[str(payload.guild_id)]["selfroles"][se]

                            guild = ""
                            for g in self.client.guilds:
                                if g.id == payload.guild_id:
                                    guild = g
                            try:
                                message += f'\n{s["name"]} : {s["type"]}, {self.client.get_emoji(s["Emojiid"])}, {guild.get_role(s["role"]).mention}, channel: {discord.utils.get(guild.channels, id=int(s["Channelid"])).mention}' 
                            except:
                                try:
                                    message += f'\n{s["name"]} : {s["type"]}, {s["Emojiname"]}, {guild.get_role(s["role"]).mention}, channel: {discord.utils.get(guild.channels, id=int(s["Channelid"])).mention}' 
                                except:
                                    try:
                                        message += f'\n{s["name"]} : {s["type"]}, {s["Emojiname"]}, Rolle Konnte nicht geladen werden., channel: {discord.utils.get(guild.channels, id=int(s["Channelid"])).mention}'
                                    except:
                                        message += f'\n{s["name"]} : {s["type"]}, {s["Emojiname"]}, Rolle Konnte nicht geladen werden., channel: Channel konnte nicht geladen werden.'
                
                except:
                    message = "Noch keine Eingerichtet."
                    raise
                embed.add_field(name="Momentane Selfroles",value=f'> {message}',inline=False)
                
                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["selfroles"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["selfroles"] = [message.id]




            if payload.emoji.name == "5️⃣":
                try:
                    serversettings[str(payload.guild_id)]
                except:
                    serversettings[str(payload.guild_id)] = {}
                try:
                    serversettings[str(payload.guild_id)]["werbung"]
                except:
                    serversettings[str(payload.guild_id)]["werbung"] = {"Werbung" : [], "Active" : False, "Werbechannel" : None}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)

                embed.add_field(name="1️⃣",value=f'> Werbeembed Ändern',inline=False)

                embed.add_field(name="2️⃣",value=f'> Demo Werbeembed Senden',inline=False)

                an = "deaktiviert"

                if serversettings[str(payload.guild_id)]["werbung"]["Active"] == True:
                    an = "aktiviert"

                embed.add_field(name="3️⃣",value=f'> Werbung Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                chan = ""
                try:
                    
                    chan = await self.client.fetch_channel(serversettings[str(payload.guild_id)]["werbung"]["Werbechannel"])
                    chan = chan.mention
                except:
                    chan = "Nicht festgelegt"

                embed.add_field(name="4️⃣",value=f'> Werbechannel ändern (momentan: {chan})',inline=False)
                
                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                await message.add_reaction("4️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["werbung"].append(message.id)
                except:
                    try:
                        settingmessages[str(payload.guild_id)]["werbung"] = [message.id]
                    except:
                        settingmessages[str(payload.guild_id)]["werbung"] = {}
                        settingmessages[str(payload.guild_id)]["werbung"] = [message.id]

            if payload.emoji.name == "4️⃣":
                try:
                    serversettings[str(payload.guild_id)]
                except:
                    serversettings[str(payload.guild_id)] = {}
                try:
                    serversettings[str(payload.guild_id)]["Serverstats"]
                except:
                    serversettings[str(payload.guild_id)]["Serverstats"]= {"User" : False, "Insgesammt_User" : False, "Bots" : False, "Userziel" : 0, "Datum" : False, "Uhrzeit" : False, "Userid" : None, "Insgesammt_Userid" : None, "Botsid" : None, "Userzielid" : None, "Datumid" : None, "Uhrzeitid" : None}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)
                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["Serverstats"]["User"] == True:
                    an = "aktiviert"

                embed.add_field(name="1️⃣",value=f'> User auf den Server Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["Serverstats"]["Insgesammt_User"] == True:
                    an = "aktiviert"

                embed.add_field(name="2️⃣",value=f'> Insgesammte User (mit Bots) auf den Server Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["Serverstats"]["Bots"] == True:
                    an = "aktiviert"

                embed.add_field(name="3️⃣",value=f'> Bots auf den Server Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["Serverstats"]["Datum"] == True:
                    an = "aktiviert"

                embed.add_field(name="4️⃣",value=f'> Datum auf den Server Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                embed.add_field(name="5️⃣",value=f'> Userziel auf den Server ändern (momentan: {an})',inline=False)

                
                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                await message.add_reaction("4️⃣")
                await message.add_reaction("5️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["Serverstats"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["Serverstats"] = [message.id]


            if payload.emoji.name == "6️⃣":
                try:
                    serversettings[str(payload.guild_id)]
                except:
                    serversettings[str(payload.guild_id)] = {}
                try:
                    serversettings[str(payload.guild_id)]["splitroles"]
                except:
                    serversettings[str(payload.guild_id)]["splitroles"] = {}

                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)

                embed.add_field(name="1️⃣",value=f'> Splitrole Splitrolle Hinzufügen',inline=False)

                embed.add_field(name="2️⃣",value=f'> Splitrole Entfernen',inline=False)



                guild = ""
                for g in self.client.guilds:
                    if g.id == payload.guild_id:
                        guild = g
                
                try:
                    serversettings[str(payload.guild_id)]["splitroles"]
                except:
                    serversettings[str(payload.guild_id)]["splitroles"] = {}
                rolestodelete = []
                for r in serversettings[str(payload.guild_id)]["splitroles"]:
                    message = ""

                    
                    for rr in serversettings[str(payload.guild_id)]["splitroles"][str(r)]:
                        try:
                            message += f"\n{guild.get_role(int(rr)).mention}"
                        except:
                            message += f"\nRolle nicht gefunden."

                    try:
                        embed.add_field(name=f"{guild.get_role(int(r)).name}",value=f'{message}',inline=False)
                    except:
                        embed.add_field(name=f"Rolle nicht gefunden :c Der eintrag wird nun gelöscht.",value=f'{message}',inline=False)
                        rolestodelete.append(r)
                        


                    
                
                message = await channel.send(embed = embed)
                for r in rolestodelete:
                    del serversettings[str(payload.guild_id)]["splitroles"][str(r)]
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["splitroles"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["splitroles"] = [message.id]


            
            if payload.emoji.name == "7️⃣":
                try:
                    serversettings[str(payload.guild_id)]["defaultroles"]
                except:
                    serversettings[str(payload.guild_id)]["defaultroles"]= {"allmembers" : [], "nonbots" : []}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)

                guild = ""
                for g in self.client.guilds:
                    if g.id == payload.guild_id:
                        guild = g

                message = ""
                for r in serversettings[str(payload.guild_id)]["defaultroles"]["allmembers"]:
                    try:
                        message += f"\n{guild.get_role(int(r)).mention}"
                    except:
                        message += f"\nRolle nicht gefunden."

                embed.add_field(name="1️⃣",value=f'> Rollen Für alle member (auch Bots) Hinzufühem: {message}',inline=False)

                message = ""
                for r in serversettings[str(payload.guild_id)]["defaultroles"]["nonbots"]:
                    try:
                        message += f"\n{guild.get_role(int(r)).mention}"
                    except:
                        message += f"\nRolle nicht gefunden."


                embed.add_field(name="2️⃣",value=f'> Rollen für Normale Member (keine Bots) Hinzufühem: {message}',inline=False)

                embed.add_field(name="3️⃣",value=f'> Rollen für alle member (auch Bots) Entfernen',inline=False)

                embed.add_field(name="4️⃣",value=f'> Rollen für Normale Member (keine Bots) Entfernen',inline=False)
                
                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                await message.add_reaction("4️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["defaultroles"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["defaultroles"] = [message.id]

            if payload.emoji.name == "8️⃣":
                try:
                    serversettings[str(payload.guild_id)]["tempchannel"]
                except:
                    serversettings[str(payload.guild_id)]["tempchannel"] = {"tempchannel_aktiviert" : False, "tempchannel_id" : None}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)
                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["tempchannel"]["tempchannel_aktiviert"] == True:
                    an = "aktiviert"

                embed.add_field(name="1️⃣",value=f'> Temporäre Channel Deaktivieren/aktivieren (momentan: {an})',inline=False)
                try:
                    try:
                        chan = await self.client.fetch_channel(serversettings[str(payload.guild_id)]["tempchannel"]["tempchannel_id"])
                        chan = chan.mention
                    except:
                        chan = "Channel konnte nicht gefunden werden."
                except:
                    chan = "Nicht festgelegt"
                embed.add_field(name="2️⃣",value=f'> Join Channel neu erstellen (momentan {chan})',inline=False)
                
                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["tempchannel"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["tempchannel"] = [message.id]

            if payload.emoji.name == "9️⃣":
                try:
                    serversettings[str(payload.guild_id)]["JoinLeavemsg"]
                except:
                    serversettings[str(payload.guild_id)]["JoinLeavemsg"] = {"joinactive" : False, "Text" : "", "image" : False, "leaveactive" : False, "lText" : "", "leaveimage" : False, "Joinmessagechannel" : None, "Leavemessagechannel" : None}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)
                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["JoinLeavemsg"]["joinactive"] == True:
                    an = "aktiviert"

                embed.add_field(name="1️⃣",value=f'> Join Nachricht Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["JoinLeavemsg"]["leaveactive"] == True:
                    an = "aktiviert"

                embed.add_field(name="2️⃣",value=f'> Leave Nachricht Aktivieren/Deaktivieren (momentan: {an})',inline=False)
                try:
                    chan = await self.client.fetch_channel(serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Joinmessagechannel"])
                    chan = chan.mention
                except:
                    chan = "Nicht festgelegt"
                embed.add_field(name="3️⃣",value=f'> Join Message Channel ändern (momentan {chan})',inline=False)

                try:
                    chan = await self.client.fetch_channel(serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Leavemessagechannel"])
                    chan = chan.mention
                except:
                    chan = "Nicht festgelegt"
                embed.add_field(name="4️⃣",value=f'> Leave Message Channel ändern (momentan {chan})',inline=False)
                
                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["JoinLeavemsg"]["image"] == True:
                    an = "aktiviert"

                embed.add_field(name="5️⃣",value=f'> Join Nachricht Bild Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                an = "deaktiviert"
                if serversettings[str(payload.guild_id)]["JoinLeavemsg"]["lText"] == True:
                    an = "aktiviert"

                embed.add_field(name="6️⃣",value=f'> Leave Nachricht Bild Aktivieren/Deaktivieren (momentan: {an})',inline=False)

                text = "Nicht festgelegt"
                if serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Text"] != "":
                    text = serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Text"]
                    try:
                        text = text.replace("uuu", payload.member.mention)
                    except:
                        text = text.replace("uuu", "Du Existierst nicht? Wie hast du das bitte hin bekommen?!")

                embed.add_field(name="7️⃣",value=f'> Join Nachricht ändern momentan: \n{text}',inline=False)

                text = "Nicht festgelegt"
                if serversettings[str(payload.guild_id)]["JoinLeavemsg"]["lText"] != "":
                    text = serversettings[str(payload.guild_id)]["JoinLeavemsg"]["lText"]
                    text.replace("uuu", str(payload.member.name))

                embed.add_field(name="8️⃣",value=f'> Leave Nachricht ändern momentan: \n{text}',inline=False)

                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                await message.add_reaction("4️⃣")
                await message.add_reaction("5️⃣")
                await message.add_reaction("6️⃣")
                await message.add_reaction("7️⃣")
                await message.add_reaction("8️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["JoinLeavemsg"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["JoinLeavemsg"] = [message.id]


            if payload.emoji.name == "🔟":
                try:
                    serversettings[str(payload.guild_id)]["birthdays"]
                except:
                    serversettings[str(payload.guild_id)]["birthdays"] = {"birthdaychannel" : None, "birthdaymsg" : "", "geburstagsrolle" : None}
                
                embed = discord.Embed(description='Tanjun Einstellungen\nReagiere mit den unten Stehenden Reaktionen um den Bot zu Personalisieren.',color=0x0000ff)
                try:
                    chan = await self.client.fetch_channel(serversettings[str(payload.guild_id)]["birthdays"]["birthdaychannel"])
                    chan = chan.mention
                except:
                    chan = "Nicht festgelegt"
                embed.add_field(name="1️⃣",value=f'> Geburstagsglückwünsche channel ändern (momentan: {chan})',inline=False)
                try:
                    msg = serversettings[str(payload.guild_id)]["birthdays"]["birthdaymsg"].replace("uuu", payload.member.mention)
                except:
                    msg = serversettings[str(payload.guild_id)]["birthdays"]["birthdaymsg"].replace("uuu", "Dich gibt es nicht :c Bitte Existiere :c")
                embed.add_field(name="2️⃣",value=f'> Glückwunschnachricht ändern (momentan {msg})',inline=False)

                try:
                    guild = self.client.get_guild(payload.guild_id)
                    chan = guild.get_role(serversettings[str(payload.guild_id)]["birthdays"]["geburstagsrolle"])
                    chan = chan.mention
                except:
                    chan = "Nicht festgelegt"

                embed.add_field(name="3️⃣",value=f'> Geburstags rolle ändern (momentan {chan})',inline=False)
                
                message = await channel.send(embed = embed)
                await message.add_reaction("1️⃣")
                await message.add_reaction("2️⃣")
                await message.add_reaction("3️⃣")
                try:
                    settingmessages[str(payload.guild_id)]["birthdays"].append(message.id)
                except:
                    settingmessages[str(payload.guild_id)]["birthdays"] = [message.id]

            

        try:
            settingmessages[str(payload.guild_id)]["birthdays"]
        except:
            settingmessages[str(payload.guild_id)]["birthdays"] = []
        
        if payload.message_id in settingmessages[str(payload.guild_id)]["birthdays"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                myEmbed = discord.Embed(description="Bitte Makiere innerhalb der nächsten 30 Sekunden den Chat, in den die Glückwunsch Nachricht gesendet werden soll.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                await channel.send(embed = myEmbed, delete_after=30)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.channel_mentions[0]
                        serversettings[str(payload.guild_id)]["birthdays"]["birthdaychannel"] = chan.id
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: seb0.",color=0xbd24e7)
                        myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {payload.member}")
                        await channel.send(embed = myEmbed)
                        return
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(description="Deine Zeit ist leider abgelaufen.",color=0xbd24e7)
                    myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                    await channel.send(embed = myEmbed, delete_after=30)
                    return


            if payload.emoji.name == "2️⃣":
                myEmbed = discord.Embed(description="Bitte schreibe innerhalb der nächsten 90 Sekunden eine Nachricht, die gesendet werden soll, wenn ein User geburstag hat. wenn du das Geburstagskind Pingen möchtest, gebe uuu ein..",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                await channel.send(embed = myEmbed, delete_after=90)
                try:
                    msg = await self.client.wait_for('message', timeout=90, check=lambda message: message.author == payload.member)
                    try:
                        serversettings[str(payload.guild_id)]["birthdays"]["birthdaymsg"] = msg.content
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: seb1.",color=0xbd24e7)
                        myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {payload.member}")
                        await channel.send(embed = myEmbed)
                        return
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(description="Deine Zeit ist leider abgelaufen.",color=0xbd24e7)
                    myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                    await channel.send(embed = myEmbed, delete_after=30)
                    return

            if payload.emoji.name == "3️⃣":

                myEmbed = discord.Embed(description="Bitte makiere innerhalb der nächsten 30 Sekunden die Rolle, die Geburstagskinder bekommen sollen.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                await channel.send(embed = myEmbed, delete_after=30)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.role_mentions[0]
                        serversettings[str(payload.guild_id)]["birthdays"]["geburstagsrolle"] = chan.id
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: seb2.",color=0xbd24e7)
                        myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {payload.member}")
                        await channel.send(embed = myEmbed)
                        return
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(description="Deine Zeit ist leider abgelaufen.",color=0xbd24e7)
                    myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                    await channel.send(embed = myEmbed, delete_after=30)
                    return



        try:
            settingmessages[str(payload.guild_id)]["tempchannel"]
        except:
            settingmessages[str(payload.guild_id)]["tempchannel"] = []
        
        if payload.message_id in settingmessages[str(payload.guild_id)]["tempchannel"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                serversettings[str(payload.guild_id)]["tempchannel"]["tempchannel_aktiviert"] = not serversettings[str(payload.guild_id)]["tempchannel"]["tempchannel_aktiviert"]
                
                await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["tempchannel"]["tempchannel_aktiviert"]}!', delete_after=10)
            if payload.emoji.name == "2️⃣":
                guild = self.client.get_guild(payload.guild_id)
                vc = await guild.create_voice_channel(name = "Join to Create")
                serversettings[str(payload.guild_id)]["tempchannel"]["tempchannel_id"] = vc.id
                await channel.send("Channel erfolgreich erstellt.\nÜbrigens: du kannst den Voice Channel jeder zeit umbenennen")
                



        try:
            settingmessages[str(payload.guild_id)]["JoinLeavemsg"]
        except:
            settingmessages[str(payload.guild_id)]["JoinLeavemsg"] = []
        
        if payload.message_id in settingmessages[str(payload.guild_id)]["JoinLeavemsg"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                serversettings[str(payload.guild_id)]["JoinLeavemsg"]["joinactive"] = not serversettings[str(payload.guild_id)]["JoinLeavemsg"]["joinactive"]
                
                await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["joinactive"]}!', delete_after=10)

            if payload.emoji.name == "2️⃣":
                serversettings[str(payload.guild_id)]["JoinLeavemsg"]["leaveactive"] = not serversettings[str(payload.guild_id)]["JoinLeavemsg"]["leaveactive"]
                
                await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["leaveactive"]}!', delete_after=10)

            if payload.emoji.name == "3️⃣":
                myEmbed = discord.Embed(description="Bitte Makiere innerhalb der nächsten 30 Sekunden den Chat, in den die Join Nachricht gesendet werden soll.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                await channel.send(embed = myEmbed, delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.channel_mentions[0]
                        serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Joinmessagechannel"] = chan.id
                        await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Joinmessagechannel"]}!', delete_after=10)
                    except:
                        myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: sejl0.",color=0xbd24e7)
                        myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {payload.member}")
                        await channel.send(embed = myEmbed)
                        return
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(description="Deine Zeit ist leider abgelaufen.",color=0xbd24e7)
                    myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                    await channel.send(embed = myEmbed, delete_after=30)
                    return

            if payload.emoji.name == "4️⃣":
                myEmbed = discord.Embed(description="Bitte Makiere innerhalb der nächsten 30 Sekunden den Chat, in den die Leave Nachricht gesendet werden soll.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                await channel.send(embed = myEmbed, delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.channel_mentions[0]
                        serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Leavemessagechannel"] = chan.id
                        await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Leavemessagechannel"]}!', delete_after=10)
                    except:
                        myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: sejl1.",color=0xbd24e7)
                        myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {payload.member}")
                        await channel.send(embed = myEmbed)
                        return
                except TimeoutError:
                    myEmbed = discord.Embed(description="Deine Zeit ist leider abgelaufen.",color=0xbd24e7)
                    myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                    await channel.send(embed = myEmbed, delete_after=30)
                    return

            if payload.emoji.name == "5️⃣":
                serversettings[str(payload.guild_id)]["JoinLeavemsg"]["image"] = not serversettings[str(payload.guild_id)]["JoinLeavemsg"]["image"]
                
                await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["image"]}!', delete_after=10)

            if payload.emoji.name == "6️⃣":
                serversettings[str(payload.guild_id)]["JoinLeavemsg"]["leaveimage"] = not serversettings[str(payload.guild_id)]["JoinLeavemsg"]["leaveimage"]
                
                await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["leaveimage"]}!', delete_after=10)

            if payload.emoji.name == "7️⃣":
                myEmbed = discord.Embed(description="Bitte gebe innerhalb der Nächsten 120 Sekunden die Nachricht ein, die gesendet werden soll, wenn jemand den Server betritt. Um den neuen User zu Pingen, schreibe `uuu`. Um denjenigen, der den neuen Eingeladen hat, zu Pingen, Schreibe `iii`. Um zu schreiben, wie Viele invites derjenige hat, der den neuen user eingeladen hat, schreibe `III`\nWenn du einen Channel oder eine Rolle Pingen willst, mache das wie üblich im Chat.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                await channel.send(embed = myEmbed, delete_after=120)
                try:
                    msg = await self.client.wait_for('message', timeout=120, check=lambda message: message.author == payload.member)
                    try:
                        serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Text"] = msg.content
                        await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["Text"]}!', delete_after=10)
                    except:
                        myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: sejl2.",color=0xbd24e7)
                        myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {payload.member}")
                        await channel.send(embed = myEmbed)
                        return
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(description="Deine Zeit ist leider abgelaufen.",color=0xbd24e7)
                    myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                    await channel.send(embed = myEmbed, delete_after=30)
                    return


            if payload.emoji.name == "8️⃣":
                myEmbed = discord.Embed(description="Bitte gebe innerhalb der Nächsten 120 Sekunden die Nachricht ein, die gesendet werden soll, wenn jemand den Server Verlässt. Um den namen des Users zu schreiben, schreibe `uuu` Um denjenigen, der den user Eingeladen hat, zu Pingen, Schreibe `iii`. Um zu schreiben, wie Viele invites derjenige hat, der den user eingeladen hat, schreibe `III`\nWenn du einen Channel oder eine Rolle Pingen willst, mache das wie üblich im Chat.",color=0xbd24e7)
                myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                await channel.send(embed = myEmbed, delete_after=120)
                try:
                    msg = await self.client.wait_for('message', timeout=120, check=lambda message: message.author == payload.member)
                    try:
                        serversettings[str(payload.guild_id)]["JoinLeavemsg"]["lText"] = msg.content
                        await channel.send(f'Erfolgreich gesetzt auf {serversettings[str(payload.guild_id)]["JoinLeavemsg"]["lText"]}!', delete_after=10)
                    except:
                        myEmbed = discord.Embed(description="Etwas ist schief gelaufen. Bitte gebe den Tanjun Support Bescheid. Fehlercode: sejl3.",color=0xbd24e7)
                        myEmbed.set_footer(text=f"Tanjun Server Einrichten ⬝ {payload.member}")
                        await channel.send(embed = myEmbed)
                        return
                except TimeoutError:
                    myEmbed = discord.Embed(description="Deine Zeit ist leider abgelaufen.",color=0xbd24e7)
                    myEmbed.set_footer(text=f"Tanjun Server Einrichtemn ⬝ {payload.member}")
                    await channel.send(embed = myEmbed, delete_after=30)
                    return



        try:
            settingmessages[str(payload.guild_id)]["Logging"]
        except:
            settingmessages[str(payload.guild_id)]["Logging"] = []
        
        if payload.message_id in settingmessages[str(payload.guild_id)]["Logging"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                serversettings[str(payload.guild_id)]["logging"]["Logging_aktiv"] = not serversettings[str(payload.guild_id)]["logging"]["Logging_aktiv"]
                
                await channel.send("Erfolgreich!", delete_after=10)
            if payload.emoji.name == "2️⃣":
                
                await channel.send("Bitte Makiere innerhalb der nächsten 30 Sekunden Den Log Channel.", delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.channel_mentions[0]
                        serversettings[str(payload.guild_id)]["logging"]["Log_Channel"] = chan.id
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                except asyncio.TimeoutError:
                    await channel.send("Zu langsam :c")
            
        try:
            settingmessages[str(payload.guild_id)]["levelsetings"]
        except:
            settingmessages[str(payload.guild_id)]["levelsetings"] = []

        if payload.message_id in settingmessages[str(payload.guild_id)]["levelsetings"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                serversettings[str(payload.guild_id)]["levelsys"]["Levelsystem_aktiviert"] = not serversettings[str(payload.guild_id)]["levelsys"]["Levelsystem_aktiviert"]
                
                await channel.send("Erfolgreich!", delete_after=10)

            if payload.emoji.name == "2️⃣":
                serversettings[str(payload.guild_id)]["levelsys"]["levelup_nachrichten"] = not serversettings[str(payload.guild_id)]["levelsys"]["levelup_nachrichten"]
                
                await channel.send("Erfolgreich!", delete_after=10)

            if payload.emoji.name == "3️⃣":
                
                await channel.send("Bitte Makiere innerhalb der nächsten 30 Sekunden einen Channel der vom Levelsystem Ausgeschlossen/wieder mit inbegriffen werden soll.", delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.channel_mentions[0]
                        if chan.id in serversettings[str(payload.guild_id)]["levelsys"]["excluded_channel"]:
                            c = 0
                            for cha in serversettings[str(payload.guild_id)]["levelsys"]["excluded_channel"]:
                                if cha == chan.id:
                                    serversettings[str(payload.guild_id)]["levelsys"]["excluded_channel"].pop(c)
                                c += 1
                        else:
                            serversettings[str(payload.guild_id)]["levelsys"]["excluded_channel"].append(chan.id)
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                except asyncio.TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "4️⃣":
                
                await channel.send("Bitte Makiere innerhalb der nächsten 30 Sekunden Eine Rolle die einen XP Boost haben soll an", delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.role_mentions[0]
                        try:
                            await channel.send("Bitte gebe jetzt innerhalb der nächsten 30 Sekunden an, um wie viel der Multiplikator erhöht werden soll (1 = doppelte XP, 2 = drei fache XP etc. Für dezimalzahlen bitte einen Punkt nutzen, z.B. 0.5)")
                            msg2 = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                            try:
                                multiplyer = float(msg2.content)
                                serversettings[str(payload.guild_id)]["levelsys"]["xpmultiplyerroles"][str(chan.id)] = multiplyer
                                await channel.send("Erfolgreich!", delete_after=10)
                            except:
                                await channel.send("Bitte gebe eine Zahl an.")

                            
                        except asyncio.TimeoutError:
                            await channel.send("Zu langsam :c")
                        
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                except asyncio.TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "5️⃣":
                
                await channel.send("Bitte Makiere innerhalb der nächsten 30 Sekunden eine XP-Belohnungsrolle an.", delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.role_mentions[0]
                        try:
                            await channel.send("Bitte gebe jetzt innerhalb der nächsten 30 Sekunden an, bei welchem Level die Rolle hinzugefügt werden soll.")
                            msg2 = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                            try:
                                multiplyer = int(msg2.content)
                                serversettings[str(payload.guild_id)]["levelsys"]["XPrewardroles"][str(chan.id)] = multiplyer
                                await channel.send("Erfolgreich!", delete_after=10)
                            except:
                                await channel.send("Bitte gebe eine Zahl an.")

                            
                        except asyncio.TimeoutError:
                            await channel.send("Zu langsam :c")
                        
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                except asyncio.TimeoutError:
                    await channel.send("Zu langsam :c")

        try:
            settingmessages[str(payload.guild_id)]["selfroles"]
        except:
            settingmessages[str(payload.guild_id)]["selfroles"] = []

        if payload.message_id in settingmessages[str(payload.guild_id)]["selfroles"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":

                await channel.send(f"Definiere die Selfroles bitte nach folgenden Syntax: <ID der Nachricht, auf die Reagiert werden soll> <Channel in dem Die Nachricht Steht Pingen> / <Synonym der 1. Reaction Role>, <1. Rolle die Hinzugefügt werden soll Pingen>, <1. Emoji den du benutzen Möchtest> / <Synonym der 2. Reaction Role>, <2. Rolle die Hinzugefügt werden soll Pingen>, <2. Emoji den du benutzen Möchtest>\nDu kannst bis zu 20 Selfroles für eine Nachricht festlegen\nBeispiel: ```4548945648974984, {channel.mention} / Beispiel Self Rolle 1, {self.client.user.mention}, 😶/ Beispiel Name, {payload.member.mention}, 🤓```")
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        split1 = msg.content.split("/")
                        split2 = split1[0].split(",")
                        channelid = split2[1].split("#")

                        channelid = channelid[1].replace(">", "")
                        for nachricht in split1[1:]:
                            name = nachricht.split(",")
                            m = name[1].split("&")
                            roleid = m[1]
                            roleid = roleid.replace(">", "")
                            try:
                                m = nachricht.split(",")
                                emojiid = m[2]
                                emojiid = emojiid.split(":")
                                emojiname = emojiid[1]
                                emojiid = emojiid[2]

                                emojiid = emojiid.replace(">", "")
                                serversettings[str(payload.guild_id)]["selfroles"][f"{name[0]}"] = {"name" : name[0], "type" : "single", "role" : int(roleid), "Emojiname" : emojiname, "Channelid" : int(channelid), "msgid" : int(split2[0]), "Emojiid" : int(emojiid)}
                                guild = self.client.get_guild(payload.guild_id)
                                emoji = await guild.fetch_emoji(int(emojiid))
                                chan = await self.client.fetch_channel(int(channelid))
                                message = await chan.fetch_message(int(split2[0]))
                                await message.add_reaction(emoji)
                                await channel.send(f"{name[0]} Erfolgreich!")


                            except:
                                try:
                                    m = nachricht.split(",")
                                    emojiname = m[2]
                                    serversettings[str(payload.guild_id)]["selfroles"][f"{name[0]}"] = {"name" : name[0], "type" : "single", "role" : int(roleid), "Emojiname" : emojiname, "Channelid" : int(channelid), "msgid" : int(split2[0])}
                                    emoji = emojiname.replace(" ", "")
                                    chan = await self.client.fetch_channel(int(channelid))
                                    message = await chan.fetch_message(int(split2[0]))
                                    await message.add_reaction(emoji)
                                    await channel.send(f"{name[0]} Erfolgreich!")
                                except:
                                    await channel.send(f"{name[0]} Erfolgreich!")
                                    raise

                            #emojiid = nachricht.split
                            #
                    except:
                        await channel.send("Etwas ist schief Gelaufen. Bitte stelle sicher, dass du alles richtig gemacht hast.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "2️⃣":

                await channel.send(f"Definiere die Selfroles bitte nach folgenden Syntax: <ID der Nachricht, auf die Reagiert werden soll> <Channel in dem Die Nachricht Steht Pingen> / <Synonym der 1. Reaction Role>, <1. Rolle die Hinzugefügt werden soll Pingen>, <1. Emoji den du benutzen Möchtest> / <Synonym der 2. Reaction Role>, <2. Rolle die Hinzugefügt werden soll Pingen>, <2. Emoji den du benutzen Möchtest>\nDu kannst bis zu 20 Selfroles für eine Nachricht festlegen\nBeispiel: ```4548945648974984, {channel.mention} / Beispiel Self Rolle 1, {self.client.user.mention}, 😶/ Beispiel Name, {payload.member.mention}, 🤓```")
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        split1 = msg.content.split("/")
                        split2 = split1[0].split(",")
                        channelid = split2[1].split("#")

                        channelid = channelid[1].replace(">", "")
                        for nachricht in split1[1:]:
                            name = nachricht.split(",")
                            m = name[1].split("&")
                            roleid = m[1]
                            roleid = roleid.replace(">", "")
                            try:
                                m = nachricht.split(",")
                                emojiid = m[2]
                                emojiid = emojiid.split(":")
                                emojiname = emojiid[1]
                                emojiid = emojiid[2]

                                emojiid = emojiid.replace(">", "")
                                serversettings[str(payload.guild_id)]["selfroles"][f"{name[0]}"] = {"name" : name[0], "type" : "multi", "role" : int(roleid), "Emojiname" : emojiname, "Channelid" : int(channelid), "msgid" : int(split2[0]), "Emojiid" : int(emojiid)}
                                guild = self.client.get_guild(payload.guild_id)
                                emoji = await guild.fetch_emoji(int(emojiid))
                                chan = await self.client.fetch_channel(int(channelid))
                                message = await chan.fetch_message(int(split2[0]))
                                await message.add_reaction(emoji)
                                await channel.send(f"{name[0]} Erfolgreich!")


                            except:
                                try:
                                    m = nachricht.split(",")
                                    emojiname = m[2]
                                    serversettings[str(payload.guild_id)]["selfroles"][f"{name[0]}"] = {"name" : name[0], "type" : "multi", "role" : int(roleid), "Emojiname" : emojiname, "Channelid" : int(channelid), "msgid" : int(split2[0])}
                                    emoji = emojiname.replace(" ", "")
                                    chan = await self.client.fetch_channel(int(channelid))
                                    message = await chan.fetch_message(int(split2[0]))
                                    await message.add_reaction(emoji)
                                    await channel.send(f"{name[0]} Erfolgreich!")
                                except:
                                    await channel.send(f"{name[0]} Erfolgreich!")
                                    raise

                            #emojiid = nachricht.split
                            #
                    except:
                        await channel.send("Etwas ist schief Gelaufen. Bitte stelle sicher, dass du alles richtig gemacht hast.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "3️⃣":
                
                await channel.send("Bitte gebe innerhalb der Nächsten 30 Sekunden den Namen der Self role an, die du Löschen möchtest", delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        try:
                            del serversettings[str(payload.guild_id)]["selfroles"][f"{msg.content}"]
                            await channel.send("Erfolgreich")
                        except:
                            await channel.send("Etwas ist schief gelaufen.")

                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                except TimeoutError:
                    await channel.send("Zu langsam :c")

        
        try:
            settingmessages[str(payload.guild_id)]["Serverstats"]
        except:
            settingmessages[str(payload.guild_id)]["Serverstats"] = []


        if payload.message_id in settingmessages[str(payload.guild_id)]["Serverstats"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)

            if payload.emoji.name == "1️⃣":
                serversettings[str(payload.guild_id)]["Serverstats"]["User"] = not serversettings[str(payload.guild_id)]["Serverstats"]["User"]
                
                if serversettings[str(payload.guild_id)]["Serverstats"]["User"] == True:
                    try:
                        vc = guild.get_channel(serversettings[str(payload.guild_id)]["Serverstats"]["Userid"])
                    except:
                        guild = ""
                        for g in self.client.guilds:
                            if g.id == payload.guild_id:
                                guild = g
                        vc = await guild.create_voice_channel(name = "User: 1")
                        serversettings[str(payload.guild_id)]["Serverstats"]["Userid"] = vc.id
                await channel.send("Erfolgreich!", delete_after=10)
                
            if payload.emoji.name == "2️⃣":
                serversettings[str(payload.guild_id)]["Serverstats"]["Insgesammt_User"] = not serversettings[str(payload.guild_id)]["Serverstats"]["Insgesammt_User"]
                
                if serversettings[str(payload.guild_id)]["Serverstats"]["Insgesammt_User"] == True:
                    try:
                        vc = guild.get_channel(serversettings[str(payload.guild_id)]["Serverstats"]["Insgesammt_Userid"])
                    except:
                        guild = ""
                        for g in self.client.guilds:
                            if g.id == payload.guild_id:
                                guild = g
                        vc = await guild.create_voice_channel(name = "Insgesammt: 8")
                        serversettings[str(payload.guild_id)]["Serverstats"]["Insgesammt_Userid"] = vc.id
                await channel.send("Erfolgreich!", delete_after=10)
                
            if payload.emoji.name == "3️⃣":
                serversettings[str(payload.guild_id)]["Serverstats"]["Bots"] = not serversettings[str(payload.guild_id)]["Serverstats"]["Bots"]
                
                if serversettings[str(payload.guild_id)]["Serverstats"]["Bots"] == True:
                    try:
                        vc = guild.get_channel(serversettings[str(payload.guild_id)]["Serverstats"]["Botsid"])
                    except:
                        guild = ""
                        for g in self.client.guilds:
                            if g.id == payload.guild_id:
                                guild = g
                        vc = await guild.create_voice_channel(name = "Bots auf dem Server: 9")
                        serversettings[str(payload.guild_id)]["Serverstats"]["Botsid"] = vc.id
                await channel.send("Erfolgreich!", delete_after=10)
                
            if payload.emoji.name == "4️⃣":
                serversettings[str(payload.guild_id)]["Serverstats"]["Datum"] = not serversettings[str(payload.guild_id)]["Serverstats"]["Datum"]
                
                if serversettings[str(payload.guild_id)]["Serverstats"]["Datum"] == True:
                    try:
                        vc = guild.get_channel(serversettings[str(payload.guild_id)]["Serverstats"]["Datumid"])
                    except:
                        guild = ""
                        for g in self.client.guilds:
                            if g.id == payload.guild_id:
                                guild = g
                        vc = await guild.create_voice_channel(name = "Datum: 0.0.2019")
                        serversettings[str(payload.guild_id)]["Serverstats"]["Datumid"] = vc.id
                await channel.send("Erfolgreich!", delete_after=10)


            if payload.emoji.name == "5️⃣":

                await channel.send("Bitte gebe inerhalb der nächsten 30 Sekunden das Userziel ein.", delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        try:
                            int(msg.content)
                            serversettings[str(payload.guild_id)]["Serverstats"]["Userziel"] = msg.content
                        except:
                            await channel.send("Bitte gebe eine Zahl ein.")
                            return
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                        return
                except TimeoutError:
                    await channel.send("Zu langsam :c")
                    return
                
                
                if serversettings[str(payload.guild_id)]["Serverstats"]["Userziel"] != 0:
                    try:
                        vc = guild.get_channel(serversettings[str(payload.guild_id)]["Serverstats"]["Uhrzeitid"])
                    except:
                        guild = ""
                        for g in self.client.guilds:
                            if g.id == payload.guild_id:
                                guild = g
                        vc = await guild.create_voice_channel(name = "Userziel: 8")
                        serversettings[str(payload.guild_id)]["Serverstats"]["Userzielid"] = vc.id
                await channel.send("Erfolgreich!", delete_after=10)
                
        try:
            settingmessages[str(payload.guild_id)]["werbung"]
        except:
            settingmessages[str(payload.guild_id)]["werbung"] = []

        if payload.message_id in settingmessages[str(payload.guild_id)]["werbung"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                
                fragen = [
                "Bitte gebe den Rotanteil der Farbe des embeds ein (0 - 255)",
                "Bitte gebe den Grünanteil der Farbe des embeds ein (0 - 255)",
                "Bitte gebe den Blauanteil der Farbe des embeds ein (0 - 255)", 
                "Was soll der Titel des Embeds sein?", 
                "Was soll die Beschreibung des Embeds sein?",
                "Was soll Das kleine Bild oben rechts im Embed sein? (wenn du keins Möchstes, Schreibe 'Nichts' ansonsten schicke eine URL Zu dem Bild)", "Was soll das Große Bild Unten im Embed sein? (wenn du keins Möchstes, Schreibe 'Nichts' ansonsten schicke eine URL Zu dem Bild)", 
                "Wie viele Felder soll dein Embed haben? (Maximal 50)",
                "Was soll der Kleine Text unten am embed sein?"
                ]
                antworten = []
                def check(m):
                    return m.author == payload.member and m.channel == channel
                for i in fragen:
                    await channel.send(i)
                    try:
                        msg = await self.client.wait_for("message",
                                                    timeout=3600,
                                                    check=check)
                    except asyncio.TimeoutError:
                        await channel.send("Die eingabe wurde abgebrochen.")
                    else:
                        antworten.append(msg.content)
                for _ in itertools.repeat(None, int(antworten[7])):
                
                    await channel.send("Bitte Gebe den Titel des Feldes ein.")
                    try:
                        msg = await self.client.wait_for("message",
                                                    timeout=3600,
                                                    check=check)
                    except asyncio.TimeoutError:
                        await channel.send("Die eingabe wurde abgebrochen.")
                    else:
                        antworten.append(msg.content)

                    await channel.send("Bitte Gebe den Inhalt des Feldes ein. Du Kannst auch Embeds Erstellen.")
                    try:
                        msg = await self.client.wait_for("message",
                                                    timeout=3600,
                                                    check=check)
                    except asyncio.TimeoutError:
                        await channel.send("Die eingabe wurde abgebrochen.")
                    else:
                        antworten.append(msg.content)

                try:
                    serversettings[str(payload.guild_id)]["werbung"]["Werbung"] = antworten
                except:
                    await channel.send("Etwas ist unerwartet Schief Gelaufen. Bitte gebe Eric bescheid!")
                    return

                await channel.send("Erfolgreich!", delete_after=10)



            if payload.emoji.name == "2️⃣":

                antworten = serversettings[str(payload.guild_id)]["werbung"]["Werbung"]
                Color = discord.Color.from_rgb(int(antworten[0]), int(antworten[1]), int(antworten[2]))
                myEmbed = discord.Embed(title=antworten[3], description=antworten[4], color=Color)
                if not antworten[5] == "Nichts":
                    myEmbed.set_thumbnail(url = antworten[5])
                if not antworten[6] == "Nichts":
                    myEmbed.set_image(url = antworten[6])
                myEmbed.set_footer(text=antworten[8])
                c = -3
                for _ in itertools.repeat(None, int((len(antworten) - 8) / 2)):
                    c += 2
                    myEmbed.add_field(name = antworten[c + 10], value  = antworten[c + 11], inline  = False)
                
                await channel.send(embed = myEmbed)

            if payload.emoji.name == "3️⃣":

                serversettings[str(payload.guild_id)]["werbung"]["Active"] = not serversettings[str(payload.guild_id)]["werbung"]["Active"]
                
                await channel.send("Erfolgreich!", delete_after=10)

            if payload.emoji.name == "4️⃣":

                await channel.send("Bitte Makiere innerhalb der nächsten 30 Sekunden Den Werbechannel.", delete_after=10)
                try:
                    msg = await self.client.wait_for('message', timeout=30, check=lambda message: message.author == payload.member)
                    try:
                        chan = msg.channel_mentions[0]
                        serversettings[str(payload.guild_id)]["werbung"]["Werbechannel"] = chan.id
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                except TimeoutError:
                    await channel.send("Zu langsam :c")

        try:
            settingmessages[str(payload.guild_id)]["splitroles"]
        except:
            settingmessages[str(payload.guild_id)]["splitroles"] = []

        if payload.message_id in settingmessages[str(payload.guild_id)]["splitroles"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                await channel.send("Bitte Makiere innerhalb der nächsten 60 Sekunden Die Splitrollen, die du Hinzufügen willst und danach alle Rollen die dieser Kategorie angehören (z.B. @Alter @10-15 @15-18 @18+)", delete_after=60)
                try:
                    msg = await self.client.wait_for('message', timeout=60, check=lambda message: message.author == payload.member)
                    try:
                        roles = msg.raw_role_mentions
                        try:
                            serversettings[str(payload.guild_id)]["splitroles"][str(roles[0])]
                        except:
                            serversettings[str(payload.guild_id)]["splitroles"][str(roles[0])] = []
                        for role in roles[1:]:
                            serversettings[str(payload.guild_id)]["splitroles"][str(roles[0])].append(role)
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "2️⃣":
                await channel.send("Bitte Makiere innerhalb der nächsten 60 Sekunden Die Splitrollen, die du Entfernen willst. (Du kannst mehrere Makieren)", delete_after=60)
                try:
                    msg = await self.client.wait_for('message', timeout=60, check=lambda message: message.author == payload.member)
                    try:
                        roles = msg.raw_role_mentions
                        for role in roles:
                            del serversettings[str(payload.guild_id)]["splitroles"][role]
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send("Etwas ist Schief gelaufen.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")

        try:
            settingmessages[str(payload.guild_id)]["defaultroles"]
        except:
            settingmessages[str(payload.guild_id)]["defaultroles"] = []

        if payload.message_id in settingmessages[str(payload.guild_id)]["defaultroles"]:
            channel = await self.client.fetch_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
            if payload.emoji.name == "1️⃣":
                await channel.send("Bitte Makiere innerhalb der nächsten 60 Sekunden all die Rollen, die Alle Member haben sollen (du kannst mehrere Rollen makieren)", delete_after=60)
                try:
                    msg = await self.client.wait_for('message', timeout=60, check=lambda message: message.author == payload.member)
                    try:
                        rollen = []
                        guild = ""
                        roles = msg.raw_role_mentions
                        for g in self.client.guilds:
                            if g.id == payload.guild_id:
                                guild = g
                        for role in roles:
                            serversettings[str(payload.guild_id)]["defaultroles"]["nonbots"].append(role)
                            rollen.append(guild.get_role(int(role)))
                        ccc = 0
                        for member in guild.members:
                            rols = rollen
                            ccc += 1
                            try:
                                rols = member.roles
                                for r in rollen:
                                    if not r in rols:
                                        rols.append(r)
                                if not rols == member.roles:
                                    await member.edit(roles = rols)
                            except:
                                raise
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send(f"Etwas ist Schief gelaufen.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "2️⃣":
                await channel.send("Bitte Makiere innerhalb der nächsten 60 Sekunden all die Rollen, die Normale Member haben sollen (du kannst mehrere Rollen makieren)", delete_after=60)
                try:
                    msg = await self.client.wait_for('message', timeout=60, check=lambda message: message.author == payload.member)
                    try:
                        rollen = []
                        guild = ""
                        roles = msg.raw_role_mentions
                        for g in self.client.guilds:
                            if g.id == payload.guild_id:
                                guild = g
                        for role in roles:
                            serversettings[str(payload.guild_id)]["defaultroles"]["nonbots"].append(role)
                            rollen.append(guild.get_role(int(role)))
                        ccc = 0
                        for member in [member for member in guild.members if not member.bot]:
                            rols = rollen
                            ccc += 1
                            try:
                                rols = member.roles
                                for r in rollen:
                                    if not r in rols:
                                        rols.append(r)
                                if not rols == member.roles:
                                    await member.edit(roles = rols)
                            except:
                                raise
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send(f"Etwas ist Schief gelaufen.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "3️⃣":
                await channel.send("Bitte Makiere innerhalb der nächsten 60 Sekunden all die Rollen, Die du aus der Liste Enfernen willst. (du kannst mehrere Makieren)", delete_after=60)
                try:
                    msg = await self.client.wait_for('message', timeout=60, check=lambda message: message.author == payload.member)
                    try:
                        roles = msg.raw_role_mentions
                        rols = serversettings[str(payload.guild_id)]["defaultroles"]["allmembers"]
                        for r in roles:
                            c = 0
                            for rr in rols:
                                if r == rr:
                                    rols.pop(c)
                                c += 1
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send(f"Etwas ist Schief gelaufen.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")

            if payload.emoji.name == "4️⃣":
                await channel.send("Bitte Makiere innerhalb der nächsten 60 Sekunden all die Rollen, Die du aus der Liste Enfernen willst. (du kannst mehrere Makieren)", delete_after=60)
                try:
                    msg = await self.client.wait_for('message', timeout=60, check=lambda message: message.author == payload.member)
                    try:
                        roles = msg.raw_role_mentions
                        rols = serversettings[str(payload.guild_id)]["defaultroles"]["nonbots"]
                        for r in roles:
                            c = 0
                            for rr in rols:
                                if r == rr:
                                    rols.pop(c)
                                c += 1
                        await channel.send("Erfolgreich!", delete_after=10)
                    except:
                        await channel.send(f"Etwas ist Schief gelaufen.")
                        raise
                except TimeoutError:
                    await channel.send("Zu langsam :c")
        try:
            print(serversettings)
            if serversettings != None:
                serversettingscollection.update_one({"_id" : payload.guild_id}, {"$set" : serversettings[str(payload.guild_id)]}, upsert = True)
            else:
                serversettings[str(payload.guild_id)]["_id"] = payload.guild_id
                serversettingscollection.insert_one(serversettings[str(payload.guild_id)])
        except:
            serversettings[str(payload.guild_id)]["_id"] = payload.guild_id
            serversettingscollection.insert_one(serversettings[str(payload.guild_id)])

        try:
            if settingmessages != None:
                settingmessagescollection.update_one({"_id" : payload.guild_id}, {"$set" : settingmessages[str(payload.guild_id)]}, upsert = True)
            else:
                settingmessages[str(payload.guild_id)]["_id"] = payload.guild_id
                settingmessagescollection.insert_one(settingmessages[str(payload.guild_id)])
        except:
            settingmessages[str(payload.guild_id)]["_id"] = payload.guild_id
            settingmessagescollection.insert_one(settingmessages[str(payload.guild_id)])




async def partnerembedsender(self):
    for guild in self.client.guilds:
        try:
            
            try:
                serversettings = serversettingscollection.find_one({"_id" : guild.id})
                if serversettings == None:
                    serversettings = {}
            except:
                serversettings = {}

            serversettings[str(guild.id)] = serversettings
            print(guild)
            antworten = serversettings[str(guild.id)]["werbung"]["Werbung"]
            Color = discord.Color.from_rgb(int(antworten[0]), int(antworten[1]), int(antworten[2]))
            myEmbed = discord.Embed(title=antworten[3], description=antworten[4], color=Color)
            if not antworten[5] == "Nichts":
                myEmbed.set_thumbnail(url = antworten[5])
            if not antworten[6] == "Nichts":
                myEmbed.set_image(url = antworten[6])
            myEmbed.set_footer(text=antworten[8])
            c = -3
            for _ in itertools.repeat(None, int((len(antworten) - 8) / 2)):
                c += 2
                myEmbed.add_field(name = antworten[c + 10], value  = antworten[c + 11], inline  = False)
            chan = self.client.get_channel(serversettings[str(guild.id)]["werbung"]["Werbechannel"])
            msg =await chan.send(embed = myEmbed)
            await msg.publish()
        except:
            pass

def setup(client):
    client.add_cog(servereinrichten(client))
            