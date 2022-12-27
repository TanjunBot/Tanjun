import os
import discord
from discord.ext import commands, tasks
import random
from random import shuffle
import urllib
import json
from requests import request
import youtube_dl as youtube_dl
from googleapiclient.discovery import build
from discord.commands import Option, slash_command
from datetime import timedelta
import re
import json
from pathlib import Path

musicbot = {}
loop = {}

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.playmusic.start()


    @slash_command(name = "add", description='Füge ein Lied zu der Playlist des Musik Bot systems hinzu.')
    async def add(self, ctx, url : Option(str, "Was ist die URL des Liedes das ich abspielen soll?", required = True)):
        global musics
        try:
            musicbot[str(ctx.guild.id)]
        except:
            musicbot[str(ctx.guild.id)] = {}  
            musicbot[str(ctx.guild.id)]["urls"] = []
        spliturl = url.split("&")
        print(spliturl)
        if len(spliturl) == 1 and not "playlist" in url:
            musicbot[str(ctx.guild.id)]["urls"].append(url)
            await ctx.message.add_reaction("👍")
        else:
            if not "playlist" in url: 
                playlistid = spliturl[1].split("list=")
                playlistid = playlistid[1]
            else:
                playlistid = url.split("list=")
                playlistid = playlistid[1]
            youtube = build("youtube", "v3", developerKey = "AIzaSyAxWJJ9vzsSbJFU49C9HdtVMKexgwfqz9c")
            nextpagetoken = None
            urls = []
            total_seconds = 0
            c = 0
            cc = 0
            while True:
                request = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=playlistid,
                maxResults=50,
                pageToken=nextpagetoken
            )
                response = request.execute()
                vid_ids = []
                for item in response["items"]:
                    vid_ids.append(item["contentDetails"]["videoId"])

                vid_request = youtube.videos().list(
                    part="contentDetails",
                    id=",".join(vid_ids)
                )
                vid_response = vid_request.execute()

                hours_pattern = re.compile(r'(\d+)H')
                minutes_pattern = re.compile(r'(\d+)M')
                seconds_pattern = re.compile(r'(\d+)S')


                cc += 1
                for item in vid_response["items"]:
                    print(item["id"])
                    urls.append(f'https://www.youtube.com/watch?v={item["id"]}')
                    c += 1

                    duration = item["contentDetails"]["duration"]

                    hours = hours_pattern.search(duration)
                    minutes = minutes_pattern.search(duration)
                    seconds = seconds_pattern.search(duration)

                    hours = int(hours.group(1)) if hours else 0
                    minutes = int(minutes.group(1)) if minutes else 0
                    seconds = int(seconds.group(1)) if seconds else 0

                    video_seconds = timedelta(
                        hours = hours,
                        minutes = minutes,
                        seconds = seconds,
                    ).total_seconds()

                    total_seconds += video_seconds
                    print()
                nextpagetoken = response.get("nextPageToken")

                print(cc)

                if not nextpagetoken or cc == 10:
                    break
            total_seconds = int(total_seconds)

            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            print(hours, minutes, seconds)
            for url in urls:
                musicbot[str(ctx.guild.id)]["urls"].append(url)
            await ctx.send(f"Es wurden erfolgreich {c} Lieder hinzugefügt. (gesammtlänge: {hours} Stunden, {minutes} Minuten)")

    @slash_command(name = "play", description='Spiele ein beliebiges Lied von YouTube ab.')
    async def play(self, ctx, url : Option(str, "Was ist die URL des Liedes das ich abspielen soll?", required = True)):
        global musics
        try:
            musicbot[str(ctx.guild.id)]
        except:
            musicbot[str(ctx.guild.id)] = {}
            musicbot[str(ctx.guild.id)]["urls"] = []
        musicbot[str(ctx.guild.id)]["vc"] = ctx.author.voice.channel.id
        spliturl = url.split("&")
        print(spliturl)
        if len(spliturl) == 1 and not "playlist" in url:
            musicbot[str(ctx.guild.id)]["urls"].append(url)
            await ctx.message.add_reaction("👍")
        else:
            if not "playlist" in url: 
                playlistid = spliturl[1].split("list=")
                playlistid = playlistid[1]
            else:
                playlistid = url.split("list=")
                playlistid = playlistid[1]
            youtube = build("youtube", "v3", developerKey = "AIzaSyAxWJJ9vzsSbJFU49C9HdtVMKexgwfqz9c")
            nextpagetoken = None
            urls = []
            total_seconds = 0
            c = 0
            while True:
                request = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=playlistid,
                maxResults=50,
                pageToken=nextpagetoken
            )
                response = request.execute()
                vid_ids = []
                for item in response["items"]:
                    vid_ids.append(item["contentDetails"]["videoId"])

                vid_request = youtube.videos().list(
                    part="contentDetails",
                    id=",".join(vid_ids)
                )
                vid_response = vid_request.execute()

                hours_pattern = re.compile(r'(\d+)H')
                minutes_pattern = re.compile(r'(\d+)M')
                seconds_pattern = re.compile(r'(\d+)S')

                for item in vid_response["items"]:

                    print(item["id"])
                    urls.append(f'https://www.youtube.com/watch?v={item["id"]}')
                    c += 1

                    duration = item["contentDetails"]["duration"]

                    hours = hours_pattern.search(duration)
                    minutes = minutes_pattern.search(duration)
                    seconds = seconds_pattern.search(duration)

                    hours = int(hours.group(1)) if hours else 0
                    minutes = int(minutes.group(1)) if minutes else 0
                    seconds = int(seconds.group(1)) if seconds else 0

                    video_seconds = timedelta(
                        hours = hours,
                        minutes = minutes,
                        seconds = seconds,
                    ).total_seconds()

                    total_seconds += video_seconds
                    print()
                nextpagetoken = response.get("nextPageToken")

                if not nextpagetoken:
                    break
            total_seconds = int(total_seconds)

            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            print(hours, minutes, seconds)
            for url in urls:
                musicbot[str(ctx.guild.id)]["urls"].append(url)
            await ctx.send(f"Es wurden erfolgreich {c} Lieder hinzugefügt. (gesammtlänge: {hours} Stunden, {minutes} Minuten)")
    
    @slash_command(name = "queue", description='Liste die Nächsten Lieder auf, die abgespielt werden.')
    async def listsongs(self, ctx):
        global musics
        try:
            urls = musicbot[str(ctx.guild.id)]["urls"]
            embed = discord.Embed(description=f"Die lieder in der Playlist.",color=0xbd24e7)

            songs = ""

            c = 0
            embedfields = 0
            totallen = 0

            for song in urls:
                if len(songs) >= 800:
                    totallen += len(songs)
                    embed.add_field(name = "** **", value = songs, inline = False)
                    songs = ""
                    embedfields += 1
                if totallen >= 5000:
                    await ctx.send(embed = embed)
                    embed = discord.Embed(description=f"Die lieder in der Playlist.",color=0xbd24e7)
                    totallen = 0
                if embedfields == 23:
                    await ctx.send(embed = embed)
                    embed = discord.Embed(description=f"Die lieder in der Playlist.",color=0xbd24e7)
                params = {"format": "json", "url": song}
                url = "https://www.youtube.com/oembed"
                query_string = urllib.parse.urlencode(params)
                url = url + "?" + query_string
                with urllib.request.urlopen(url) as response:
                    response_text = response.read()
                    data = json.loads(response_text.decode())
                    songs += f"\n{data['title']}   ID: {c}"

                c += 1
            embed.add_field(name = "** **", value = songs, inline = False)
            await ctx.send(embed = embed)
        except:
            await ctx.send("Du hast noch keine Lieder hinzugefügt. Bitte benutze addsong {yt-Link} um ein Lied hinzuzufügen. Bitte beachte dass momentan nur lieder von YouTube unterstützt werden.")
            raise

    @slash_command(name = "leave", description='Lasse den Bot disconnecten.')
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild = ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
            await ctx.message.add_reaction("👋")

    @slash_command(name = "pause", description='Pausiere das momentane Lied.')
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild = ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.message.add_reaction("⏸")

    @slash_command(name = "resume", description='Fahre das momentane Lied fort.')
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild = ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.message.add_reaction("▶️")

    @slash_command(name = "skip", description='überspringe das momentane Lied.')
    async def skip(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild = ctx.guild)
        voice.stop()
        await ctx.message.add_reaction("⏭")

    @slash_command(name = "loop", description='Loope die Playlist (comming soon).')
    async def loop(self, ctx):
        global loop
        if not loop[str(ctx.guild.id)]:
            loop[str(ctx.guild.id)] = False
        loop[str(ctx.guild.id)] = not loop[str(ctx.guild.id)]
        await ctx.message.add_reaction("🔄")

    @slash_command(name = shuffle, description='shuffle die Playlist.')
    async def shuffle(self, ctx):
        global musics
        shuffle(musicbot[str(ctx.guild.id)]["urls"])
        await ctx.message.add_reaction("🔀")

    @slash_command(name = "clearqueue", description='Leere die Playlist.')
    async def clearplaylist(self, ctx):
        musicbot[str(ctx.guild.id)]["urls"] = []
        await ctx.send("Playlist erfolgreich geleert. Das aktuelle lied wird trotzdem noch zuende spielen.")

    @commands.has_permissions(kick_members=True)
    @slash_command(name = "deletesong", description='Entferne einen bestimmten Song per ID aus der Playlist. Die ID bekommst du mit den listsongs befehl.')
    async def deletesong(self, ctx, id : int):
        global musics
        try:
            musicbot[str(ctx.guild.id)]["urls"].pop(id)
            await ctx.send(f"Das Lied mit der id {id} wurde erfolgreich gelöscht.")
        except:
            await ctx.send("ein Lied mit dieser ID Existiert nicht.")

    @tasks.loop(seconds=1)
    async def playmusic(self):

        for guild in self.client.guilds:

            try:
                name = ""
                voiceChannel = discord.utils.get(guild.voice_channels, id=musicbot[str(guild.id)]["vc"])

                try:
                    await voiceChannel.connect()
                except:
                    pass
                voice = discord.utils.get(self.client.voice_clients, guild = guild)
                if voice.is_playing() == False:
                    songs = musicbot[str(guild.id)]["urls"]
                    url = songs[0]
                    musicbot[str(guild.id)]["urls"].pop(0)
                    song_there = os.path.isfile(f"songs({str(guild.id)}).webm")
                    try:
                        if song_there:
                            os.remove(f"songs({str(guild.id)}).webm")
                    except PermissionError:
                        return
                    voice = discord.utils.get(self.client.voice_clients, guild=guild)
                    ydl_opts = {
                        'format': '249',
                        'http_chunk_size': 10097152
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    for file in os.listdir("./"):
                        if file.endswith(".webm") and not file in "songs":
                            os.rename(file, f"songs({str(guild.id)}).webm")
                    voice.play(discord.FFmpegOpusAudio(f"songs({str(guild.id)}).webm"))
            except:
                #print(f"Error bei der Gilde {guild}")
                pass



def setup(client):
    client.add_cog(Music(client))