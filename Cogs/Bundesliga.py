import requests
import discord
from discord.ext import commands

class Bundesliga(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(brief='Sehe die Aktuelle Bundesliga Tabelle', description='Mit diesen Befehl kannst du die Bundesliga Tabelle sehen.')
    async def bundesliga2(self, ctx, Jahr : int = 2021, Spieltag : int = 465416545456):
        await ctx.defer()
        async with ctx.typing():

            if Spieltag == 465416545456:
                tabelle = {}
                for tag in range(36):
                    r = requests.get(f'https://api.openligadb.de/getmatchdata/bl2/{Jahr}/{tag}')
                    r = r.json()
                    for match in r:
                        try:
                            try:
                                tabelle[match["team1"]["teamName"]]
                            except:
                                tabelle[match["team1"]["teamName"]] = {"goals" : 0, "points" : 0, "wins" : 0, "draws" : 0, "looses" : 0}

                            try:
                                tabelle[match["team2"]["teamName"]]
                            except:
                                tabelle[match["team2"]["teamName"]] = {"goals" : 0, "points" : 0, "wins" : 0, "draws" : 0, "looses" : 0}

                            tabelle[match["team1"]["teamName"]]["goals"] += match["matchResults"][0]["pointsTeam1"]
                            tabelle[match["team2"]["teamName"]]["goals"] += match["matchResults"][0]["pointsTeam2"]
                            if match["matchResults"][0]["pointsTeam1"] == match["matchResults"][0]["pointsTeam2"]:
                                tabelle[match["team1"]["teamName"]]["draws"] += 1
                                tabelle[match["team2"]["teamName"]]["draws"] += 1
                            if match["matchResults"][0]["pointsTeam1"] > match["matchResults"][0]["pointsTeam2"]: 
                                tabelle[match["team1"]["teamName"]]["wins"] += 1
                                tabelle[match["team2"]["teamName"]]["looses"] += 1
                            if match["matchResults"][0]["pointsTeam1"] < match["matchResults"][0]["pointsTeam2"]: 
                                tabelle[match["team2"]["teamName"]]["wins"] += 1
                                tabelle[match["team1"]["teamName"]]["looses"] += 1
                        except:
                            pass
                for team in tabelle:
                    punkte = 0
                    punkte += tabelle[team]["wins"] * 3
                    punkte += tabelle[team]["draws"]
                    tabelle[team]["points"] = punkte

                ranking = sorted(tabelle.items(),key=lambda x: x[1]['wins'],reverse=True)
                myEmbed = discord.Embed(title = "__**[LIVE] Sportzentrum**__",description=f"2. Bundesliga Tabelle {Jahr}",color=0x598ee7)
                myEmbed.set_footer(text=f"Sportzentrum Bundesliga ⬝ {ctx.author}")
                myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
                myEmbed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/933058702636875826/933323992008376320/R_2.png")




                counter = 1
                for rank in ranking:
                    myEmbed.add_field(name = f"{counter}. Platz: {rank[0]}", value = f"Siege: {tabelle[rank[0]]['wins']}\nGleichstand: {tabelle[rank[0]]['draws']}\nVerloren: {tabelle[rank[0]]['looses']}\nPunkte: {tabelle[rank[0]]['points']}\n\n", inline = False)
                    counter += 1
                await ctx.send(embed = myEmbed)
                return




            r = requests.get(f'https://api.openligadb.de/getmatchdata/bl2/{Jahr}/{Spieltag}')
            myEmbed = discord.Embed(title = "__**[LIVE] Sportzentrum**__",description=f"2. Bundesliga Spiele {Jahr} {Spieltag}. Spieltag",color=0x598ee7)
            myEmbed.set_footer(text=f"Sportzentrum Bundesliga ⬝ {ctx.author}")
            myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
            myEmbed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/933058702636875826/933323992008376320/R_2.png")
            r = r.json()
            counter = 1



            for match in r:
                try:
                    team1 = match["team1"]["teamName"]
                    team2 = match["team2"]["teamName"]
                    Ergebniss = {"team1" : match["matchResults"][0]["pointsTeam1"], "team2" : match["matchResults"][0]["pointsTeam2"]}
                    if Ergebniss["team1"] > Ergebniss["team2"]:
                        winner = f"{team1} hat gewonnen"
                    elif Ergebniss["team1"] < Ergebniss["team2"]:
                        winner = f"{team2} hat gewonnen"
                    else:
                        winner = "Unentschieden"

                    myEmbed.add_field(name = f"{counter}.Spiel: {team1} vs. {team2}", value = f"Tore {team1}: {Ergebniss['team1']}\nTore {team2}: {Ergebniss['team2']}\n**{winner}**\n\n", inline = False)
                except:
                    await ctx.send(embed = myEmbed)
                    return
                counter += 1

            await ctx.send(embed = myEmbed)


    @commands.command(brief='Sehe die Aktuelle Bundesliga Tabelle', description='Mit diesen Befehl kannst du die Bundesliga Tabelle sehen.')
    async def bundesliga3(self, ctx, Jahr : int = 2021, Spieltag : int = 465416545456):
        async with ctx.typing():

            if Spieltag == 465416545456:
                tabelle = {}
                for tag in range(36):
                    r = requests.get(f'https://api.openligadb.de/getmatchdata/bl3/{Jahr}/{tag}')
                    r = r.json()
                    for match in r:
                        try:
                            try:
                                tabelle[match["team1"]["teamName"]]
                            except:
                                tabelle[match["team1"]["teamName"]] = {"goals" : 0, "points" : 0, "wins" : 0, "draws" : 0, "looses" : 0}

                            try:
                                tabelle[match["team2"]["teamName"]]
                            except:
                                tabelle[match["team2"]["teamName"]] = {"goals" : 0, "points" : 0, "wins" : 0, "draws" : 0, "looses" : 0}

                            tabelle[match["team1"]["teamName"]]["goals"] += match["matchResults"][0]["pointsTeam1"]
                            tabelle[match["team2"]["teamName"]]["goals"] += match["matchResults"][0]["pointsTeam2"]
                            if match["matchResults"][0]["pointsTeam1"] == match["matchResults"][0]["pointsTeam2"]:
                                tabelle[match["team1"]["teamName"]]["draws"] += 1
                                tabelle[match["team2"]["teamName"]]["draws"] += 1
                            if match["matchResults"][0]["pointsTeam1"] > match["matchResults"][0]["pointsTeam2"]: 
                                tabelle[match["team1"]["teamName"]]["wins"] += 1
                                tabelle[match["team2"]["teamName"]]["looses"] += 1
                            if match["matchResults"][0]["pointsTeam1"] < match["matchResults"][0]["pointsTeam2"]: 
                                tabelle[match["team2"]["teamName"]]["wins"] += 1
                                tabelle[match["team1"]["teamName"]]["looses"] += 1
                        except:
                            pass
                for team in tabelle:
                    punkte = 0
                    punkte += tabelle[team]["wins"] * 3
                    punkte += tabelle[team]["draws"]
                    tabelle[team]["points"] = punkte

                ranking = sorted(tabelle.items(),key=lambda x: x[1]['wins'],reverse=True)
                myEmbed = discord.Embed(title = "__**[LIVE] Sportzentrum**__",description=f"3. Bundesliga Tabelle {Jahr}",color=0x598ee7)
                myEmbed.set_footer(text=f"Sportzentrum Bundesliga ⬝ {ctx.author}")
                myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
                myEmbed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/933058702636875826/933323992008376320/R_2.png")




                counter = 1
                for rank in ranking:
                    myEmbed.add_field(name = f"{counter}. Platz: {rank[0]}", value = f"Siege: {tabelle[rank[0]]['wins']}\nGleichstand: {tabelle[rank[0]]['draws']}\nVerloren: {tabelle[rank[0]]['looses']}\nPunkte: {tabelle[rank[0]]['points']}\n\n", inline = False)
                    counter += 1
                await ctx.send(embed = myEmbed)
                return




            r = requests.get(f'https://api.openligadb.de/getmatchdata/bl3/{Jahr}/{Spieltag}')
            myEmbed = discord.Embed(title = "__**[LIVE] Sportzentrum**__",description=f"3. Bundesliga Spiele {Jahr} {Spieltag}. Spieltag",color=0x598ee7)
            myEmbed.set_footer(text=f"Sportzentrum Bundesliga ⬝ {ctx.author}")
            myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
            myEmbed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/933058702636875826/933323992008376320/R_2.png")
            r = r.json()
            counter = 1



            for match in r:
                try:
                    team1 = match["team1"]["teamName"]
                    team2 = match["team2"]["teamName"]
                    Ergebniss = {"team1" : match["matchResults"][0]["pointsTeam1"], "team2" : match["matchResults"][0]["pointsTeam2"]}
                    if Ergebniss["team1"] > Ergebniss["team2"]:
                        winner = f"{team1} hat gewonnen"
                    elif Ergebniss["team1"] < Ergebniss["team2"]:
                        winner = f"{team2} hat gewonnen"
                    else:
                        winner = "Unentschieden"

                    myEmbed.add_field(name = f"{counter}.Spiel: {team1} vs. {team2}", value = f"Tore {team1}: {Ergebniss['team1']}\nTore {team2}: {Ergebniss['team2']}\n**{winner}**\n\n", inline = False)
                except:
                    await ctx.send(embed = myEmbed)
                    return
                counter += 1

            await ctx.send(embed = myEmbed)

    @commands.command(brief='Sehe die Aktuelle Bundesliga Tabelle', description='Mit diesen Befehl kannst du die Bundesliga Tabelle sehen.')
    async def bundesliga(self, ctx, Jahr : int = 2021, Spieltag : int = 465416545456):
        async with ctx.typing():

            if Spieltag == 465416545456:
                tabelle = {}
                for tag in range(36):
                    r = requests.get(f'https://api.openligadb.de/getmatchdata/bl1/{Jahr}/{tag}')
                    r = r.json()
                    for match in r:
                        try:
                            try:
                                tabelle[match["team1"]["teamName"]]
                            except:
                                tabelle[match["team1"]["teamName"]] = {"goals" : 0, "points" : 0, "wins" : 0, "draws" : 0, "looses" : 0}
    
                            try:
                                tabelle[match["team2"]["teamName"]]
                            except:
                                tabelle[match["team2"]["teamName"]] = {"goals" : 0, "points" : 0, "wins" : 0, "draws" : 0, "looses" : 0}
    
                            tabelle[match["team1"]["teamName"]]["goals"] += match["matchResults"][0]["pointsTeam1"]
                            tabelle[match["team2"]["teamName"]]["goals"] += match["matchResults"][0]["pointsTeam2"]
                            if match["matchResults"][0]["pointsTeam1"] == match["matchResults"][0]["pointsTeam2"]:
                                tabelle[match["team1"]["teamName"]]["draws"] += 1
                                tabelle[match["team2"]["teamName"]]["draws"] += 1
                            if match["matchResults"][0]["pointsTeam1"] > match["matchResults"][0]["pointsTeam2"]: 
                                tabelle[match["team1"]["teamName"]]["wins"] += 1
                                tabelle[match["team2"]["teamName"]]["looses"] += 1
                            if match["matchResults"][0]["pointsTeam1"] < match["matchResults"][0]["pointsTeam2"]: 
                                tabelle[match["team2"]["teamName"]]["wins"] += 1
                                tabelle[match["team1"]["teamName"]]["looses"] += 1
                        except:
                            pass
                for team in tabelle:
                    punkte = 0
                    punkte += tabelle[team]["wins"] * 3
                    punkte += tabelle[team]["draws"]
                    tabelle[team]["points"] = punkte
                    
                ranking = sorted(tabelle.items(),key=lambda x: x[1]['wins'],reverse=True)
                myEmbed = discord.Embed(title = "__**[LIVE] Sportzentrum**__",description=f"1. Bundesliga Tabelle {Jahr}",color=0x598ee7)
                myEmbed.set_footer(text=f"Sportzentrum Bundesliga ⬝ {ctx.author}")
                myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
                myEmbed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/933058702636875826/933323992008376320/R_2.png")
                
                guild = self.client.get_guild(850699358458347530)
    

                counter = 1
                for rank in ranking:
                    myEmbed.add_field(name = f"{counter}. Platz: | {rank[0]}", value = f"Siege: {tabelle[rank[0]]['wins']}\nGleichstand: {tabelle[rank[0]]['draws']}\nVerloren: {tabelle[rank[0]]['looses']}\nPunkte: {tabelle[rank[0]]['points']}\n\n", inline = False)
                    counter += 1
                await ctx.send(embed = myEmbed)
                return
    
                    
    
    
            r = requests.get(f'https://api.openligadb.de/getmatchdata/bl1/{Jahr}/{Spieltag}')
            myEmbed = discord.Embed(title = "__**[LIVE] Sportzentrum**__",description=f"1. Bundesliga Spiele {Jahr} {Spieltag}. Spieltag",color=0x598ee7)
            myEmbed.set_footer(text=f"Sportzentrum Bundesliga ⬝ {ctx.author}")
            myEmbed.set_image(url = "https://cdn.discordapp.com/attachments/933023626800803840/933318387881365504/31D84AFB-A150-4A40-81CF-930D30B9E547.gif")
            myEmbed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/933058702636875826/933323992008376320/R_2.png")
            r = r.json()
            counter = 1
    
        
    
            for match in r:
                try:
                    team1 = match["team1"]["teamName"]
                    team2 = match["team2"]["teamName"]
                    Ergebniss = {"team1" : match["matchResults"][0]["pointsTeam1"], "team2" : match["matchResults"][0]["pointsTeam2"]}
                    if Ergebniss["team1"] > Ergebniss["team2"]:
                        winner = f"{team1} hat gewonnen"
                    elif Ergebniss["team1"] < Ergebniss["team2"]:
                        winner = f"{team2} hat gewonnen"
                    else:
                        winner = "Unentschieden"
    
                    myEmbed.add_field(name = f"{counter}.Spiel: {team1} vs. {team2}", value = f"Tore {team1}: {Ergebniss['team1']}\nTore {team2}: {Ergebniss['team2']}\n**{winner}**\n\n", inline = False)
                except:
                    await ctx.send(embed = myEmbed)
                    return
                counter += 1
    
            await ctx.send(embed = myEmbed)


def setup(client):
    client.add_cog(Bundesliga(client))