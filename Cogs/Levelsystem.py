from code import interact
from operator import le
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageOps
import itertools as itertools 
import time
from discord.commands import Option, slash_command
from discord.ui import Select, View
from numpy import put_along_axis
from pymongo import MongoClient

levelsssss = {}

cluster = MongoClient("")

db = cluster["Main"]
levelsyscollection = db["levelsys"]
blacklistcollection = db["blacklist"]

class Levelsystem(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.update_levelsssss.start()

    @tasks.loop(seconds=30)
    async def update_levelsssss(self):
        global levelsssss
        for guild in self.client.guilds:
            x = levelsyscollection.find_one({"_id" : guild.id})
            levelsssss[str(guild.id)] = x

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):



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

        try:
            levelsyscollection.update_one({"_id" : message.guild.id}, {"$inc" : {f"user.{message.author.id}.weekly" : 1}}, upsert = True)
            levelup, level = await addxp(message.guild.id, message.author.id, 10, self)
            x = levelsyscollection.find_one({"_id" : message.guild.id})
            if x == None:
                return
            try:
                disabled = x["disabled"]
            except:
                disabled = False
            if levelup == True and disabled == False:
                myEmbed = discord.Embed(title = "Herzlichen Glückwunsch!", description= f"{message.author.mention}, Du bist soeben ein Level aufgestiegen! Du bist jetzt Level {level}!", color=0xbd24e7)
                await message.channel.send(embed = myEmbed)
        except:
            pass

    @has_permissions(manage_guild=True)
    @slash_command(name='disablelevelsystem', description='Schalte das Levelsystem ab.')
    async def disablelevelsystem(self, ctx):
        await ctx.defer()
        levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {"disabled" : True}})
        await ctx.respond("Ich habe das Levelsystem deaktiviert 😔")

    @has_permissions(manage_guild=True)
    @slash_command(name='enablelevelsystem', description='Schalte das Levelsystem ein.')
    async def enablelevelsystem(self, ctx):
        await ctx.defer()
        levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {"disabled" : False}})
        await ctx.respond("Das Levelsystem ist (wieder) aktiviert 😃😃😃😃😃😃😃😃😃😃😃😃😃😃😃😃😃😃😃")

    @has_permissions(administrator=True)
    @slash_command(name='setxpboost', description='Gebe jemandem einen XP Boost')
    async def setboost(self, ctx, boost : Option(int, "Wie stark soll der XP Boost sein?", required = True, default = None), user : Option(discord.Member, "Von wen möchtest du den Boost ändern?", required = False), role : Option(discord.Role, "Von wen möchtest du den Boost ändern?", required = False, default = None)):
        await ctx.defer()
        try:
            await ctx.respond("Bitte gebe mir einen Moment... <a:Gears_Loading:960472817441329172>")
        except:
            await ctx.send("Bitte gebe mir einen Moment... <a:Gears_Loading:960472817441329172>")
        print(role)
        if role == None:
            x = levelsssss[str(ctx.guild.id)]
            if x == None:
                levelsyscollection.insert_one({"_id" : ctx.guild.id, "User" : { str(user.id) : {"xp" : 0, "allxp" : 0, "level" : 1, "xptonextlevel" : 500, "boost" : boost}}})
                levelsyscollection.update_one({"_id" : "guilds"}, {"$addToSet" : {str(ctx.guild.id) : user.id}})
            else:
                try:
                    xp = xp * x[str(ctx.guild.id)]["boost"]
                except:
                    pass
                levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{user.id}.boost" : boost}})
            await ctx.send("Der XP Boost wurde erfolgreich gesetzt!")
        else:
            x = levelsssss[str(ctx.guild.id)]
            if x == None:
                levelsyscollection.insert_one({"_id" : ctx.guild.id, str("boostroles") : {role.id : boost}})
            else:
                levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"boostroles.{role.id}" : boost}})
            await ctx.send("Der XP Boost wurde erfolgreich gesetzt!")

    
    @slash_command(name='boost', description='Erfahre, wie hoch der momentaner XP Boost von jemandem ist.')
    async def boost(self, ctx, user : Option(discord.Member, "Möchtest du von wem anders den XP Boost sehen?", required = False)):
        await ctx.defer()
        if user == None:
            user = ctx.author
        x = levelsssss[str(ctx.guild.id)]
        print(x)
        boost = 1
        try:
            if x["user"][str(user.id)]["boost"] <= boost:
                boost = x["user"][str(user.id)]["boost"]
            for role in user.roles:
                try:
                    if boost <= x["boostroles"][str(role.id)]:
                        boost = x["boostroles"][str(role.id)]
                except:
                    pass
            xp = xp * boost
        except:
            pass
        try:
            await ctx.respond(f"{user.mention} hat momentan einen XP Boost von {boost}")
        except:
            await ctx.send(f"{user.mention} hat momentan einen XP Boost von {boost}")

    @slash_command(name='rank', description='Erfahre, welches Level du bist.')
    async def rank(self, ctx, user : Option(discord.Member, "Möchtest du von wem anders das level sehen?", required = False)):
        await ctx.defer()
        if user == None:
            user = ctx.author
        if user.bot == True:
            await ctx.respond("Bots haben kein level!")
            return
        try:
            await ctx.respond("Ich erstelle deine Rankcard!")
        except:
            await ctx.send("Ich erstelle deine Rankcard!")
        async with ctx.typing():
            try:
                
                rankcard = await createrankcard(user, ctx.guild, self)
                print(rankcard)
                await ctx.send(embed = rankcard, content = None)
            except Exception as e:
                await ctx.send(f"Ich konnte irgendwie keine Rankcard erstellen. Kann es sein, dass {user} noch nie etwas geschrieben hat? Naja, wie dem auch sei, hier ist mein Error: \n{e}")


    @slash_command(name='changecolor', description='Ändere deine Farbe für die Rankcard! Nur für Booster')
    async def changecolor(self, ctx):
        await ctx.defer()

        async def customcolor():
            boostsince = ctx.author.premium_since
            if boostsince == None and ctx.author.id != 471036610561966111:
                await ctx.send("Nur Booster des Servers dürfen sich eine Eigene Farbe aussuchen.")
                return
            def check(m):
                return m.channel == ctx.channel and m.author == ctx.author
            y = await ctx.send("Du kannst jetzt deine Eigene Farbe auswählen!")
            async def nachrichten(error = False):
                if error == False:
                    myEmbed = discord.Embed(title = f"RGB Code eingeben!",description=f"\nBitte gebe den RBG Code ein!\nDen RGB Code kannst du dir z.B. [HIER](https://www.rapidtables.com/web/color/RGB_Color.html) Generieren.\nGebe den Code wie folgr an:\n`(R, G, B)`\n**Bitte gebe auch die Klammern an!**\nR = Rot, G = Grün, B = Blau",color=0xdb4646)
                if error == True:
                    myEmbed = discord.Embed(title = f"RGB Code eingeben!",description=f"\nBitte gebe den RBG Code ein!\nDen RGB Code kannst du dir z.B. [HIER](https://www.rapidtables.com/web/color/RGB_Color.html) Generieren.\nGebe den Code wie folgr an:\n`(R, G, B)`\n**Bitte gebe auch die Klammern an!**\nR = Rot, G = Grün, B = Blau\nBitte stelle sicher, dass du alles richtig eingibst!",color=0xdb4646)
                await y.edit(embed = myEmbed)
                color = await self.client.wait_for('message', check=check, timeout=120)
                try:
                
                    if not color.content[0] == "(":
                        print(color[0])
                        color = await nachrichten(error = True)
                    if not color.content[-1] == ")":
                        print(color[-1])
                        color = await nachrichten(error = True)

                except:
                    color = await nachrichten(error = True)
                return color
            color = await nachrichten(error = False)
            print(color.content)
            x = color.content.replace("(", "")
            x = x.replace(")", "")
            x = x.split(",")
            print(x)
            x = (int(x[0]), int(x[1]), int(x[2]))
            print(x)
            levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{ctx.user.id}.color" : x}})
            return "success"
            #await ctx.send("Deine Farbe wurde erfolgreich geändert!")

        class DrowDownMenu(discord.ui.View):
            @discord.ui.select(placeholder="Wähle deine Farbe aus!", options=[
                discord.SelectOption(label = "Grün", description = "Klicke, um Grün auszuwählen", emoji = "🟩", value = "Green"),
                discord.SelectOption(label = "Rot", description = "Klicke, um Rot auszuwählen", emoji = "🟥", value = "Red"),
                discord.SelectOption(label = "Gelb", description = "Klicke, um Gelb auszuwählen", emoji = "🟨", value = "Yellow"),
                discord.SelectOption(label = "Blau", description = "Klicke, um Blau auszuwählen", emoji = "🟦", value = "Blue"),
                discord.SelectOption(label = "Eigene Farbe", description = "Klicke, um eine eigene Farbe auszuwählen!", emoji = "🏳️‍🌈", value = "custom"),
            ])

            async def callback(self, select, interaction : discord.Interaction):
                if select.values[0] == "Green":
                    levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{ctx.author.id}.color" : (124, 252, 0)}})
                    await interaction.response.send_message("Deine Farbe wurde erfolgreich geändert! ||es kann bis zu 30 Sekunden dauern bis die änderung inkraft tritt||")
                if select.values[0] == "Red":
                    levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{ctx.author.id}.color" : (220, 20, 60)}})
                    await interaction.response.send_message("Deine Farbe wurde erfolgreich geändert! ||es kann bis zu 30 Sekunden dauern bis die änderung inkraft tritt||")
                if select.values[0] == "Yellow":
                    levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{ctx.author.id}.color" : (255, 255, 0)}})
                    await interaction.response.send_message("Deine Farbe wurde erfolgreich geändert! ||es kann bis zu 30 Sekunden dauern bis die änderung inkraft tritt||")
                if select.values[0] == "Blue":
                    levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{ctx.author.id}.color" : (0, 0, 255) }})
                    await interaction.response.send_message("Deine Farbe wurde erfolgreich geändert! ||es kann bis zu 30 Sekunden dauern bis die änderung inkraft tritt||")
                elif select.values[0] == "custom":
                    fetig = await customcolor()
                    if fetig == "success":
                        await interaction.response.send_message("Deine Farbe wurde erfolgreich geändert! ||es kann bis zu 30 Sekunden dauern bis die änderung inkraft tritt||")
                    else:
                        await interaction.response.send_message("Irgendwas ist schief gelaufen :c")
        myEmbed = discord.Embed(title = f"Wähle deine eigene Farbe aus!",description=f"› **Klicke auf eine Option** - um eine Farbe deiner Wahl auszuwählen",color=0xbd24e7)

        
        view = DrowDownMenu()


        await ctx.respond(embed = myEmbed, view = view, ephemeral = True)

    @has_permissions(administrator=True)
    @slash_command(name='purgelevel', description='Nehme jemandem Level weg')
    async def purgelevel(self, ctx, user : Option(discord.Member, "Wem möchtest du Level wegnehmen?", required = True), level : Option(int, "Wie viele level sollen genommen werden?", required = True)):
        await ctx.defer()
        x = levelsssss[str(ctx.guild.id)]["user"]
        if x != None:
            x  = x[str(user.id)]
        else:
            x = {"level" : 1, "xp" : 0, "allxp" : 0, "xptonextlevel" : 500, "boost" : 1, "color" : (0, 0, 255)}

        xptosteal = 0
        for i in range(x["level"] - level):
            xptosteal += i * 500
        x["level"] -= level
        x["xp"] = 0
        x["allxp"] = xptosteal
        x["xptonextlevel"] = (x["level"] - level) * 500

        levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{user.id}" : x}})
        try:
            await ctx.respond("Die Level wurden erfolgreich genommen.")
        except:
            await ctx.send("Die Level wurden erfolgreich genommen.")

    @has_permissions(administrator=True)
    @slash_command(name='givelevel', description='Gebe jemandem Level.')
    async def givelevel(self, ctx, user : Option(discord.Member, "Wem möchtest du Level geben?", required = True), level : Option(int, "Wie viele level sollen gegeben werden?", required = True)):
        await ctx.defer()
        x = levelsssss[str(ctx.guild.id)]["user"]
        try:
            x  = x[str(user.id)]
        except:
            x = {"level" : 1, "xp" : 0, "allxp" : 0, "xptonextlevel" : 500, "boost" : 1, "color" : (0, 0, 255)}
        print(level)
        xptogive = 0
        for i in range(x["level"] + level):
            xptogive += i * 500
        print(xptogive)
        x["level"] += level
        x["xp"] = 0
        x["allxp"] = xptogive
        x["xptonextlevel"] = (x["level"] + level) * 500

        levelsyscollection.update_one({"_id" : ctx.guild.id}, {"$set" : {f"user.{user.id}" : x}}, upsert = True)
        try:
            await ctx.respond("Die Level wurden erfolgreich gegeben.")
        except:
            await ctx.send("Die Level wurden erfolgreich gegeben.")

    @has_permissions(administrator=True)
    @slash_command(name='addlevelrank', description='Füge eine Rolle hinzu, die man bei einem bestimmten Level bekommt')
    async def addlevelrank(self, ctx, rolle : Option(discord.Role, "Welche Rolle soll gegeben werden?", required = True), level : Option(int, "bei welchem Level soll die Rolle gegeben werden?", required = True)):
        await ctx.defer()
        x = levelsssss[str(ctx.guild.id)]

        try:
            levelsyscollection.insert_one({"_id" : ctx.guild.id, str(level) : rolle.id})
        except:
            levelsyscollection.update_one({"_id" : ctx.guild.id},{"$set" : {str(level) : rolle.id}})
        try:
            await ctx.respond("Die Rolle wurde erfolgreich als Levelbelohnung hinzugefügt!")
        except:
            await ctx.send("Die Rolle wurde erfolgreich als Levelbelohnung hinzugefügt!")

    @slash_command(name='leaderboard', description='Sehe die Top 10 User auf dem Server.')
    async def leaderboard(self, ctx, seite : Option(int, "Welche Seite?", required = False, default = 1)):
        await ctx.defer()

        seite = seite

        message = None

        async def makeleaderboard():
            nonlocal message

            view = discord.ui.View()

            button_last = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=seite == 1, row = 1, custom_id="Last")
            button_last.callback = last_callback

            button_next = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1, custom_id="Next")
            button_next.callback = next_callback

            view.add_item(button_last)
            view.add_item(button_next)

            if message == None:
                levelsys = levelsssss[str(ctx.guild.id)]

                levels = levelsys["user"]
                msg = ""
                ranking = sorted(levels.items(),key=lambda x: x[1]['allxp'],reverse=True)

                for x in range(10):
                    try:
                        msg += f"`Platz {x + ((seite - 1) * 10) + 1}`: <@{ranking[x + ((seite - 1) * 10)][0]}> Level: {ranking[x + ((seite - 1) * 10)][1]['level']}\n\n"
                    except:
                        msg += f"Es gibt keinen Platz  {x + ((seite - 1) * 10) + 1} 😔\n"


                myEmbed = discord.Embed(title = f"Das Ranking! Seite: {seite}",description=msg, color=0xbd24e7)


                message = await ctx.respond(embed = myEmbed, view = view)
            else:
                levelsys = levelsssss[str(ctx.guild.id)]

                levels = levelsys["user"]
                msg = ""
                ranking = sorted(levels.items(),key=lambda x: x[1]['allxp'],reverse=True)

                for x in range(10):
                    try:
                        msg += f"`Platz {x + ((seite - 1) * 10) + 1}`: <@{ranking[x + ((seite - 1) * 10)][0]}> Level: {ranking[x + ((seite - 1) * 10)][1]['level']}\n\n"
                    except:
                        msg += f"Es gibt keinen Platz  {x + ((seite - 1) * 10) + 1} 😔\n"


                myEmbed = discord.Embed(title = f"Das Ranking! Seite: {seite}",description=msg, color=0xbd24e7)


                await ctx.edit(embed = myEmbed, view = view)

        async def last_callback(interaction):
            nonlocal seite
            seite -= 1
            await makeleaderboard()

        async def next_callback(interaction):
            nonlocal seite
            seite += 1
            await makeleaderboard()


        await makeleaderboard()

    @slash_command(name='showlevelroles', description='Sehe die Levelrollen auf deinen Server.')
    async def showlevelroles(self, ctx):
        try:
            x = levelsssss[str(ctx.guild.id)]
        except:
            await ctx.respond("Huch.. Seltsam. Bitte versuche es, den Befehl in 30 Sekunden noch einmal auszuführen. Sollte dieser dann noch immer nicht klappen wende dich bitte an den Tanjun support.")
        await ctx.defer()
        txt = ""
        for lvl in range(1000):
            try:
                rank = x[str(lvl)]
                role = ctx.guild.get_role(rank)
                txt += f"{lvl} - {role.mention}\n\n"

            except:
                pass
        myEmbed = discord.Embed(title = "Deine Levelrollen", description=txt, color=0xbd24e7 )
        await ctx.respond(embed = myEmbed)

    @slash_command(name='weekly', description='Sehe die Top 10 User dieser Woche auf dem Server.')
    async def weekly(self, ctx, seite : Option(int, "Welche Seite?", required = False, default = 1)):
        await ctx.defer()

        seite = seite

        message = None

        async def makeleaderboard():
            nonlocal message

            view = discord.ui.View()

            button_last = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=seite == 1, row = 1, custom_id="Last")
            button_last.callback = last_callback

            button_next = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1, custom_id="Next")
            button_next.callback = next_callback

            view.add_item(button_last)
            view.add_item(button_next)

            if message == None:
                levelsys = levelsssss[str(ctx.guild.id)]
        
                levels = levelsys["user"]
                levels2 = dict(levels)
    
                print(levels)
    
                for user in levels2:
                    print(user)
                    print(levels[str(user)])
                    try:
                        x = levels[str(user)]["weekly"]
    
                    except:
                        levels[str(user)]["weekly"] = 0
                    print(levels[str(user)])
    
                msg = ""
                ranking = sorted(levels.items(),key=lambda x: x[1]['weekly'],reverse=True)
    
                for x in range(10):
                    try:
                        msg += f"`Platz {x + ((seite - 1) * 10) + 1}`: <@{ranking[x + ((seite - 1) * 10)][0]}> weekly xp: {ranking[x + ((seite - 1) * 10)][1]['weekly']}\n\n"
                    except:
                        msg += f"Es gibt keinen Platz  {x + ((seite - 1) * 10) + 1} 😔\n"


                myEmbed = discord.Embed(title = f"Das Weekly Ranking! Seite: {seite}",description=msg, color=0xbd24e7)


                message = await ctx.respond(embed = myEmbed, view = view)
            else:
                levelsys = levelsssss[str(ctx.guild.id)]

                levels = levelsys["user"]
                levels2 = dict(levels)

                print(levels)

                for user in levels2:
                    print(user)
                    print(levels[str(user)])
                    try:
                        x = levels[str(user)]["weekly"]

                    except:
                        levels[str(user)]["weekly"] = 0
                    print(levels[str(user)])

                msg = ""
                ranking = sorted(levels.items(),key=lambda x: x[1]['weekly'],reverse=True)

                for x in range(10):
                    try:
                        msg += f"`Platz {x + ((seite - 1) * 10) + 1}`: <@{ranking[x + ((seite - 1) * 10)][0]}> weekly xp: {ranking[x + ((seite - 1) * 10)][1]['weekly']}\n\n"
                    except:
                        msg += f"Es gibt keinen Platz  {x + ((seite - 1) * 10) + 1} 😔\n"


                myEmbed = discord.Embed(title = f"Das Weekly Ranking! Seite: {seite}",description=msg, color=0xbd24e7)


                await ctx.edit(embed = myEmbed, view = view)

        async def last_callback(interaction):
            nonlocal seite
            seite -= 1
            await makeleaderboard()

        async def next_callback(interaction):
            nonlocal seite
            seite += 1
            await makeleaderboard()


        await makeleaderboard()



