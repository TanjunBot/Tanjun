import discord
from discord.ext import commands, tasks
import json
from discord.ui import Button, View
from datetime import date, timedelta
from datetime import datetime
import random
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
import time
from pymongo import MongoClient
from random import randint

cluster = MongoClient("")

db = cluster["Main"]
economycollection = db["economy"]
lottery = db["lotterie"]
global ersteZahl
global zweiteZahl
global dritteZahl

def addmoney(playerid, vonid, zuid, menge, von, zu):
    generalinformations = economycollection.find_one({"_id" : "general"})
    rechnungid = generalinformations["nextid"]
    economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})
    economycollection.insert_one({"_id" : rechnungid, "type" : "Rechnung", "von" : von, "zu" : zu, "von_id" : vonid, "zu_id" : zuid, "geld" : menge})
    player = economycollection.find_one({"_id" : playerid})
    if player["partner"] == None:
        economycollection.update_one({"_id" : playerid}, {"$inc" : {"money" : menge}})
    else:
        kontoid = player["money"]
        economycollection.update_one({"_id" : kontoid}, {"$inc" : {"money" : menge}})


class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client



    @slash_command(name='start', description='Starte das Economy System!')
    async def start(self, ctx, name : Option(str, "Wie möchtest du heißen?", required = False, default = None), beschreibung : Option(str, "Beschreibe dich?", required = False, default = None)):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})
        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist bereits beim Economy System angemeldet.", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed)
            return
        if name != None and beschreibung != None:
            playerid = generalinformations["nextid"]
            economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})
            economycollection.update_one({"_id" : "general"}, {"$addToSet" : {"registerdplayers" : ctx.author.id}})
            economycollection.update_one({"_id" : "general"}, {"$set" : {f"players.{ctx.author.id}" : playerid}})

            myEmbed = discord.Embed(title = "Erfolgreich begonnen!", description=f"Du bist jetzt erfolgreich beim economy system dabei! gehe doch gleich mal zu den `/arbeitsamt` und suche dir einen Job! ||oder du gehst `/spazieren` und schaust, was passiert 👀||", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return
        class MyModal(discord.ui.Modal):
            def __init__(self) -> None:
                super().__init__("Dein Economy Profil!")
                self.add_item(discord.ui.InputText(label = "Dein Name", placeholder = "Bitte gebe deinen Namen ein"))
                self.add_item(discord.ui.InputText(style = discord.InputTextStyle.long, label = "Deine Beschreibung", placeholder = "Erzähle etwas über dich"))

            async def callback(self, interaction : discord.Interaction):
                name = self.children[0].value
                Beschreibung = self.children[1].value

                
                playerid = generalinformations["nextid"]
                economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})
                economycollection.update_one({"_id" : "general"}, {"$addToSet" : {"registerdplayers" : ctx.author.id}})
                economycollection.update_one({"_id" : "general"}, {"$set" : {f"players.{ctx.author.id}" : playerid}})

                economycollection.insert_one({"_id" : playerid, "type" : "player", "name" : name, "beschreibung" : Beschreibung, "money" : 100, "partner" : None, "clan" : None, "Kopfgeld" : 0, "job" : None, "lastworked" : None, "sometimer" : None})

                myEmbed = discord.Embed(title = "Erfolgreich begonnen!", description=f"Du bist jetzt erfolgreich beim economy system dabei! gehe doch gleich mal zu den `/arbeitsamt` und suche dir einen Job! ||oder du gehst `/spazieren` und schaust, was passiert 👀||", color = 0xbd24e7)
                await interaction.response.send_message(embed = myEmbed, ephemeral= True)
        
        modal = MyModal()
        await ctx.send_modal(modal)
    
    @slash_command(name='insertjob', description='Füge einen Job hinzu')
    async def insertjob(self, ctx, name : Option(str, "Wie heißt der Job?", required = True), beschreibung : Option(str, "Was macht man in dem Job?", required = True), lohn : Option(int, "Wie viel verdient man in dem Job?", required = True), plätze : Option(int, "Wie viele freie Plätze hat der Job?", required = True)):
        await ctx.defer()
        if ctx.author.id == 471036610561966111:
            generalinformations = economycollection.find_one({"_id" : "general"})
            jobid = generalinformations["nextid"]

            economycollection.update_one({"_id" : "general"}, {"$addToSet" : {"jobs" : jobid}})

            economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})

            economycollection.insert_one({"_id" : jobid, "type" : "job", "name" : name, "beschreibung" : beschreibung, "lohn" : lohn, "plätze" : plätze})

            await ctx.respond(content = f"Der Job {name} wurde hinzugefügt!")
        else:
            await ctx.respond("🙅‍♂️")

    @slash_command(name='insertspaziergang', description='Füge einen Spaziergang hinzu')
    async def insertspaziergang(self, ctx, beschreibung : Option(str, "Was soll ich sagen?", required = True), geld : Option(int, "Wie viel Geld soll man bekommen?", required = True)):
        await ctx.defer()
        if ctx.author.id == 471036610561966111:
            generalinformations = economycollection.find_one({"_id" : "general"})
            spazierid = generalinformations["nextid"]

            economycollection.update_one({"_id" : "general"}, {"$addToSet" : {"spaziergänge" : spazierid}})

            economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})

            economycollection.insert_one({"_id" : spazierid, "type" : "spaziergang", "name" : beschreibung, "Geld" : geld})

            await ctx.respond(content = f"Der Spaziergang {beschreibung} wurde hinzugefügt!")
        else:
            await ctx.respond("🙅‍♂️")

    @slash_command(name='arbeitsamt', description='Suche dir einen (neuen) Job.')
    async def arbeitsamt(self, ctx):
        await ctx.defer()
        print("Du bist jetzt im Arbeitsamt!")
        generalinformations = economycollection.find_one({"_id" : "general"})



        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        jobs = generalinformations["jobs"]

        print(jobs)

        jobid = random.choice(jobs)

        job = economycollection.find_one({"_id" : jobid})

        while job["plätze"] == 0:
            print(job["plätze"])
            jobid = random.choice(jobs)

            job = economycollection.find_one({"_id" : jobid})

        async def annehmen_callback(interaction):
            economycollection.update_one({"_id" : jobid}, {"$inc" : {"plätze" : -1}})
            allplayerid = generalinformations["players"]
            playerid = allplayerid[str(ctx.author.id)]
            player = economycollection.find_one({"_id" : playerid})
            oldjobid = player["job"]
            if oldjobid != None:
                economycollection.update_one({"_id" : oldjobid}, {"$inc" : {"plätze" : 1}})
            economycollection.update_one({"_id" : playerid}, {"$set" : {"job" : jobid}})
            myEmbed = discord.Embed(title = "Du hast einen neuen Job!", description=f"Du hast jetzt einen neuen Job! Arbeite doch direkt mit dem `/work` Befehl!", color = 0xbd24e7)
            await ctx.interaction.channel.send(embed = myEmbed)

        annehmen = Button(label = "annehmen", style = discord.ButtonStyle.green)
        annehmen.callback = annehmen_callback

        view = View()

        view.add_item(annehmen)

        myEmbed = discord.Embed(title = "Dein vorgestellter Job", description=f"Der Job {job['name']} hat noch {job['plätze']} freie Plätze. Du wirst in dem Job {job['lohn']}€ verdienen.", color = 0xbd24e7)

        await ctx.respond(embed = myEmbed, view = view)

    @slash_command(name='work', description='Arbeite')
    async def work(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(ctx.author.id)]
        player = economycollection.find_one({"_id" : playerid})
        if player["job"] != None:
            timenow = int(time.time())
            timenow -= 3600
            lastworked = player["lastworked"]
            if lastworked == None:
                lastworked = 0
            if timenow > lastworked:
                jobid = player["job"]
                job = economycollection.find_one({"_id" : jobid})
                lohn = job["lohn"]
                plus = 0
                try:
                    plus = player["plus"]
                except:
                    pass
                addmoney(von = "Arbeit", zu = player["name"], playerid = playerid, menge = lohn + plus, vonid = jobid, zuid = playerid)
                economycollection.update_one({"_id" : playerid}, {"$set" : {"lastworked" : timenow + 3600}})

                myEmbed = discord.Embed(title = "Erfolgreich gearbeitet!", description=f"Du hast erfolgreich als {job['name']} gearbeitet und {lohn + plus}€ verdient.\nDu kannst erneut <t:{timenow + 3600 + 3600}:R> arbeiten.", color = 0xbd24e7)
                await ctx.respond(embed = myEmbed)
            else:
                myEmbed = discord.Embed(title = "Du kannst noch nicht arbeiten!", description=f"Komme <t:{lastworked + 3600}:R> zurück um wieder zu arbeiten.", color = 0xbd24e7)
                await ctx.respond(embed = myEmbed)

    @slash_command(name='daily', description='Bekomme deinen täglichen Bonus')
    async def daily(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(ctx.author.id)]
        player = economycollection.find_one({"_id" : playerid})
        try:
            lastdaily = player["lastdaily"]
            dailystreak = player["dailystreak"]
        except:
            lastdaily = ""
            dailystreak = 0
        now = datetime.now() 
        strtime = now.strftime("%d.%m.%Y")
        if lastdaily == strtime:
            await ctx.respond("Du hast heute bereits deinen Täglichen Bonus eingefordert.", ephemeral = True)
            return
        else:
            yesterday = date.today() - timedelta(days=1)
            strtime2 = now.strftime("%d.%m.%Y")
            if lastdaily == strtime2:
                dailystreak += 1
                moneytogive = dailystreak * 100
                addmoney(playerid = playerid, vonid = 0, zuid = playerid, menge = moneytogive, von = "Daily", zu = player["name"])
                await ctx.respond(f"Du hast erfolgreich {moneytogive}€ für deinen Täglichen Bonus bekommen! Komme jeden Tag wieder, um deine Streak nicht zu verlieren!")
                economycollection.update_one({"_id": playerid}, {"$set" : {"lastdaily" : strtime, "dailystreak" : dailystreak}})
            else:
                dailystreak = 1
                moneytogive = dailystreak * 100
                addmoney(playerid = playerid, vonid = 0, zuid = playerid, menge = moneytogive, von = "Daily", zu = player["name"])
                await ctx.respond(f"Du hast erfolgreich {moneytogive}€ für deinen Täglichen Bonus bekommen! Leider hast du dir gestern deinen Täglichen Bonus nicht abgeholt, weshalb deine Streak nun wieder auf 1 ist. Komme jeden Tag wieder, um deine Streak nicht zu verlieren!")
                economycollection.update_one({"_id": playerid}, {"$set" : {"lastdaily" : strtime, "dailystreak" : dailystreak}})

    @slash_command(name='gehalt', description='Frage nach einer Gehaltserhöhung')
    async def gehalt(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(ctx.author.id)]
        player = economycollection.find_one({"_id" : playerid})
        try:
            moneyPlus = player["plus"]
        except:
            moneyPlus = False

        try:
            if moneyPlus == False:
                yesOrNo = random.randint(1,2)
                if yesOrNo == 1:
                    myEmbed = discord.Embed(title = "Pech gehabt", description=f"Du bekommst leider keine Gehaltserhöhung", color = 0xbd24e7)
                    await ctx.respond(embed = myEmbed)
                else:
                    economycollection.update_one({"_id" : playerid}, {"$set" : {"plus" : random.randint(1, 50)}}, upsert=True)
                    myEmbed = discord.Embed(title = "Herzlichen Glückwunsch!", description=f"Du bekommst eine Gehaltserhöhung :)", color = 0xbd24e7)
                    economycollection.update_one({"_id" : playerid}, {"$set" : {"plus" : True}})
                    await ctx.respond(embed = myEmbed)
            else:
                await ctx.respond("Du hast schon eine Gehaltserhöhung erhalten")
        except:
            yesOrNo = random.randint(1,2)
            if yesOrNo == 1:
                myEmbed = discord.Embed(title = "Pech gehabt", description=f"Du bekommst leider keine Gehaltserhöhung", color = 0xbd24e7)
                await ctx.respond(embed = myEmbed)
            else:
                economycollection.update_one({"_id" : playerid}, {"$set" : {"plus" : random.randint(1, 50)}}, upsert=True)
                myEmbed = discord.Embed(title = "Herzlichen Glückwunsch!", description=f"Du bekommst eine Gehaltserhöhung :)", color = 0xbd24e7)
                economycollection.update_one({"_id" : playerid}, {"$set" : {"plus" : True}})
                await ctx.respond(embed = myEmbed)

    @slash_command(name='antrag', description='Mache jemanden einen Heiratsantrag.')
    async def antrag(self, ctx, member : Option(discord.Member, "Wem möchtest du einen Heiratsantrag machen?", required = True)):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        player1id = allplayerid[str(ctx.author.id)]
        player2id = allplayerid[str(member.id)]
        player1 = economycollection.find_one({"_id" : player1id})
        player2 = economycollection.find_one({"_id" : player2id})
        if player1["partner"] == None:
            if player2["partner"] == None:
                async def annehmen_callback(interaction):
                    economycollection.update_one({"_id" : player1id}, {"$set" : {"partner" : player2id}})
                    economycollection.update_one({"_id" : player2id}, {"$set" : {"partner" : player1id}})
                    generalinformations = economycollection.find_one({"_id" : "general"})
                    kontoid = generalinformations["nextid"]

                    economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})

                    partner1money = player1["money"]
                    partner2money = player2["money"]

                    economycollection.update_one({"_id" : player1id}, {"$set" : {"money" : kontoid}})

                    economycollection.update_one({"_id" : player2id}, {"$set" : {"money" : kontoid}})

                    economycollection.insert_one({"_id" : kontoid, "type" : "Konto", "money" : partner1money + partner2money, "Owner1" : player1id, "Owner2" : player2id})
                    myEmbed = discord.Embed(title = "Ihr seid jetzt Verheiratet!", description=f"{player1['name']} und {player2['name']} sind jetzt verheiratet!", color = 0xbd24e7)
                    await ctx.interaction.channel.send(embed = myEmbed)

                annehmen = Button(label = "Ja, ich will!", style = discord.ButtonStyle.green)
                annehmen.callback = annehmen_callback

                view = View()

                view.add_item(annehmen)

                myEmbed = discord.Embed(title = "Möchtest du den Heiratsantrag annehmen?", description=f"{player1['name']} Hat dir einen Heiratsantrag gemacht. Möchtest du ihn annehmen?", color = 0xbd24e7)

                await ctx.respond(embed = myEmbed, view = view)
                await ctx.send(f"{member.mention}", delete_after = 0.1)

    @slash_command(name='spazieren', description='Gehe spazieren')
    async def spazieren(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(ctx.author.id)]
        player = economycollection.find_one({"_id" : playerid})
        spaziergänge = generalinformations["spaziergänge"]
        spaziergangid = random.choice(spaziergänge)
        if spaziergangid == 62 and player["clan"] == None:
            pass
        else:
            illegalids = [62, 63, 64, 65, 66, 67, 68, 69, 70]
            if not player["clan"] == None:
                illegalids.pop(player["clan"])
            while spaziergangid in illegalids:
                spaziergangid = random.choice(spaziergänge)

        if spaziergangid == 63 and player["clan"] == 1:
            pass
        else:
            illegalids = [62, 63, 64, 65, 66, 67, 68, 69, 70]
            if not player["clan"] == None:
                illegalids.pop(player["clan"])
            while spaziergangid in illegalids:
                spaziergangid = random.choice(spaziergänge)
                zeitbis = int(time.time())
                zeitbis += 120
                economycollection.update_one({"_id" : playerid}, {"$set" : {"sometimer" : zeitbis}})

        zeitjetzt = int(time.time())
        if spaziergangid == 64 and player["clan"] == 2 and player["sometimer"] < zeitjetzt:
            pass
        else:
            illegalids = [62, 63, 64, 65, 66, 67, 68, 69, 70]
            if not player["clan"] == None:
                illegalids.pop(player["clan"])
            while spaziergangid in illegalids:
                spaziergangid = random.choice(spaziergänge)

        verkäufe = [65, 66, 67, 68, 69, 70]
        if spaziergangid in verkäufe and player["clan"] == 3:
            pass
        else:
            illegalids = [62, 63, 64, 65, 66, 67, 68, 69, 70]
            if not player["clan"] == None:
                illegalids.pop(player["clan"])
            while spaziergangid in illegalids:
                spaziergangid = random.choice(spaziergänge)


        spaziergang = economycollection.find_one({"_id" : spaziergangid})
        geld = spaziergang["Geld"]
        if geld > 0:
            addmoney(von = "Spaziergang", zu = player["name"], playerid = playerid, menge = geld, vonid = spaziergangid, zuid = playerid)
        elif geld < 0:
            addmoney(zu = "Spaziergang", von = player["name"], playerid = playerid, menge = geld, zuid = spaziergangid, vonid = playerid)
        myEmbed = discord.Embed(title = "Du warst spazieren!", description=spaziergang["name"], color = 0xbd24e7)
        await ctx.respond(embed = myEmbed)
     
    @slash_command(name='me', description='Bekomme Informationen über dein Economy Profil.')
    async def me(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(ctx.author.id)]
        player = economycollection.find_one({"_id" : playerid})

        if player["partner"] == None:
            money = player["money"]
        else:
            bankid = player["money"]
            bank = economycollection.find_one({"_id" : bankid})
            money = bank["money"]

        jobid = player["job"]
        if jobid == None:
            job = {"name" : "Arbeitslos", "beschreibung" : "Du Arbeitest nicht."}
        else:
            job = economycollection.find_one({"_id" : jobid})
        
        kopfgeld = player["Kopfgeld"]
        
        partnerid = player["partner"]

        if partnerid != None:
            partner = economycollection.find_one({"_id" : partnerid})
        else:
            partner = None

        name = player["name"]
        
        beschreibung = player["beschreibung"]

        description = f"`Name:`{name}\n{beschreibung}\n\n"

        description += f"`Geld`: {money} €\n\n"



        if partner != None:
            description += f"`Partner`: {partner['name']}\n\n"
        
        if kopfgeld != 0:
            description += f"`Kopfgeld`: {player['Kopfgeld']}\n\n"

        description += f"`Job`: {job['name']}\n{job['beschreibung']}\n\n"


        try:
            inventory = player["inventory"]
            for item in inventory:
                description += f"{item['name']}\n{item['beschreibung']}\n\n"
        except:
            pass    


        myEmbed = discord.Embed(title = "Das bist du!", description=description, color = 0xbd24e7)
        await ctx.respond(embed = myEmbed)

    @slash_command(name='watch', description='Starre jemand anderen an.')
    async def watch(self, ctx, user : Option(discord.Member, "Wen möchtest du anstarren? 👀👀👀👀👀👀👀👀👀👀👀👀👀", required = True)):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if user.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Die Person die du anstarren willst ist Nackig! Das wäre ja eine Schandtat wenn du sie so anstarrst‼️ Sage der Person, dass sie sich mit den `/start` Befehl etwas anziehen soll!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(user.id)]
        player = economycollection.find_one({"_id" : playerid})

        if player["partner"] == None:
            money = player["money"]
        else:
            bankid = player["money"]
            bank = economycollection.find_one({"_id" : bankid})
            money = bank["money"]

        jobid = player["job"]
        if jobid == None:
            job = {"name" : "Arbeitslos", "beschreibung" : "Du Arbeitest nicht."}
        else:
            job = economycollection.find_one({"_id" : jobid})
        
        kopfgeld = player["Kopfgeld"]
        
        partnerid = player["partner"]

        if partnerid != None:
            partner = economycollection.find_one({"_id" : partnerid})
        else:
            partner = None

        name = player["name"]
        
        beschreibung = player["beschreibung"]

        description = f"`Name:`{name}\n{beschreibung}\n\n"

        description += f"`Geld`: {money} €\n\n"



        if partner != None:
            description += f"`Partner`: {partner['name']}\n\n"
        
        if kopfgeld != 0:
            description += f"`Kopfgeld`: {player['Kopfgeld']}\n\n"

        description += f"`Job`: {job['name']}\n{job['beschreibung']}\n\n"


        try:
            inventory = player["inventory"]
            for item in inventory:
                description += f"{item['name']}\n{item['beschreibung']}\n\n"
        except:
            pass    


        myEmbed = discord.Embed(title = f"Das ist {user}!", description=description, color = 0xbd24e7)
        await ctx.respond(embed = myEmbed)

    möglichkeiten_konsumierbar = [
        discord.OptionChoice(name = "Das Item soll nur einmal benutzt werden können.", value = "True"),
        discord.OptionChoice(name = "Das Item soll unendlich oft benutzt werden können.", value = "False")
    ]

    möglichkeiten_dm = [
        discord.OptionChoice(name = "Ich möchte eine DM bekommen, wenn jemand das Item benutzt.", value = "1"),
        discord.OptionChoice(name = "Ich möchte gepingt werden wenn jemand das Item benutzt.", value = "2"),
        discord.OptionChoice(name = "Ich möchte nicht benachrichtigt werden, wenn jemand das Item benutzt.", value = "3")
    ]

    möglichkeiten_häufigkeit = [
        discord.OptionChoice(name = "Mein Item soll es nur einmal geben.", value = "1"),
        discord.OptionChoice(name = "Mein Item soll es 10 mal geben.", value = "10"),
        discord.OptionChoice(name = "Mein Item soll es unbegrenzt oft geben.", value = "372036854775807")
    ]

    möglichkeiten_verschenkbar = [
        discord.OptionChoice(name = "Mein Item soll verschenkt werden können.", value = "True"),
        discord.OptionChoice(name = "Mein Item soll nicht Verschenkt werden können.", value = "False")
    ]


    @slash_command(name='additem', description='Füge ein Item hinzu.')
    async def additem(self, ctx, name : Option(str, "Wie soll dein Item heißen?", required = True), beschreibung : Option(str, "Bitte beschreibe dein Item?", required = True), preis : Option(int, "Wie viel soll dein Item kosten?", required = True), konsumierbar : Option(str, "Soll dein Item Konsumiert werden können?", required = True, choices = möglichkeiten_konsumierbar), dm : Option(str, "Möchtest du eine DM bekommen wenn jemand dein Item benutzt?", required = True, choices = möglichkeiten_dm), häufigkeit : Option(str, "Wie oft soll es dein Item geben?", required = True, choices = möglichkeiten_häufigkeit), verschenkbar : Option(str, "Soll dein Item verschenkt werden können?", required = True, choices = möglichkeiten_verschenkbar)):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})

        
        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        itemid = generalinformations["nextid"]


        economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})

        itemsnow = economycollection.find_one({"_id" : "general"})
        try:
            itemsnow["items"][str(ctx.author.id)].append(itemid)
        except:
            itemsnow["items"][str(ctx.author.id)] = [itemid]

        economycollection.update_one({"_id" : "general"}, {"$set" : {f"items.{ctx.author.id}" : itemsnow["items"][str(ctx.author.id)]}}, upsert=True)

        economycollection.insert_one({"_id" : itemid, "type" : "item", "name" : name, "beschreibung" : beschreibung, "kosten" : preis, "konsumierbar" : bool(konsumierbar), "benachrichtigung" : int(dm), "häufigkeit" : int(häufigkeit), "verschenkbar" : bool(verschenkbar), "addedby" : ctx.author.id})

        await ctx.respond(f"Dein Item {name} wurde erfolgreich hinzugefügt. Es hat die ID {itemid}. Du kannst es mit dem `/shop` Befehl verkaufen!")

    @slash_command(name='shop', description='Gehe in den Einkaufsbereich.')
    async def shop(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        
        view = discord.ui.View()

        async def shop_erstellen(interaction):

            class MyModal(discord.ui.Modal):
                def __init__(self) -> None:
                    super().__init__("Dein Shop!")
                    self.add_item(discord.ui.InputText(label = "Name des Shops", placeholder = "Wie heißt dein Shop"))
                    self.add_item(discord.ui.InputText(style = discord.InputTextStyle.long, label = "Beschreibung des Shops", placeholder = "Erzähle, was man in deinem Shop kaufen kann!"))

                async def callback(self, interaction : discord.Interaction):
                    name = self.children[0].value
                    Beschreibung = self.children[1].value
                    


                    shopid = generalinformations["nextid"]

                    print(shopid)

                    economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})
                    economycollection.update_one({"_id" : "general"}, {"$addToSet" : {"shops" : int(shopid)}}, upsert=True)
                    economycollection.update_one({"_id" : "general"}, {"$addToSet" : {"playerswithshop" : ctx.author.id}}, upsert=True)
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(ctx.author.id)]
                    economycollection.update_one({"_id" : playerid}, {"$set" : {"shop" : shopid}}, upsert=True)

                    economycollection.insert_one({"_id" : shopid, "type" : "shop", "name" : name, "beschreibung" : Beschreibung, "angebot" : [], "level" : 1})

                    myEmbed = discord.Embed(title = "Shop erfolgreich erstellt!", description=f'Dein Shop "{name}" wurde erfolgreich erstellt. benutze den `/shop` befehl, um Items zu verkaufen.', color = 0xbd24e7)
                    await interaction.response.send_message(embed = myEmbed, ephemeral= True)
        
            modal = MyModal()

            await interaction.response.send_modal(modal)

        async def shop_bearbeiten(interaction):



            allitemids = generalinformations["items"][str(ctx.author.id)]
            items = []

            for id in allitemids:
                item = economycollection.find_one({"_id" : id})
                items.append(item)

            c = 0
            options1 = []
            options2 = []
            options3 = []
            options4 = []
            options5 = []

            for item in items:
                c += 1
                label = str(item["name"])
                description = str(item["beschreibung"])
                if c >= 25 and c <= 50:
                    options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                elif c >= 50 and c <= 75:
                    options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                elif c >= 75 and c <= 100:
                    options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                elif c >= 100 and c <= 125:
                    options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                else:
                    options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))


            class DrowDownMenu(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options1,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    economycollection.update_one({"_id" : shopid}, {"$addToSet" : {"angebot" : int(self.values[0])}})
                    await interaction.response.send_message(f"Das Item wurde erfolgreich hinzugefügt.", ephemeral= True)

            class DrowDownMenu2(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options2,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    economycollection.update_one({"_id" : shopid}, {"$addToSet" : {"angebot" : int(self.values[0])}})
                    await interaction.response.send_message(f"Das Item wurde erfolgreich hinzugefügt.", ephemeral= True)

            class DrowDownMenu3(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options3,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    economycollection.update_one({"_id" : shopid}, {"$addToSet" : {"angebot" : int(self.values[0])}})
                    await interaction.response.send_message(f"Das Item wurde erfolgreich hinzugefügt.", ephemeral= True)

            class DrowDownMenu4(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options4,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    economycollection.update_one({"_id" : shopid}, {"$addToSet" : {"angebot" : int(self.values[0])}})
                    await interaction.response.send_message(f"Das Item wurde erfolgreich hinzugefügt.", ephemeral= True)

            class DrowDownMenu5(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options5,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    economycollection.update_one({"_id" : shopid}, {"$addToSet" : {"angebot" : int(self.values[0])}})
                    await interaction.response.send_message(f"Das Item wurde erfolgreich hinzugefügt.", ephemeral= True)


            class DropDownView(discord.ui.View):
                def __init__(self):
                    super().__init__()

                    self.add_item(DrowDownMenu())
                    if len(options2) != 0:
                        self.add_item(DrowDownMenu2())
                    if len(options3) != 0:
                        self.add_item(DrowDownMenu3())
                    if len(options4) != 0:
                        self.add_item(DrowDownMenu4())
                    if len(options5) != 0:
                        self.add_item(DrowDownMenu5())



            view = DropDownView()
            await interaction.response.send_message(content = f"Bitte wähle das Item aus, das du hinzufügen möchtest.", view = view , ephemeral= True)

        async def shop_besuchen(interaction):
            allshopsids = generalinformations["shops"]
            allshops = []

            for shopid in allshopsids:
                shop = economycollection.find_one({"_id" : shopid})
                allshops.append(shop)


            c = 0
            options1 = []
            options2 = []
            options3 = []
            options4 = []
            options5 = []

            for item in allshops:
                print(item)
                c += 1
                label = str(item["name"])
                description = str(item["beschreibung"])
                if c >= 25 and c <= 50:
                    options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                elif c >= 50 and c <= 75:
                    options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                elif c >= 75 and c <= 100:
                    options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                elif c >= 100 and c <= 125:
                    options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                else:
                    options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))


            class DrowDownMenu(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welchen Shop möchtest du besuchen?",
                        min_values=1,
                        max_values=1,
                        options=options1,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    print(self.values[0])
                    shopid = int(self.values[0])
                    shop = economycollection.find_one({"_id" : shopid})
                    allitemids = shop["angebot"]
                    items = []

                    for itemid in allitemids:
                        item = economycollection.find_one({"_id" : itemid})
                        items.append(item)
                    
                    c = 0
                    options1 = []
                    options2 = []
                    options3 = []
                    options4 = []
                    options5 = []

                    for item in items:
                        c += 1
                        label = str(item["name"])
                        description = str(item["kosten"]) + "€"
                        if c >= 25 and c <= 50:
                            options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 50 and c <= 75:
                            options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 75 and c <= 100:
                            options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 100 and c <= 125:
                            options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        else:
                            options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))


                    class DrowDownMenu(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options1,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            print(itemid)
                            item = economycollection.find_one({"_id" : int(itemid)})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu2(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options2,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu3(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options3,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu4(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options4,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu5(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options5,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)


                    class DropDownView(discord.ui.View):
                        def __init__(self):
                            super().__init__()

                            self.add_item(DrowDownMenu())
                            if len(options2) != 0:
                                self.add_item(DrowDownMenu2())
                            if len(options3) != 0:
                                self.add_item(DrowDownMenu3())
                            if len(options4) != 0:
                                self.add_item(DrowDownMenu4())
                            if len(options5) != 0:
                                self.add_item(DrowDownMenu5())



                    view = DropDownView()
                    await interaction.response.send_message(content = f"Bitte wähle das Item aus, das du kaufen möchtest.", view = view, ephemeral= True)


            class DrowDownMenu2(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du kaufen?",
                        min_values=1,
                        max_values=1,
                        options=options2,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    shop = economycollection.find_one({"_id" : shopid})
                    allitemids = shop["angebot"]
                    items = []

                    for itemid in allitemids:
                        item = economycollection.find_one({"_id" : itemid})
                        items.append(item)
                    
                    c = 0
                    options1 = []
                    options2 = []
                    options3 = []
                    options4 = []
                    options5 = []

                    for item in items:
                        c += 1
                        label = str(item["name"])
                        description = str(item["kosten"]) + "€"
                        if c >= 25 and c <= 50:
                            options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 50 and c <= 75:
                            options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 75 and c <= 100:
                            options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 100 and c <= 125:
                            options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        else:
                            options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))


                    class DrowDownMenu(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options1,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu2(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options2,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu3(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options3,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu4(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options4,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu5(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options5,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)


                    class DropDownView(discord.ui.View):
                        def __init__(self):
                            super().__init__()

                            self.add_item(DrowDownMenu())
                            if len(options2) != 0:
                                self.add_item(DrowDownMenu2())
                            if len(options3) != 0:
                                self.add_item(DrowDownMenu3())
                            if len(options4) != 0:
                                self.add_item(DrowDownMenu4())
                            if len(options5) != 0:
                                self.add_item(DrowDownMenu5())



                    view = DropDownView()
                    await interaction.response.send_message(content = f"Bitte wähle das Item aus, das du kaufen möchtest.", view = view, ephemeral= True)

            class DrowDownMenu3(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options3,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    shop = economycollection.find_one({"_id" : shopid})
                    allitemids = shop["angebot"]
                    items = []

                    for itemid in allitemids:
                        item = economycollection.find_one({"_id" : itemid})
                        items.append(item)
                    
                    c = 0
                    options1 = []
                    options2 = []
                    options3 = []
                    options4 = []
                    options5 = []

                    for item in items:
                        c += 1
                        label = str(item["name"])
                        description = str(item["kosten"]) + "€"
                        if c >= 25 and c <= 50:
                            options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 50 and c <= 75:
                            options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 75 and c <= 100:
                            options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 100 and c <= 125:
                            options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        else:
                            options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))


                    class DrowDownMenu(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options1,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu2(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options2,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu3(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options3,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu4(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options4,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu5(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options5,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)


                    class DropDownView(discord.ui.View):
                        def __init__(self):
                            super().__init__()

                            self.add_item(DrowDownMenu())
                            if len(options2) != 0:
                                self.add_item(DrowDownMenu2())
                            if len(options3) != 0:
                                self.add_item(DrowDownMenu3())
                            if len(options4) != 0:
                                self.add_item(DrowDownMenu4())
                            if len(options5) != 0:
                                self.add_item(DrowDownMenu5())



                    view = DropDownView()
                    await interaction.response.send_message(content = f"Bitte wähle das Item aus, das du kaufen möchtest.", view = view, ephemeral= True)

            class DrowDownMenu4(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options4,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    shop = economycollection.find_one({"_id" : shopid})
                    allitemids = shop["angebot"]
                    items = []

                    for itemid in allitemids:
                        item = economycollection.find_one({"_id" : itemid})
                        items.append(item)
                    
                    c = 0
                    options1 = []
                    options2 = []
                    options3 = []
                    options4 = []
                    options5 = []

                    for item in items:
                        c += 1
                        label = str(item["name"])
                        description = str(item["kosten"]) + "€"
                        if c >= 25 and c <= 50:
                            options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 50 and c <= 75:
                            options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 75 and c <= 100:
                            options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 100 and c <= 125:
                            options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        else:
                            options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))


                    class DrowDownMenu(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options1,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu2(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options2,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu3(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options3,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu4(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options4,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu5(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options5,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)


                    class DropDownView(discord.ui.View):
                        def __init__(self):
                            super().__init__()

                            self.add_item(DrowDownMenu())
                            if len(options2) != 0:
                                self.add_item(DrowDownMenu2())
                            if len(options3) != 0:
                                self.add_item(DrowDownMenu3())
                            if len(options4) != 0:
                                self.add_item(DrowDownMenu4())
                            if len(options5) != 0:
                                self.add_item(DrowDownMenu5())



                    view = DropDownView()
                    await interaction.response.send_message(content = f"Bitte wähle das Item aus, das du kaufen möchtest.", view = view, ephemeral= True)

            class DrowDownMenu5(discord.ui.Select):
                def __init__(self):

                    super().__init__(
                        placeholder="Welches Item möchtest du hinzufügen?",
                        min_values=1,
                        max_values=1,
                        options=options5,
                        custom_id="1"
                    )


                async def callback(self, interaction : discord.Interaction):
                    allplayerid = generalinformations["players"]
                    playerid = allplayerid[str(interaction.user.id)]
                    player = economycollection.find_one({"_id" : playerid})
                    shopid = player["shop"]
                    shop = economycollection.find_one({"_id" : shopid})
                    allitemids = shop["angebot"]
                    items = []

                    for itemid in allitemids:
                        item = economycollection.find_one({"_id" : itemid})
                        items.append(item)
                    
                    c = 0
                    options1 = []
                    options2 = []
                    options3 = []
                    options4 = []
                    options5 = []

                    for item in items:
                        c += 1
                        label = str(item["name"])
                        description = str(item["kosten"]) + "€"
                        if c >= 25 and c <= 50:
                            options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 50 and c <= 75:
                            options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 75 and c <= 100:
                            options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        elif c >= 100 and c <= 125:
                            options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))
                        else:
                            options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = item["_id"]))


                    class DrowDownMenu(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options1,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu2(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options2,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu3(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options3,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu4(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options4,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)

                    class DrowDownMenu5(discord.ui.Select):
                        def __init__(self):
                        
                            super().__init__(
                                placeholder="Welches Item möchtest du kaufen?",
                                min_values=1,
                                max_values=1,
                                options=options5,
                                custom_id="1"
                            )


                        async def callback(self, interaction : discord.Interaction):
                            itemid = self.values[0]
                            item = economycollection.find_one({"_id" : itemid})
                            allplayerid = generalinformations["players"]
                            playerid = allplayerid[str(interaction.user.id)]
                            player = economycollection.find_one({"_id" : playerid})
                            preis = item["kosten"]

                            if player["partner"] == None:
                                money = player["money"]
                            else:
                                bankid = player["money"]
                                bank = economycollection.find_one({"_id" : bankid})
                                money = bank["money"]

                            if money >= preis:
                                reciverid = allplayerid[str(item["addedby"])]
                                reciver = economycollection.find_one({"_id" : reciverid})
                                addmoney(playerid = playerid, vonid = playerid, zuid = reciverid, menge = preis * -1, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                addmoney(playerid = reciverid, vonid = playerid, zuid = reciverid, menge = preis, von = f"{player['name']} hat {item['name']} Gekauft.", zu = reciver['name'])
                                economycollection.update_one({"_id" : playerid}, {"$addToSet" : {"inventory" : item}}, upsert= True)
                                await interaction.response.send_message(f"Du hast erfolgreich {item['name']} für {preis}€ gekauft.", ephemeral= True)
                            else:
                                await interaction.response.send_message(f"Du hast nicht genug Geld um {item['name']} für {preis}€ zu kaufen. <:P_SadCat:907549840161005598>", ephemeral=True)


                    class DropDownView(discord.ui.View):
                        def __init__(self):
                            super().__init__()

                            self.add_item(DrowDownMenu())
                            if len(options2) != 0:
                                self.add_item(DrowDownMenu2())
                            if len(options3) != 0:
                                self.add_item(DrowDownMenu3())
                            if len(options4) != 0:
                                self.add_item(DrowDownMenu4())
                            if len(options5) != 0:
                                self.add_item(DrowDownMenu5())



                    view = DropDownView()
                    await interaction.response.send_message(content = f"Bitte wähle das Item aus, das du kaufen möchtest.", view = view, ephemeral= True)


            class DropDownView(discord.ui.View):
                def __init__(self):
                    super().__init__()

                    self.add_item(DrowDownMenu())
                    if len(options2) != 0:
                        self.add_item(DrowDownMenu2())
                    if len(options3) != 0:
                        self.add_item(DrowDownMenu3())
                    if len(options4) != 0:
                        self.add_item(DrowDownMenu4())
                    if len(options5) != 0:
                        self.add_item(DrowDownMenu5())



            view = DropDownView()
            await interaction.response.send_message(content = f"Bitte wähle den Shop aus, den du besuchen möchtest.", view = view, ephemeral= True)
            

        playerswithshops = generalinformations["playerswithshop"]

        new_shop = discord.ui.Button(label = "Shop eröffnen", style = discord.ButtonStyle.blurple, disabled=ctx.author.id in playerswithshops, row = 1)
        new_shop.callback = shop_erstellen

        edit_shop = discord.ui.Button(label = "Shop bearbeiten", style = discord.ButtonStyle.blurple, disabled=ctx.author.id not in playerswithshops, row = 1)
        edit_shop.callback = shop_bearbeiten

        visit_shop = discord.ui.Button(label = "Shop besuchen", style = discord.ButtonStyle.blurple, disabled=False, row = 1)
        visit_shop.callback = shop_besuchen

        view.add_item(new_shop)
        view.add_item(edit_shop)
        view.add_item(visit_shop)

        await ctx.respond(content = "Was möchtest du machen?", view = view , ephemeral= True)


    @slash_command(name='gift', description='Gehe in den Einkaufsbereich.')
    async def gift(self, ctx, user : Option(discord.Member, "Wem möchtest du ein Item schenken?", required = True)):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(ctx.author.id)]
        player = economycollection.find_one({"_id" : playerid})

        reciverid = allplayerid[str(user.id)]
        reciver = economycollection.find_one({"_id" : reciverid})

        items = player["inventory"]
        c = 0
        options1 = []
        options2 = []
        options3 = []
        options4 = []
        options5 = []

        for item in items:
            c += 1
            label = str(item["name"])
            description = str(item["beschreibung"])
            if c >= 25 and c <= 50 and item["verschenkbar"] == True:
                options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            elif c >= 50 and c <= 75 and item["verschenkbar"] == True:
                options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            elif c >= 75 and c <= 100 and item["verschenkbar"] == True:
                options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            elif c >= 100 and c <= 125 and item["verschenkbar"] == True:
                options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            else:
                if item["verschenkbar"] == True:
                    options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))



        class DrowDownMenu(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du verschenken?",
                    min_values=1,
                    max_values=1,
                    options=options1,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]


                reciver = economycollection.find_one({"_id" : reciverid})
                inv = reciver["inventory"]
                inv.append(playerinv[int(self.values[0])])
                economycollection.update_one({"_id" : reciverid}, {"$set" : {"inventory" : inv}})

                
                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message(f"Das Item wurde erfolgreich verschenkt!", ephemeral= True)

        class DrowDownMenu2(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du verschenken?",
                    min_values=1,
                    max_values=1,
                    options=options2,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]


                reciver = economycollection.find_one({"_id" : reciverid})
                inv = reciver["inventory"]
                inv.append(playerinv[int(self.values[0])])
                economycollection.update_one({"_id" : reciverid}, {"$set" : {"inventory" : inv}})

                
                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message(f"Das Item wurde erfolgreich verschenkt!", ephemeral= True)

        class DrowDownMenu3(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du hinzufügen?",
                    min_values=1,
                    max_values=1,
                    options=options3,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]


                reciver = economycollection.find_one({"_id" : reciverid})
                inv = reciver["inventory"]
                inv.append(playerinv[int(self.values[0])])
                economycollection.update_one({"_id" : reciverid}, {"$set" : {"inventory" : inv}})

                
                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message(f"Das Item wurde erfolgreich verschenkt!", ephemeral= True)

        class DrowDownMenu4(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du verschenken?",
                    min_values=1,
                    max_values=1,
                    options=options4,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]


                reciver = economycollection.find_one({"_id" : reciverid})
                inv = reciver["inventory"]
                inv.append(playerinv[int(self.values[0])])
                economycollection.update_one({"_id" : reciverid}, {"$set" : {"inventory" : inv}})

                
                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message(f"Das item wurde erfolgreich verschenkt!", ephemeral= True)

        class DrowDownMenu5(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du hinzufügen?",
                    min_values=1,
                    max_values=1,
                    options=options5,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]


                reciver = economycollection.find_one({"_id" : reciverid})
                inv = reciver["inventory"]
                inv.append(playerinv[int(self.values[0])])
                economycollection.update_one({"_id" : reciverid}, {"$set" : {"inventory" : inv}})

                
                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message(f"Das item wurde erfolgreich verschenkt!", ephemeral= True)


        class DropDownView(discord.ui.View):
            def __init__(self):
                super().__init__()

                self.add_item(DrowDownMenu())
                if len(options2) != 0:
                    self.add_item(DrowDownMenu2())
                if len(options3) != 0:
                    self.add_item(DrowDownMenu3())
                if len(options4) != 0:
                    self.add_item(DrowDownMenu4())
                if len(options5) != 0:
                    self.add_item(DrowDownMenu5())



        view = DropDownView()
        await ctx.respond(content = f"Bitte wähle das Item aus, das du hinzufügen möchtest.", view = view)


    @slash_command(name='use', description='Benutze ein Item.')
    async def use(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})


        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id not in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist noch nicht im Economy System angemeldet. Bitte erstelle dir mit `/start` einen Account!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed, ephemeral= True)
            return

        allplayerid = generalinformations["players"]
        playerid = allplayerid[str(ctx.author.id)]
        player = economycollection.find_one({"_id" : playerid})

        items = player["inventory"]
        c = 0
        options1 = []
        options2 = []
        options3 = []
        options4 = []
        options5 = []

        for item in items:
            c += 1
            label = str(item["name"])
            description = str(item["beschreibung"])
            if c >= 25 and c <= 50 and item["konsumierbar"] == True:
                options2.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            elif c >= 50 and c <= 75 and item["konsumierbar"] == True:
                options3.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            elif c >= 75 and c <= 100 and item["konsumierbar"] == True:
                options4.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            elif c >= 100 and c <= 125 and item["konsumierbar"] == True:
                options5.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))
            else:
                if item["konsumierbar"] == True:
                    options1.append(discord.SelectOption(label = label[:90], description = description[:90], value = c - 1))



        class DrowDownMenu(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du benutzen?",
                    min_values=1,
                    max_values=1,
                    options=options1,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]

                item = playerinv[int(self.values[0])]


                benachrichtigung = item["benachrichtigung"]

                if benachrichtigung == 1:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    try:
                        await member.send(f"{interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.")
                    except:
                        if member != None:
                            await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                        else:
                            await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                if benachrichtigung == 2:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    if member != None:
                        await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                    else:
                        await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message("Das Item wurde erfolgreich benutzt.", ephemeral= True)




        class DrowDownMenu2(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du benutzen?",
                    min_values=1,
                    max_values=1,
                    options=options2,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]

                item = playerinv[int(self.values[0])]


                benachrichtigung = item["benachrichtigung"]

                if benachrichtigung == 1:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    try:
                        await member.send(f"{interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.")
                    except:
                        if member != None:
                            await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                        else:
                            await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                if benachrichtigung == 2:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    if member != None:
                        await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                    else:
                        await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message("Das Item wurde erfolgreich benutzt.", ephemeral= True)

        class DrowDownMenu3(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du benutzen?",
                    min_values=1,
                    max_values=1,
                    options=options3,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]

                item = playerinv[int(self.values[0])]


                benachrichtigung = item["benachrichtigung"]

                if benachrichtigung == 1:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    try:
                        await member.send(f"{interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.")
                    except:
                        if member != None:
                            await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                        else:
                            await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                if benachrichtigung == 2:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    if member != None:
                        await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                    else:
                        await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message("Das Item wurde erfolgreich benutzt.", ephemeral= True)

        class DrowDownMenu4(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du benutzen?",
                    min_values=1,
                    max_values=1,
                    options=options4,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]

                item = playerinv[int(self.values[0])]


                benachrichtigung = item["benachrichtigung"]

                if benachrichtigung == 1:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    try:
                        await member.send(f"{interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.")
                    except:
                        if member != None:
                            await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                        else:
                            await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                if benachrichtigung == 2:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    if member != None:
                        await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                    else:
                        await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message("Das Item wurde erfolgreich benutzt.", ephemeral= True)

        class DrowDownMenu5(discord.ui.Select):
            def __init__(self):

                super().__init__(
                    placeholder="Welches Item möchtest du benutzen?",
                    min_values=1,
                    max_values=1,
                    options=options5,
                    custom_id="1"
                )


            async def callback(self, interaction : discord.Interaction):
                player = economycollection.find_one({"_id" : playerid})
                playerinv = player["inventory"]

                item = playerinv[int(self.values[0])]


                benachrichtigung = item["benachrichtigung"]

                if benachrichtigung == 1:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    try:
                        await member.send(f"{interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.")
                    except:
                        if member != None:
                            await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                        else:
                            await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                if benachrichtigung == 2:
                    try:
                        member = self.client.get_user(int(item["addedby"]))
                    except:
                        member = None
                    if member != None:
                        await ctx.channel.send(f"{member.mention} {interaction.user.name}#{interaction.user.discriminator} hat grade dein Item {item['name']} benutzt.\n||Eigentlich wollte ich dir eine DM schreiben, aber irgendwie hat das nicht geklappt. Sind deine DMs offen? 👀||")
                    else:
                        await ctx.channel.send(f"Bitte sage {member.name}#{member.discriminator} dass du grade das Item {item['name']} benutzt hast.")

                playerinv.pop(int(self.values[0]))
                economycollection.update_one({"_id" : playerid}, {"$set" : {"inventory" : playerinv}})

                await interaction.response.send_message("Das Item wurde erfolgreich benutzt.", ephemeral= True)


        class DropDownView(discord.ui.View):
            def __init__(self):
                super().__init__()

                self.add_item(DrowDownMenu())
                if len(options2) != 0:
                    self.add_item(DrowDownMenu2())
                if len(options3) != 0:
                    self.add_item(DrowDownMenu3())
                if len(options4) != 0:
                    self.add_item(DrowDownMenu4())
                if len(options5) != 0:
                    self.add_item(DrowDownMenu5())



        view = DropDownView()
        await ctx.respond(content = f"Bitte wähle das Item aus, das du benutzen möchtest.", view = view)


    möglichkeitenLottery = [
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
    ]


    @slash_command(name='playlottery', description='Spiele in der Lotterie')
    async def playlottery(self, ctx, erstezahl : Option(str, "Wie lautet die erste Zahl", required = True, choices = möglichkeitenLottery), zweitezahl : Option(str, "Wie lautet die zweite Zahl", required = True, choices = möglichkeitenLottery), drittezahl : Option(str, "Wie lautet die dritte Zahl", required = True, choices = möglichkeitenLottery)):
        await ctx.defer()
        try:
            findTrue = lottery.find_one({"_id" : ctx.author.id})
            if findTrue["bereitsEinLos"] == None:
                lottery.insert_one({"_id" : ctx.author.id, "Lotterie" : f"{erstezahl}-{zweitezahl}-{drittezahl}", "ErsteZahl" : erstezahl, "ZweiteZahl" : zweitezahl, "DritteZahl" : drittezahl, "bereitsEinLos" : True})
                await ctx.respond("Du nimmst nun an der Lotterie teil :)", ephemeral=True)
            else:
                if findTrue["bereitsEinLos"] == True:
                    await ctx.respond("Du nimmst schon an der Lotterie teil", ephemeral=True)
                else:
                    lottery.insert_one({"_id" : ctx.author.id, "Lotterie" : f"{erstezahl}-{zweitezahl}-{drittezahl}", "ErsteZahl" : erstezahl, "ZweiteZahl" : zweitezahl, "DritteZahl" : drittezahl, "bereitsEinLos" : True})
                    await ctx.respond("Du nimmst nun an der Lotterie teil :)", ephemeral=True)
        except:
            lottery.insert_one({"_id" : ctx.author.id, "Lotterie" : f"{erstezahl}-{zweitezahl}-{drittezahl}", "ErsteZahl" : erstezahl, "ZweiteZahl" : zweitezahl, "DritteZahl" : drittezahl, "bereitsEinLos" : True})
            await ctx.respond("Du nimmst nun an der Lotterie teil :)", ephemeral=True)


    @tasks.loop(seconds = 1)
    async def checkforLottery(self):
        x = datetime.now()
        print(x.hour)
        channelLottery = self.client.get_channel(int(923324336570515497))
        if x.hour == 18 and x.minute == 0 and x.second == 0:
            await channelLottery.send(f"Die Ausziehung der heutigen Lotterie vom {x.day}.{x.month}.{x.year} startet in wenigen Sekunden!")
            try:
                lottery.insert_one({"_id" : 1234, "win" : False})
            except:
                pass

        if x.hour == 18 and x.minute == 0 and x.second == 10:
            try:
                ersteZahl = random.randint(0, 10)
                await channelLottery.send(f"Die erste Zahl der heutigen Ziehung lautet {ersteZahl}")
                lottery.insert_one({"_id" : 9999999999, "ErsteZahl" : f"{ersteZahl}"})
            except:
                pass
        if x.hour == 18 and x.minute == 0 and x.second == 20:
            try:
                zweiteZahl = random.randint(0, 10)
                await channelLottery.send(f"Die zweite Zahl der heutigen Ziehung lautet {zweiteZahl}")
                lottery.insert_one({"_id" : 99999999999, "ZweiteZahl" : f"{zweiteZahl}"})
            except:
                pass

        if x.hour == 18 and x.minute == 0 and x.second == 30:
                dritteZahl = random.randint(0, 10)
                lotteryErsteZahl = lottery.find_one({"_id" : 9999999999})
                lotteryZweiteZahl = lottery.find_one({"_id" : 99999999999})
                zahlEins = lotteryErsteZahl["ErsteZahl"]
                zahlZwei = lotteryZweiteZahl["ZweiteZahl"]
                ergebnis = f"{zahlEins}-{zahlZwei}-{dritteZahl}"
                try:
                    lottery.insert_one({"_id" : 999999999999, "Ziehung" : f"{ergebnis}"})
                    lottery.insert_one({"_id" : 9999999999991, "DritteZahl" : f"{dritteZahl}"})
                except:
                    pass
                await channelLottery.send(f"Die dritte und letzte Zahl der heutigen Ziehung lautet {dritteZahl}\nDamit lauten die heutigen Gewinnzahlen: {ergebnis}. Die Ergebnisse werden jeden Moment verglichen.")
        
        if x.hour == 18 and x.minute == 0 and x.second == 40:
            for guild in self.client.guilds:
                for member in guild.members:
                    try:
                        x2 = lottery.find_one({"_id" : member.id})
                        numberOneFind = lottery.find_one({"_id" : 9999999999})
                        numberOne = numberOneFind["ErsteZahl"]
                        numberTwoFind = lottery.find_one({"_id" : 99999999999})
                        numberTwo = numberTwoFind["ZweiteZahl"]
                        numberThreeFind = lottery.find_one({"_id" : 9999999999991})
                        numberThree = numberThreeFind["DritteZahl"]
                        lotteryErgebnis = lottery.find_one({"_id" : 999999999999})
                        lotteryResult = lotteryErgebnis["Ziehung"]
                        if x2['Lotterie'] == lotteryResult:
                            try:
                                await channelLottery.send(f"{member.mention} hat alle Zahlen richtig und somit 200.000€ gewonnen. Gratulation :O")
                                generalinformations = economycollection.find_one({"_id" : "general"})
                                allplayerid = generalinformations["players"]
                                playerid = allplayerid[str(member.id)]
                                player = economycollection.find_one({"_id" : playerid})
                                addmoney(von = "Lotterie", zu = player["name"], playerid = playerid, menge = 200000, vonid = 0, zuid = playerid)
                                lottery.delete_many({})
                                await channelLottery.send("Das war die heutige Ausziehung. Glückwunsch an unsere/n Gewinner/in :)")
                            except:
                                pass
                        else:
                            if x2['ErsteZahl'] == numberOne:
                                generalinformations = economycollection.find_one({"_id" : "general"})
                                allplayerid = generalinformations["players"]
                                playerid = allplayerid[str(member.id)]
                                player = economycollection.find_one({"_id" : playerid})
                                addmoney(von = "Lotterie", zu = player["name"], playerid = playerid, menge = 2000, vonid = 0, zuid = playerid)
                                await channelLottery.send(f"{member.mention} hat die erste Zahl richtig und somit 2.000€ gewonnen")
                                try:
                                    lottery.update_one({"_id" : 1234, "win" : True})
                                except:
                                    pass
                            elif x2['ZweiteZahl'] == numberTwo:
                                generalinformations = economycollection.find_one({"_id" : "general"})
                                allplayerid = generalinformations["players"]
                                playerid = allplayerid[str(member.id)]
                                player = economycollection.find_one({"_id" : playerid})
                                addmoney(von = "Lotterie", zu = player["name"], playerid = playerid, menge = 2000, vonid = 0, zuid = playerid)
                                await channelLottery.send(f"{member.mention} hat die zweite Zahl richtig und somit 2.000€ gewonnen")
                                try:
                                    lottery.update_one({"_id" : 1234, "win" : True})
                                except:
                                    pass
                            elif x2['DritteZahl'] == numberThree:
                                generalinformations = economycollection.find_one({"_id" : "general"})
                                allplayerid = generalinformations["players"]
                                playerid = allplayerid[str(member.id)]
                                player = economycollection.find_one({"_id" : playerid})
                                addmoney(von = "Lotterie", zu = player["name"], playerid = playerid, menge = 2000, vonid = 0, zuid = playerid)
                                await channelLottery.send(f"{member.mention} hat die dritte Zahl richtig und somit 2.000€ gewonnen")
                                try:
                                    lottery.update_one({"_id" : 1234, "win" : True})
                                except:
                                    pass
                            
                            isThereAWin = lottery.find_one({"_id" : 1234})
                            maybeWin = isThereAWin["win"]

                            if maybeWin == False:
                                await channelLottery.send("Das war die heutige Ausziehung. Leider hat keiner gewonnen")
                                lottery.delete_many({})
                            else:
                                await channelLottery.send("Das war die heutige Ausziehung. Glückwunsch an unsere/n Gewinner/in")
                                lottery.delete_many({})
                    except:
                        if x2 == None:
                            pass
                        else:
                            raise
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.checkforLottery.start()


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
    client.add_cog(Economy(client))