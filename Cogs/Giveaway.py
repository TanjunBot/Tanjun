from csv import excel_tab
from email.policy import default
from os import times
from telnetlib import SE
from aiohttp import request
from io import BytesIO
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageOps
import discord
from discord.ext import commands, tasks
import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from discord.ext.commands import has_permissions
from discord.ui import Button, View, Select
import asyncio
import DiscordUtils
import time
import numpy as np
from discord.commands import Option, slash_command

cluster = MongoClient("")

db = cluster["Main"]
collection = db["giveaways"]
messagecounter = db["messagecount"]
serversettingscollection = db["serversettings"]
invitecounter = db["invitecount"]
entrycounter = db["entrys"]
blacklistcollection = db["blacklist"]
Pfeilrot = "ᐅ"
Pin = "📌"
Pfeilblau = "➛"
emoji = "🎉"





class Giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.tracker = DiscordUtils.InviteTracker(self.client)

    @commands.Cog.listener()
    async def on_ready(self):
        self.updategiveaways.start()

    @slash_command(name='removenachrichten', description='Nehme jemanden Nachrichten weg.')
    async def removenachrichten(self, ctx, user : Option(discord.Member, "Wem möchtest du die Nachrichten entfernen?", required = True), menge : Option(int, "Wie viele Nachrichen möchtest du entfernen?", required = True)):
        await ctx.defer()
        menge = menge *-1

        x = messagecounter.find_one({"_id" : user.id})

        if x == None:
            x = messagecounter.insert_one({"_id" : user.id, str(ctx.guild.id) : menge})
        else:
            x = messagecounter.update_one({"_id" : user.id}, {"$inc" : { str(ctx.guild.id) : menge}})
            
        await ctx.respond(f"Ich habe erfolgreich **{menge * -1}** Nachrichten von **{user}** entfernt.")


    @slash_command(name='nachrichten', description='Sehe wie viele Nachrichten jemand (oder eine ganze Rolle) geschrieben hat!')
    async def nachrichten(self, ctx, user : Option(discord.Member, "Von wen möchtest du die Nachrichten sehen?", required = False, default = None), role : Option(discord.Role, "Von wen möchtest du die Nachrichten sehen?", required = False, default = None)):
        await ctx.defer()
        print(role)
        counter = 0
        if role != None:
            ladebalken = await ctx.send("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%")
            embeds = []
            await ctx.respond("Dieser Prozess könnte etwas Dauern!")
            msg = f"Hier sind die Nachrichten aller Member mit der Rolle {role.mention}\n"

            Nachrichtending = {}
            counter = 0
            for member in role.members:
                counter += 1
                if int(counter / len(role.members) * 100) == 10:
                    if ladebalken.content != "🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ 10%":
                        ladebalken = await ladebalken.edit("🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ 10%")


                if int(counter / len(role.members) * 100) == 20:
                    if ladebalken.content != "🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜ 20%":
                        ladebalken = await ladebalken.edit("🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜ 20%")

                if int(counter / len(role.members) * 100) == 30:
                    if ladebalken.content != "🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜ 30%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜ 30%")

                if int(counter / len(role.members) * 100) == 40:
                    if ladebalken.content != "🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜ 40%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜ 40%")

                if int(counter / len(role.members) * 100) == 50:
                    if ladebalken.content != "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜ 50%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜ 50%")

                if int(counter / len(role.members) * 100) == 60:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜ 60%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜ 60%")

                if int(counter / len(role.members) * 100) == 70:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜ 70%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜ 70%")

                if int(counter / len(role.members) * 100) == 80:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ 80%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ 80%")

                if int(counter / len(role.members) * 100) == 90:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜ 90%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜ 90%")

                if int(counter / len(role.members) * 100) == 100:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 100%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 100%")
                print(member)
                try:
                    messages = messagecounter.find_one({"_id" : member.id})
                    Nachrichtending[member.id] = {"Anzahl" :  int(messages[str(ctx.guild.id)]), "membermention" : member.mention}
                except:
                    pass
                
            print(Nachrichtending)
            ranking = sorted(Nachrichtending.items(),key=lambda x: x[1]["Anzahl"],reverse=True)

            c = 1
            for rank in ranking:
                print(rank)
                rank = rank[1]
                msg += f"`Platz {c}:` *{rank['membermention']}* mit **{rank['Anzahl']}** Nachrichten.\n" 
                if len(msg) >= 1700:
                    myEmbed = discord.Embed(title = "Nachrichten", description= msg, color=0xbd24e7)
                    msg = ""
                    
                    await ctx.send(embed = myEmbed)
                c += 1
            if msg == f"Hier sind die Nachrichten aller Member mit der Rolle {role.mention}\n":
                msg += "\nWie es scheint hat niemand eine Nachricht geschrieben 😔"
            myEmbed = discord.Embed(title = "Nachrichten", description= msg, color=0xbd24e7)
            await ctx.send(embed = myEmbed)
            
            return
        else:
            if user == None:
                user = ctx.author
            messages = messagecounter.find_one({"_id" : user.id})
            embed = discord.Embed(title = "Nachrichten", description= f"{user.mention} hat momentan {messages[str(ctx.guild.id)]} Nachrichten!" , color=0xbd24e7)
            await ctx.respond(embed = embed)

    @slash_command(name='einladungen', description='Finde heraus, wie viele Leute du und andere bereits eingeladen haben!.')
    async def einladungen(self, ctx, user : Option(discord.Member, "Von wen möchtest du die Einladungen sehen?", required = False, default = None), role : Option(discord.Role, "Von wen möchtest du die Einladungen sehen?", required = False, default = None)):
        await ctx.defer()
        print(role)
        counter = 0
        if role != None:
            ladebalken = await ctx.send("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%")
            embeds = []
            await ctx.respond("Dieser Prozess könnte etwas Dauern!")
            msg = f"Hier sind die Einladungen aller Member mit der Rolle {role.mention}\n"

            Nachrichtending = {}
            counter = 0
            for member in role.members:
                counter += 1
                if int(counter / len(role.members) * 100) == 10:
                    if ladebalken.content != "🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ 10%":
                        ladebalken = await ladebalken.edit("🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ 10%")


                if int(counter / len(role.members) * 100) == 20:
                    if ladebalken.content != "🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜ 20%":
                        ladebalken = await ladebalken.edit("🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜ 20%")

                if int(counter / len(role.members) * 100) == 30:
                    if ladebalken.content != "🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜ 30%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜ 30%")

                if int(counter / len(role.members) * 100) == 40:
                    if ladebalken.content != "🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜ 40%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜ 40%")

                if int(counter / len(role.members) * 100) == 50:
                    if ladebalken.content != "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜ 50%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜ 50%")

                if int(counter / len(role.members) * 100) == 60:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜ 60%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜ 60%")

                if int(counter / len(role.members) * 100) == 70:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜ 70%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜ 70%")

                if int(counter / len(role.members) * 100) == 80:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ 80%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜ 80%")

                if int(counter / len(role.members) * 100) == 90:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜ 90%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜ 90%")

                if int(counter / len(role.members) * 100) == 100:
                    if ladebalken.content != "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 100%":
                        ladebalken = await ladebalken.edit("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 100%")
                print(member)
                try:
                    messages = invitecounter.find_one({"_id" : member.id})
                    Nachrichtending[member.id] = {"Anzahl" :  int(messages[str(ctx.guild.id)]), "membermention" : member.mention}
                except:
                    pass
                
            print(Nachrichtending)
            ranking = sorted(Nachrichtending.items(),key=lambda x: x[1]["Anzahl"],reverse=True)

            c = 1
            for rank in ranking:
                print(rank)
                rank = rank[1]
                msg += f"`Platz {c}:` *{rank['membermention']}* mit **{rank['Anzahl']}** Einladungen.\n" 
                if len(msg) >= 1700:
                    myEmbed = discord.Embed(title = "Einladungen", description= msg, color=0xbd24e7)
                    msg = ""
                    
                    await ctx.send(embed = myEmbed)
                c += 1
            if msg == f"Hier sind die Einladungen aller Member mit der Rolle {role.mention}\n":
                msg += "\nWie es scheint hat niemand jemanden eingeladen 😔"
            myEmbed = discord.Embed(title = "Einladungen", description= msg)
            await ctx.send(embed = myEmbed)
            
            return
        else:
            if user == None:
                user = ctx.author
            messages = invitecounter.find_one({"_id" : user.id})
            embed = discord.Embed(title = "Einladungen", description= f"{user.mention} hat momentan {messages[str(ctx.guild.id)]} Einladungen!" , color=0xbd24e7)
            await ctx.respond(embed = embed)
    
    @has_permissions(manage_events=True)
    @slash_command(name='gwend', description='Beende ein Giveaway frühzeitig.')
    async def gwend(self, ctx, giveawayid : Option(str, "Wie lautet die ID der Giveaway-Nachricht?", required = True)):
        await ctx.defer()
        giveaway = collection.find_one({"_id" : int(giveawayid)})
        channel = self.client.get_channel(int(giveaway["channel"]))
        msg = await channel.fetch_message(giveawayid)
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winners = await getwinner(users, giveaway["winneramount"], giveawayid, ctx.guild.id)
        winnerstr = ""
        c = 0
        for winner in winners:
            if c == 0:
                winnerstr += (f"{winner.mention}")
            else:
                winnerstr += (f", {winner.mention}")
            c += 1
        gegenstand = giveaway["gegenstand"]
        gilde = self.client.get_guild(933307298011562006)
        Pfeilrot = await gilde.fetch_emoji(934772227491127347)
        Tröte = await gilde.fetch_emoji(934771963241566228)
        Herz = await gilde.fetch_emoji(934185048402448394)
        
        myEmbed = discord.Embed(title = f"{gegenstand}",description=f"** - GIVEAWAY GEWINNER - **\n\n› __Informationen__\n{Pfeilrot}  Gewinner: {winnerstr}\n{Pfeilrot} gesponsored von <@{giveaway['creator_id']}>",color=0xbd24e7)
        await msg.edit(embed = myEmbed)
        if c == 1:
            await channel.send(f"Herzlichen Glückwunsch {winnerstr}! Du hast {gegenstand} gewonnen!")
        else:
            await channel.send(f"Herzlichen Glückwunsch {winnerstr}! Ihr habt {gegenstand} gewonnen!")
        collection.delete_one({"_id" : giveawayid})
        await ctx.respond("Das Giveaway wurde erfolgreich frühzeitig beendet.")

    @has_permissions(manage_events=True)
    @slash_command(name='greroll', description='Lose einen neuen Gewinner für ein Giveaway aus.')
    async def greroll(self, ctx, giveawayid : Option(str, "Wie lautet die ID der Giveaway-Nachricht?", required = True)):
        await ctx.defer()
        giveaway = collection.find_one({"_id" : int(giveawayid)})
        channel = self.client.get_channel(int(giveaway["channel"]))
        msg = await channel.fetch_message(giveawayid)
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winners = await getwinner(users, giveaway["winneramount"], giveawayid, ctx.guild.id)
        winnerstr = ""
        c = 0
        for winner in winners:
            if c == 0:
                winnerstr += (f"{winner.mention}")
            else:
                winnerstr += (f", {winner.mention}")
            c += 1
        gegenstand = giveaway["gegenstand"]
        
        myEmbed = discord.Embed(title = f"{gegenstand}",description=f"** - GIVEAWAY GEWINNER - **\n\n› __Informationen__\n{Pfeilrot}  Gewinner: {winnerstr}",color=0xbd24e7)
        await msg.edit(embed = myEmbed)
        if c == 1:
            await channel.send(f"Herzlichen Glückwunsch {winnerstr}! Du hast {gegenstand} gewonnen!")
        else:
            await channel.send(f"Herzlichen Glückwunsch {winnerstr}! Ihr habt {gegenstand} gewonnen!")
        collection.delete_one({"_id" : giveawayid})
        if c == 1:
            await ctx.respond("Es wurde erfolgreich ein neuer Gewinner ausgelost.")  
        else:
            await ctx.respond("Es wurden erfolgreich neue Gewinner ausgelost.")               

    möglichkeiten = [
        discord.OptionChoice(name = "Keine Bedingung", value = "0"),
        discord.OptionChoice(name = "Bestimmt viele Nachrichten", value = "1"),
        discord.OptionChoice(name = "Bestimmt viele Einladungen", value = "2"),
        discord.OptionChoice(name = "Bestimmte Rolle", value = "3"),
        discord.OptionChoice(name = "Server Empfehlen", value = "4"),
        discord.OptionChoice(name = "Mitglied seit x Tagen", value = "5"),
        discord.OptionChoice(name = "Eigene Bedingung", value = "6")
    ]

    möglichkeiten2 = [
        discord.OptionChoice(name = "Bedingung umkehren", value = "True"),
        discord.OptionChoice(name = "Bedingung nicht umkehren", value = "False")
    ]

    @has_permissions(manage_events=True)
    @slash_command(name='gstart', description='Starte ein Giveaway')
    async def gstart(self, ctx, länge: Option(str, "Wie lange soll das Giveaway für die Teilnahme geöffnet sein? (z.B.10h)", required = True), gewinner: Option(int, "Wie viele Gewinner soll es geben?", required = True), gewinn: Option(str, "Was soll verlost werden?", required = True), bedingung: Option(str, "Welche Bedingung(en) soll es geben?", required = True, choices = möglichkeiten), bedingung_umkehren: Option(str, "Soll(en) die Bedingung(en) umgekehrt werden?", required = True, choices = möglichkeiten2), channel: Option(discord.TextChannel, "In welchem Channel soll das Giveaway veranstaltet werden?", required = False, default = None), sponsor: Option(discord.Member, "Ist das Giveaway von jemanden gesponsert?", required = False, default = None)):
        await ctx.defer()
        if channel == None:
            channel = ctx.channel
        
        if bedingung_umkehren == "True":
            bedingung_umkehren = True
        else:
            bedingung_umkehren = False

        if sponsor == None:
            sponsor = ctx.author

        länge = convert(länge)
        if länge == -1:
            await ctx.respond("Bitte gebe die Zeit nach dem folgendem Schema an: `10h` oder `12m`!")
        if länge == -2:
            await ctx.respond("Bitte gebe die Zeit nach dem folgendem Schema an: `10h` oder `12m`!")

        def check(m):
            print(m)
            return m.channel == ctx.channel and m.author == ctx.author

        timestamp = int(time.time())

        if bedingung == "0":
            anforderung = None
            bedingungid = 0
            bedingungzusatz = None

        if bedingung == "1":
            async def get_nachrichten_anzahl(error = False):
                if error == False:
                    myEmbed = discord.Embed(title = f"**NACHRICHTENANZAHL WÄHLEN**",description=f"\n› Schreibe in den Chat wie viele Nachrichten die Server-Mitglieder zum teilnehmen benötigen.",color=0xbd24e7)
                else:
                    myEmbed = discord.Embed(title = f"**NACHRICHTENANZAHL WÄHLEN**",description=f"\n› Schreibe in den Chat wie viele Nachrichtendie Server-Mitglieder zum teilnehmen benötigen.\nBeispiel: __1__",color=0xbd24e7)
                view = View()
                await ctx.send(embed = myEmbed, view = view)
                try:
                    nachrichtenmsg = await self.client.wait_for('message', check=check, timeout=120)
                    try:
                        nachrichten = int(nachrichtenmsg.content)
                        return nachrichten
                    except:
                        await get_nachrichten_anzahl(error = True)
                
                    await nachrichtenmsg.delete()
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(title = f"Bist du noch da?",description=f"Du hast zu lange keine Antwort gegeben. Ich hab auch andere Dinge zu tun :c Das Setup wurde abgebrochen.",color=0xbd24e7)
                    await ctx.send(embed = myEmbed, view = view)
                    return "Error"


            nachrichten = await get_nachrichten_anzahl()
            if nachrichten == "Error":
                return
            anforderung = f"Du musst mindestens {nachrichten} Nachichten senden!"
            bedingungid = 1
            bedingungzusatz = nachrichten


        if bedingung == "2":
            async def get_einladungen_anzahl(error = False):
                if error == True:
                    myEmbed = discord.Embed(title = f"**INVITEANZAHL WÄHLEN**",description=f"\n› Schreibe in den Chat wie viele Invites die Server-Mitglieder zum teilnehmen benötigen.\nBeispiel: __1__",color=0xbd24e7)

                else:
                    myEmbed = discord.Embed(title = f"**INVITEANZAHL WÄHLEN**",description=f"\n› Schreibe in den Chat wie viele Invites die Server-Mitglieder zum teilnehmen benötigen.",color=0xbd24e7)

                view = View()
                await ctx.send(embed = myEmbed, view = view)
                try:
                    einladungenmsg = await self.client.wait_for('message', check=check, timeout=60)
                    try:
                        einladungen = int(einladungenmsg.content)
                        return einladungen
                    except:
                        await get_einladungen_anzahl(error = True)
                
                    await einladungenmsg.delete()
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(title = f"Bist du noch da?",description=f"Du hast zu lange keine Antwort gegeben. Ich hab auch andere Dinge zu tun :c Das Setup wurde abgebrochen.",color=0xbd24e7)
                    await ctx.send(embed = myEmbed, view = view)
                    return "Error"

            einladungen = await get_einladungen_anzahl()
            if einladungen == "Error":
                return
            anforderung = f"Du musst mindestens {einladungen} Personen eingeladen haben!"
            bedingungid = 6
            bedingungzusatz = einladungen
      

        if bedingung == "3":
            async def get_role(error = False):
                if error == True:
                    myEmbed = discord.Embed(title = f"** - BESTIMMTE ROLLE WÄHLEN**",description=f"\n› __**Erwähne die Rolle**__, welche Mitglieder benötigen, um an dem Gewinnspiel teilnehmen zu können. {Pin}",color=0xbd24e7)

                else:
                    myEmbed = discord.Embed(title = f"** - BESTIMMTE ROLLE WÄHLEN**",description=f"\n› Erwähne die Rolle, welche Mitglieder benötigen, um an dem Gewinnspiel teilnehmen zu können. {Pin}",color=0xbd24e7)


                view = View()
                await ctx.send(embed = myEmbed, view = view)
                try:
                    rolemsg = await self.client.wait_for('message', check=check, timeout=60)
                    try:
                        role = rolemsg.role_mentions
                        role = role[0]
                        await rolemsg.delete()
                        return role
                    except:
                        role = await role(error = True)
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(title = f"Bist du noch da?",description=f"Du hast zu lange keine Antwort gegeben. Ich hab auch andere Dinge zu tun :c Das Setup wurde abgebrochen.",color=0xbd24e7)
                    await ctx.send(embed = myEmbed, view = view)
                    return "Error"
                
            role = await get_role()
            if role == "Error":
                return
            anforderung = f"Du benötigst die {role.mention} Rolle!"
            bedingungid = 2
            bedingungzusatz = role.id


        if bedingung == "4":
            async def get_server(error = False):
                if error == True:
                    myEmbed = discord.Embed(title = f"**- SERVER-EMPFEHLUNG WÄHLEN**",description=f"\n› Schicke einen Einladungslink von dem Server, welcher in dem Gewinnspiel erwähnt werden soll. {Pin}\n**__DIESER LINK SOLLTE NIE ABLAUFEN**__\nDie Einladung.. oder was auch immer du da geschick hast?! darf nicht länger als 100 Zeichen sein.",color=0xbd24e7)

                else:
                    myEmbed = discord.Embed(title = f"**- SERVER-EMPFEHLUNG WÄHLEN**",description=f"\n› Schicke einen Einladungslink von dem Server, welcher in dem Gewinnspiel erwähnt werden soll. {Pin}\n**__DIESER LINK SOLLTE NIE ABLAUFEN**__",color=0xbd24e7)

                view = View()
                await ctx.send(embed = myEmbed, view = view)
                try:
                    link = await self.client.wait_for('message', check=check, timeout=60)
                    if len(link.content) > 200:
                        link = await get_server(error = True)
                    await link.delete()
                    return link.content
                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(title = f"Bist du noch da?",description=f"Du hast zu lange keine Antwort gegeben. Ich hab auch andere Dinge zu tun :c Das Setup wurde abgebrochen.",color=0xbd24e7)
                    await ctx.send(embed = myEmbed, view = view)
                    return "Error"
            link = await get_server()
            if link == "Error":
                return
            anforderung = f"Schaue bei diesem [Discord-Server]({link}) vorbei! [Keine Pflicht]!"
            bedingungid = 3
            bedingungzusatz = link

        if bedingung == "5":
            async def get_member_since(error = False):
                if error == True:
                    myEmbed = discord.Embed(title = f"** - MITGLIED SEIT X TAGEN - WÄHLEN**",description=f"\n› Wähle eine Zeit, wie viele Tage ein Mitglied auf dem Server sein muss, um teilzunehmen. :PepeBox: \nBeispiel: 1d, 5m, 10d",color=0xbd24e7)
        
                    myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
                    
                else:
                    myEmbed = discord.Embed(title = f"** - MITGLIED SEIT X TAGEN - WÄHLEN**",description=f"\n› Wähle eine Zeit, wie viele Tage ein Mitglied auf dem Server sein muss, um teilzunehmen. :PepeBox: \nBeispiel: __1d, 5m, 10d__",color=0xbd24e7)

                view = View()
                await ctx.send(embed = myEmbed, view = view)
                try:
                    membersincemsg = await self.client.wait_for('message', check=check, timeout=60)
                    länge = membersincemsg.content
                    länge = convert(länge)
                    if länge == -1:
                        return await get_member_since(error = True)
                    if länge == -2:
                        return await get_member_since(error = True)
                    await membersincemsg.delete()
                    return länge

                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(title = f"Bist du noch da?",description=f"Du hast zu lange keine Antwort gegeben. Ich hab auch andere Dinge zu tun :c Das Setup wurde abgebrochen.",color=0xbd24e7)
                    await ctx.send(embed = myEmbed, view = view)
                    return "Error"

            membersince = await get_member_since()
            if membersince == "Error":
                return
            anforderung = f"Du musst mindestens seit <t:{timestamp - membersince}:D> Mitglied des Servers sein."
            bedingungid = 4
            bedingungzusatz = timestamp - membersince


        if bedingung == "6":
            async def eigene_bedingung(error = False):
                if error == True:
                    myEmbed = discord.Embed(title = f"**EIGENE BEDINGUNG WÄHLEN**",description=f"\n❌ › Schreibe cancel um das Setup jederzeit sofort abzubrechen.\n\n› Schreibe eine Teilnahmebedingung in den Chat, die du möchtest, welche nicht aufgelistet war. {emoji}",color=0xbd24e7)
        
                    myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
                    
                else:
                    myEmbed = discord.Embed(title = f" **  - EIGENE BEDINGUNG - WÄHLEN**",description=f"\n❌ › Schreibe cancel um das Setup jederzeit sofort abzubrechen.\n\n› Schreibe eine Teilnahmebedingung in den Chat, die du möchtest, welche nicht aufgelistet war. {emoji}",color=0xbd24e7)

                
                view = View()
                await ctx.send(embed = myEmbed, view = view)
                try:
                    bedingungmsg = await self.client.wait_for('message', check=check, timeout=60)
                    if len(bedingungmsg.content) >= 500:
                        return await eigene_bedingung(error = True)
                    await bedingungmsg.delete()
                    return bedingungmsg.content

                except asyncio.TimeoutError:
                    myEmbed = discord.Embed(title = f"Bist du noch da?",description=f"Du hast zu lange keine Antwort gegeben. Ich hab auch andere Dinge zu tun :c Das Setup wurde abgebrochen.",color=0xbd24e7)
                    await ctx.send(embed = myEmbed, view = view)
                    return "Error"
            
            anforderung = await eigene_bedingung(error = False)
            if anforderung == "Error":
                return
            bedingungzusatz = None
            bedingungid = 5


        if sponsor == None:
            if anforderung == None:
                myEmbed = discord.Embed(title = f"{gewinn}",description=f"** - GIVEAWAY**\n\n› __Informationen__\n{Pfeilrot} **{gewinner}** Gewinner\n{Pfeilrot} gesponsert von {sponsor.mention}\n{Pfeilrot} Endet <t:{timestamp + länge}:R> (<t:{timestamp + länge}:D>)\n\n{Pin}› __Anforderungen__\n{Pfeilblau} Reagiere mit {emoji} um **teilzunehmen**!",color=0xbd24e7)
            else:
                if bool(bedingung_umkehren) == False:
                    myEmbed = discord.Embed(title = f"{gewinn}",description=f"** - GIVEAWAY**\n\n› __Informationen__\n{Pfeilrot} **{gewinner}** Gewinner\n{Pfeilrot} gesponsert von {sponsor.mention}\n{Pfeilrot} Endet <t:{timestamp + länge}:R> (<t:{timestamp + länge}:D>)\n\n{Pin}› __Anforderungen__\n{Pfeilblau} {anforderung}\n{Pfeilblau} Reagiere mit {emoji} um **teilzunehmen**!",color=0xbd24e7)
                else:
                    myEmbed = discord.Embed(title = f"{gewinn}",description=f"** - GIVEAWAY**\n\n› __Informationen__\n{Pfeilrot} **{gewinner}** Gewinner\n{Pfeilrot} gesponsert von {sponsor.mention}\n{Pfeilrot} Endet <t:{timestamp + länge}:R> (<t:{timestamp + länge}:D>)\n\n{Pin}› __Anforderungen__\n{Pfeilblau} {anforderung} (Anforderung darf **NICHT** Erfüllt sein)\n{Pfeilblau} Reagiere mit {emoji} um **teilzunehmen**!",color=0xbd24e7)
        else:
            if anforderung == None:
                myEmbed = discord.Embed(title = f"{gewinn}",description=f"** - GIVEAWAY**\n\n› __Informationen__\n{Pfeilrot} **{gewinner}** Gewinner\n{Pfeilrot} gesponsert von {sponsor.mention}\n{Pfeilrot} Endet <t:{timestamp + länge}:R> (<t:{timestamp + länge}:D>)\n\n{Pin}› __Anforderungen__\n{Pfeilblau} Reagiere mit {emoji} um **teilzunehmen**!",color=0xbd24e7)
            else:
                if bool(bedingung_umkehren) == False:
                    myEmbed = discord.Embed(title = f"{gewinn}",description=f"** - GIVEAWAY**\n\n› __Informationen__\n{Pfeilrot} **{gewinner}** Gewinner\n{Pfeilrot} gesponsert von {sponsor.mention}\n{Pfeilrot} Endet <t:{timestamp + länge}:R> (<t:{timestamp + länge}:D>)\n\n{Pin}› __Anforderungen__\n{Pfeilblau} {anforderung}\n{Pfeilblau} Reagiere mit {emoji} um **teilzunehmen**!",color=0xbd24e7)
                else:
                    myEmbed = discord.Embed(title = f"{gewinn}",description=f"** - GIVEAWAY**\n\n› __Informationen__\n{Pfeilrot} **{gewinner}** Gewinner\n{Pfeilrot} gesponsert von {sponsor.mention}\n{Pfeilrot} Endet <t:{timestamp + länge}:R> (<t:{timestamp + länge}:D>)\n\n{Pin}› __Anforderungen__\n{Pfeilblau} {anforderung} (Anforderung darf **NICHT** Erfüllt sein)\n{Pfeilblau} Reagiere mit {emoji} um **teilzunehmen**!",color=0xbd24e7)

        if bedingungid == 3:
            giveawaymessage = await channel.send(content = bedingungzusatz, embed = myEmbed)
        else:
            giveawaymessage = await channel.send(embed = myEmbed)
    
        await giveawaymessage.add_reaction(emoji)
        post = {"_id" : giveawaymessage.id, "time" : timestamp + länge, "channel" : giveawaymessage.channel.id, "winneramount" : gewinner, "gegenstand" : gewinn, "endet" : False, "creator_id" : sponsor.id, "bedingungid" : bedingungid, "bedingungzusatz" : bedingungzusatz, "bedingung_umgekehrt" : bool(bedingung_umkehren)}
        collection.insert_one(post)
        collection.update_one({"_id" : "Guilds_with_giveaways"}, {"$addToSet":{"guilds" : {str(ctx.guild.id) : giveawaymessage.id}}})
        collection.update_one({"_id" : "giveawayids"}, {"$addToSet":{"ids" : giveawaymessage.id}})
        await ctx.respond(f"Das Gewinnspiel wurde erfolgreich gestartet!")

    @tasks.loop(seconds=10)
    async def updategiveaways(self):
        timestamp = int(time.time())
        guildids = collection.find_one({"_id" : "Guilds_with_giveaways"})
        if guildids == None:
            collection.insert_one({"_id" : "Guilds_with_giveaways", "guilds" : []})

        for guildid in guildids["guilds"]:
            try:
                for serverid, msgid in guildid.items():
                    giveaway = collection.find_one({"_id" : msgid})
                    channel = self.client.get_channel(int(giveaway["channel"]))
                    msg = await channel.fetch_message(msgid)
                    await checkwinners(self, msg)
                    if giveaway["endet"] == False:
                        if giveaway["time"] <= timestamp:
                            users = await msg.reactions[0].users().flatten()
                            users.pop(users.index(self.client.user))
                            winners = await getwinner(users, giveaway["winneramount"], msgid, serverid)
                            winnerstr = ""
                            c = 0
                            for winner in winners:
                                if c == 0:
                                    winnerstr += (f"{winner.mention}")
                                else:
                                    winnerstr += (f", {winner.mention}")
                                c += 1
                            gegenstand = giveaway["gegenstand"]
                            
                            myEmbed = discord.Embed(title = f"{gegenstand}",description=f"** - GIVEAWAY GEWINNER - **\n\n› __Informationen__\n{Pfeilrot}  Gewinner: {winnerstr}\n{Pfeilrot} gesponsored von <@{giveaway['creator_id']}>",color=0xbd24e7)

                            await msg.edit(embed = myEmbed)

                            if c == 1:
                                await channel.send(f"Herzlichen Glückwunsch {winnerstr}! Du hast {gegenstand} gewonnen!")
                            else:
                                await channel.send(f"Herzlichen Glückwunsch {winnerstr}! Ihr habt {gegenstand} gewonnen!")

                            collection.delete_one({"_id" : msgid})
                            

            except:
                pass
            print(guildid)

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):

        print("Msg!")

        if message.channel.id == 936428366125490276:
            return
        
        if message.guild == None:
            return
        
        if message.author.bot == True:
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

        x = messagecounter.find_one({"_id" : message.author.id})

        if x == None:
            x = messagecounter.insert_one({"_id" : message.author.id, str(message.guild.id) : 1})
        else:
            x = messagecounter.update_one({"_id" : message.author.id}, {"$inc" : { str(message.guild.id) : 1}})

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot == True:
            return
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        await checkwinners(self, message)
        

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        x = invitecounter.find_one({"_id" : member.id})
        inviter = int(x["inviter"])
        try:
            invitecounter.update_one({"_id" : inviter}, {"$inc" : {str(member.guild.id) : -1}}, upsert=True)
            x = serversettingscollection.find_one({"_id" : member.guild.id})
            if x["JoinLeavemsg"]["leaveactive"] == True:
                try:
                    channel = await self.client.fetch_channel(x["JoinLeavemsg"]["Leavemessagechannel"])
                    if x["JoinLeavemsg"]["lText"] != "":
                        if x["JoinLeavemsg"]["leaveimage"] == False:
                            text = x["JoinLeavemsg"]["lText"]
                            try:
                                text = text.replace("uuu", member.mention)
                            except:
                                text = text.replace("uuu", "Member nicht gefunden!")

                            try:
                                
                                text = text.replace("iii", f"<@{inviter}>")
                            except:
                                text = text.replace("iii", "Member konnte nicht gefunden werden.")

                            try:
                                messages = invitecounter.find_one({"_id" : inviter})

                                text = text.replace("III", str(messages[str(member.guild.id)]))
                            except:
                                text = text.replace("III", "0 (Vielleicht irre ich mich hierbei!)")
                            leaveembed = discord.Embed(title='Jemand hat uns verlassen <:P_SadCat:907549840161005598>',description=text,color=0xBD24E7)
                            await channel.send(embed = leaveembed)
                        else:
                            asset = member.avatar.with_size(256)
                            data = BytesIO(await asset.read())
                            pfp = Image.open(data)
                            pfp = pfp.resize((200, 200))
                            pfp.save("Images/Profilbild.png")
                            pfp = Image.open("Images/Profilbild.png").convert("RGB")
                            npImage = np.array(pfp)
                            h, w = pfp.size

                            # Create same size alpha layer with circle
                            alpha = Image.new('L', pfp.size, 0)
                            draw = ImageDraw.Draw(alpha)
                            draw.pieslice([0, 0, h, w], 0, 360, fill=255)

                            # Convert alpha Image to numpy array
                            npAlpha = np.array(alpha)

                            # Add alpha layer to RGB
                            npImage = np.dstack((npImage, npAlpha))

                            Image.fromarray(npImage).save('Images/result.png')

                            pfp = Image.open("Images/result.png").convert("RGB")

                            npImage = np.array(pfp)
                            h, w = pfp.size

                            # Create same size alpha layer with circle
                            alpha = Image.new('L', pfp.size, 0)
                            draw = ImageDraw.Draw(alpha)
                            draw.pieslice([0, 0, h, w], 0, 360, fill=255)

                            # Convert alpha Image to numpy array
                            npAlpha = np.array(alpha)

                            # Add alpha layer to RGB
                            npImage = np.dstack((npImage, npAlpha))

                            Image.fromarray(npImage).save('Images/result.png')

                            Bild = Image.open("Images/JoinLeavebg.jpg").convert("RGB")

                            pfp = Image.open("Images/result.png")

                            Bild.paste(pfp, (400, 100), pfp)
                            draw = ImageDraw.Draw(Bild)
                            font_type = ImageFont.truetype("Fonts/JoinFont.ttf", 50)
                            draw.text((500, 350), f"Leider ist er von uns gegangen :c", font=font_type, fill ="white",anchor="mm")

                            text = x["JoinLeavemsg"]["lText"]
                            try:
                                text = text.replace("uuu", member.mention)
                            except:
                                text = text.replace("uuu", "Member nicht gefunden!")

                            try:
                                text = text.replace("iii", f"<@{inviter}>")
                            except:
                                text = text.replace("iii", "Member konnte nicht gefunden werden.")

                            try:
                                messages = invitecounter.find_one({"_id" : inviter})

                                text = text.replace("III", str(messages[str(member.guild.id)]))
                            except:
                                text = text.replace("III", "0 (Vielleicht irre ich mich hierbei!)")

                            font_type = ImageFont.truetype("Fonts/JoinFont.ttf", 50)
                            draw = ImageDraw.Draw(Bild)
                            draw.text((500, 50), f"Auf wiedersehen {member.name}", font=font_type, fill ="white",anchor="mm")


                            Bild.save("Images/temp2.png")
                            leaveembed2 = discord.Embed(title='Jemand hat uns verlassen <:P_SadCat:907549840161005598>',description=text,color=0xBD24E7)
                            msg2 = await channel.send(embed = leaveembed2, file=discord.File("Images/temp2.png"))
                except:
                    raise
        except:
                raise




    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            inviter = await self.tracker.fetch_inviter(member)
        except:
            return



        created_at = member.created_at 
        print(inviter)

        x = serversettingscollection.find_one({"_id" : member.guild.id})

        if x["JoinLeavemsg"]["joinactive"] == True:

            try:
                invitecounter.update_one({"_id" : inviter.id}, {"$inc" : {str(member.guild.id) : 1}}, upsert=True)
                invitecounter.update_one({"_id" : member.id}, {"$set" : {"inviter" : str(inviter.id)}}, upsert = True)
                channel = await self.client.fetch_channel(x["JoinLeavemsg"]["Joinmessagechannel"])
                if x["JoinLeavemsg"]["Text"] != "":
                    if x["JoinLeavemsg"]["image"] == False:
                        text = x["JoinLeavemsg"]["Text"]
                        try:
                            text = text.replace("uuu", member.mention)
                        except:
                            text = text.replace("uuu", "Member nicht gefunden!")

                        try:
                            text = text.replace("iii", inviter.mention)
                        except:
                            text = text.replace("iii", "Member konnte nicht gefunden werden")

                        try:
                            messages = invitecounter.find_one({"_id" : inviter.id})
                            
                            text = text.replace("III", str(messages[str(member.guild.id)]))
                        except:
                            text = text.replace("III", "0 (Vielleicht irre ich mich hierbei!)")

                        await channel.send(text)
                    else:
                        asset = member.avatar.with_size(256)
                        data = BytesIO(await asset.read())
                        pfp = Image.open(data)
                        pfp = pfp.resize((200, 200))
                        pfp.save("Images/Profilbild.png")
                        pfp = Image.open("Images/Profilbild.png").convert("RGB")
                        npImage = np.array(pfp)
                        h, w = pfp.size

                        # Create same size alpha layer with circle
                        alpha = Image.new('L', pfp.size, 0)
                        draw = ImageDraw.Draw(alpha)
                        draw.pieslice([0, 0, h, w], 0, 360, fill=255)

                        # Convert alpha Image to numpy array
                        npAlpha = np.array(alpha)

                        # Add alpha layer to RGB
                        npImage = np.dstack((npImage, npAlpha))

                        Image.fromarray(npImage).save('Images/result.png')

                        pfp = Image.open("Images/result.png").convert("RGB")

                        npImage = np.array(pfp)
                        h, w = pfp.size

                        # Create same size alpha layer with circle
                        alpha = Image.new('L', pfp.size, 0)
                        draw = ImageDraw.Draw(alpha)
                        draw.pieslice([0, 0, h, w], 0, 360, fill=255)

                        # Convert alpha Image to numpy array
                        npAlpha = np.array(alpha)

                        # Add alpha layer to RGB
                        npImage = np.dstack((npImage, npAlpha))

                        Image.fromarray(npImage).save('Images/result.png')

                        if not member.guild.id == 831161440705839124:
                            Bild = Image.open("Images/JoinLeavebg.jpg").convert("RGB")
                        else:
                            Bild = Image.open("Images/PokemonWecomebg.jpg").convert("RGB")

                        pfp = Image.open("Images/result.png")

                        Bild.paste(pfp, (400, 100), pfp)

                        circle = Image.open("Images/circle.png")

                        Bild.paste(circle, (0, 0), circle)

                        draw = ImageDraw.Draw(Bild)
                        font_type = ImageFont.truetype("Fonts/JoinFont.ttf", 50)
                        draw.text((500, 350), f"Member Nummer {len(member.guild.members)}!", font=font_type, fill ="white",anchor="mm")

                        text = x["JoinLeavemsg"]["Text"]
                        try:
                            text = text.replace("uuu", member.mention)
                        except:
                            text = text.replace("uuu", "Member nicht gefunden!")

                        try:
                            text = text.replace("iii", inviter.mention)
                        except:
                            
                            text = text.replace("iii", "Member konnte nicht gefunden werden.")

                        try:
                            messages = invitecounter.find_one({"_id" : inviter.id})
                            
                            text = text.replace("III", str(messages[str(member.guild.id)]))
                        except:
                            text = text.replace("III", "0 (Vielleicht irre ich mich hierbei!)")
                            raise

                        font_type = ImageFont.truetype("Fonts/JoinFont.ttf", 50)
                        draw = ImageDraw.Draw(Bild)
                        draw.text((500, 50), f"Willkommen {member.name}", font=font_type, fill ="white",anchor="mm")


                        Bild.save("Images/temp2.png")
                        msg2 = await channel.send(content = text, file=discord.File("Images/temp2.png"))


            except:
                raise

        rols = []
        if member.bot == False:
            try:
                for r in x["defaultroles"]["nonbots"]:
                    rols.append(member.guild.get_role(int(r)))
            except:
                pass
        else:
            try:
                for r in x["defaultroles"]["nonbots"]:
                    rols.append(member.guild.get_role(int(r)))
                for r in x["defaultroles"]["allmembers"]:
                    rols.append(member.guild.get_role(int(r)))
            except:
                pass
        try:
            await member.edit(roles = rols)
        except:
            pass

        if  True:
            channel = await inviter.create_dm()
            myEmbed = discord.Embed(title = f"{member} hat grade deine Einladung angenommen, jedoch ist der Account jünger als 14 Tage. Die Einladung wird somit nicht gezählt.",color=0xbd24e7)
            try:
                await channel.send(embed = myEmbed)
            except:
                pass
            return

        x = invitecounter.find_one({"_id" : inviter.id})

        if x == None:
            x = invitecounter.insert_one({"_id" : inviter.id, str(member.guild.id) : 1})
        else:
            x = invitecounter.update_one({"_id" : inviter.id}, {"$inc" : { str(member.guild.id) : 1}})

    @slash_command(name='chance', description='Finde heraus, wie hoch deine Gewinnchance ist.')
    async def chance(self, ctx, user : Option(discord.Member, "Von wen möchtest du die Gewinnchance sehen?", required = False, default = None), gewinnspielid : Option(str, "von welchem Giveaway möchtest du deine Gewinnchance sehen?", required = False, default = None)):
        await ctx.defer()
        if user == None:
            user = ctx.author
        
        chance = 0
        entrys = entrycounter.find_one({"_id" : user.id})
        if entrys == None:
            myEmbed = discord.Embed(title = f"Gewinnchance!", description=f"Die Gewinnchance von {user.mention} ist um 0% erhöht.",color=0xbd24e7)
            await ctx.respond(embed = myEmbed)
            return
        chance += int(entrys[str(ctx.guild.id)])
        if not gewinnspielid == None:
            try:
                chance += int(entrys[str(gewinnspielid)])
            except:
                pass
            myEmbed = discord.Embed(title = f"Gewinnchance!", description=f"Die Gewinnchance von {user.mention} ist um {chance}% erhöht für das Gewinnspiel mit der ID {gewinnspielid}",color=0xbd24e7)
        else:
            myEmbed = discord.Embed(title = f"Gewinnchance!", description=f"Die Gewinnchance von {user.mention} ist um {chance}% eröht",color=0xbd24e7)
        
        await ctx.respond(embed = myEmbed)

    @has_permissions(administrator=True)
    @slash_command(name='setchance', description='Beeinflusse die Gewinnchance von jemanden.')
    async def setchance(self, ctx, user : Option(discord.Member, "Von wen möchtest du die Gewinnchance ändern?", required = True), chance : Option(str, "Wie viel soll die Chance erhöht werden?", required = True, default = None), gewinnspielid : Option(str, "von welchem Giveaway möchtest du deine Gewinnchance ändern?", required = False, default = None)):
        await ctx.defer()
        if gewinnspielid == None:
            x = entrycounter.find_one({"_id" : user.id})

            if x == None:
                x = entrycounter.insert_one({"_id" : user.id, str(ctx.guild.id) : chance})
            else:
                x = entrycounter.update_one({"_id" : user.id}, {"$inc" : { str(ctx.guild.id) : chance}})
            
        else:
            x = entrycounter.find_one({"_id" : user.id})

            if x == None:
                x = entrycounter.insert_one({"_id" : user.id, str(gewinnspielid) : chance})
            else:
                x = entrycounter.update_one({"_id" : user.id}, {"$inc" : { str(gewinnspielid) : chance}})
        await ctx.respond(f"Die gewinnchance von {user.mention} wurde erfolgreich um {chance}% erhöht!")


    @has_permissions(administrator=True)
    @slash_command(name='reset', description='Setze die Nachrichten/Invites für diesen Server zurück.')
    async def reset(self, ctx):
        await ctx.defer()
        async def nachrichten_callback(interaction):
            await ctx.send("Die Nachrichten werden jetzt zurückgesetzt.")
            for member in ctx.guild.members:
                messagecounter.update_one({"_id" : member.id}, {"$set" : { str(member.guild.id) : 0}})
            await ctx.send("Die Nachrichten wurden erfolgreich zurückgesetzt.")

        async def invites_callback(interaction):
            await ctx.send("Die Einladungen werden jetzt zurückgesetzt.")
            for member in ctx.guild.members:
                invitecounter.update_one({"_id" : member.id}, {"$set" : { str(member.guild.id) : 0}})
            await ctx.send("Die Einladungen wurden erfolgreich zurückgesetzt.")

        nachrichten = Button(label = "Nachrichten", style = discord.ButtonStyle.red)
        nachrichten.callback = nachrichten_callback

        invites = Button(label = "Einladungen", style = discord.ButtonStyle.red)
        invites.callback = invites_callback

        view = View()

        view.add_item(nachrichten)
        view.add_item(invites)

        await ctx.send(content = "Was möchtest du zurücksetzen?", view = view)