async def addxp(guildid, userid, xp, self):
    x = levelsssss[str(guildid)]

    if x == None:
        levelsyscollection.insert_one({"_id" : guildid, str(userid) : {"xp" : xp, "allxp" : xp, "level" : 1, "xptonextlevel" : 500, "boost" : 1, "color" : (0, 0, 255)}})
    else:
        boost = 1
        try:
            if x["user"][str(user.id)]["boost"] <= boost:
                boost = x["user"][str(user.id)]["boost"]
            for role in user.roles:
                try:
                    if boost <= x["boostroles"][str(role.id)]:
                        boost = x["boostroles"][str(role.id)]
                except:
                    pass
            xp = xp * boost
        except:
            pass
        try:
            m = x["user"][str(userid)]
        except:
            m = None
        print(m)
        if m != None:

            level = 1
            xptonextlevel = 500
            calcxp = x["user"][str(userid)]["allxp"]

            while xptonextlevel <= calcxp:
                level += 1
                calcxp -= xptonextlevel
                xptonextlevel += 500


            x = x["user"][str(userid)]
            
            x["xp"] += xp
            x["allxp"] += xp

            allxp = int(x["allxp"])
            xp = int(x["xp"])

            print(x)

            levelsyscollection.update_one({"_id" : guildid}, {"$set" : {f"user.{userid}.xp" : xp, f"user.{userid}.allxp" : allxp}})
        else:
            post = {"xp" : xp, "allxp" : xp, "level" : 1, "xptonextlevel" : 500, "boost" : 1, "color" : (0, 0, 255)}
            levelsyscollection.update_one({"_id" : guildid}, {"$set" : {f"user.{userid}" : post}})
    
    levels = levelsssss[str(guildid)]
    print(levels)
    levels = levels["user"][str(userid)]
    if levels["xp"] >= levels["xptonextlevel"]:
        levels["xp"] -= levels["xptonextlevel"]
        levels["level"] += 1
        levels["xptonextlevel"] += 500
        levelsyscollection.update_one({"_id" : guildid}, {"$set" : {"user." + str(userid) : levels}})
        y = levelsssss[str(guildid)]
        for x in range(levels["level"]):
            try:
                roleid = y[str(x)]
                guild = self.client.get_guild(guildid)
                role = guild.get_role(int(roleid))
                user = guild.get_member(int(userid))
                await user.add_roles(role)
            except:
                pass
            
        return True, levels["level"]
    return False, 0

