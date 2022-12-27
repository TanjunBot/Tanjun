import discord
from discord.ext import commands, tasks
import json
from discord.ui import Button, View
from datetime import datetime
import random
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
import time
from pymongo import MongoClient

cluster = MongoClient("")

db = cluster["Main"]
economycollection = db["minigameSport"]


class miniGameSport(commands.Cog):

    def __init__(self, client):
        self.client = client



    @slash_command(name='startcareer', description='Starte deine Sportkarriere')
    async def startcareer(self, ctx):
        await ctx.defer()
        generalinformations = economycollection.find_one({"_id" : "general"})
        registerdplayers = generalinformations["registerdplayers"]
        if ctx.author.id in registerdplayers:
            myEmbed = discord.Embed(title = "Fehler!", description=f"Du bist bereits angemeldet!", color = 0xbd24e7)
            await ctx.respond(embed = myEmbed)
            return
        class MyModal(discord.ui.Modal):
            def __init__(self) -> None:
                super().__init__("Deine Sportkarriere")
                self.add_item(discord.ui.InputText(label = "Dein Name", placeholder = "Bitte gebe deinen Namen ein"))
                self.add_item(discord.ui.InputText(style = discord.InputTextStyle.long, label = "Deine Beschreibung", placeholder = "Erzähle etwas über dich"))

            async def callback(self, interaction : discord.Interaction):
                name = self.children[0].value
                Beschreibung = self.children[1].value
                schusskraft = random.randint(30, 56)
                stärke = random.randint(30, 56)
                geschwindigkeit = random.randint(30, 56)
                defensive = random.randint(30, 56)
                passen = random.randint(30, 56)
                gesamt = (int) ((schusskraft + stärke + geschwindigkeit + defensive + passen) / 5)
                
                playerid = generalinformations["nextid"]
                economycollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})
                economycollection.update_one({"_id" : "general"}, {"$addToSet" : {"registerdplayers" : ctx.author.id}})
                economycollection.update_one({"_id" : "general"}, {"$set" : {f"players.{ctx.author.id}" : playerid}})

                economycollection.insert_one({"_id" : playerid, "type" : "player", "name" : name, "beschreibung" : Beschreibung, "wert" : 100, "schusskraft": schusskraft, "geschwindigkeit": geschwindigkeit, "passen" : passen, "defensive" : defensive, "stärke" : stärke, "gesamt" : gesamt, "vertrag" : None, "verein" : None, "Kopfgeld" : 0, "lasttraining" : None, "lastGame" : None})

                myEmbed = discord.Embed(title = "Erfolgreich begonnen!", description=f"Du bist jetzt erfolgreich beim Sport system dabei! gehe doch gleich mal `/trainieren` und verbessere deine Stärken! ||oder du gehst dir einen Verein suchen (`/verein`) und schaust, was passiert 👀||", color = 0xbd24e7)
                await interaction.response.send_message(embed = myEmbed)
        
        modal = MyModal()
        await ctx.send_modal(modal)  

def setup(client):
    client.add_cog(miniGameSport(client))