async def getwinner(entrys, winneramount, gid, guildid):
    participants = []
    for entry in entrys:
        for _ in range(100):
            participants.append(entry)
        entrys = entrycounter.find_one({"_id" : entry.id})
        try:
            for _ in range(int(entrys[str(guildid)])):
                participants.append(entry)
        except:
            pass
        try:
            for _ in range(int(entrys[str(gid)])):
                participants.append(entry)
        except:
            pass
        
    print(participants)
    winners = []
    for _ in range(winneramount):
        winners.append(random.choice(participants))
    print(winners)
    return winners


async def checkwinners(self, msg):

    giveaway = collection.find_one({"_id" : msg.id})
    for r in msg.reactions:
        try:
            if r.emoji == "🎉":
                users = await r.users().flatten()

                umgekehrt = giveaway["bedingung_umgekehrt"]
                print(umgekehrt)

                for user in users:
                    print()
                    print()
                    print("Ich teste jetzt:")
                    print(user)
                    print()
                    print()
                    if user.bot == False:
                        print(f"{user} wird jetzt getestet.")
                        bedingungid = giveaway["bedingungid"]
                        if bedingungid == 0:
                            pass
                            
                        if bedingungid == 1:
                            print("Ich teste jetzt nach nachrichten :)")
                            try:
                                msgcount = messagecounter.find_one({"_id" : user.id})
                                print(msgcount)
                                msgcount = msgcount[str(msg.guild.id)]
                            except:
                                raise
                                msgcount = 0
                            maxmessagecount = int(giveaway['bedingungzusatz'])
                            guild = ""
                            if msgcount > maxmessagecount:
                                if umgekehrt == False:
                                    print("Der User hat genug 👍")
                                    pass
                                else:
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Du hast {msgcount - maxmessagecount} Nachrichten zu viel.",color=0xbd24e7)
                                
                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                                    print("Hab ihn weg gemacht :p")
                            else:  
                                if umgekehrt == False:
                                    print("der User hat nicht Genug >:c")
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Dir fehlen noch {maxmessagecount - msgcount} Nachrichten.",color=0xbd24e7)


                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                                    print("Hab ihn weg gemacht :p")
                                else:
                                    pass
                            
                        if bedingungid == 6:

                            msgcount = invitecounter.find_one({"_id" : user.id})
                            msgcount = msgcount[msg.guild.id]
                            maxmessagecount = int(giveaway['bedingungzusatz'])
                            guild = ""
                            if msgcount > maxmessagecount:
                                if umgekehrt == False:
                                    pass
                                else:
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Du hast {msgcount - maxmessagecount} Einladungen zu viel.",color=0xbd24e7)
                                
                                
                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                            
                            else:   
                                if umgekehrt == False: 
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Dir fehlen noch {maxmessagecount - msgcount} Einladungen.",color=0xbd24e7)


                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                                else:
                                    pass
                            
                        if bedingungid == 2:
                            guild = await self.client.fetch_guild(msg.guild.id)
                            role = discord.utils.find(lambda r: r.id == int(giveaway['bedingungzusatz']), guild.roles)
                            if role in user.roles:
                                if umgekehrt == False:
                                    pass
                                else:
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Du hast die Erforderliche Rolle <@{int(giveaway['bedingungzusatz'])}>.",color=0xbd24e7)
                                
                                
                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                                
                            else:
                                if umgekehrt == False:
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Du hast die Erforderliche Rolle <@{int(giveaway['bedingungzusatz'])}> Nicht.",color=0xbd24e7)


                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                                else:
                                    pass
                                
                        if bedingungid == 3:
                            pass
                        if bedingungid == 4:
                            länge = user.joined_at
                            print(int(länge.timestamp()))
                            print(int(giveaway['bedingungzusatz']))
                            if int(länge.timestamp()) < int(giveaway['bedingungzusatz']):
                                if umgekehrt == False:
                                    pass
                                else:
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Du bist zu lang auf den Server.",color=0xbd24e7)
                                
                                
                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                                
                            else:
                                if umgekehrt == False:
                                    myEmbed = discord.Embed(title = f"Teilnahme Fehlgeschlagen!",description=f"Du kannst nicht an dem [Gewinnspiel](https://discord.com/channels/@me/{giveaway['channel']}/{msg.id}) teilnehmen. Du bist nicht lang genug auf den Server.",color=0xbd24e7)


                                    channel = await user.create_dm()
                                    try:
                                        await channel.send(embed = myEmbed)
                                    except:
                                        pass
                                    await msg.remove_reaction(emoji, user)
                                else:
                                    pass
                                
                            
                        if bedingungid == 5:
                            pass
            else:
                pass
        except:
            try:
                await msg.remove_reaction(emoji, user)
            except:
                pass
            

def convert(time):
    pos = ["s", "m", "h", "d", "w", "M"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800, "M" : 2628000}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]
        

def setup(client):
    client.add_cog(Giveaway(client))