def getranking(guildid, userid):
    levels = {}

    print("Erstmal alle User zusammenschaufeln..")

    levelsys = levelsssss[str(guildid)]
    
    levels = levelsys["user"]


    ranking = sorted(levels.items(),key=lambda x: x[1]['allxp'],reverse=True)

    c = 1
    for place in ranking:
        #print(place)
        if int(place[0]) == userid:
            return c
        c += 1

def getweeklyrank(guildid, userid):
    levels = {}

    print("Erstmal alle User zusammenschaufeln..")

    levelsys = levelsssss[str(guildid)]
    
    levels = levelsys["user"]

    levels2 = dict(levels)

    print(levels)

    for user in levels2:
        print(user)
        print(levels[str(user)])
        try:
            x = levels[str(user)]["weekly"]

        except:
            levels[str(user)]["weekly"] = 0
        print(levels[str(user)])


    ranking = sorted(levels.items(),key=lambda x: x[1]['weekly'],reverse=True)

    c = 1
    for place in ranking:
        if int(place[0]) == userid:
            return c
        c += 1

async def createrankcard(user, guild, self):

    print("Ich erstelle jetzt eine Rank Card!")

    guildid = guild.id
    tic = time.perf_counter()
    x = levelsssss[str(guildid)]
    toc = time.perf_counter()
    timetilldatabase = toc - tic
    print(timetilldatabase * 1000)
    
    if x == None:
        xp = 0
        xptonextlevel = 500
        level = 1
        booster = 1
        color = (0, 0, 255)
    else:
        xp = x["user"][str(user.id)]["xp"]
        xptonextlevel = x["user"][str(user.id)]["xptonextlevel"]
        level = x["user"][str(user.id)]["level"]
        booster = x["user"][str(user.id)]["boost"]
        color = tuple(x["user"][str(user.id)]["color"])

    


    if xp <= 0:
        xp = 1
    
    if xptonextlevel <= 0:
        xptonextlevel = 1


    
    fillingneed = xp / xptonextlevel

    percent = int(fillingneed * 100)
    fillingneed *= 15

    fillingneed = int(fillingneed)

    booster = "Boost: "
    lvlup = ""
    boost = 1
    try:
        if x["user"][str(user.id)]["boost"] <= boost:
            boost = x["user"][str(user.id)]["boost"]
            print(boost)
        for role in user.roles:
            print(role.name)
            try:
                if boost <= x["boostroles"][str(role.id)]:
                    boost = x["boostroles"][str(role.id)]
            except:
                pass
        xp = xp * boost
    except:
        raise
    print("Ich schau mal nach dem rang.")
    rank = getranking(guildid, user.id)
    weeklyrank = getweeklyrank(guildid, user.id)

    print(f"Ah, rang {rank}, cool!")

    myEmbed = discord.Embed(title = f"Rankcard von {user}",color=0xbd24e7)
    myEmbed.add_field(name = "__Level:__", value = f"{level}")
    myEmbed.add_field(name = "__Server Rang:__", value = f"{rank}.")
    myEmbed.add_field(name = "__Weekly Rang:__", value = f"{weeklyrank}.")
    myEmbed.add_field(name = "__XP Boost:__", value = f"x{boost}")
    if not user.avatar == None:
        myEmbed.set_thumbnail(url = user.avatar.url)

    print("Das Embed hab ich schonmal!")

    Bild = Image.open(f"Images/bg.png").convert("RGBA")
    font_type = ImageFont.truetype("Fonts/Font.ttf", int(150/ 8))
    draw = ImageDraw.Draw(Bild)
    fillingneed = (int(xp / xptonextlevel* 6570))
    white = (0, 0, 0)
    counter = 0
    for _ in itertools.repeat(None, int(6570 / 8)):
        draw.ellipse(((int(100 / 8) + counter, int(100 / 8)), (int(400 / 8) + counter, int(400 / 8))),
                     fill =color)
        counter += 1

    counter  =0
    for _ in itertools.repeat(None, int(6570/ 8) ):
        draw.ellipse(((int(120/ 8) + counter, int(120/ 8)), (int(380/ 8) + counter, int(380/ 8))),
                     fill =white)
        counter += 1

    counter = 0
    for _ in itertools.repeat(None, int(fillingneed / 8)):
        draw.ellipse(((int(100/ 8) + counter, int(100/ 8) ), (int(400/ 8) + counter, int(400/ 8))),
                     fill =color)
        counter += 1

    txt = f'{percent}%'
    draw.text((int(3537/ 8), int(150/ 8)),
              txt,
              fill="white",
              font=font_type,
              align="center",
              stroke_width = 2,
              stroke_fill = "black")

    png_info = Bild.info

    print("Jetzt noch das Bild speichern...")

    Bild.save("Rankcard.png", **png_info)

    print("Jetzt gleich senden")

    guild = self.client.get_guild(933307298011562006)

    channel = guild.get_channel(938841182119796746)

    print(channel)

    message = await channel.send(file=discord.File("Rankcard.png"))


    print(message)

    if len(message.attachments) > 0:
        myEmbed.set_image(url = message.attachments[0].url)

    print("FERTIG!")

    print(myEmbed)

    return myEmbed





def setup(client):
    client.add_cog(Levelsystem(client))