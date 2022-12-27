import discord
from discord.ext import commands, tasks
import json
import asyncio
import numerize 



client = commands.Bot(command_prefix="wummmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm.", intents=discord.Intents.all())


@client.event
async def on_ready():
    updatestats.start()
    print("Main Commands Loaded")




@tasks.loop(seconds=10)
async def updatestats():
        with open('idlewumpus.json', 'r') as fp:
            idlepokécollection = json.load(fp)
        print(idlepokécollection)
        for player in idlepokécollection:
            try:
                p = idlepokécollection[str(player)]
                print(p)
                coins = p["coins"]
                guild = client.get_guild(int(p["server"]))
                thread = guild.get_channel_or_thread(int(p["threadid"]))
                print(coins)

                try:
                    enton = p["enton"]
                except:
                    enton = False

                try:
                    Evoli = p["Evoli"]
                except:
                    Evoli = False

                try:
                    Vulpix = p["Vulpix"]
                except:
                    Vulpix = False

                try:
                    Fukano = p["Fukano"]
                except:
                    Fukano = False

                try:
                    Abra = p["Abra"]
                except:
                    Abra = False

                try:
                    Ponita = p["Ponita"]
                except:
                    Ponita = False

                try:
                    Dodu = p["Dodu"]
                except:
                    Dodu = False

                try:
                    Natu = p["Natu"]
                except:
                    Natu = False

                try:
                    Sandan = p["Sandan"]
                except:
                    Sandan = False

                try:
                    Dratini = p["Dratini"]
                except:
                    Dratini = False

                try:
                    Mampfaxo = p["Mampfaxo"]
                except:
                    Mampfaxo = False

                try:
                    Hunduster = p["Hunduster"]
                except:
                    Hunduster = False

                try:
                    Hydropi = p["Hydropi"]
                except:
                    Hydropi = False

                try:
                    Zigzachs = p["Zigzachs"]
                except:
                    Zigzachs = False

                try:
                    Azurill = p["Azurill"]
                except:
                    Azurill = False

                try:
                    Kindwurm = p["Kindwurm"]
                except:
                    Kindwurm = False

                try:
                    Plinfa = p["Plinfa"]
                except:
                    Plinfa = False

                try:
                    Sheinux = p["Sheinux"]
                except:
                    Sheinux = False

                try:
                    Mobai = p["Mobai"]
                except:
                    Mobai = False

                try:
                    Riolu = p["Riolu"]
                except:
                    Riolu = False

                try:
                    Zorua = p["Zorua"]
                except:
                    Zorua = False

                try:
                    Bauz = p["Bauz"]
                except:
                    Bauz = False

                try:
                    Flamiau = p["Flamiau"]
                except:
                    Flamiau = False

                try:
                    Wuffels = p["Wuffels"]
                except:
                    Wuffels = False

                try:
                    Cosmog = p["Cosmog"]
                except:
                    Cosmog = False


                if coins >= 1000000000 and Evoli == False:
                    idlepokécollection[str(player)]["Evoli"] =  {"level" : 0, "cps" : 10, "lvl" : 1, "kostennextlevel" : 15, "kostenmultiplyer" : 2, "cpsmultiplyer" : 2}

                if coins >= 100000000000000000000 and Vulpix == False:
                    idlepokécollection[str(player)]["Vulpix"] =  {"level" : 0, "cps" : 75, "lvl" : 1, "kostennextlevel" : 100, "kostenmultiplyer" : 3, "cpsmultiplyer" : 3}

                if coins >= 100000000000000000000000 and Fukano == False:
                    idlepokécollection[str(player)]["Fukano"] =  {"level" : 0, "cps" : 100, "lvl" : 1, "kostennextlevel" : 2500, "kostenmultiplyer" : 5, "cpsmultiplyer" : 4}

                if coins >= 1000000000000000000000000000000000000000000000000 and Abra == False:
                    idlepokécollection[str(player)]["Abra"] =  {"level" : 0, "cps" : 2500, "lvl" : 1, "kostennextlevel" : 7000, "kostenmultiplyer" : 6, "cpsmultiplyer" : 5}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000 and Ponita == False:
                    idlepokécollection[str(player)]["Ponita"] =  {"level" : 0, "cps" : 10000, "lvl" : 1, "kostennextlevel" : 20000, "kostenmultiplyer" : 7, "cpsmultiplyer" : 8}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Dodu == False:
                    idlepokécollection[str(player)]["Dodu"] =  {"level" : 0, "cps" : 25000, "lvl" : 1, "kostennextlevel" : 45000, "kostenmultiplyer" : 8, "cpsmultiplyer" : 9}

                if coins >= 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Natu == False:
                    idlepokécollection[str(player)]["Natu"] =  {"level" : 0, "cps" : 45000, "lvl" : 1, "kostennextlevel" : 450000, "kostenmultiplyer" : 9, "cpsmultiplyer" : 10}

                if coins >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Sandan == False:
                    idlepokécollection[str(player)]["Sandan"] =  {"level" : 0, "cps" : 100000, "lvl" : 1, "kostennextlevel" : 1000000, "kostenmultiplyer" : 10, "cpsmultiplyer" : 12}

                if coins >= 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Dratini == False:
                    idlepokécollection[str(player)]["Dratini"] =  {"level" : 0, "cps" : 4500000, "lvl" : 1, "kostennextlevel" : 10000000, "kostenmultiplyer" : 11, "cpsmultiplyer" : 17}

                if coins >= 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Mampfaxo == False:
                    idlepokécollection[str(player)]["Mampfaxo"] =  {"level" : 0, "cps" : 9000000, "lvl" : 1, "kostennextlevel" : 50000000, "kostenmultiplyer" : 10, "cpsmultiplyer" : 15}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Hunduster == False:
                    idlepokécollection[str(player)]["Hunduster"] =  {"level" : 0, "cps" : 14000000, "lvl" : 1, "kostennextlevel" : 90000000, "kostenmultiplyer" : 6, "cpsmultiplyer" : 8}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Hydropi == False:
                    idlepokécollection[str(player)]["Hydropi"] =  {"level" : 0, "cps" : 29000000, "lvl" : 1, "kostennextlevel" : 150000000, "kostenmultiplyer" : 8, "cpsmultiplyer" : 9}

                if coins >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Zigzachs == False:
                    idlepokécollection[str(player)]["Zigzachs"] =  {"level" : 0, "cps" : 50000000, "lvl" : 1, "kostennextlevel" : 500000000, "kostenmultiplyer" : 9, "cpsmultiplyer" : 7}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Azurill == False:
                    idlepokécollection[str(player)]["Azurill"] =  {"level" : 0, "cps" : 90000000, "lvl" : 1, "kostennextlevel" : 1000000000, "kostenmultiplyer" : 7, "cpsmultiplyer" : 5}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Kindwurm == False:
                    idlepokécollection[str(player)]["Kindwurm"] =  {"level" : 0, "cps" : 250000000, "lvl" : 1, "kostennextlevel" : 4000000000, "kostenmultiplyer" : 12, "cpsmultiplyer" : 15}

                if coins >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Plinfa == False:
                    idlepokécollection[str(player)]["Plinfa"] =  {"level" : 0, "cps" : 800000000, "lvl" : 1, "kostennextlevel" : 27000000000, "kostenmultiplyer" : 15, "cpsmultiplyer" : 20}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Sheinux == False:
                    idlepokécollection[str(player)]["Sheinux"] =  {"level" : 0, "cps" : 2900000000, "lvl" : 1, "kostennextlevel" : 150000000000, "kostenmultiplyer" : 8, "cpsmultiplyer" : 12}

                if coins >= 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Mobai == False:
                    idlepokécollection[str(player)]["Mobai"] =  {"level" : 0, "cps" : 8700000000, "lvl" : 1, "kostennextlevel" : 5000000000000, "kostenmultiplyer" : 7, "cpsmultiplyer" : 8}

                if coins >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Riolu == False:
                    idlepokécollection[str(player)]["Riolu"] =  {"level" : 0, "cps" : 10000000000, "lvl" : 1, "kostennextlevel" : 10000000000000, "kostenmultiplyer" : 3, "cpsmultiplyer" : 5}

                if coins >= 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Zorua == False:
                    idlepokécollection[str(player)]["Zorua"] =  {"level" : 0, "cps" : 300000000000, "lvl" : 1, "kostennextlevel" : 80000000000000, "kostenmultiplyer" : 2, "cpsmultiplyer" : 6}

                if coins >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Bauz == False:
                    idlepokécollection[str(player)]["Bauz"] =  {"level" : 0, "cps" : 500000000000, "lvl" : 1, "kostennextlevel" : 80000000000000000, "kostenmultiplyer" : 8, "cpsmultiplyer" : 10}

                if coins >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Flamiau == False:
                    idlepokécollection[str(player)]["Flamiau"] =  {"level" : 0, "cps" : 7000000000000, "lvl" : 1, "kostennextlevel" : 8000000000000000000, "kostenmultiplyer" : 20, "cpsmultiplyer" : 30}

                if coins >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Wuffels == False:
                    idlepokécollection[str(player)]["Wuffels"] =  {"level" : 0, "cps" : 700000000000000, "lvl" : 1, "kostennextlevel" : 200000000000000000000, "kostenmultiplyer" : 27, "cpsmultiplyer" : 50}

                if coins >= 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and Cosmog == False:
                    idlepokécollection[str(player)]["Cosmog"] =  {"level" : 0, "cps" : 10000000000000000000000000000, "lvl" : 1, "kostennextlevel" : 200000000000000000000000000, "kostenmultiplyer" : 35, "cpsmultiplyer" : 100}


                if enton != False:
                    if enton["level"] >= 100 and enton["lvl"] == 1:
                        idlepokécollection[str(player)]["enton"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Enton` hat sich zu `Entoron` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)


                if Evoli != False:
                    try:
                        mentiones = idlepokécollection[str(player)]["Evoli"]["mentioned"]
                    except:
                        mentiones = False
                    if Evoli["level"] >= 100 and Evoli["lvl"] == 1 and mentiones == False:
                        class Dropdown(discord.ui.Select):
                            def __init__(self):
                                options = [
                                    discord.SelectOption(label = "Aquana", value="2"),
                                    discord.SelectOption(label = "Blitza", value="3"),
                                    discord.SelectOption(label = "Flamara", value="4"),
                                    discord.SelectOption(label = "Psiana", value="5"),
                                    discord.SelectOption(label = "Nachtara", value="6"),
                                    discord.SelectOption(label = "Folipurba", value="7"),
                                    discord.SelectOption(label = "Glaziola", value="8"),
                                    discord.SelectOption(label = "Feelinara", value="9")
                                ]

                                super().__init__(
                                    placeholder="Wähle die Entwicklung aus",
                                    min_values=1,
                                    max_values=1,
                                    options=options
                                )

                            async def callback(select, interaction : discord.Interaction):

                                entwicklung = int(select.values[0])

                                idlepokécollection[str(interaction.user.id)]["Evoli"]["lvl"] = entwicklung

                                await interaction.response.send_message("Dein Poké wurde hat sich erfolgreich Entwickelt!", ephemeral=True)

                        class DropdownView(discord.ui.View):
                            def __init__(self):
                                super().__init__()


                                self.add_item(Dropdown())

                        view = DropdownView()

                        await thread.send(content = f"Dein `Evoli` kann sich entwickeln! In was soll es sich entwickeln?", view = view)

                        idlepokécollection[str(player)]["Evoli"]["mentioned"] = True

                if Vulpix != False:
                    if Vulpix["level"] >= 100 and Vulpix["lvl"] == 1:
                        idlepokécollection[str(player)]["Vulpix"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Vulpix` hat sich zu `Vulnona` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Fukano != False:
                    if Fukano["level"] >= 100 and Fukano["lvl"] == 1:
                        idlepokécollection[str(player)]["Fukano"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Fukano` hat sich zu `Arkani` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Abra != False:
                    if Abra["level"] >= 100 and Abra["lvl"] == 1:
                        idlepokécollection[str(player)]["Abra"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Abra` hat sich zu `Kadabra` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Abra["level"] >= 200 and Abra["lvl"] == 2:
                        idlepokécollection[str(player)]["Abra"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Kadabra` hat sich zu `Simsala` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Ponita != False:
                    if Ponita["level"] >= 100 and Ponita["lvl"] == 1:
                        idlepokécollection[str(player)]["Ponita"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Ponita` hat sich zu `Gallopa` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Dodu != False:
                    if Dodu["level"] >= 100 and Dodu["lvl"] == 1:
                        idlepokécollection[str(player)]["Dodu"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Dodu` hat sich zu `Dodri` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Natu != False:
                    if Natu["level"] >= 100 and Natu["lvl"] == 1:
                        idlepokécollection[str(player)]["Natu"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Natu` hat sich zu `Xatu` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Sandan != False:
                    if Sandan["level"] >= 100 and Sandan["lvl"] == 1:
                        idlepokécollection[str(player)]["Sandan"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Sandan` hat sich zu `Sandamer` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Dratini != False:
                    if Dratini["level"] >= 100 and Dratini["lvl"] == 1:
                        idlepokécollection[str(player)]["Dratini"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Dratini` hat sich zu `Dragonir` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Dratini["level"] >= 200 and Dratini["lvl"] == 2:
                        idlepokécollection[str(player)]["Dratini"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Dragonir` hat sich zu `Dragoran` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Mampfaxo != False:
                    if Mampfaxo["level"] >= 100 and Mampfaxo["lvl"] == 1:
                        idlepokécollection[str(player)]["Mampfaxo"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Mampfaxo` hat sich zu `Relaxo` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Hunduster != False:
                    if Hunduster["level"] >= 100 and Hunduster["lvl"] == 1:
                        idlepokécollection[str(player)]["Hunduster"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Hunduster` hat sich zu `Hundemon` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Hydropi != False:
                    if Hydropi["level"] >= 100 and Hydropi["lvl"] == 1:
                        idlepokécollection[str(player)]["Hydropi"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Hydropi` hat sich zu `Moorabbel` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Hydropi["level"] >= 100 and Hydropi["lvl"] == 1:
                        idlepokécollection[str(player)]["Hydropi"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Moorabbel` hat sich zu `Sumpex` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Zigzachs != False:
                    if Zigzachs["level"] >= 100 and Zigzachs["lvl"] == 1:
                        idlepokécollection[str(player)]["Zigzachs"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Zigzachs` hat sich zu `Geradaks` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Azurill != False:
                    if Azurill["level"] >= 100 and Azurill["lvl"] == 1:
                        idlepokécollection[str(player)]["Azurill"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Azurill` hat sich zu `Marill` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Azurill["level"] >= 200 and Azurill["lvl"] == 2:
                        idlepokécollection[str(player)]["Azurill"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Marill` hat sich zu `Azumarill` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Kindwurm != False:
                    if Kindwurm["level"] >= 100 and Kindwurm["lvl"] == 1:
                        idlepokécollection[str(player)]["Kindwurm"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Kindwurm` hat sich zu `Draschel` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Kindwurm["level"] >= 200 and Kindwurm["lvl"] == 2:
                        idlepokécollection[str(player)]["Kindwurm"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Draschel` hat sich zu `Brutalanda` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Plinfa != False:
                    if Plinfa["level"] >= 100 and Plinfa["lvl"] == 1:
                        idlepokécollection[str(player)]["Plinfa"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Plinfa` hat sich zu `Pliprin` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Plinfa["level"] >= 200 and Plinfa["lvl"] == 2:
                        idlepokécollection[str(player)]["Plinfa"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Pliprin` hat sich zu `Impoleon` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Sheinux != False:
                    if Sheinux["level"] >= 100 and Sheinux["lvl"] == 1:
                        idlepokécollection[str(player)]["Sheinux"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Sheinux` hat sich zu `Luxio` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Sheinux["level"] >= 200 and Sheinux["lvl"] == 2:
                        idlepokécollection[str(player)]["Sheinux"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Luxio` hat sich zu `Luxtra` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Mobai != False:
                    if Mobai["level"] >= 100 and Mobai["lvl"] == 1:
                        idlepokécollection[str(player)]["Mobai"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Mobai` hat sich zu `Mogelbaum` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Riolu != False:
                    if Riolu["level"] >= 100 and Riolu["lvl"] == 1:
                        idlepokécollection[str(player)]["Riolu"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Riolu` hat sich zu `Lucario` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Zorua != False:
                    if Zorua["level"] >= 100 and Zorua["lvl"] == 1:
                        idlepokécollection[str(player)]["Zorua"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Zorua` hat sich zu `Zoroark` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Bauz != False:
                    if Bauz["level"] >= 100 and Bauz["lvl"] == 1:
                        idlepokécollection[str(player)]["Bauz"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Bauz` hat sich zu `Arboretoss` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Bauz["level"] >= 200 and Bauz["lvl"] == 2:
                        idlepokécollection[str(player)]["Bauz"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Arboretoss` hat sich zu `Silvarro` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Flamiau != False:
                    if Flamiau["level"] >= 100 and Flamiau["lvl"] == 1:
                        idlepokécollection[str(player)]["Flamiau"]["lvl"] = 2
                        await thread.send(content = "WOW! Dein `Flamiau` hat sich zu `Miezunder` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)
                    if Flamiau["level"] >= 200 and Flamiau["lvl"] == 2:
                        idlepokécollection[str(player)]["Flamiau"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Miezunder` hat sich zu `Fuegro` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Wuffels != False:
                    if Wuffels["level"] >= 200 and Wuffels["lvl"] == 1:
                        idlepokécollection[str(player)]["Wuffels"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Wuffels` hat sich zu `Wolwerock` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                if Cosmog != False:
                    if Cosmog["level"] >= 100 and Cosmog["lvl"] == 1:
                        idlepokécollection[str(player)]["Cosmog"]["lvl"] = 3
                        await thread.send(content = "WOW! Dein `Cosmog` hat sich zu `Cosmovum` entwickelt <a:P_pikaOMG:950001061593235469>", delete_after = 60)

                    try:
                        mentiones = idlepokécollection[str(player)]["Cosmog"]["mentioned"]
                    except:
                        mentiones = False

                    if Cosmog["level"] >= 200 and Cosmog["lvl"] == 1 and mentiones == False:
                        class Dropdown(discord.ui.Select):
                            def __init__(self):
                                options = [
                                    discord.SelectOption(label = "Solgaleo", value="3"),
                                    discord.SelectOption(label = "Lunala", value="4"),
                                ]

                                super().__init__(
                                    placeholder="Wähle die Entwicklung aus",
                                    min_values=1,
                                    max_values=1,
                                    options=options
                                )

                            async def callback(select, interaction : discord.Interaction):

                                entwicklung = int(select.values[0])

                                idlepokécollection[str(interaction.user.id)]["Cosmog"] = entwicklung

                                await interaction.response.send_message("Dein Poké wurde hat sich erfolgreich Entwickelt!", ephemeral=True)

                        class DropdownView(discord.ui.View):
                            def __init__(self):
                                super().__init__()


                                self.add_item(Dropdown())

                        view = DropdownView()

                        await thread.send(content = f"Dein `Cosmovum` kann sich entwickeln! In was soll es sich entwickeln?", view = view)

                        idlepokécollection[str(player)]["Cosmog"]["mentioned"] = True

                message = f"`Deine Pokécoins: {numerize.numerize(coins)}`\n\n"

                if enton != False:
                    if enton["lvl"] == 1:
                        message += f"`Enton`\n`Level: {numerize.numerize(enton['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(enton['cps'])}`\n\n"
                    elif enton["lvl"] == 2:
                        message += f"`Entoron`\n`Level: {numerize.numerize(enton['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(enton['cps'])}`\n\n"

                if Evoli != False:
                    if Evoli["lvl"] == 1:
                        message += f"`Evoli`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 2:
                        message += f"`Aquana`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 3:
                        message += f"`Blitza`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 4:
                        message += f"`Flamara`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 5:
                        message += f"`Psiana`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 6:
                        message += f"`Nachtara`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 7:
                        message += f"`Folipurba`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 8:
                        message += f"`Glaziola`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"
                    elif Evoli["lvl"] == 9:
                        message += f"`Feelinara`\n`Level: {numerize.numerize(Evoli['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Evoli['cps'])}`\n\n"

                if Vulpix != False:
                    if Vulpix["lvl"] == 1:
                        message += f"`Vulpix`\n`Level: {numerize.numerize(Vulpix['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Vulpix['cps'])}`\n\n"
                    elif Vulpix["lvl"] == 2:
                        message += f"`Vulnona`\n`Level: {numerize.numerize(Vulpix['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Vulpix['cps'])}`\n\n"

                if Fukano != False:
                    if Fukano["lvl"] == 1:
                        message += f"`Fukano`\n`Level: {numerize.numerize(Fukano['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Fukano['cps'])}`\n\n"
                    elif Fukano["lvl"] == 2:
                        message += f"`Arkani`\n`Level: {numerize.numerize(Fukano['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Fukano['cps'])}`\n\n"

                if Abra != False:
                    if Abra["lvl"] == 1:
                        message += f"`Abra`\n`Level: {numerize.numerize(Abra['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Abra['cps'])}`\n\n"
                    elif Abra["lvl"] == 2:
                        message += f"`Kadabra`\n`Level: {numerize.numerize(Abra['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Abra['cps'])}`\n\n"
                    elif Abra["lvl"] == 3:
                        message += f"`Simsala`\n`Level: {numerize.numerize(Abra['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Abra['cps'])}`\n\n"

                if Ponita != False:
                    if Ponita["lvl"] == 1:
                        message += f"`Ponita`\n`Level: {numerize.numerize(Ponita['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Ponita['cps'])}`\n\n"
                    elif Ponita["lvl"] == 2:
                        message += f"`Gallopa`\n`Level: {numerize.numerize(Ponita['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Ponita['cps'])}`\n\n"

                if Dodu != False:
                    if Dodu["lvl"] == 1:
                        message += f"`Dodu`\n`Level: {numerize.numerize(Dodu['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Dodu['cps'])}`\n\n"
                    elif Dodu["lvl"] == 2:
                        message += f"`Dodri`\n`Level: {numerize.numerize(Dodu['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Dodu['cps'])}`\n\n"

                if Natu != False:
                    if Natu["lvl"] == 1:
                        message += f"`Natu`\n`Level: {numerize.numerize(Natu['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Natu['cps'])}`\n\n"
                    elif Natu["lvl"] == 2:
                        message += f"`Xatu`\n`Level: {numerize.numerize(Natu['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Natu['cps'])}`\n\n"

                if Sandan != False:
                    if Sandan["lvl"] == 1:
                        message += f"`Sandan`\n`Level: {numerize.numerize(Sandan['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Sandan['cps'])}`\n\n"
                    elif Sandan["lvl"] == 2:
                        message += f"`Sandamer`\n`Level: {numerize.numerize(Sandan['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Sandan['cps'])}`\n\n"

                if Dratini != False:
                    if Dratini["lvl"] == 1:
                        message += f"`Dratini`\n`Level: {numerize.numerize(Dratini['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Dratini['cps'])}`\n\n"
                    elif Dratini["lvl"] == 2:
                        message += f"`Dragonir`\n`Level: {numerize.numerize(Dratini['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Dratini['cps'])}`\n\n"
                    elif Dratini["lvl"] == 3:
                        message += f"`Dragoran`\n`Level: {numerize.numerize(Dratini['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Dratini['cps'])}`\n\n"

                if Mampfaxo != False:
                    if Mampfaxo["lvl"] == 1:
                        message += f"`Mampfaxo`\n`Level: {numerize.numerize(Mampfaxo['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Mampfaxo['cps'])}`\n\n"
                    elif Mampfaxo["lvl"] == 2:
                        message += f"`Relaxo`\n`Level: {numerize.numerize(Mampfaxo['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Mampfaxo['cps'])}`\n\n"

                if Hunduster != False:
                    if Hunduster["lvl"] == 1:
                        message += f"`Hunduster`\n`Level: {numerize.numerize(Hunduster['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Hunduster['cps'])}`\n\n"
                    elif Hunduster["lvl"] == 2:
                        message += f"`Hundemon`\n`Level: {numerize.numerize(Hunduster['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Hunduster['cps'])}`\n\n"

                if Hydropi != False:
                    if Hydropi["lvl"] == 1:
                        message += f"`Hydropi`\n`Level: {numerize.numerize(Hydropi['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Hydropi['cps'])}`\n\n"
                    elif Hydropi["lvl"] == 2:
                        message += f"`Moorabbel`\n`Level: {numerize.numerize(Hydropi['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Hydropi['cps'])}`\n\n"
                    elif Hydropi["lvl"] == 3:
                        message += f"`Sumpex`\n`Level: {numerize.numerize(Hydropi['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Hydropi['cps'])}`\n\n"

                if Zigzachs != False:
                    if Zigzachs["lvl"] == 1:
                        message += f"`Zigzachs`\n`Level: {numerize.numerize(Zigzachs['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Zigzachs['cps'])}`\n\n"
                    elif Zigzachs["lvl"] == 2:
                        message += f"`Geradaks`\n`Level: {numerize.numerize(Zigzachs['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Zigzachs['cps'])}`\n\n"

                if Azurill != False:
                    if Azurill["lvl"] == 1:
                        message += f"`Azurill`\n`Level: {numerize.numerize(Azurill['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Azurill['cps'])}`\n\n"
                    elif Azurill["lvl"] == 2:
                        message += f"`Marill`\n`Level: {numerize.numerize(Azurill['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Azurill['cps'])}`\n\n"
                    elif Azurill["lvl"] == 3:
                        message += f"`Azumarill`\n`Level: {numerize.numerize(Azurill['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Azurill['cps'])}`\n\n"

                if Kindwurm != False:
                    if Kindwurm["lvl"] == 1:
                        message += f"`Kindwurm`\n`Level: {numerize.numerize(Kindwurm['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Kindwurm['cps'])}`\n\n"
                    elif Kindwurm["lvl"] == 2:
                        message += f"`Draschel`\n`Level: {numerize.numerize(Kindwurm['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Kindwurm['cps'])}`\n\n"
                    elif Kindwurm["lvl"] == 2:
                        message += f"`Brutalanda`\n`Level: {numerize.numerize(Kindwurm['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Kindwurm['cps'])}`\n\n"

                if Plinfa != False:
                    if Plinfa["lvl"] == 1:
                        message += f"`Plinfa`\n`Level: {numerize.numerize(Plinfa['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Plinfa['cps'])}`\n\n"
                    elif Plinfa["lvl"] == 2:
                        message += f"`Pliprin`\n`Level: {numerize.numerize(Plinfa['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Plinfa['cps'])}`\n\n"
                    elif Plinfa["lvl"] == 2:
                        message += f"`Impoleon`\n`Level: {numerize.numerize(Plinfa['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Plinfa['cps'])}`\n\n"

                if Sheinux != False:
                    if Sheinux["lvl"] == 1:
                        message += f"`Sheinux`\n`Level: {numerize.numerize(Sheinux['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Sheinux['cps'])}`\n\n"
                    elif Sheinux["lvl"] == 2:
                        message += f"`Luxio`\n`Level: {numerize.numerize(Sheinux['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Sheinux['cps'])}`\n\n"
                    elif Sheinux["lvl"] == 3:
                        message += f"`Luxtra`\n`Level: {numerize.numerize(Sheinux['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Sheinux['cps'])}`\n\n"

                if Mobai != False:
                    if Mobai["lvl"] == 1:
                        message += f"`Mobai`\n`Level: {numerize.numerize(Mobai['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Mobai['cps'])}`\n\n"
                    elif Mobai["lvl"] == 2:
                        message += f"`Mogelbaum`\n`Level: {numerize.numerize(Mobai['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Mobai['cps'])}`\n\n"

                if Riolu != False:
                    if Riolu["lvl"] == 1:
                        message += f"`Riolu`\n`Level: {numerize.numerize(Riolu['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Riolu['cps'])}`\n\n"
                    elif Riolu["lvl"] == 2:
                        message += f"`Lucario`\n`Level: {numerize.numerize(Riolu['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Riolu['cps'])}`\n\n"

                if Zorua != False:
                    if Zorua["lvl"] == 1:
                        message += f"`Zorua`\n`Level: {numerize.numerize(Zorua['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Zorua['cps'])}`\n\n"
                    elif Zorua["lvl"] == 2:
                        message += f"`Zoroark`\n`Level: {numerize.numerize(Zorua['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Zorua['cps'])}`\n\n"

                if Bauz != False:
                    if Bauz["lvl"] == 1:
                        message += f"`Bauz`\n`Level: {numerize.numerize(Bauz['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Bauz['cps'])}`\n\n"
                    elif Bauz["lvl"] == 2:
                        message += f"`Arboretoss`\n`Level: {numerize.numerize(Bauz['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Bauz['cps'])}`\n\n"
                    elif Bauz["lvl"] == 3:
                        message += f"`Silvarro`\n`Level: {numerize.numerize(Bauz['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Bauz['cps'])}`\n\n"

                if Flamiau != False:
                    if Flamiau["lvl"] == 1:
                        message += f"`Flamiau`\n`Level: {numerize.numerize(Flamiau['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Flamiau['cps'])}`\n\n"
                    elif Flamiau["lvl"] == 2:
                        message += f"`Miezunder`\n`Level: {numerize.numerize(Flamiau['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Flamiau['cps'])}`\n\n"
                    elif Flamiau["lvl"] == 3:
                        message += f"`Fuegro`\n`Level: {numerize.numerize(Flamiau['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Flamiau['cps'])}`\n\n"

                if Wuffels != False:
                    if Wuffels["lvl"] == 1:
                        message += f"`Wuffels`\n`Level: {numerize.numerize(Wuffels['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Wuffels['cps'])}`\n\n"
                    elif Wuffels["lvl"] == 2:
                        message += f"`Wolwerock`\n`Level: {numerize.numerize(Wuffels['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Wuffels['cps'])}`\n\n"

                if Cosmog != False:
                    if Cosmog["lvl"] == 1:
                        message += f"`Cosmog`\n`Level: {numerize.numerize(Cosmog['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Cosmog['cps'])}`\n\n"
                    elif Cosmog["lvl"] == 2:
                        message += f"`Cosmovum`\n`Level: {numerize.numerize(Cosmog['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Cosmog['cps'])}`\n\n"
                    elif Cosmog["lvl"] == 3:
                        message += f"`Solgaleo`\n`Level: {numerize.numerize(Cosmog['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Cosmog['cps'])}`\n\n"
                    elif Cosmog["lvl"] == 4:
                        message += f"`Lunala`\n`Level: {numerize.numerize(Cosmog['level'])}`\n`Pokécoins pro Sekunde: {numerize.numerize(Cosmog['cps'])}`\n\n"


                message += "\nBenutze den /upgrade Befehl um eines deiner pokés zu upgraden!"
                myEmbed = discord.Embed(title = f"Idle Poké!",description=message,color=0xbd24e7)
                message = await thread.fetch_message(int(p["messageid"]))
                await message.edit(embed = myEmbed)
            except:
                pass
        


client.run("ODg1OTg0MTM5MzE1MTIyMjA2.YTu_Bw.KDIRWPRMjo2bZPvMgQZqesmFAgk")
