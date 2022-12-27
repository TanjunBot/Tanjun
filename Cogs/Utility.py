
import os
from pydoc import describe
import random
import asyncio
import itertools
import pytz
import discord
from icrawler.builtin import GoogleImageCrawler
from discord.ext.commands import has_permissions
import time
from discord.commands import Option, slash_command
import requests # request img from web
from io import BytesIO
from PIL import Image
from discord.ext import commands
from num2words import num2words
import requests
import urllib.request
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
#import Utility

dev_list = [471036610561966111, 760155365710102549, 766350321638309958, 689565769230712866, 810484550727761940]
arions_aktueller_botinvitelink = "https://discord.com/oauth2/authorize?client_id=885984139315122206&permissions=8&redirect_uri=https%3A%2F%2Fr.arion2000.xyz&response_type=code&scope=identify%20bot%20applications.commands%20guilds"

from pymongo import MongoClient

cluster = MongoClient("")
serverstatscluster = MongoClient("")

db = cluster["Main"]
serverstatsdb = serverstatscluster["Main"]
levelsyscollection = db["levelsys"]
flaggenquizcollection = db["flaggenquiz"]
emojiquizcollecton = db["emojiquiz"]
oneWordcollection = db["oneword"]
ideas = db["ideas"]
umfragecollection = db["ideen"]
changelogcollection = db["changelog"]
statscollection = serverstatsdb["stats"]
bdaycollection = db["bdays"]
blacklistcollection = db["blacklist"]
countingcollection = db["counting"]
gamecollection = db["game"]
serverideecollection = db["serverideen"]


allemojipacks =  requests.get('https://emoji.gg/api/').json()
allemojis = []
for emoji in allemojipacks:
        #print(emoji)
        allemojis.append(emoji)


class utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    actions = [
        discord.OptionChoice(name = "setemojiquizchannel.", value = "setemojiquizchannel"),
        discord.OptionChoice(name = "Wortkettechannel.", value = "oneword"),
        discord.OptionChoice(name = "Flaggenquizchannel", value = "Flaggenquizchannel"),
        discord.OptionChoice(name = "birthdaychannel", value = "birthdaychannel"),
        discord.OptionChoice(name = "countingchannel", value = "countingchannel"),
        discord.OptionChoice(name = "gamechannel", value = "gamechannel"),
        discord.OptionChoice(name = "serverideechannel", value = "serverideechannel")
    ]

    @slash_command(name='set', description='Lege einen Channel fest.')
    async def set(self, ctx, action : Option(str, "Für was möchtest du den Channel festlegen?", required = True, choices = actions), channel : Option(discord.TextChannel, "Welchen Channel?.", required = True)):
        await ctx.defer()
        if action == "setemojiquizchannel":
            emojiquizcollecton.update_one({"_id": ctx.guild.id}, {"$set": {"channelid": channel.id, "sentence" : ""}}, upsert=True)
            quizzes = emojiquizcollecton.find_one({"_id" : "general"})

            quiz = random.choice(quizzes["quizze"])

            emojiquizcollecton.update_one({"_id": ctx.guild.id}, {"$set": {"lösung": quiz["lösung"]}}, upsert=True)

            await channel.send(content = f"Für was stehen diese Emojis?\n\n{quiz['emojis']}")


            await ctx.respond(f"Der Channel für das Emojiquiz wurde erfolgreich auf {channel.mention} gesetzt.")

        elif action == "oneword":
            oneWordcollection.update_one({"_id": ctx.guild.id}, {"$set": {"channelid": channel.id, "sentence" : ""}}, upsert=True)

            await ctx.respond(f"Der Channel für Wortkette wurde erfolgreich auf {channel.mention} gesetzt.")

        elif action == "Flaggenquizchannel":
            flaggenquizcollection.update_one({"_id": ctx.guild.id}, {"$set": {"channelid": channel.id}}, upsert=True)
            länder = ["Abchasien","Afghanistan","Ägypten","Albanien","Algerien","Andorra","Angola","Anguilla","Antarktis","Antigua und Barbuda","Äquatorialguinea","Argentinien","Armenien","Aruba","Aserbaidschan","Äthiopien","Australien","Azoren","Bahamas","Bahrain","Bangladesch","Barbados","Belarus","Belgien","Belize","Benin","Bhutan","Bolivien","Bosnien und Herzegowina","Botsuana","Brasilien","Brunei","Bulgarien","Burkina Faso","Myanmar","Burundi","Chile","China","Cookinseln","Costa Rica","Dänemark","Kongo","Deutschland, Dominica","Dschibuti","Ecuador","Elfenbeinküste","El Salvador","Eritrea, Estland","Eswatini","Falklandinseln","Fidschi","Finnland","Föderierte Staaten von Mikronesien","Frankreich","Französisch-Polynesien","Französisch-Guayana","Gabun","Gambia","Georgien","Ghana","Grenada","Griechenland","Großbritannien","Grönland","Guadeloupe","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Indien","Indonesien","Irak","Iran","Irland","Island","Israel","Italien","Jamaika","Japan","Jemen","Jordanien","Kambodscha","Kamerun","Kanada","Kap Verde","Kasachstan","Katar","Kenia","Kirgisistan","Kiribati","Kolumbien","Komoren","Kongo","Kroatien","Kuba","Kuwait","Kosovo","Laos","Lesotho","Lettland","Libanon","Liberia","Libyen","Liechtenstein","Litauen","Luxemburg","Madagaskar","Madeira","Malawi","Malaysia","Malediven","Mali","Malta","Marokko","Marshallinseln","Martinique","Mauretanien","Mauritius","Mexiko","Moldau","Monaco","Mongolei","Montenegro","Mosambik","Myanmar","Namibia","Nauru","Nepal","Neuseeland","Nicaragua","Niederlande","Niederländische Antillen","Niger","Nigeria","Nordkorea","Nordmazedonien","Nordzypern","Norwegen","Oman","Österreich","Osttimor","Pakistan","Palau","Palästina","Panama","Papua-Neuguinea","Paraguay","Peru","Philippinen","Polen","Portugal","Puerto Rico","Réunion","Ruanda","Rumänien","Russland","Saint Kitts und Nevis","Saint Lucia","Saint Pierre und Miquelon","Saint Vincent und die Grenadinen","Salomonen","Sambia","Samoa","San Marino","São Tomé und Príncipe","Saudi-Arabien","Schweden","Schweiz","Senegal","Serbien","Seychellen","Sierra Leone","Singapur","Simbabwe","Slowakei","Slowenien","Somalia","Spanien","Sri Lanka","Südafrika","Sudan","Südkorea","Südsudan","Suriname","Syrien","Tadschikistan","Taiwan","Tansania","Thailand","Togo","Tokelau","Tonga","Trinidad und Tobago","Tschad","Tschechien","Tunesien","Türkei","Turkmenistan","Tuvalu","Uganda","Ukraine","Ungarn","USA","Uruguay","Usbekistan","Vanuatu","Vatikan","Venezuela","Vereinigte Arabische Emirate","Vereinigtes Königreich","Vereinigte Staaten von Amerika","Vietnam","Wallis und Futuna","Westsahara","Zentralafrikanische Republik","Zypern"]

            land = random.choice(länder)

            flaggenquizcollection.update_one({"_id": ctx.guild.id}, {"$set": {"land": land}})

            google_crawler = GoogleImageCrawler(storage={'root_dir': 'Googlebild'})
            google_crawler.crawl(keyword=f"{land} Flagge", max_num=1)
            for file in os.listdir('Googlebild'):
                await channel.send(file=discord.File(f"Googlebild/{file}"), content ="Welches Land ist das?")
                os.remove(f"Googlebild/{file}")

            await ctx.respond(f"Der Channel für das Flaggenquiz wurde erfolgreich auf {channel.mention} gesetzt.")

        elif action == "birthdaychannel":
            bdaycollection.update_one({"_id" : ctx.guild.id}, {"$set":{"channel" : channel.id}})

            await ctx.respond(f"Der neue Channel lautet <#{channel.id}>")
        
        elif action == "countingchannel":
            x = countingcollection.find_one({"_id" : ctx.guild.id})
            if x == None:
                countingcollection.insert_one({"_id" : ctx.guild.id, "channel" : channel.id})
            else:
                countingcollection.update_one({"_id" : ctx.guild.id, "channel" : channel.id})
            await ctx.respond(f"Countingchannel erfolgreich auf `{channel.mention}` gesetzt.")

        elif action == "gamechannel":
            x = gamecollection.find_one({"_id" : ctx.guild.id})
            if x == None:
                gamecollection.insert_one({"_id" : ctx.guild.id, "channel" : channel.id})
            else:
                gamecollection.update_one({"_id" : ctx.guild.id, "channel" : channel.id})

            länder = ["Abchasien","Afghanistan","Ägypten","Albanien","Algerien","Andorra","Angola","Anguilla","Antarktis","Antigua und Barbuda","Äquatorialguinea","Argentinien","Armenien","Aruba","Aserbaidschan","Äthiopien","Australien","Azoren","Bahamas","Bahrain","Bangladesch","Barbados","Belarus","Belgien","Belize","Benin","Bhutan","Bolivien","Bosnien und Herzegowina","Botsuana","Brasilien","Brunei","Bulgarien","Burkina Faso","Myanmar","Burundi","Chile","China","Cookinseln","Costa Rica","Dänemark","Kongo","Deutschland, Dominica","Dschibuti","Ecuador","Elfenbeinküste","El Salvador","Eritrea, Estland","Eswatini","Falklandinseln","Fidschi","Finnland","Föderierte Staaten von Mikronesien","Frankreich","Französisch-Polynesien","Französisch-Guayana","Gabun","Gambia","Georgien","Ghana","Grenada","Griechenland","Großbritannien","Grönland","Guadeloupe","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Indien","Indonesien","Irak","Iran","Irland","Island","Israel","Italien","Jamaika","Japan","Jemen","Jordanien","Kambodscha","Kamerun","Kanada","Kap Verde","Kasachstan","Katar","Kenia","Kirgisistan","Kiribati","Kolumbien","Komoren","Kongo","Kroatien","Kuba","Kuwait","Kosovo","Laos","Lesotho","Lettland","Libanon","Liberia","Libyen","Liechtenstein","Litauen","Luxemburg","Madagaskar","Madeira","Malawi","Malaysia","Malediven","Mali","Malta","Marokko","Marshallinseln","Martinique","Mauretanien","Mauritius","Mexiko","Moldau","Monaco","Mongolei","Montenegro","Mosambik","Myanmar","Namibia","Nauru","Nepal","Neuseeland","Nicaragua","Niederlande","Niederländische Antillen","Niger","Nigeria","Nordkorea","Nordmazedonien","Nordzypern","Norwegen","Oman","Österreich","Osttimor","Pakistan","Palau","Palästina","Panama","Papua-Neuguinea","Paraguay","Peru","Philippinen","Polen","Portugal","Puerto Rico","Réunion","Ruanda","Rumänien","Russland","Saint Kitts und Nevis","Saint Lucia","Saint Pierre und Miquelon","Saint Vincent und die Grenadinen","Salomonen","Sambia","Samoa","San Marino","São Tomé und Príncipe","Saudi-Arabien","Schweden","Schweiz","Senegal","Serbien","Seychellen","Sierra Leone","Singapur","Simbabwe","Slowakei","Slowenien","Somalia","Spanien","Sri Lanka","Südafrika","Sudan","Südkorea","Südsudan","Suriname","Syrien","Tadschikistan","Taiwan","Tansania","Thailand","Togo","Tokelau","Tonga","Trinidad und Tobago","Tschad","Tschechien","Tunesien","Türkei","Turkmenistan","Tuvalu","Uganda","Ukraine","Ungarn","USA","Uruguay","Usbekistan","Vanuatu","Vatikan","Venezuela","Vereinigte Arabische Emirate","Vereinigtes Königreich","Vereinigte Staaten von Amerika","Vietnam","Wallis und Futuna","Westsahara","Zentralafrikanische Republik","Zypern"]

            land = random.choice(länder)

            gamecollection.update_one({"_id": ctx.guild.id}, {"$set": {"awnser": land}})

            google_crawler = GoogleImageCrawler(storage={'root_dir': 'Googlebild'})
            google_crawler.crawl(keyword=f"{land} Flagge", max_num=1)
            for file in os.listdir('Googlebild'):
                await channel.send(file=discord.File(f"Googlebild/{file}"), content ="Welches Land ist das?")
                os.remove(f"Googlebild/{file}")

            await ctx.respond(f"gamechannel erfolgreich auf `{channel.mention}` gesetzt.")


        elif action == "serverideechannel":
            serverideecollection.update_one({"_id": ctx.guild.id}, {"$set": {"channelid": channel.id}}, upsert=True)

            await ctx.respond(f"Der Channel für Wortkette wurde erfolgreich auf {channel.mention} gesetzt.")


    @slash_command(name='blacklistrole', description='Lasse eine Rolle vom Bot ignorieren.')
    async def blacklistrole(self, ctx, role : Option(discord.Role, "Welche Rolle möchtest du ignorieren?", required = True)):
        await ctx.defer()

        blacklistcollection.update_one({"_id" : ctx.guild.id}, {"$addToSet":{"blacklistedroles" : role.id}}, upsert=True)

        await ctx.respond(f"die Rolle {role.mention} wurde erfolgreich geblacklistet. Ich werde auf niemanden mit dieser Rolle mehr reagieren. Außerdem gibt es für diese Rolle keine XP. Auch Nachrichten werde ich für diese Personen nicht mehr mitzählen.")


    @slash_command(name='blacklist', description='Lasse Channel vom Bot ignorieren.')
    async def blacklist(self, ctx, channel : Option(discord.TextChannel, "Welchen Channel möchtest du ignorieren?", required = True)):
        await ctx.defer()

        blacklistcollection.update_one({"_id" : ctx.guild.id}, {"$addToSet":{"blacklistedchannel" : channel.id}}, upsert=True)

        await ctx.respond(f"Der Channel <#{channel.id}> wurde erfolgreich geblacklistet. In diesen werde ich nicht mehr reagieren. Außerdem gibt es hier keine XP mehr. Auch Nachrichten werde ich hier nicht mehr mitzählen.")


    @slash_command(name='serverinfo', description='Bekomme Informationen über einen bestimmten User.')
    async def serverinfo(self, ctx):
        await ctx.defer()
        txt = ""
        txt += f"`ID: `{ctx.guild.id}\n\n"
        if ctx.guild.afk_channel != None:
            txt += f"`AFK Channel: `{ctx.guild.afk_channel.mention}\n\n"
            txt += f"`AFK Zeit: `{ctx.guild.afk_timeout}\n\n"
        if ctx.guild.afk_channel != None:
            txt += f"`Regel Kanal: `{ctx.guild.rules_channel.mention}\n\n"
        txt += f"`bitrate limit: `{ctx.guild.bitrate_limit}\n\n"
        x = ctx.guild.created_at.strftime('%d.%m.%Y %H:%M')
        txt += f"`Erstellt: `{x} Uhr\n\n"
        if ctx.guild.description != None:
            txt += f"`Beschreibung: `{ctx.guild.description}\n\n"
        txt += f"`emoji limit: `{ctx.guild.emoji_limit}\n\n"
        txt += f"`owner: `{ctx.guild.owner.mention}\n\n"
        txt += f"`Booster: `{ctx.guild.premium_subscription_count}\n\n"
        txt += f"`Level: `{ctx.guild.premium_tier}\n\n"


        cats = ""
        for categorie in ctx.guild.channels:
            cats += categorie.mention + ", "
        if cats != "":
            txt += f"`Kanäle: `{cats}\n\n"
        myEmbed = discord.Embed(title = f"Informationen über {ctx.guild.name}", description=txt, color=0xbd24e7)

        if ctx.guild.banner != None:
            myEmbed.set_image(url = ctx.guild.banner.url)
        if ctx.guild.icon != None:
            myEmbed.set_thumbnail(url = ctx.guild.icon.url)


        await ctx.respond(embed = myEmbed)

    @slash_command(name='userinfo', description='Bekomme Informationen über einen bestimmten User.')
    async def userinfo(self, ctx, user : Option(discord.Member, "Von wen möchtest du die Informationen erhalten?", required = False, default = None)):
        await ctx.defer()
        if user == None:
            user = ctx.author

        
        txt = ""
        txt += f"`ID: `{user.id}\n\n"
        if user.timed_out == True:
            txt += f"`Timeout bis: `{user.communication_disabled_until}\n\n"
        x = user.created_at.strftime('%d.%m.%Y %H:%M')
        txt += f"`Account Erstellt: `{x} Uhr\n\n"
        x = user.joined_at.strftime('%d.%m.%Y %H:%M')
        txt += f"`Server beigetreten: `{x} Uhr\n\n"
        txt += f"`display Name: `{user.display_name}\n\n"
        if user.guild_avatar != None:
            txt += f"`Server Avatar: `{user.guild_avatar.url}\n\n"
        if user.premium_since != None:
            x = user.premium_since.strftime('%d.%m.%Y %H:%M')
            txt += f"`Boostet seit: `{x} Uhr\n\n"
        if user.top_role != None:
            txt += f"`Höchste Rolle: `{user.top_role.mention}\n\n"
        perms = ""
        for permission in user.guild_permissions:
            if permission[1] == True:
                perms += f"**{permission[0]}**, "
        txt += f"`Berechtigungen: `{perms}\n\n"

        myEmbed = discord.Embed(title = f"Informationen über {user}", description=txt, color=0xbd24e7)

        use = await self.client.fetch_user(user.id)
        if use.banner != None:
            myEmbed.set_image(url = use.banner.url)
        if use.avatar != None:
            myEmbed.set_thumbnail(url = use.avatar.url)


        await ctx.respond(embed = myEmbed)

    @slash_command(name='invite', description='Bekomme den Einladungslink von Tanjun')
    async def invite(self, ctx):
        await ctx.defer()
        myEmbed = discord.Embed(title="Du willst mich einladen?", description=f"Wie nett von dir!😊 Lade mich mit [diesem]({arions_aktueller_botinvitelink}) Link auf deinen Server ein, dann können wir eine Tasse Kaffe trinken!\n[Klicke hier...]({arions_aktueller_botinvitelink})",color=0xbd24e7)
        myEmbed.set_footer(text=f"Tanjun Utility Cmds ⬝ {ctx.author}")
        try:
            await ctx.respond(embed = myEmbed)
        except:
            await ctx.send(embed = myEmbed)

    @has_permissions(view_audit_log=True)
    @slash_command(name='editembed', description='bearbeite ein Embed')
    async def editembed(self, ctx, messageid : Option(str,"Bitte gebe die ID des Embeds an, welches ich bearbeiten soll", required = True), channel : Option(discord.TextChannel,"In welchen Channel steht das Embed?", required = True)):
        await ctx.defer()
        await ctx.respond("Dir werden nun einige Fragen zu dem Embed gestellt. Wenn du ein Textfeld frei lassen möchtest, kannst du ganz einfach zwei Sterne, eine Leertaste und wieder 2 Sterne schreiben.\n\n\n\n")
        fragen = [
          "Bitte gebe den Rotanteil der Farbe des Embeds ein (0 - 255)",
          "Bitte gebe den Grünanteil der Farbe des Embeds ein (0 - 255)",
          "Bitte gebe den Blauanteil der Farbe des Embeds ein (0 - 255)", 
          "Was soll der Titel des Embeds sein?", 
          "Was soll die Beschreibung des Embeds sein?",
          "Was soll Das kleine Bild oben rechts im Embed sein? (Wenn du keines möchstest, schreibe 'Nichts' ansonsten schicke eine URL zu dem Bild)","Was soll das große Bild unten im Embed sein? (wenn du keines möchstest, schreibe 'Nichts' ansonsten schicke eine URL zu dem Bild)", 
          "Wie viele Felder soll dein Embed haben? (Maximal 50)",
          "Was soll der kleine Text unten am Embed sein?"
            ]
        antworten = []
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        for i in fragen:
            await ctx.send(i)
            try:
                msg = await self.client.wait_for("message",
                                            timeout=3600,
                                            check=check)
            except asyncio.TimeoutError:
                await ctx.send("Die Eingabe wurde abgebrochen.")
                return
            else:
                antworten.append(msg.content)
        for _ in itertools.repeat(None, int(antworten[7])):

            await ctx.send("Bitte gebe den Titel des Feldes ein.")
            try:
                msg = await self.client.wait_for("message",
                                            timeout=3600,
                                            check=check)
            except asyncio.TimeoutError:
                await ctx.send("Die Eingabe wurde abgebrochen.")
                return
            else:
                antworten.append(msg.content)

            await ctx.send("Bitte gebe den Inhalt des Feldes ein. Du kannst auch Embeds erstellen.")
            try:
                msg = await self.client.wait_for("message",
                                            timeout=3600,
                                            check=check)
            except asyncio.TimeoutError:
                await ctx.send("Die Eingabe wurde abgebrochen.")
                return
            else:
                antworten.append(msg.content)
        Color = discord.Color.from_rgb(int(antworten[0]), int(antworten[1]), int(antworten[2]))

        myEmbed = discord.Embed(title=antworten[3], description=antworten[4], color=Color)
        if not antworten[5] =="Nichts":
            myEmbed.set_thumbnail(url = antworten[5])
        if not antworten[6] =="Nichts":
            myEmbed.set_image(url = antworten[6])
        myEmbed.set_footer(text=antworten[8])
        c = -3
        for _ in itertools.repeat(None, int((len(antworten) - 8) / 2)):
            c += 2
            myEmbed.add_field(name = antworten[c + 10], value  = antworten[c + 11], inline  = False)



        new_msg = await channel.fetch_message(messageid)
        await new_msg.edit(embed = myEmbed)
        try:
            cd = self.client.get_channel(ctx.channel.id)
            await cd.send("Die Nachricht wurde erfolgreich bearbeitet.")
        except:
            cd = self.client.get_channel(ctx.channel)
            await cd.send("Die Nachricht wurde erfolgreich bearbeitet.")
        


    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        print(message)

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

        wavers = ["hallö", "Hallö", "hallu", "Hallu", "Hello", "hello", "Hellö", "hellö", "<a:Wavy:947761835250180146>", "Hellu", "hellu"]
        if message.content in wavers and message.author.bot != True:
            await message.channel.send("<a:Wavy:947761835250180146>")

        yayers = ["<a:YAY:958744453701599342>", "JAA", "JAAAAAAAAA", "yay", "YAY", "JAAAAAAAAAAAAAAAAAAAAAAAA", "WUHU", "Wuhu", "Yay"]
        if message.content in yayers and message.author.bot != True:
            await message.channel.send("<a:YAY:958744453701599342>")

        party = ["Party!", "PARTY!!!!", "<a:P_Party:960412011060162600>"]
        if message.content in party and message.author.bot != True:
            await message.channel.send("<a:P_Party:960412011060162600>")
        
        O = [":O", ":o", "o:", "O:", "😮", "😯", "😲"]
        if message.content in O and message.author.bot != True:
            await message.channel.send(":O")

        if message.guild == None:
            return

        flaggenquiz = flaggenquizcollection.find_one({"_id": message.guild.id})
        if not flaggenquiz == None:
            channelid = flaggenquiz["channelid"]
            if message.channel.id == channelid:
                Lösung = flaggenquiz["land"]
                lösung = flaggenquiz["land"].lower()
                guess = message.content.lower()
                if lösung in guess and message.author.bot == False:
                    await message.add_reaction("✅")
                    länder = ["Abchasien","Afghanistan","Ägypten","Albanien","Algerien","Andorra","Angola","Anguilla","Antarktis","Antigua und Barbuda","Äquatorialguinea","Argentinien","Armenien","Aruba","Aserbaidschan","Äthiopien","Australien","Azoren","Bahamas","Bahrain","Bangladesch","Barbados","Belarus","Belgien","Belize","Benin","Bhutan","Bolivien","Bosnien und Herzegowina","Botsuana","Brasilien","Brunei","Bulgarien","Burkina Faso","Myanmar","Burundi","Chile","China","Cookinseln","Costa Rica","Dänemark","Kongo","Deutschland, Dominica","Dschibuti","Ecuador","Elfenbeinküste","El Salvador","Eritrea, Estland","Eswatini","Falklandinseln","Fidschi","Finnland","Föderierte Staaten von Mikronesien","Frankreich","Französisch-Polynesien","Französisch-Guayana","Gabun","Gambia","Georgien","Ghana","Grenada","Griechenland","Großbritannien","Grönland","Guadeloupe","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Indien","Indonesien","Irak","Iran","Irland","Island","Israel","Italien","Jamaika","Japan","Jemen","Jordanien","Kambodscha","Kamerun","Kanada","Kap Verde","Kasachstan","Katar","Kenia","Kirgisistan","Kiribati","Kolumbien","Komoren","Kongo","Kroatien","Kuba","Kuwait","Kosovo","Laos","Lesotho","Lettland","Libanon","Liberia","Libyen","Liechtenstein","Litauen","Luxemburg","Madagaskar","Madeira","Malawi","Malaysia","Malediven","Mali","Malta","Marokko","Marshallinseln","Martinique","Mauretanien","Mauritius","Mexiko","Moldau","Monaco","Mongolei","Montenegro","Mosambik","Myanmar","Namibia","Nauru","Nepal","Neuseeland","Nicaragua","Niederlande","Niederländische Antillen","Niger","Nigeria","Nordkorea","Nordmazedonien","Nordzypern","Norwegen","Oman","Österreich","Osttimor","Pakistan","Palau","Palästina","Panama","Papua-Neuguinea","Paraguay","Peru","Philippinen","Polen","Portugal","Puerto Rico","Réunion","Ruanda","Rumänien","Russland","Saint Kitts und Nevis","Saint Lucia","Saint Pierre und Miquelon","Saint Vincent und die Grenadinen","Salomonen","Sambia","Samoa","San Marino","São Tomé und Príncipe","Saudi-Arabien","Schweden","Schweiz","Senegal","Serbien","Seychellen","Sierra Leone","Singapur","Simbabwe","Slowakei","Slowenien","Somalia","Spanien","Sri Lanka","Südafrika","Sudan","Südkorea","Südsudan","Suriname","Syrien","Tadschikistan","Taiwan","Tansania","Thailand","Togo","Tokelau","Tonga","Trinidad und Tobago","Tschad","Tschechien","Tunesien","Türkei","Turkmenistan","Tuvalu","Uganda","Ukraine","Ungarn","USA","Uruguay","Usbekistan","Vanuatu","Vatikan","Venezuela","Vereinigte Arabische Emirate","Vereinigtes Königreich","Vereinigte Staaten von Amerika","Vietnam","Wallis und Futuna","Westsahara","Zentralafrikanische Republik","Zypern"]
        
                    land = random.choice(länder)

                    flaggenquizcollection.update_one({"_id": message.guild.id}, {"$set": {"land": land}})

                    google_crawler = GoogleImageCrawler(storage={'root_dir': 'Googlebild'})
                    google_crawler.crawl(keyword=f"{land} Flagge", max_num=1)
                    for file in os.listdir('Googlebild'):
                        await message.channel.send(file=discord.File(f"Googlebild/{file}"), content = f"{message.author.mention} hat das letzte Land ({Lösung}) erfolgreich erraten!\nWelches Land ist das?")
                        os.remove(f"Googlebild/{file}")
                else:
                    if not"continue"in message.content.lower():
                        if message.author.bot == False:
                            await message.add_reaction("❌")
                    else:
                        if message.author.guild_permissions.view_audit_log == True:
                            länder = ["Abchasien","Afghanistan","Ägypten","Albanien","Algerien","Andorra","Angola","Anguilla","Antarktis","Antigua und Barbuda","Äquatorialguinea","Argentinien","Armenien","Aruba","Aserbaidschan","Äthiopien","Australien","Azoren","Bahamas","Bahrain","Bangladesch","Barbados","Belarus","Belgien","Belize","Benin","Bhutan","Bolivien","Bosnien und Herzegowina","Botsuana","Brasilien","Brunei","Bulgarien","Burkina Faso","Myanmar","Burundi","Chile","China","Cookinseln","Costa Rica","Dänemark","Kongo","Deutschland, Dominica","Dschibuti","Ecuador","Elfenbeinküste","El Salvador","Eritrea, Estland","Eswatini","Falklandinseln","Fidschi","Finnland","Föderierte Staaten von Mikronesien","Frankreich","Französisch-Polynesien","Französisch-Guayana","Gabun","Gambia","Georgien","Ghana","Grenada","Griechenland","Großbritannien","Grönland","Guadeloupe","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Indien","Indonesien","Irak","Iran","Irland","Island","Israel","Italien","Jamaika","Japan","Jemen","Jordanien","Kambodscha","Kamerun","Kanada","Kap Verde","Kasachstan","Katar","Kenia","Kirgisistan","Kiribati","Kolumbien","Komoren","Kongo","Kroatien","Kuba","Kuwait","Kosovo","Laos","Lesotho","Lettland","Libanon","Liberia","Libyen","Liechtenstein","Litauen","Luxemburg","Madagaskar","Madeira","Malawi","Malaysia","Malediven","Mali","Malta","Marokko","Marshallinseln","Martinique","Mauretanien","Mauritius","Mexiko","Moldau","Monaco","Mongolei","Montenegro","Mosambik","Myanmar","Namibia","Nauru","Nepal","Neuseeland","Nicaragua","Niederlande","Niederländische Antillen","Niger","Nigeria","Nordkorea","Nordmazedonien","Nordzypern","Norwegen","Oman","Österreich","Osttimor","Pakistan","Palau","Palästina","Panama","Papua-Neuguinea","Paraguay","Peru","Philippinen","Polen","Portugal","Puerto Rico","Réunion","Ruanda","Rumänien","Russland","Saint Kitts und Nevis","Saint Lucia","Saint Pierre und Miquelon","Saint Vincent und die Grenadinen","Salomonen","Sambia","Samoa","San Marino","São Tomé und Príncipe","Saudi-Arabien","Schweden","Schweiz","Senegal","Serbien","Seychellen","Sierra Leone","Singapur","Simbabwe","Slowakei","Slowenien","Somalia","Spanien","Sri Lanka","Südafrika","Sudan","Südkorea","Südsudan","Suriname","Syrien","Tadschikistan","Taiwan","Tansania","Thailand","Togo","Tokelau","Tonga","Trinidad und Tobago","Tschad","Tschechien","Tunesien","Türkei","Turkmenistan","Tuvalu","Uganda","Ukraine","Ungarn","USA","Uruguay","Usbekistan","Vanuatu","Vatikan","Venezuela","Vereinigte Arabische Emirate","Vereinigtes Königreich","Vereinigte Staaten von Amerika","Vietnam","Wallis und Futuna","Westsahara","Zentralafrikanische Republik","Zypern"]
        
                            land = random.choice(länder)

                            flaggenquizcollection.update_one({"_id": message.guild.id}, {"$set": {"land": land}})

                            google_crawler = GoogleImageCrawler(storage={'root_dir': 'Googlebild'})
                            google_crawler.crawl(keyword=f"{land} Flagge", max_num=1)
                            for file in os.listdir('Googlebild'):
                                await message.channel.send(file=discord.File(f"Googlebild/{file}"), content = f"{message.author.mention} hat das letzte Land ({Lösung}) übersprungen!\nWelches Land ist das?")
                                os.remove(f"Googlebild/{file}")

        emojiquiz = emojiquizcollecton.find_one({"_id" : message.guild.id})
        if not emojiquiz == None:
            try:
                emojiquizchannelid = emojiquiz["channelid"]
            except:
                emojiquizchannelid = 0
            if message.channel.id == emojiquizchannelid:
                Lösung = emojiquiz["lösung"]
                lösung = emojiquiz["lösung"].lower()
                guess = message.content.lower()
                if lösung in guess and message.author.bot == False:
                    await message.add_reaction("✅")
                    quizzes = emojiquizcollecton.find_one({"_id" : "general"})
        
                    quiz = random.choice(quizzes["quizze"])

                    emojiquizcollecton.update_one({"_id": message.guild.id}, {"$set": {"lösung": quiz["lösung"]}}, upsert=True)

                    await message.channel.send(content = f"Das letzte Quiz ({Lösung}) wurde erfolgreich von {message.author.mention} gelöst!\nFür was stehen diese Emojis?\n\n{quiz['emojis']}")
                else:
                    if not"continue"in message.content.lower():
                        if message.author.bot == False:
                            await message.add_reaction("❌")
                    else:
                        if message.author.guild_permissions.view_audit_log == True:
                            quizzes = emojiquizcollecton.find_one({"_id" : "general"})
        
                            quiz = random.choice(quizzes["quizze"])

                            emojiquizcollecton.update_one({"_id": message.guild.id}, {"$set": {"lösung": quiz["lösung"]}}, upsert=True)

                            await message.channel.send(content = f"Das letzte Quiz ({Lösung}) wurde von {message.author.mention} übersprungen!\nFür was stehen diese Emojis?\n\n{quiz['emojis']}")
        
        oneword = oneWordcollection.find_one({"_id" : message.guild.id})
        if not oneword == None and message.author.bot == False:
            try:
                onewordchannel = oneword["channelid"]
            except:
                onewordchannel = 0
            if message.channel.id == onewordchannel:
                try:
                    lastworder = oneword["lastworder"]
                except:
                    lastworder = 0
                
                if not int(lastworder) == message.author.id:

                    checkerword = message.content
                    checkerword = checkerword.split(" ")
                    if len(checkerword) == 1:

                        word = message.content
                        word.replace(" ", "")
                        sentence = oneword["sentence"]
                        if sentence == "":
                            sentence += f"{word}"
                        else: 
                            if not word == ".":
                                if not word == ",":
                                    sentence += f" {word}"
                                else:
                                    sentence += f"{word}"
                            else:
                                sentence += f"{word}"

                        oneWordcollection.update_one({"_id": message.guild.id}, {"$set": {"sentence" : sentence}}, upsert=True)
                        oneWordcollection.update_one({"_id": message.guild.id}, {"$set": {"lastworder" : message.author.id}}, upsert=True)
                        if message.content == "." or message.content == "?" or message.content == "!":
                            myEmbed = discord.Embed(title = f"Ein toller Satz! <:P_ohaaa:869947368383057990>",description=sentence,color=0xbd24e7)

                            m = await message.channel.send(embed = myEmbed)
                            try:
                                await m.pin()
                                await message.channel.purge(limit = 1)
                                oneWordcollection.update_one({"_id": message.guild.id}, {"$set": {"shouldremember" : True}}, upsert=True)
                            except:
                                try:
                                    shuldremember = oneword["shouldremember"]
                                except:
                                    shuldremember = True
                                if shuldremember == True:
                                    myEmbed = discord.Embed(title = f"<:P_SadRelaxo:885107512423104542>",description="Eigentlich wollte ich den neuen Satz anpinnen aber leider kann ich das nicht mehr. Bitte sortiere ein Paar der angepinnten Nachrichten hier im Channel aus, dass ich wieder Nachrichten anpinnen kann <:P_SadRelaxo:885107512423104542> ||Ich werde dich nicht noch einmal erinnern falls du die Pins nicht aufräumst. Wenn ich jedoch nach den Nächsten Satz wieder eine Nachricht anpinnen darf, werde ich dich wieder erinnern||",color=0xbd24e7)
                                    await message.send(embed = myEmbed)
                                    shuldremember = False
                                oneWordcollection.update_one({"_id": message.guild.id}, {"$set": {"shouldremember" : shuldremember}}, upsert=True)
                            oneWordcollection.update_one({"_id": message.guild.id}, {"$set": {"sentence" : ""}})
                    else:
                        await message.delete()
                else:
                    await message.delete()

        gamequiz = gamecollection.find_one({"_id" : message.guild.id})
        if not gamequiz == None:
            try:
                channelid = gamequiz["channel"]
            except:
                channelid = 0
            if message.channel.id == channelid:
                lösung = gamequiz["awnser"].lower()
                guess = message.content.lower()
                if lösung in guess and message.author.bot == False:
                    await message.add_reaction("✅")
                    gamecollection.update_one({"_id": message.guild.id}, {"$inc": {f"{message.author.id}": 1}}, upsert=True)
                    gamequiz = gamecollection.find_one({"_id" : message.guild.id})
                    x = random.randint(1, 2)
                    if x == 1:
                        quizzes = emojiquizcollecton.find_one({"_id" : "general"})

                        quiz = random.choice(quizzes["quizze"])

                        print(quiz)

                        gamecollection.update_one({"_id": message.guild.id}, {"$set": {"awnser": quiz["lösung"]}}, upsert=True)

                        await message.channel.send(content = f"Das letzte Quiz ({lösung}) wurde erfolgreich von {message.author.mention} gelöst! Damit hat {message.author.mention} jetzt {gamequiz[str(message.author.id)]} Punkte\nFür was stehen diese Emojis?\n\n{quiz['emojis']}")
                    else:

                        länder = ["Abchasien","Afghanistan","Ägypten","Albanien","Algerien","Andorra","Angola","Anguilla","Antarktis","Antigua und Barbuda","Äquatorialguinea","Argentinien","Armenien","Aruba","Aserbaidschan","Äthiopien","Australien","Azoren","Bahamas","Bahrain","Bangladesch","Barbados","Belarus","Belgien","Belize","Benin","Bhutan","Bolivien","Bosnien und Herzegowina","Botsuana","Brasilien","Brunei","Bulgarien","Burkina Faso","Myanmar","Burundi","Chile","China","Cookinseln","Costa Rica","Dänemark","Kongo","Deutschland, Dominica","Dschibuti","Ecuador","Elfenbeinküste","El Salvador","Eritrea, Estland","Eswatini","Falklandinseln","Fidschi","Finnland","Föderierte Staaten von Mikronesien","Frankreich","Französisch-Polynesien","Französisch-Guayana","Gabun","Gambia","Georgien","Ghana","Grenada","Griechenland","Großbritannien","Grönland","Guadeloupe","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Indien","Indonesien","Irak","Iran","Irland","Island","Israel","Italien","Jamaika","Japan","Jemen","Jordanien","Kambodscha","Kamerun","Kanada","Kap Verde","Kasachstan","Katar","Kenia","Kirgisistan","Kiribati","Kolumbien","Komoren","Kongo","Kroatien","Kuba","Kuwait","Kosovo","Laos","Lesotho","Lettland","Libanon","Liberia","Libyen","Liechtenstein","Litauen","Luxemburg","Madagaskar","Madeira","Malawi","Malaysia","Malediven","Mali","Malta","Marokko","Marshallinseln","Martinique","Mauretanien","Mauritius","Mexiko","Moldau","Monaco","Mongolei","Montenegro","Mosambik","Myanmar","Namibia","Nauru","Nepal","Neuseeland","Nicaragua","Niederlande","Niederländische Antillen","Niger","Nigeria","Nordkorea","Nordmazedonien","Nordzypern","Norwegen","Oman","Österreich","Osttimor","Pakistan","Palau","Palästina","Panama","Papua-Neuguinea","Paraguay","Peru","Philippinen","Polen","Portugal","Puerto Rico","Réunion","Ruanda","Rumänien","Russland","Saint Kitts und Nevis","Saint Lucia","Saint Pierre und Miquelon","Saint Vincent und die Grenadinen","Salomonen","Sambia","Samoa","San Marino","São Tomé und Príncipe","Saudi-Arabien","Schweden","Schweiz","Senegal","Serbien","Seychellen","Sierra Leone","Singapur","Simbabwe","Slowakei","Slowenien","Somalia","Spanien","Sri Lanka","Südafrika","Sudan","Südkorea","Südsudan","Suriname","Syrien","Tadschikistan","Taiwan","Tansania","Thailand","Togo","Tokelau","Tonga","Trinidad und Tobago","Tschad","Tschechien","Tunesien","Türkei","Turkmenistan","Tuvalu","Uganda","Ukraine","Ungarn","USA","Uruguay","Usbekistan","Vanuatu","Vatikan","Venezuela","Vereinigte Arabische Emirate","Vereinigtes Königreich","Vereinigte Staaten von Amerika","Vietnam","Wallis und Futuna","Westsahara","Zentralafrikanische Republik","Zypern"]

                        land = random.choice(länder)

                        gamecollection.update_one({"_id": message.guild.id}, {"$set": {"awnser": land}})

                        google_crawler = GoogleImageCrawler(storage={'root_dir': 'Googlebild'})
                        google_crawler.crawl(keyword=f"{land} Flagge", max_num=1)
                        for file in os.listdir('Googlebild'):
                            await message.channel.send(file=discord.File(f"Googlebild/{file}"), content = f"{message.author.mention} hat das letzte Quiz ({lösung}) erfolgreich erraten! Damit hat {message.author.mention} jetzt {gamequiz[str(message.author.id)]} Punkte!\nWelches Land ist das?")
                            os.remove(f"Googlebild/{file}")

                else:
                    if not"continue"in message.content.lower():
                        if message.author.bot == False:
                            await message.add_reaction("❌")
                    else:
                        if message.author.guild_permissions.view_audit_log == True:
                            x = random.randint(1, 2)
                            if x == 1:
                                quizzes = emojiquizcollecton.find_one({"_id" : "general"})

                                quiz = random.choice(quizzes["quizze"])

                                print(quiz)

                                gamecollection.update_one({"_id": message.guild.id}, {"$set": {"awnser": quiz["lösung"]}}, upsert=True)

                                await message.channel.send(content = f"Das letzte Quiz ({lösung}) wurde erfolgreich von {message.author.mention} übersprungen!\nFür was stehen diese Emojis?\n\n{quiz['emojis']}")
                            else:
                            
                                länder = ["Abchasien","Afghanistan","Ägypten","Albanien","Algerien","Andorra","Angola","Anguilla","Antarktis","Antigua und Barbuda","Äquatorialguinea","Argentinien","Armenien","Aruba","Aserbaidschan","Äthiopien","Australien","Azoren","Bahamas","Bahrain","Bangladesch","Barbados","Belarus","Belgien","Belize","Benin","Bhutan","Bolivien","Bosnien und Herzegowina","Botsuana","Brasilien","Brunei","Bulgarien","Burkina Faso","Myanmar","Burundi","Chile","China","Cookinseln","Costa Rica","Dänemark","Kongo","Deutschland, Dominica","Dschibuti","Ecuador","Elfenbeinküste","El Salvador","Eritrea, Estland","Eswatini","Falklandinseln","Fidschi","Finnland","Föderierte Staaten von Mikronesien","Frankreich","Französisch-Polynesien","Französisch-Guayana","Gabun","Gambia","Georgien","Ghana","Grenada","Griechenland","Großbritannien","Grönland","Guadeloupe","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Indien","Indonesien","Irak","Iran","Irland","Island","Israel","Italien","Jamaika","Japan","Jemen","Jordanien","Kambodscha","Kamerun","Kanada","Kap Verde","Kasachstan","Katar","Kenia","Kirgisistan","Kiribati","Kolumbien","Komoren","Kongo","Kroatien","Kuba","Kuwait","Kosovo","Laos","Lesotho","Lettland","Libanon","Liberia","Libyen","Liechtenstein","Litauen","Luxemburg","Madagaskar","Madeira","Malawi","Malaysia","Malediven","Mali","Malta","Marokko","Marshallinseln","Martinique","Mauretanien","Mauritius","Mexiko","Moldau","Monaco","Mongolei","Montenegro","Mosambik","Myanmar","Namibia","Nauru","Nepal","Neuseeland","Nicaragua","Niederlande","Niederländische Antillen","Niger","Nigeria","Nordkorea","Nordmazedonien","Nordzypern","Norwegen","Oman","Österreich","Osttimor","Pakistan","Palau","Palästina","Panama","Papua-Neuguinea","Paraguay","Peru","Philippinen","Polen","Portugal","Puerto Rico","Réunion","Ruanda","Rumänien","Russland","Saint Kitts und Nevis","Saint Lucia","Saint Pierre und Miquelon","Saint Vincent und die Grenadinen","Salomonen","Sambia","Samoa","San Marino","São Tomé und Príncipe","Saudi-Arabien","Schweden","Schweiz","Senegal","Serbien","Seychellen","Sierra Leone","Singapur","Simbabwe","Slowakei","Slowenien","Somalia","Spanien","Sri Lanka","Südafrika","Sudan","Südkorea","Südsudan","Suriname","Syrien","Tadschikistan","Taiwan","Tansania","Thailand","Togo","Tokelau","Tonga","Trinidad und Tobago","Tschad","Tschechien","Tunesien","Türkei","Turkmenistan","Tuvalu","Uganda","Ukraine","Ungarn","USA","Uruguay","Usbekistan","Vanuatu","Vatikan","Venezuela","Vereinigte Arabische Emirate","Vereinigtes Königreich","Vereinigte Staaten von Amerika","Vietnam","Wallis und Futuna","Westsahara","Zentralafrikanische Republik","Zypern"]

                                land = random.choice(länder)

                                gamecollection.update_one({"_id": message.guild.id}, {"$set": {"awnser": land}})

                                google_crawler = GoogleImageCrawler(storage={'root_dir': 'Googlebild'})
                                google_crawler.crawl(keyword=f"{land} Flagge", max_num=1)
                                for file in os.listdir('Googlebild'):
                                    await message.channel.send(file=discord.File(f"Googlebild/{file}"), content = f"{message.author.mention} hat das letzte Quiz ({lösung}) übersprungen!\nWelches Land ist das?")
                                    os.remove(f"Googlebild/{file}")

        authorid = message.author.id
        channelid = message.channel.id
        channelmentions = message.channel_mentions
        content = message.content.lower()
        membermentions = message.mentions
        rolementions = message.role_mentions
        istts = message.tts
        words = content.split(" ")
        xwords = list(words)
        words = []
        for word in xwords:
            word.replace(" ", "")
            word.replace(".", "")
            words.append(word)
        wörter = []
        emojis = []
        for word in words:
            if any(str(emoji) in word for emoji in message.guild.emojis):
                if word != "":
                    emojis.append(word)
            else:
                if word != "":
                    wörter.append(word)

        now = datetime.now() 
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")

        statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.messageamount" : 1}}, upsert=True)
        statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.messagesfrom.{authorid}" : 1}}, upsert=True)
        statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.messagesin.{channelid}" : 1}}, upsert=True)
        for channel in channelmentions:
            statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.mentionedchannel.{channel.id}" : 1}}, upsert=True)
        for word in wörter:
            try:
                if isinstance(word, str):
                    statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.usedwords.{word}" : 1}}, upsert=True)
            except:
                pass
        for emoji in emojis:
            statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.usedemojis.{emoji}" : 1}}, upsert=True)
        for member in membermentions:
            statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.mentionedmember.{member.id}" : 1}}, upsert=True)
        for role in rolementions:
            statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.mentionedroles.{role.id}" : 1}}, upsert=True)
        if istts == True:
            statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.ttsmessages" : 1}}, upsert=True)
        else:
            statscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"{year}.{month}.{day}.nonttsmessages" : 1}}, upsert=True)



    @slash_command(name='insertemojiquiz', description='Füge eine Möglichkeit für ein Emojiquiz hinzu!')
    async def insertemojiquiz(self, ctx, emojis : Option(str,"Welche Emojis?", required = True), lösung : Option(str,"wofür stehen die Emojis??", required = True)):
        await ctx.defer()
        whitelisted = [766350321638309958, 471036610561966111, 760155365710102549, 810484550727761940]
        if ctx.author.id in whitelisted:
            emojiquizcollecton.update_one({"_id" : "general"}, {"$addToSet" : {"quizze" : {"emojis" : emojis, "lösung" : lösung}}}, upsert=True)
            await ctx.respond("✅")
        else:
            await ctx.respond("Du darfst diesen Befehl nicht ausführen.")


    
        
    @slash_command(name='zahlinwort', description='Gebe mir eine Zahl und ich sage dir, wie die Zahl ausgeschrieben heißt!')
    async def zahlinwort(self, ctx, zahl : Option(str,"Welche Zahl?", required = True)):
        await ctx.defer()
        wort = num2words(zahl, lang='de')
        myEmbed = discord.Embed(title ="Deine Zahl", description=f"Die Zahl `{zahl}` ist `{wort}` ausgeschrieben!", color = 0xbd24e7)
        await ctx.respond(embed = myEmbed)

    @has_permissions(view_audit_log=True)
    @slash_command(name='emojipicker', description='Füge ein Emoji aus dem Picker zum Server hinzu')
    async def emojipicker(self, ctx):
        await ctx.defer()         
        if ctx.channel.nsfw == True:
            global allemojis
            
            ctx.respond("Emojipicker gestartet!", ephemeral=True)
            
            now = random.choice(allemojis)
            print(now)
            myEmbed = discord.Embed(title = "Emojipicker", description=now["title"], color = 0xbd24e7)
            myEmbed.set_image(url = now["image"])
            last = None

            
            next = random.choice(allemojis)

            async def last_callback(interaction):
                nonlocal now
                nonlocal last
                nonlocal next
                next = now
                now = last
                last = None
                myEmbed = discord.Embed(title = "Emojipicker", description=now["title"], color = 0xbd24e7)
                myEmbed.set_image(url = now["image"])

                view = discord.ui.View()


                button_last = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=last != None, row = 1, custom_id="Last")
                button_last.callback = last_callback

                button_hinzufuegen = discord.ui.Button(label = "als Emoji Hinzufügen", style = discord.ButtonStyle.blurple, disabled=len(ctx.guild.emojis) >= ctx.guild.emoji_limit, row = 1, custom_id="Emoji")
                button_hinzufuegen.callback = add_callback

                button_sticker_hinzufuegen = discord.ui.Button(label = "als Sticker Hinzufügen", style = discord.ButtonStyle.blurple, disabled=len(ctx.guild.stickers) >= ctx.guild.sticker_limit, row = 1, custom_id="Sticker")
                button_sticker_hinzufuegen.callback = add_sticker

                button_next = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1, custom_id="Next")
                button_next.callback = next_callback

                view.add_item(button_last)
                view.add_item(button_hinzufuegen)
                view.add_item(button_sticker_hinzufuegen)
                view.add_item(button_next)



                await message.edit(embed = myEmbed, view = view)

            async def add_callback(interaction):
                nonlocal now
                nonlocal last
                nonlocal next

                url = now["image"]
                r = requests.get(url)
                img = Image.open(BytesIO(r.content), mode = "r")
                try:
                    img.seek(1)
                
                except EOFError:
                    is_animated = False

                else:
                    is_animated = True
                
                if is_animated == True:
                    b = BytesIO()
                    img.save(b, format = "GIF")
                    b_value = b.getvalue()
                    emoji = await ctx.guild.create_custom_emoji(image=b_value, name = now["title"])
                    await ctx.channel.send(f"{emoji}")
                
                elif is_animated == False:
                    b = BytesIO()
                    img.save(b, format = "PNG")
                    b_value = b.getvalue()
                    emoji = await ctx.guild.create_custom_emoji(image=b_value, name = now["title"])
                    await ctx.channel.send(f"{emoji}")
                

            async def add_sticker(interaction):
                nonlocal now
                nonlocal last
                nonlocal next

                url = now["image"]
                r = requests.get(url)
                img = Image.open(BytesIO(r.content), mode = "r")
                try:
                    img.seek(1)
                
                except EOFError:
                    is_animated = False

                else:
                    is_animated = True
                
                if is_animated == True:
                    await ctx.channel.send("We do not support animated emojis")
                
                elif is_animated == False:
                    b = BytesIO()
                    img.save(b, format = "PNG")
                    b_value = b.getvalue()
                    did_it = False
                    c = 0
                    emojis = ["👀" ,"👍","👎","✔️","➡️","❌","💕","🙌","💖","😔","‼️","✅","🤡","😿","😠","🚮","💥","😊","😂","😆","😭","🤣","❤️","🚗","😶‍🌫️","😶","😑","😐","🤨","😏","😣","😮","🤐","😯","🥲","😘","😍","😞","😢","😭","🙁","☹️","😲","🤑","🙃","😕","😮‍💨","😰","😱","🥵","🥶","😳","😡","😠","🥴","😵‍💫","😵‍💫","😵","🤪","🤬","😷","🤒","🤕","🤢","🤮","🤠","🥺","🥸","🥳","😇","🤧","🤡","🤥","🤫","🤭","🧐","🤓","☠️","💀","💀","👺","👹","👿","😈","👻","👽","👾","🤖","💩","😺"]
                    while did_it != True:
                        emoji = await ctx.guild.create_sticker(file=b_value, name = now["title"], emoji = emojis[c])
                        c += 1
                    await ctx.channel.send(f"{emoji}")

            async def next_callback(interaction):
                nonlocal now
                nonlocal last
                nonlocal next
                nonlocal message
                last = now
                now = next
                next = random.choice(allemojis)
                myEmbed = discord.Embed(title = "Emojipicker", description=now["title"], color = 0xbd24e7)
                myEmbed.set_image(url = now["image"])

                view = discord.ui.View()


                button_last = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=last != None, row = 1, custom_id="Last")
                button_last.callback = last_callback

                button_hinzufuegen = discord.ui.Button(label = "als Emoji Hinzufügen", style = discord.ButtonStyle.blurple, disabled=len(ctx.guild.emojis) >= ctx.guild.emoji_limit, row = 1, custom_id="Emoji")
                button_hinzufuegen.callback = add_callback

                button_sticker_hinzufuegen = discord.ui.Button(label = "als Sticker Hinzufügen", style = discord.ButtonStyle.blurple, disabled=len(ctx.guild.stickers) >= ctx.guild.sticker_limit, row = 1, custom_id="Sticker")
                button_sticker_hinzufuegen.callback = add_sticker

                button_next = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1, custom_id="Next")
                button_next.callback = next_callback

                view.add_item(button_last)
                view.add_item(button_hinzufuegen)
                view.add_item(button_sticker_hinzufuegen)
                view.add_item(button_next)




                await message.edit(embed = myEmbed, view = view)




            view = discord.ui.View()

            button_last = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=last != None, row = 1, custom_id="Last")
            button_last.callback = last_callback

            button_hinzufuegen = discord.ui.Button(label = "als Emoji Hinzufügen", style = discord.ButtonStyle.blurple, disabled=len(ctx.guild.emojis) >= ctx.guild.emoji_limit, row = 1, custom_id="Emoji")
            button_hinzufuegen.callback = add_callback

            button_sticker_hinzufuegen = discord.ui.Button(label = "als Sticker Hinzufügen", style = discord.ButtonStyle.blurple, disabled=len(ctx.guild.stickers) >= ctx.guild.sticker_limit, row = 1, custom_id="Sticker")
            button_sticker_hinzufuegen.callback = add_sticker

            button_next = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1, custom_id="Next")
            button_next.callback = next_callback

            view.add_item(button_last)
            view.add_item(button_hinzufuegen)
            view.add_item(button_sticker_hinzufuegen)
            view.add_item(button_next)

            message = await ctx.channel.send(embed = myEmbed, view = view)

        else:
            await ctx.respond("Du darfst den Emojipicker nur in NSFW Kanälen benutzen.", ephemeral=True)

    @has_permissions(view_audit_log=True)
    @slash_command(name='embed', description='Sende ein Embed', guild_ids = [907216584341348373])
    async def embed(self, ctx, channel : Option(discord.TextChannel,"In welchen Channel soll das Embed stehen?", required = True)):
        await ctx.defer()

        
        message = await ctx.respond("Was soll der Titel deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.")
        
        async def gettitle(Error = False):
            nonlocal message
            if Error == False:
                if message.content != "Was soll der Titel deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.":
                    message = await message.edit("Was soll der Titel deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.")
            else:
                if message.content != "Was soll der Titel deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.\nDer Titel darf Maximal 256 Zeichen lang sein.":
                    message = await message.edit("Was soll der Titel deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.\nDer Titel darf Maximal 256 Zeichen lang sein.")
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel
    
            msg = await self.client.wait_for('message', check=check)
    
            await msg.delete()
    
            title = msg.content

            if title == "continue":
                return discord.Embed.Empty
    
            if not len(title) < 256:
                title = await gettitle(True)
            return title
        
        title = await gettitle()

        async def getdescription(Error = False):
            nonlocal message
            if Error == False:
                if message.content != "Was soll die Beschreibung deines Embeds sein?":
                    message = await message.edit("Was soll die Beschreibung deines Embeds sein?")
            else:
                if message.content != "Was soll die Beschreibung deines Embeds sein?\nDie Beschreibung darf Maximal 4096  Zeichen lang sein.":
                    message = await message.edit("Was soll die Beschreibung deines Embeds sein?\nDie Beschreibung darf Maximal 4096  Zeichen lang sein.")
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel
    
            msg = await self.client.wait_for('message', check=check)
    
            await msg.delete()
    
            title = msg.content

    
            if not len(title) < 4096:
                title = await getdescription(True)
            return title
        
        description = await getdescription()

        myEmbed = None

        async def getcolor(Error = False):
            nonlocal message
            if Error == False:
                if message.content != f"Bitte gebe den RBG Code ein!\nDen RGB Code kannst du dir z.B. hier: https://www.rapidtables.com/web/color/RGB_Color.html Generieren.\nGebe den Code wie folgr an:\n`(R, G, B)`\n**Bitte gebe auch die Klammern an!**\nR = Rot, G = Grün, B = Blau\nWenn du keine haben willst, schreibe bitte `continue`":
                    message = await message.edit(f"Bitte gebe den RBG Code ein!\nDen RGB Code kannst du dir z.B. hier: https://www.rapidtables.com/web/color/RGB_Color.html Generieren.\nGebe den Code wie folgr an:\n`(R, G, B)`\n**Bitte gebe auch die Klammern an!**\nR = Rot, G = Grün, B = Blau\nWenn du keine haben willst, schreibe bitte `continue`")
            if Error == True:
                if message.content != f"Bitte gebe den RBG Code ein!\nDen RGB Code kannst du dir z.B. hier: https://www.rapidtables.com/web/color/RGB_Color.html Generieren.\nGebe den Code wie folgr an:\n`(R, G, B)`\n**Bitte gebe auch die Klammern an!**\nR = Rot, G = Grün, B = Blau\nWenn du keine haben willst, schreibe bitte `continue`\nBitte stelle sicher, dass du alles richtig eingibst!":
                    message = await message.edit(f"Bitte gebe den RBG Code ein!\nDen RGB Code kannst du dir z.B. hier: https://www.rapidtables.com/web/color/RGB_Color.html Generieren.\nGebe den Code wie folgr an:\n`(R, G, B)`\n**Bitte gebe auch die Klammern an!**\nR = Rot, G = Grün, B = Blau\nWenn du keine haben willst, schreibe bitte `continue`\nBitte stelle sicher, dass du alles richtig eingibst!")
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel
    
            msg = await self.client.wait_for('message', check=check)
            await msg.delete()

            if msg.content == "continue":
                return 0xbd24e7

            try:
            
                if not msg.content[0] == "(":
                    msg = await getcolor(Error = True)
                if not msg.content[-1] == ")":
                    msg = await getcolor(Error = True)
                x = msg.content.replace("(", "")
                x = x.replace(")", "")
                x = x.split(",")
                color  = discord.Color.from_rgb(int(x[0]), int(x[1]), int(x[2]))
                print(color)
                return color

            except:
                await getcolor(Error = True)
        color = await getcolor(Error = False)

        myEmbed = discord.Embed(title = title, description= description, color = color)

        async def getfooter(Error = False):
            nonlocal message
            maxlen = 0
            if 6000 - len(myEmbed) > 2048:
                maxlen = 2048
            else:
                maxlen = 6000 - len(myEmbed)
            if Error == False:
                if message.content != "Was soll der footer deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.":
                    message = await message.edit("Was soll der footer deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.")
            else:
                if message.content != f"Was soll der footer deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.\nDer Footer darf Maximal {maxlen}  Zeichen lang sein.":
                    message = await message.edit(f"Was soll der footer deines Embeds sein? Wenn du keinen möchtest, kannst du einfach `continue` Schreiben.\nDie Beschreibung darf Maximal {maxlen}  Zeichen lang sein.")
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel
    
            msg = await self.client.wait_for('message', check=check)
    
            await msg.delete()
    
            footer = msg.content

            if footer == "continue":
                return "465465465489478946513546894894869416848464868448646456156213211355644568778987946513246898948695165156418794"
    
            if not len(footer) < maxlen:
                footer = await getfooter(True)
            return footer
        
        footer = await getfooter()
        if footer != "465465465489478946513546894894869416848464868448646456156213211355644568778987946513246898948695165156418794":
            myEmbed.set_footer(text = footer)

        async def getfields(Error = False):
            nonlocal message
            if Error == False:
                if message.content != "Wie viele Felder soll dein Embed haben? Wenn du keine Möchtest dann gebe einfach 0 ein.":
                    message = await message.edit("Wie viele Felder soll dein Embed haben? Wenn du keine Möchtest dann gebe einfach 0 ein.")
            else:
                if message.content != "Wie viele Felder soll dein Embed haben? Wenn du keine Möchtest dann gebe einfach 0 ein.\nBitte gebe eine ganze Zahl zwischen 0 und 50 ein.":
                    message = await message.edit("Wie viele Felder soll dein Embed haben? Wenn du keine Möchtest dann gebe einfach 0 ein.\nBitte gebe eine ganze Zahl zwischen 0 und 50 ein.")
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel
    
            msg = await self.client.wait_for('message', check=check)
    
            await msg.delete()
    
            fields = msg.content
            try:
                fields = int(fields)
            except:
                await getfields(True)

            if fields > 50:
                await getfields(True)
            
            if fields < 0:
                await getfields(True)

            return fields
        
        fields = await getfields()

        toolong = False

        for fieldnumber in range(fields):
            async def getname(Error = False):
                nonlocal message
                if Error == False:
                    if message.content != f"Was soll die überschrift des {fieldnumber + 1}. Feldes sein?":
                        message = await message.edit(f"Was soll die überschrift des {fieldnumber + 1}. Feldes sein?")
                else:
                    if message.content != f"Was soll die überschrift des {fieldnumber + 1}. Feldes sein?\nBitte gebe maximal 256 Zeichen an.":
                        message = await message.edit(f"Was soll die überschrift des {fieldnumber + 1}. Feldes sein?\nBitte gebe maximal 256 Zeichen an.")
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel

                msg = await self.client.wait_for('message', check=check)

                await msg.delete()

                name = msg.content

                if not len(name) < 256:
                    name = await getname(True)
                return name
        
            name = await getname()

            async def getvalue(Error = False):
                nonlocal message
                if Error == False:
                    if message.content != f"Was soll der Inhalt des {fieldnumber + 1}. Feldes sein?":
                        message = await message.edit(f"Was soll der Inhalt des {fieldnumber + 1}. Feldes sein?")
                else:
                    if message.content != f"Was soll der Inhalt des {fieldnumber + 1}. Feldes sein?\nbitte gebe maximal 1024 Zeichen an.":
                        message = await message.edit(f"Was soll der Inhalt des {fieldnumber + 1}. Feldes sein?\nbitte gebe maximal 1024 Zeichen an.")
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel

                msg = await self.client.wait_for('message', check=check)

                await msg.delete()

                value = msg.content

                if not len(value) < 1024:
                    value = await getvalue(True)
                return value
        
            value = await getvalue()

            tempembed = myEmbed
            tempembed.add_field(name = name, value = value, inline = False)
            if len(tempembed) >= 6000:
                myEmbed.add_field(name = name, value = value, inline = False)
            else:
                toolong = True
                await message.edit(f"Dein Embed ist zu lang. Wegen Discord darf ein Embed leider nur maximal 6000 Zeichen lang sein. Deshalb wurde dein Embed jetzt schon gesendet. Wenn du noch Informationen schreiben willst, erstelle bitte ein 2. Embed.")
                await channel.send(embed = myEmbed)
                break
        if toolong == False:
            await channel.send(embed = myEmbed)
            await message.edit(f"Dein Embed wurde erfolgreich gesendet.")


    @slash_command(name='avatar', description='Sehe den Avatar von jemandem.')
    async def avatar(self, ctx, member : Option(discord.Member,"Von wem möchtest du den Avatar sehen?", required = True)):
        await ctx.defer()
        embed = discord.Embed(title=f"Avatar von {member.name}", color=0xbd24e7)
        try:
            embed.set_image(url = member.avatar.url)
            embed.set_footer(text=f"Tanjun Utility Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)
        except:
            await ctx.respond("Wie es scheint hat diese Person kein profilbild <:P_sad_kuromi:892125483553136661>")

    @slash_command(name='banner', description='Sehe den Banner von jemanden.')
    async def banner(self, ctx, member : Option(discord.Member,"Von wem möchtest du den Banner sehen?", required = True)):
        await ctx.defer()
        embed = discord.Embed(title=f"Banner von {member.name}", color=0xbd24e7)
        member = await self.client.fetch_user(member.id)
        try:
            embed.set_image(url = member.banner.url)
            embed.set_footer(text=f"Tanjun Utility Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)
        except:
            await ctx.respond("Wie es scheint hat diese Person kein Banner <:P_Picapepe:954792709644775435>")

    
    @slash_command(name='mball', description='Stell mir eine Frage!')
    async def mball(self, ctx, message : Option(str,"Was möchtest du fragen?", required = True)):
        await ctx.defer()
        magicball = [
 "Ja","Nein","Vielleicht","Manchmal","Eventuell","Morgen vielleicht",
 "Irgendwann mal","Vergiss es","Eines Tages Vielleicht",
 "Frag doch einfach nochmal","Nö","Nein. Das ist nicht in Ordnung."
 "Woher soll ich das wissen?","Weiß ich doch nicht",
 "Bekomme ich dann Chips?",
 "Klar","Geh lieber in den Chat und sei dort aktiv!",
 "Herzlichen Glückwunsch, du schuldest dem ganzem Server jetzt eine Tüte Chips!",
 "Bin heute gut drauf, also ja",'Frage mich später nochmal',
        'Bist du dir da wirklich sicher?', 'Das glaube ich nicht',
        'Ich möchte darauf nicht antworten',
        'Definitiv nicht du...', 'Stör mich nicht, ich esse Chips.',
        'Ich bin beschäftigt, geh <@760155365710102549> fragen. (Ne mach das nicht, sonst gibts nen Timeout <:lul:924395409974128720>)',
        'Was fragst du mich, bin ich Google?',
 "Ja, aber es ist okay, dass es so ist.",
 "Er ist so schlimm, da ist es zu riskant hier zu sein",
 "Alright, da stimme ich dir zu",
 "Ich entschuldige mich, aber das ist zu viel für mich.",
  "Das ist keine Frage lul","Lass uns diese Konversation in nen Funcommands Channel verschieben.",
  "ERROR 404",
  "Wie gehts dir?","Gute Frage, allerdings hab ich keine Ahnung also die nächste bitte..",
  "Cool, aber warum?","Alles klar du Oberzicke","Da stimm ich dir 100% zu!","Da könnt ich dir 100% zustimmen. ||Tuh ich aber nicht <:lul:924395409974128720>||"
  "Meine Ordnung durcheinander bringen, ja das kannst du gut... Stehe ich überhaupt nicht drauf.","Das ist echt perfekt. Aber auch maximal dumm! <:P_SUPERFUNNYBREAD:867370461931372544>",
  "hmmm... Ich bin mir unsicher. EXTREM unsicher ||ob diese Frage ernst gemeint ist...||",
  "Du kriegst eine Antwort die dich glücklich macht und ich bekomme 200€ von dir, Deal?"
    ]
        embed = discord.Embed(description=f"🎱Magic Ball🎱", color=0xbd24e7)
        genommener_spruch = random.choice(magicball)
        embed.add_field(name=f"Frage: {message}",
                        value=str(genommener_spruch),
                        inline=False)
        embed.set_footer(text=f"Tanjun Utility Cmds ⬝ {ctx.author}")
        await ctx.send(embed=embed)
        

    @slash_command(name='benchmark', description='Teste die Leistung des Bots')
    async def benchmark(self, ctx):
            await ctx.defer()
            tic = time.perf_counter()
            newmsg = await ctx.send("[]", delete_after = 0.01)
            toc = time.perf_counter()
            pingtillmessagesend =  toc - tic
            tic = time.perf_counter()
            levelsyscollection.find_one({"_id": ctx.guild.id}, {"multi": True})
            toc = time.perf_counter()
            timetilldatabase = toc - tic
            user = self.client.get_user(471036610561966111)
            guild = self.client.get_guild(933307298011562006)
            dclatenz = self.client.latency
            embed = discord.Embed(title=f"Benchmark Ergebnisse!", description = f"Um Nachrichten zu senden benötige ich {round(pingtillmessagesend * 1000, 3)}ms.\n\nUm die Datenbank aufzurufen, benötige ich {round(timetilldatabase * 1000, 3)}ms pro Aufruf.\n\nDie Latenz zu den Discord Servern beträgt aktuell {round(dclatenz * 1000, 3)}ms.", color=0x598ee7)
            await ctx.respond(embed = embed)
        
    @slash_command(name='google', description='Google etwas')
    async def google(self, ctx, message : Option(str,"Was möchtest du googlen?", required = True)):
        await ctx.defer()
        if ctx.channel.is_nsfw() == False:
            embed = discord.Embed(description=f'Leider musste ich feststellen, dass es möglich ist, mit den google command nsfw inhalte zu googeln. Deshalb ist dieser Command nur noch in NSFW Channel verfügbar :c', color=0xbd24e7)
            embed.set_footer(text=f"Tanjun Utility Cmds ⬝ {ctx.author}")
            await ctx.send(embed = embed)
            return
        google_crawler = GoogleImageCrawler(storage={'root_dir': 'Googlebild'})
        google_crawler.crawl(keyword=message, max_num=1)
        for file in os.listdir('Googlebild'):
            msg2 = await ctx.send(file=discord.File(f"Googlebild/{file}"))
            Attratchment = msg2.attachments
            await msg2.delete()
            link = Attratchment[0]
            embed = discord.Embed(title='Dein Suchergebnis!', description=f'{ctx.author.mention}, Hier ist ein Bild der suche **{message}**.', color=0xbd24e7)
            embed.set_image(url = link)
            embed.set_footer(text=f"Tanjun Utility Cmds ⬝ {ctx.author}")
            await ctx.send(embed=embed)
            os.remove(f"Googlebild/{file}")
        
    @has_permissions(manage_channels=True)
    @slash_command(name='setslowmode', description='Lege den Slowmode für einen Kanal fest.')
    async def setcooldown(self, ctx, cooldown : Option(int,"Auf wie viele Sekunden möchtest du den Slowmode setzen?", required = True), channel : Option(discord.TextChannel,"In welchem Channel möchtest du den Slowmode ändern?", required = False, default = None)):
        await ctx.defer()
        if channel == None:
            channel = ctx.channel
        await channel.edit(slowmode_delay = cooldown)
        await ctx.respond(f"Der Slowmode von {channel.mention} wurde erfolgreich auf {cooldown} gesetzt.")        

    @slash_command(name='sm', description='DEV-ONLY')
    async def sm(self, ctx, msg : Option(str,"Deine Nachricht", required = True), channel : Option(discord.TextChannel,"", required = False, default = None)):
        await ctx.defer()
        if channel == None:
            channel = ctx.channel
        cd = self.client.get_channel(959513664589791293)
        if ctx.author.id in dev_list:
            await ctx.respond(f"Ich habe die folgende Nachricht erfolgreich gesendet:\n`{msg}` ➡️ in: {channel.mention}", ephemeral=True)
            await channel.send(msg)
            try:
                await cd.send(f'**Jemand hat versucht, eine Nachricht per `/sm` zu senden!**\n\n*Gesendete Nachricht:*\n"{msg}"\n\nKanal: {channel.mention}\n\n> User: <@{ctx.author.id}> (`{ctx.author.id}`)\n\n__Senden der Nachricht war erfolgreich?__ | ✅', delete_after=500)
            except:
                await ctx.respond(f"**ERROR:** Ich konnte keinen Bericht in <#{cd}> senden.\nDies liegt wahrscheinlich daran, dass sich der Kanal nicht auf diesem Server befindet...", ephemeral=True)
        else:
            await ctx.respond("❌ | Du hast nicht genug Rechte, um diesen Command auszuführen!", ephemeral=True)
            try:
                await cd.send(f'**Jemand hat versucht, eine Nachricht per `/sm` zu senden!**\n\n*Gesendete Nachricht:*\n"{msg}"\n\nKanal: {channel.mention}/<#{ctx.channel.id}>\n\n> User: <@{ctx.author.id}> (`{ctx.author.id}`)\n\n__Senden der Nachricht war erfolgreich?__ | ❌', delete_after=500)
            except:
                await ctx.respond(f"**ERROR:** Ich konnte keinen Bericht in <#{cd}> senden.\nDies liegt wahrscheinlich daran, dass sich der Kanal nicht auf diesem Server befindet...", ephemeral=True)
            
    
    @slash_command(name='change', description='DEV-ONLY')
    async def change(self, ctx, aenderung : Option(str,"Was hast du geändert?", required = True)):
        await ctx.defer()
        if ctx.author.id in dev_list:
            timenow = int(time.time())
            changelogcollection.update_one({"_id" : "changelog"}, {"$addToSet" : {"change" : {"timestamp" : timenow, "adder" : ctx.author.id, "change" : aenderung}}}, upsert=True)
            await ctx.respond("Änderung erfolgreich zum Changelog hinzugefügt!")
        else:
            await ctx.respond("❌ | Du hast nicht genug Rechte, um diesen Command auszuführen!", ephemeral=True)

    @slash_command(name='serveridee', description='Schlage etwas für den Server vor')
    async def serveridee(self, ctx, idea: Option(str, "Wie lautet deine Idee?", required=True)):
        await ctx.defer()
        serverideen = serverideecollection.find_one({"_id": ctx.guild.id})
        try:
            channelid = serverideen["channelid"]
            channel = self.client.get_channel(channelid)
            emojis_mit_leerzeichen_getrennt = "✅ ❌"
            titel_der_umfrage = "Eine neue IDEE! <:P_ohaaa:869947368383057990>"
            umfrage = f"> {idea} \n\n**Idee eingereicht von: {ctx.author}**\n\n**Community Umfrage:\n**Wie findet ihr diese Idee? :)"
            dauer_der_umfrage = "7d"

            try:
                umfragen = umfragecollection.find_one({"_id" : ctx.guild.id})
                if umfragen == None:
                    umfragen = {}
            except:
                umfragen = {}
            curr_dt = datetime.now(tz=pytz.timezone("Europe/Berlin"))
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
                await msg.add_reaction(em)
    
            try:
                umfragecollection.update_one({"_id" : ctx.guild.id}, {"$set" : umfragen[str(ctx.guild.id)]}, upsert = True)
            except:
                raise
            await ctx.respond("Deine Idee wurde gesendet", ephemeral=True)
        except:
            await ctx.respond("Es wurde kein Channel fürs Server Ideen senden festgelegt.", ephemeral=True)

    @slash_command(name='tanjunidee', description='Schlage etwas für den Bot Tanjun vor')
    async def tanjunidee(self, ctx, idea: Option(str, "Wie lautet deine Idee?", required=True)):
        await ctx.defer()
        print("Eine neue Idee :o")
        channel = self.client.get_channel(959514276983345152)   
        emojis_mit_leerzeichen_getrennt = "✅ ❌"
        titel_der_umfrage = "Eine neue IDEE! <:P_ohaaa:869947368383057990>"
        umfrage = f"> {idea} \n\n**Idee eingereicht von: {ctx.author}**\n\n**Community Umfrage:\n**Wie findet ihr diese Idee? :)"
        dauer_der_umfrage = "7d"
    

        try:
            umfragen = umfragecollection.find_one({"_id" : ctx.guild.id})
            if umfragen == None:
                umfragen = {}
        except:
            umfragen = {}
        curr_dt = datetime.now(tz=pytz.timezone("Europe/Berlin"))
        timestamp = int(round(curr_dt.timestamp()))
        dauer_der_umfrage = timestamp + int(convert(dauer_der_umfrage))

        umfragen[str(ctx.guild.id)] = dict(umfragen)


        myEmbed = discord.Embed(title=titel_der_umfrage, description=f"{umfrage} \nUmfragenende: <t:{dauer_der_umfrage}:R>",color=0xbd24e7)

        guild = self.client.get_guild(831161440705839124)
        role = guild.get_role(955129741504040972)

        msg = await channel.send(content = role.mention, embed = myEmbed)
        try:
            umfragen[str(ctx.guild.id)]
        except:
            umfragen[str(ctx.guild.id)] = {}

        umfragen[str(ctx.guild.id)][str(msg.id)] = {"endet" : False, "time" : dauer_der_umfrage, "titel" : titel_der_umfrage, "umfrage" : umfrage, "channel" : channel.id}
        for em in emojis_mit_leerzeichen_getrennt.split(" "):
            await msg.add_reaction(em)

        try:
            umfragecollection.update_one({"_id" : ctx.guild.id}, {"$set" : umfragen[str(ctx.guild.id)]}, upsert = True)
        except:
            raise
        await ctx.respond("Deine Idee wurde gesendet", ephemeral=True)


    möglichkeitenKey = [
        discord.OptionChoice(name = "0", value = "0"),
        discord.OptionChoice(name = "1", value = "1"),
        discord.OptionChoice(name = "2", value = "2"),
        discord.OptionChoice(name = "3", value = "3"),
        discord.OptionChoice(name = "4", value = "4"),
        discord.OptionChoice(name = "5", value = "5"),
        discord.OptionChoice(name = "6", value = "6"),
        discord.OptionChoice(name = "7", value = "7"),
        discord.OptionChoice(name = "8", value = "8"),
        discord.OptionChoice(name = "9", value = "9"),
        discord.OptionChoice(name = "10", value = "10"),
        discord.OptionChoice(name = "11", value = "11"),
        discord.OptionChoice(name = "12", value = "12"),
        discord.OptionChoice(name = "13", value = "13"),
        discord.OptionChoice(name = "14", value = "14"),
        discord.OptionChoice(name = "15", value = "15"),
        discord.OptionChoice(name = "16", value = "16"),
        discord.OptionChoice(name = "17", value = "17"),
        discord.OptionChoice(name = "18", value = "18"),
        discord.OptionChoice(name = "19", value = "19"),
        discord.OptionChoice(name = "20", value = "20"),
    ]

    @slash_command(name = 'sendencodetext', description='Sende einen verschlüsselten Text')
    async def sendencodetext(self, ctx, member : discord.Member, nachricht: Option(str, "Wie lautet deine Nachricht", required=True), key: Option(int, "Wie lautet der Verschlüsselungskey", required=True)):
        await ctx.defer()
        if(key < 0):
            await ctx.respond("Der Key ist ungültig. Er darf nicht kleiner als 0 sein", ephemeral= True)
        else:
            alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Ü", "ß", " ", "!", "?" , "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "§", '"', "$", "%", "&", "/", "(", ")", "=", "´", "`", "@", "€", "^", "°", "<", ">", "|", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "+", "*", "~", "#", "'", ",", ";", ".", ":", "-", "_"]
            encodeText = ""
            add = 0


            i = 0
            while (i < len(nachricht)) :
                j = 0
                while (j < len(alphabet)) :
                    if alphabet[j] == nachricht[i] :
                        if (j + key < len(alphabet)) :
                            encodeText += alphabet[j + key]
                        else :
                            k = 0
                            while (k <= key) :
                                if (j + k == len(alphabet) - 1) :
                                    add = key - k
                                k += 1
                            encodeText += alphabet[add]
                    j += 1
                i += 1

            async def callbacl1(interaction):
                channel = await member.create_dm()
                myEmbed = discord.Embed(title = f"Verschlüsselte Nachricht",description=f"Du hast die verschlüsselte Nachricht von <@{ctx.author.id}> entschlüsselt\n\nDie Nachricht lautet nun: {nachricht}",color=0x598ee7)
                await channel.send(embed=myEmbed)

            view = discord.ui.View()

            decode = discord.ui.Button(label = "Entschlüssle den Text", style = discord.ButtonStyle.blurple, disabled=False, row = 1)
            decode.callback = callbacl1


            view.add_item(decode)

            myEmbed = discord.Embed(title = f"Eine nachricht",description=f"Du hast eine verschlüsselte Nachricht von <@{ctx.author.id}> erhalten\n\nDie Nachricht lautet: {encodeText}",color=0x598ee7)
            channel = await member.create_dm()
            try:
                await channel.send(embed = myEmbed, view = view)
            except:
                pass

            await ctx.respond("Deine Nachricht wurde versendet", ephemeral= True)


    @commands.Cog.listener()
    async def on_ready(self):
        self.umfragen_aktuallisieren.start()
        self.sendchangelog.start()

    @tasks.loop(seconds=60)
    async def sendchangelog(self):
        now = datetime.now() 
        strtime = now.strftime("%a.%H.%M")
        print(strtime)
        if strtime == "Sun.15.55":
            changes = changelogcollection.find_one({"_id" : "changelog"})
            channel = self.client.get_channel(959513949726969906)
            content = ""
            await channel.send("<@&950018262954033152>")
            for change in changes["change"]:
                content += f"*{change['change']}* Geändert von <@{change['adder']}> <t:{change['timestamp']}:F>\n\n"
                if len(content) >= 4000:
                    myEmbed = discord.Embed(title='Der Wöchentliche Changelog <:P_ohaaa:869947368383057990>', description=content, color=0xbd24e7)
                    await channel.send(embed = myEmbed)
                    content = ""
            


            changelogcollection.update_one({"_id" : "changelog"}, {"$set" : {"change" : []}})
            

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
                                    embed = discord.Embed(title="Eine neue IDEE! <:P_ohaaa:869947368383057990>",description=f"{umfragetext}\n> **Community Umfrage zu dieser Idee beendet!**",color=0xbd24e7)
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
    



def setup(client):
    client.add_cog(utility(client))


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
