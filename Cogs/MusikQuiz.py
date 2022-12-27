import discord
from discord.ext import commands, tasks
import os
import random
import asyncio
import youtube_dl
import json
from pathlib import Path

data_folder = Path("Jsons/")
file_to_open = data_folder / "MusikQuiz.json"
with open(file_to_open, "r") as config:
    musicbot = json.load(config)


class MusikQuiz(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        self.saveecon.start()
        self.is_still_playing.start()

    @tasks.loop(seconds=5)
    async def saveecon(self):
        data_folder = Path("Jsons/")
        file_to_open = data_folder / "MusikQuiz.json"
        with open(file_to_open, 'w') as fp:
            json.dump(musicbot, fp,  indent=4)

    @tasks.loop(seconds=2)
    async def is_still_playing(self):
        global mquiz
        for guild in self.client.guilds:
            try:
                if musicbot[str(guild.id)]["current"]["Is_Started"] == True:
                    voice = discord.utils.get(self.client.voice_clients, guild=guild)
                    if not voice.is_playing():
                        await asyncio.sleep(3)
                        if not voice.is_playing():
                            channel = self.client.get_channel(musicbot[str(guild.id)]["current"]["channelid"])
                            await channel.send("Leider hat niemand das Lied erraten :c Wir gehen mal lieber schnell zum Nächsten Lied!")
                            vcid = musicbot[str(guild.id)]["current"]["VC_id"]
                            song_there = os.path.isfile()
                            song_there = os.path.isfile(f"mq{guild.id}.webm")
                            if song_there:
                                os.remove(f"mq{guild.id}.webm")
                            voiceChannel = discord.utils.get(guild.voice_channels, id=vcid)
                            try:
                                await voiceChannel.connect()
                            except:
                                i = 1
                            lied = random.choice(musicbot["Songs"])
                            musicbot[str(guild.id)]["current"]["Richtiger_name"] = lied["name"]
                            musicbot[str(guild.id)]["current"]["Richtiger_Interpret"] = lied["interpret"]
                            musicbot[str(guild.id)]["current"]["name_erraten"] = False
                            musicbot[str(guild.id)]["current"]["interpret_erraten"] = False
                            ydl_opts = {
                            'format': '249/250/251'
                            }
                            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([lied["url"]])
                            for file in os.listdir("./"):
                                    if file.endswith(".webm") and not "mq" in file:
                                        os.rename(file, f"mq{guild.id}.webm")

                            voice.play(discord.FFmpegPCMAudio(f"mq{guild.id}.webm"))
            except:
                pass


                

    @commands.command(brief='Ein Lied in das Musik Quiz Hinzufügen.', description='Dieser befehl ist nur für mich, EntchenEric#5771. Also brauch dich nicht zu interessieren, wie das hier funktioniert (:')
    async def addmusicquizsong(self, ctx, url, name, *, interpret):
        if ctx.author.id in [471036610561966111, 810484550727761940] :
            if musicbot[str(ctx.guild.id)] == None:
                musicbot[str(ctx.guild.id)] = {"Songs" : []}

            musicbot[str(ctx.guild.id)]["Songs"].append({"url" : url, "name" : name, "interpret" : interpret})

            await ctx.send("Lied erfolgreich hinzugefügt (:")
        else:
            myEmbed = discord.Embed(description="Diesen befehl können nur bestimmte leute ausführen.",color=0xbd24e7)
            myEmbed.set_footer(text=f"Tanjun Musik Quiz ⬝ {ctx.author}")
            await ctx.send(embed = myEmbed)
            return

    @commands.command(brief='Zeigt alle Songs, die im Musik Quiz kommen können.', description='Dieser befehl ist nur für mich, EntchenEric#5771. Also brauch dich nicht zu interessieren, wie das hier funktioniert (:')
    async def listmusicquizsonglinks(self, ctx):
        if ctx.author.id == 471036610561966111:
            c = 0
            msg = ""
            myEmbed = discord.Embed(title="", description="",color=0xbd24e7)
            for song in musicbot[str(ctx.guild.id)]["Songs"]:
                if len(msg) >= 800 and c != 0:
                    myEmbed.add_field(name="** **",value=msg,inline=False)
                    msg = ""

                msg += f"\n{song['name']} von {song['interpret']} URL: {song['url']}"
                c += 1
            myEmbed.add_field(name="** **",value=msg,inline=False)
            await ctx.send(embed = myEmbed) 
        else:
            myEmbed = discord.Embed(description="Diesen befehl können nur bestimmte leute ausführen.",color=0xbd24e7)
            myEmbed.set_footer(text=f"Tanjun Musik Quiz ⬝ {ctx.author}")
            await ctx.send(embed = myEmbed)
            return

    @commands.command(brief='Starte ein Musik Quiz!.', description='Starte ein musik Quiz in einen Beliebigen Channel mit beliebig vielen Runden!')
    async def startmusicquiz(self, ctx, runden : int, channel : discord.TextChannel):
        if musicbot[str(ctx.guild.id)] == None:
            musicbot[str(ctx.guild.id)] = {"current" : {}}
        lied = random.choice(musicbot["Songs"])
        musicbot[str(ctx.guild.id)]["current"] = {"Punkte" : {}, "Runden" : runden, "Aktuelle_Runde" : 0, "Is_Started" : True, "Richtiger_name" : lied["name"], "Richtiger_Interpret" : lied["interpret"], "channelid" : channel.id, "name_erraten" : False, "interpret_erraten" : False, "VC_id" : ctx.author.voice.channel.id}
        song_there = os.path.isfile(f"mq{ctx.guild.id}.webm")
        if song_there:
            os.remove(f"mq{ctx.guild.id}.webm")
        voiceChannel = ctx.author.voice.channel
        try:
            await voiceChannel.connect()
        except:
            i = 1
        url = lied["url"]
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        ydl_opts = {
                        'format': '249/250/251'
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
                if file.endswith(".webm"):
                    os.rename(file, f"mq{ctx.guild.id}.webm")   
        voice.play(discord.FFmpegPCMAudio(f"mq{ctx.guild.id}.webm"))

    @commands.Cog.listener()
    async def on_message(self, msg):
        try:
            if msg.author.bot == True:
                return


            try:
                if msg.channel.id == musicbot[str(msg.guild.id)]["current"]["channelid"] and musicbot[str(msg.guild.id)]["current"]["Is_Started"] == True:
                    lied = musicbot[str(msg.guild.id)]["current"]["Richtiger_name"]
                    interpret = musicbot[str(msg.guild.id)]["current"]["Richtiger_Interpret"]
                    voice = discord.utils.get(self.client.voice_clients, guild=msg.guild)
                    versuch = msg.content.lower()
                    versuch = versuch.replace("'", "")
                    versuch = versuch.replace("´", "")

                    richtiges = [interpret.lower(), lied.lower()]

                    if versuch in richtiges:

                        if lied.lower() in versuch:
                            await msg.add_reaction("👍")
                            try:
                                musicbot[str(msg.guild.id)]["current"]["Punkte"][str(msg.author.id)] += 2
                            except:
                                musicbot[str(msg.guild.id)]["current"]["Punkte"][str(msg.author.id)] = 2
                            musicbot[str(msg.guild.id)]["current"]["name_erraten"] = True
                            await msg.channel.send(f"{msg.author.mention} hat den Richtigen Namen Erraten und bekommt dafür 2 Punkt")


                        else:
                            try:
                                await msg.add_reaction("👍")
                                try:
                                    musicbot[str(msg.guild.id)]["current"]["Punkte"][str(msg.author.id)] += 1
                                except:
                                    musicbot[str(msg.guild.id)]["Punkte"][str(msg.author.id)] = 1
                                musicbot[str(msg.guild.id)]["current"]["interpret_erraten"] = True
                                await msg.channel.send(f"{msg.author.mention} hat den Richtigen Interpreten Erraten und bekommt dafür 1 Punkt")
                            except:
                                raise


                        if musicbot[str(msg.guild.id)]["current"]["name_erraten"] == True and musicbot[str(msg.guild.id)]["current"]["interpret_erraten"] == True:
                            musicbot[str(msg.guild.id)]["current"]["Aktuelle_Runde"] += 1
                            if musicbot[str(msg.guild.id)]["current"]["Aktuelle_Runde"] >= musicbot[str(msg.guild.id)]["current"]["Runden"]:
                                await msg.channel.send("Das Musik Quiz ist hiermit beendet! Es Folgen die Top teilnehmer. Das Aktuelle Lied wird weiter laufen")
                                embed = discord.Embed(title='Das Top 5 Ranking des Musik Quizzes!')
                                ranking = [[0, "Niemand"], [0, "Niemand"], [0, "Niemand"], [0, "Niemand"], [0, "Niemand"]]
                                for m in musicbot[str(msg.guild.id)]["current"]["Punkte"]:
                                    if musicbot[str(msg.guild.id)]["current"]["Punkte"][m] > ranking[0][0]:
                                        member = ""
                                        for mem in msg.guild.members:
                                            if mem.id == int(m):
                                                member = mem
                                        ranking[0] = [musicbot[str(msg.guild.id)]["current"]["Punkte"][m], member.name]
                                    elif musicbot[str(msg.guild.id)]["current"]["Punkte"][m] > ranking[1][0]:
                                        member = ""
                                        for mem in msg.guild.members:
                                            if int(mem.id) == int(m):
                                                member = mem
                                        ranking[1] = [musicbot[str(msg.guild.id)]["current"]["Punkte"][m], member.name]
                                    elif musicbot[str(msg.guild.id)]["current"]["Punkte"][m] > ranking[2][0]:
                                        member = ""
                                        for mem in msg.guild.members:
                                            if mem.id == int(m):
                                                member = mem
                                        ranking[2] = [musicbot[str(msg.guild.id)]["current"]["Punkte"][m], member.name]
                                    elif musicbot[str(msg.guild.id)]["current"]["Punkte"][m] > ranking[3][0]:
                                        member = ""
                                        for mem in msg.guild.members:
                                            if mem.id == int(m):
                                                member = mem
                                        ranking[3] = [musicbot[str(msg.guild.id)]["current"]["Punkte"][m], member.name]
                                    elif musicbot[str(msg.guild.id)]["current"]["Punkte"][m] > ranking[4][0]:
                                        member = ""
                                        for mem in msg.guild.members:
                                            if mem.id == int(m):
                                                member = mem
                                        ranking[4] = [musicbot[str(msg.guild.id)]["current"]["Punkte"][m], member.name]
                                c = 0
                                for rank in ranking:
                                    c += 1
                                    embed.add_field(name=f"Platz {c}",
                                    value=f'{rank[1]} mit {rank[0]} Punkten',
                                    inline=True)
                                await msg.channel.send(embed = embed)
                                musicbot[str(msg.guild.id)]["current"]["Is_Started"] = False
                                #musicbot[str(msg.guild.id)]["current"] = {"Punkte" : {}, "Runden" : 0, "Aktuelle_Runde" : 0, "Is_Started" : False, "Richtiger_name" : lied["name"], "Richtiger_Interpret" : lied["interpret"], "channelid" : None, "name_erraten" : False, "interpret_erraten" : False, "Vc_id" : None}
                            else:
                                voice.stop()
                                await asyncio.sleep(2)
                                vcid = musicbot[str(msg.guild.id)]["current"]["VC_id"]
                                song_there = os.path.isfile(f"mq{msg.guild.id}.webm")
                                if song_there:
                                    os.remove(f"mq{msg.guild.id}.webm")
                                voiceChannel = discord.utils.get(msg.guild.voice_channels, id=vcid)
                                try:
                                    await voiceChannel.connect()
                                except:
                                    i = 1
                                lied = random.choice(musicbot["Songs"])
                                musicbot[str(msg.guild.id)]["current"]["Richtiger_name"] = lied["name"]
                                musicbot[str(msg.guild.id)]["current"]["Richtiger_Interpret"] = lied["interpret"]
                                musicbot[str(msg.guild.id)]["current"]["name_erraten"] = False
                                musicbot[str(msg.guild.id)]["current"]["interpret_erraten"] = False
                                ydl_opts = {
                                'format': '249/250/251'
                                }
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                    ydl.download([lied["url"]])
                                for file in os.listdir("./"):
                                        if file.endswith(".webm"):
                                            os.rename(file, f"mq{msg.guild.id}.webm")

                                voice.play(discord.FFmpegPCMAudio(f"mq{msg.guild.id}.webm"))

                    else:
                        await msg.add_reaction("👎")
            except:
                pass
        except:
            pass
          


def setup(client):
    client.add_cog(MusikQuiz(client))