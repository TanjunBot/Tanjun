from pydoc import describe
import discord
from discord.ext import commands
import os
import pymongo
import random
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw
from icrawler.builtin import GoogleImageCrawler
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
from io import BytesIO
import random
import textwrap
import numpy as np
from datetime import date, datetime
import praw as praw
reddit = praw.Reddit(client_id="",
                     client_secret="-oc6WA",
                     username="",
                     password="",
                     user_agent="",
                     check_for_async=False)
from random import randint
import pyimgur


class Funcmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    actions = [
        discord.OptionChoice(name = "Lache jemanden Aus.", value = "1"),
        discord.OptionChoice(name = "Mache jemanden an.", value = "2"),
        discord.OptionChoice(name = "Mache jemanden aus", value = "3"),
        discord.OptionChoice(name = "Umarme jemanden", value = "4"),
        discord.OptionChoice(name = "Schlage jemanden", value = "5"),
        discord.OptionChoice(name = "Küsse jemanden", value = "6"),
        discord.OptionChoice(name = "Heirate jemanden", value = "7"),
        discord.OptionChoice(name = "Übernachte bei jemanden!", value = "8"),
        discord.OptionChoice(name = "Esse mit jemanden Chips!", value = "9"),
        discord.OptionChoice(name = "Knabbere jemanden an", value = "10"),
        discord.OptionChoice(name = "Kuschel mit jemanden", value = "11"),
        discord.OptionChoice(name = "Gehe mit jemanden auf Toilette", value = "12"),
        discord.OptionChoice(name = "Tröste jemanden", value = "13"),
        discord.OptionChoice(name = "Töte jemanden", value = "14"),
        discord.OptionChoice(name = "Patte jemanden", value = "15"),
        discord.OptionChoice(name = "Halte mit jemanden Händchen", value = "16"),
        discord.OptionChoice(name = "Entschuldige dich bei jemanden", value = "17"),
        discord.OptionChoice(name = "Finde das Alter von jemanden heraus", value = "18"),
        discord.OptionChoice(name = "Werfe jemanden in den Brunnen", value = "19"),
        discord.OptionChoice(name = "Rip 😞", value = "20"),
        discord.OptionChoice(name = "Zeichne jemanden aus", value = "21"),
        discord.OptionChoice(name = "Zeige jemanden an", value = "22"),
        discord.OptionChoice(name = "Mache aus jemanden Chips", value = "23"),
        discord.OptionChoice(name = "Tweete etwas", value = "24"),
        discord.OptionChoice(name = "Suche jemanden.", value = "25"),
    ]

    @slash_command(name='action', description='Mache etwas')
    async def action(self, ctx, command : Option(str, "Welchen Command möchtest du ausführen?", required = True, choices = actions), member : Option(discord.Member, "Bitte gebe an, mit wem du etwas machen möchtest.", required = True), message : Option(str, "Text?", required = True)):
        await ctx.defer()
        if command == "1":
            Auslachengifs = ["https://media.tenor.com/images/1d3e261b0447150bad4aebe8de786d58/tenor.gif", "https://media.tenor.com/images/58da3874fbf792c6682bdbb577052e9d/tenor.gif", "https://media.tenor.com/images/280056b1dc40deea3bf1131f6b9a1aa1/tenor.gif", "https://media.tenor.com/images/58da3874fbf792c6682bdbb577052e9d/tenor.gif", "https://media.tenor.com/images/8a5927b8b5e9eaaa4dc8d5677cd70a7a/tenor.gif", "https://media.tenor.com/images/b3fa3e23470374ab460a2efe6e5e9c51/tenor.gif", "https://media.tenor.com/images/2dc856471dd6d56578c1c255c076a701/tenor.gif",
                             "https://media.tenor.com/images/f9d332775b80b6a07b20775c5a8a257d/tenor.gif", "https://media.tenor.com/images/acea1a340a3e2e94b7d1da5dd522310d/tenor.gif", "https://media.tenor.com/images/5923bc6f9aec490d3f87a77a523dfee0/tenor.gif", "https://media.tenor.com/images/6ba045554d917ed1ee96c0ff916f9ca4/tenor.gif", "https://media.tenor.com/images/d1a455a115942a372a54cd7ffb2c8182/tenor.gif", "https://media.tenor.com/images/41b745cd92fc4211e5c4c7c3db13a7c1/tenor.gif", "https://media.tenor.com/images/7f127e87401602e1f270d2cef72a5764/tenor.gif"]

            url = random.choice(Auslachengifs)
            embed = discord.Embed(
                description=f"😂{ctx.author.mention} lacht {member.mention} aus😂\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "2":
            Anmachsprüche = ["Sind deine Eltern Terroristen? Denn du bist scharf wie eine Bombe.", "Sorry, ich habe meine Telefonnummer verloren, kannst du mir deine borgen?", "Du bist so süß! Wenn ich dich anschaue, bekomme ich sofort Diabetes.", "Hey Praline, brauchst du noch ne cremige Füllung?", "Hast du Zucker gefrühstückt oder warum bist du so süß?", "Hey Schnitte, schon belegt?", "Wenn du eine Kartoffel wärst, dann wärst du eine Süßkartoffel.", "Hey Praline, darf ich dich vernaschen?", "Ist es so heiß hier drin oder bist du das?", "Behältst du mich, wenn ich dir bis nach Hause nachlaufe?", "Darf ich dir heute Nacht Honig um den Bauchnabel streichen?", "Dein Bild hab ich irgendwo schon einmal gesehen… Stimmt, im Lexikon! Direkt neben Boah ey.", "Du bist der süßeste Snack, der mir je über den Weg gelaufen ist. Darf ich dich ohne Reue vernaschen?", "Du musst der wahre Grund für die globale Erderwärmung sein.", "Eigentlich wollte ich dich ja anbaggern, aber ich hab meinen Bagger leider vergessen. Dafür habe ich meinen Löffel dabei. Darf ich dich auch anlöffeln?", "Du bist so schön, dass es weh tut, dich anzusehen.", "Endlich die pasresponde Frau zu meiner Bettwäsche.",
                         "Auf welchen Anmachspruch würdest du denn am positivsten reagieren?", "Hab mein Bett heute frisch bezogen, leider mit zwei Bettdecken. Willst du eine abhaben?", "Hey du, was willst du morgen zum Frühstück ans Bett?", "Kannst du essen? Kannst du gehen? Lass uns essen gehen!", "Ich finde, mein Nachname passt gut zu deinem Vornamen.", "Hast du mal einen Stift? Ich möchte mir deine Nummer aufschreiben.", "Du siehst so aus, als hättest du das dringende Bedürfnis, mir deinen Namen zu nennen.", "Ich bin vom TÜV, darf ich mal deine Hupen testen?", "Ich bin vom ADAC, ich bin hier um dich abzuschleppen.", "Ich bin Umzugshelfer, soll ich dir beim Ausziehen helfen?", "Was machst du denn hier? Du müsstest schon längst in meinem Bett sein.", "Wow, siehst du zerknittert aus – soll ich mal über dich drüberbügeln?", "Ich bin so schlecht im Bett, das musst du unbedingt mal erlebt haben.", "Ich habe gelesen, dass Küssen das Leben verlängert. Komm mit zu mir nach Hause und lass uns unsterblich werden!", "Sag mal, ist dein Pullover aus Kamelhaar, oder warum hast du so wohlgeformte Höcker?", "Hey, ich bin Ken. Willst du meine Barbie sein?", 
                         "Wie schwer ist ein Eisbär? Schwer genug um das Eis zwischen uns zu brechen"]

            Anmachspruch = random.choice(Anmachsprüche)
            embed = discord.Embed(
                description=f"😳{ctx.author.mention} macht {member.mention} an😳\n{message}", color=0xbd24e7)
            embed.add_field(name=Anmachspruch, value="** **", inline=False)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)
        
        elif command == "3":
            Ausmachgifs = ["https://media.tenor.com/images/e9813fb08878844e8d851cd80fd0737d/tenor.gif", "https://media.tenor.com/images/7a78eec379f5ac9d2de1eefdcf86e190/tenor.gif", "https://media.tenor.com/images/83442d0bd392ff4ceda4e22820702531/tenor.gif", "https://media.tenor.com/images/b58d0a1d6a5725c36df00b105597f201/tenor.gif", "https://media.tenor.com/images/c3bb7134d019d6251e90e08ad8f929a9/tenor.gif",
                           "https://media.tenor.com/images/61f4dfe71c7b4140db79653f42592da3/tenor.gif", "https://media.tenor.com/images/33d642a80f721f5bae8fa929565624c2/tenor.gif", "https://media.tenor.com/images/c92e5ea551f4ec2a7b667da66e947e5a/tenor.gif", "https://media.tenor.com/images/0cca9b963a0c5fa91c97bbc108a9f0d1/tenor.gif", "https://media.tenor.com/images/60e9fd7d2b0e157604cc408e76a2d3d7/tenor.gif", "https://media.tenor.com/images/024cba60a8b579fada881f3c6ec490fb/tenor.gif"]

            url = random.choice(Ausmachgifs)
            embed = discord.Embed(
                description=f"😔{ctx.author.mention} macht {member.mention} aus😔\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "4":
            Huggifs = ["https://media.tenor.com/images/0a1652de311806ce55820a7115993853/tenor.gif", "https://media.tenor.com/images/bc8e962e6888249486a3e103edd30dd9/tenor.gif", "https://media.tenor.com/images/564eac526a8af795c90ce5985904096e/tenor.gif", "https://media.tenor.com/images/5d5565fe47af258d83b4caa2a668ccfa/tenor.gif", "https://media.tenor.com/images/3a9d2bd1bde9ed8ea02b2222988be6da/tenor.gif", "https://media.tenor.com/images/9164f10a0dbbf7cdb6aeb46184b16365/tenor.gif", "https://media.tenor.com/images/8090081dc5386a5272feb8bb29747a5d/tenor.gif", "https://media.tenor.com/images/f4cf111515c51d3e9faa2186e1432937/tenor.gif", "https://media.tenor.com/images/c7dfca55fa89585a5cbbfef17405a02e/tenor.gif",
                   "https://media.tenor.com/images/4a1e01bfa2f536bfe88e2dafc0a139af/tenor.gif", "https://media.tenor.com/images/de8075dd7db2c14e4799fc220e96bc62/tenor.gif", "https://media.tenor.com/images/1e058dc8d0ccd337b6d26cbab43b6e30/tenor.gif", "https://media.tenor.com/images/7d3a251e2d7bf9af9925137c37bc1a9d/tenor.gif", "https://media.tenor.com/images/f842f1ea35e0fc654880c0b2e6be012d/tenor.gif", "https://media.tenor.com/images/c15b5716c63e9fa3ac88edcdb65232ee/tenor.gif", "https://media.tenor.com/images/4bfcb1c5c5d639036a0bd867a8a6feaf/tenor.gif", "https://media.tenor.com/images/5509b0049259c2c20a07755bfce04e3d/tenor.gif", "https://media.tenor.com/images/39caba1632bdaafa0e882a62a74a81e3/tenor.gif", "https://media.tenor.com/images/2b821a1dc983cacc20d721cf2e5f2190/tenor.gif"]

            url = random.choice(Huggifs)
            embed = discord.Embed(
                description=f"🤗{ctx.author.mention} Umarmt {member.mention}🤗\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "5":
            Slapgifs = ["https://media.tenor.com/images/fd0718e35a95a53dbc27ddb9340f5db3/tenor.gif", "https://media.tenor.com/images/02c9c90d08a72c54ef8018ad31dfee63/tenor.gif", "https://media.tenor.com/images/70bae52444728ca8386c899d9c5798bf/tenor.gif", "https://media.tenor.com/images/ac09dd389d43f3bc0adad6432a942532/tenor.gif", "https://media.tenor.com/images/4bd7e5dff5f9f80627215da17066123d/tenor.gif", "https://media.tenor.com/images/e5b314426d5a7578a2653098d6df5750/tenor.gif", "https://media.tenor.com/images/e3c933eda0397820d9dcbfef090ec14b/tenor.gif",
                        "https://media.tenor.com/images/e42c4d9ba7e0d074455fe8e5d492a483/tenor.gif", "https://media.tenor.com/images/e42c4d9ba7e0d074455fe8e5d492a483/tenor.gif", "https://media.tenor.com/images/28237ac3e7af9c7c1699606210ade5ce/tenor.gif", "https://media.tenor.com/images/a8abd7318311c10e9782adddb85d8093/tenor.gif", "https://media.tenor.com/images/decd3218a876b28c71e4f32e7287fa12/tenor.gif", "https://media.tenor.com/images/abd26cbaefa0363c10fd12c43b64c539/tenor.gif", "https://media.tenor.com/images/f176d43c8c188a432c95ee240e623f24/tenor.gif"]

            url = random.choice(Slapgifs)
            embed = discord.Embed(
                description=f"💥{ctx.author.mention} Schlägt {member.mention}💥\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)
        
        elif command == "6":
            kissgifs = ["https://media.tenor.com/images/83bceada9e9a957a3909934de9c4a0f6/tenor.gif", "https://media.tenor.com/images/39fe167bdab90223bcc890bcb067b761/tenor.gif", "https://media.tenor.com/images/cd4582aea4d353f63a21173dc9b7f473/tenor.gif", "https://media.tenor.com/images/894f7f8efac0f1af5206c66e8297f311/tenor.gif",
                    "https://media.tenor.com/images/c0828ddd44542bc87a949cdf3d4d2488/tenor.gif", "https://media.tenor.com/images/21f81aacb412f880f4a82acb0e11aa74/tenor.gif", "https://media.tenor.com/images/1839d93138d41c0079f32a7664e34500/tenor.gif", "https://media.tenor.com/images/bb468f09379c0a3965e228529844fe7d/tenor.gif"]

            url = random.choice(kissgifs)
            embed = discord.Embed(
                description=f"😘{ctx.author.mention} küsst {member.mention}😘\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "7":
            Marrygifs = ["https://media.tenor.com/images/f36699e2c4156a4f75952faa9b71d8b6/tenor.gif", "https://media.tenor.com/images/4954ae61e20c39d38164e17401f6267f/tenor.gif", "https://media.tenor.com/images/671163941d31bfe46b33c10139171a3f/tenor.gif", "https://media.tenor.com/images/62c61ec9c941a61c4c9aa48ecafe6789/tenor.gif", "https://media.tenor.com/images/d349549e098e7be32c8bd21a99f3c9ef/tenor.gif",
                     "https://media.tenor.com/images/752aaaf1708c7b0939ff5f5abbc36483/tenor.gif", "https://media.tenor.com/images/d0282aea40bbd97482dbee37533f7f0e/tenor.gif", "https://media.tenor.com/images/aa1d2faa0698b0e375dc9b001893ef96/tenor.gif", "https://media.tenor.com/images/044d083952e6141e97816a16b1613edd/tenor.gif", "https://media.tenor.com/images/e9978e0dcfb6e6aae1b8d89382f0770a/tenor.gif"]

            url = random.choice(Marrygifs)
            embed = discord.Embed(
                description=f"💍{ctx.author.mention} Heiratet {member.mention}💍\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "8":
            uebernachtungsgif = ["https://media.tenor.com/images/006dec6a6420cc689ae88a21fb42acf0/tenor.gif", "https://media.tenor.com/images/f8d3ebe27832f330772b08631c1e7e55/tenor.gif",
                             "https://media.tenor.com/images/46727540d98bd83fac8184d942ab0a5e/tenor.gif", "https://media.tenor.com/images/1d3439a9e1edecbcc795fa3d0a75c1a1/tenor.gif", "https://media.tenor.com/images/06824b26491afe9852aa99f61a20d302/tenor.gif"]

            url = random.choice(uebernachtungsgif)
            embed = discord.Embed(
                description=f"🛏️{ctx.author.mention} Schmeißt mit {member.mention} eine Übernachtungsparty!🛏️\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "9":
            chipsessengifs = ["https://media.tenor.com/images/28986826775485538ed22604c1dc99e5/tenor.gif", "https://media.tenor.com/images/6bd01d1663312529e9016cbfbc2ea925/tenor.gif", "https://media.tenor.com/images/f6fc795cae703fc20021d65e1f128a31/tenor.gif", "https://media.tenor.com/images/b5d571bdde42a2b5bc49ebde3693104c/tenor.gif", "https://media.tenor.com/images/cc0e089ea62ee7b64d45d1bebc55abc3/tenor.gif", "https://media.tenor.com/images/6a6c2c69d95f0b4540f9a2edfecfc866/tenor.gif", "https://media.tenor.com/images/97e15713350a741a6f7b767c48ca4012/tenor.gif",
                              "https://media.tenor.com/images/d969e13c621c3a44dc9cad6a898538bf/tenor.gif", "https://media.tenor.com/images/df36da33b050b887fb4299b76d730f27/tenor.gif", "https://media.tenor.com/images/7a44959d9723b3d2ee0a1ca4fa346081/tenor.gif", "https://media.tenor.com/images/b8e4d66a30198f2ff0436a81f771bc5e/tenor.gif", "https://media.tenor.com/images/4b37e389d5176ad6c5dede49d7d97c4f/tenor.gif", "https://media.tenor.com/images/e3b076b28964401dcc8c88aa6b5a04bb/tenor.gif", "https://media.tenor.com/images/df49ae85b370488a13396d557a6a1897/tenor.gif"]

            url = random.choice(chipsessengifs)
            embed = discord.Embed(
                description=f"🤤{ctx.author.mention} isst gemeinsam mit {member.mention} Chips!🤤\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "10":
            anknabberngifs = ["https://media.tenor.com/images/616dcf3690e7edfac70c0e02c6d73559/tenor.gif", "https://media.tenor.com/images/b06d6a26b08516ac069b7a9acdd001e5/tenor.gif", "https://media.tenor.com/images/557723325e65671bae3f9cd061220c3e/tenor.gif", "https://media.tenor.com/images/bb5bcd9ebab8d7076609b06c83a33720/tenor.gif", "https://media.tenor.com/images/b3f77685f5fed03749ffff22a4c84dbb/tenor.gif",
                              "https://media.tenor.com/images/12aaaf60c46d563e3f8f2609f1df3c53/tenor.gif", "https://media.tenor.com/images/68cde02ac3e17c8f08bf142f02c6325f/tenor.gif", "https://media.tenor.com/images/a51b7045a4e45956e1e8eea56ca666ea/tenor.gif", "https://media.tenor.com/images/0db9387aff47ade00fb43c7b3f6f6498/tenor.gif", "https://media.tenor.com/images/4f6c5ad80164566034ff4854761651bf/tenor.gif", "https://media.tenor.com/images/777029607cf365f58e8b8ac57d548f19/tenor.gif"]

            url = random.choice(anknabberngifs)
            embed = discord.Embed(
                description=f"😋{ctx.author.mention} Findet {member.mention} Zum anbeißen!😋\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "11":
            Kuschelgifs = ["https://media.tenor.com/images/977f39af63e95cc8e513b4a46b3684c4/tenor.gif", "https://media.tenor.com/images/ea118b9c6c4a188df262d89899db199a/tenor.gif", "https://media.tenor.com/images/ea118b9c6c4a188df262d89899db199a/tenor.gif", "https://media.tenor.com/images/9c4a6d3cb294d01177a5b1e1544a5b9b/tenor.gif", "https://media.tenor.com/images/096e4f761ed797cc9914c29c36459430/tenor.gif",
                           "https://media.tenor.com/images/99159490e06c2bb45ec8437e082b014c/tenor.gif", "https://media.tenor.com/images/a847fb535e74ea9f8a49cd3d274feb39/tenor.gif", "https://media.tenor.com/images/ed47cfa4e3802f8cd68f7180b6dec3d3/tenor.gif", "https://media.tenor.com/images/3aab2ed61401f3d85e6d6b5f8605d52a/tenor.gif", "https://media.tenor.com/images/bfe6d12e6b5bf41a6b50b7737c64c06e/tenor.gif"]

            url = random.choice(Kuschelgifs)
            embed = discord.Embed(
                description=f"🥺{ctx.author.mention} Kuschelt mit {member.mention}!🥺\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "12":
            Toilettengifs = ["https://media.tenor.com/images/dcc63c5d497e9c60e74c1268cf3b2a65/tenor.gif", "https://media.tenor.com/images/c6e0e367edd2ae8006c4dd85f584ce0b/tenor.gif", "https://media.tenor.com/images/1a0f1de5804679dcdafe2a73eb2da560/tenor.gif",
                         "https://media.tenor.com/images/1df05fef4e5e53547ee074d733f65172/tenor.gif", "https://media.tenor.com/images/32a8cfc47342929df1d87bcb41bdc867/tenor.gif", "https://media.tenor.com/images/9fe4c78fe669580f3831d23175080477/tenor.gif", "https://media.tenor.com/images/accacfeb0805627491945ccfa198f099/tenor.gif"]

            url = random.choice(Toilettengifs)
            embed = discord.Embed(
                description=f"🚽{ctx.author.mention} Geht gemeinsam mit {member.mention} auf Toilette🚽\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)
        
        elif command == "13":
            troestengif = ["https://media.tenor.com/images/06b0b693cfcbece1c9e47b6c4d6b9f86/tenor.gif", "https://media.tenor.com/images/46230193e9d3f913531a3c00ef772963/tenor.gif", "https://media.tenor.com/images/c81489b50f2e61efcf155e995a835f2a/tenor.gif",
                       "https://media.tenor.com/images/21c1228517cafcd13dff38e2253b4713/tenor.gif", "https://media.tenor.com/images/9de2ea8ab13ccd9c5594a3c5892e4085/tenor.gif", "https://media.tenor.com/images/d50657a46d2e0a1ba86f12b1551544a7/tenor.gif", "https://media.tenor.com/images/fec973cdb301f5179dca6eef16499ab0/tenor.gif"]

            url = random.choice(troestengif)
            embed = discord.Embed(
                description=f"😌{ctx.author.mention} Tröstet {member.mention}!😌\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "14":
            killgifs = ["https://media.tenor.com/images/9a67b536e0272b32fc95d07fefd47a0e/tenor.gif", "https://media.tenor.com/images/3ad1c23b8c6a7b676906ab000b7a5575/tenor.gif", "https://media.tenor.com/images/6a49177686f7b2f2f6c989e5522c43a3/tenor.gif", "https://media.tenor.com/images/021d8ee64ce95e4c23449ecfd77fcbc6/tenor.gif",
                    "https://media.tenor.com/images/bafc48f1e9cd2b2b0cebcf59bd3101ac/tenor.gif", "https://media.tenor.com/images/5727ffc94ecdc95f1d3d79be986174a8/tenor.gif", "https://media.tenor.com/images/6e58a15c4c7004be03da413f7d6eb3dc/tenor.gif", "https://media.tenor.com/images/b794fa298fb6520829ade80a96fb9707/tenor.gif"]

            url = random.choice(killgifs)
            embed = discord.Embed(
                description=f"🔪{ctx.author.mention} beseitigt {member.mention}!🔪\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "15":
            Patgifs = ["https://media.tenor.com/images/0203a7bdba3302f6d8a473ba461e1581/tenor.gif", "https://media.tenor.com/images/dfe3267cca9596be840fbf9d5e86b747/tenor.gif", "https://media.tenor.com/images/8237d7da8cbd7227d67d735d437612cf/tenor.gif", "https://media.tenor.com/images/5e0fcbf53276d7b05b6dbf90d38f7fde/tenor.gif", "https://media.tenor.com/images/3768a9bfac80ec14257538c3b6bb9ad3/tenor.gif",
                       "https://media.tenor.com/images/943a52d38d896bda734a6396b1ffca89/tenor.gif", "https://media.tenor.com/images/5e341dca1b5233374cd426debdb01bad/tenor.gif", "https://media.tenor.com/images/a3a1aa34878fe2f2255cbff3f138d10e/tenor.gif", "https://media.tenor.com/images/6580eef39d70b792bf697da0b3e5e221/tenor.gif", "https://media.tenor.com/images/8bb1413ab7cee647d688df4ed20ab8cb/tenor.gif"]

            url = random.choice(Patgifs)
            embed = discord.Embed(
                description=f"😯{ctx.author.mention} gibt {member.mention} Head Pats!😯\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)
        
        elif command == "16":
            Händchenhaltengifs = ["https://media.tenor.com/images/6f9515756379626b413935733a75f301/tenor.gif", "https://media.tenor.com/images/7d9895dede351ae4bdd3acd4c15973ee/tenor.gif",
                                  "https://media.tenor.com/images/358773d3eafb8cf94a0a89b8eb2ba0d4/tenor.gif", "https://media.tenor.com/images/374d21d8fc63519956cbe1937efc8b03/tenor.gif", "https://media.tenor.com/images/d895ef08195768413cef0385c2d4b3a5/tenor.gif"]

            url = random.choice(Händchenhaltengifs)
            embed = discord.Embed(
                description=f"🤝{ctx.author.mention} Hält mit {member.mention} Händchen!🤝\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "17":
            Entschuldigungsgifs = ["https://media.tenor.com/images/f8d89820cc3c37fe4fa661316c9effac/tenor.gif", "https://media.tenor.com/images/1de42186cd837ed6e6de7d73ffedeae1/tenor.gif", "https://media.tenor.com/images/fb835ba37fd6d24f6014a36d51c8aac2/tenor.gif", "https://media.tenor.com/images/cd71e829028d7af85dd64f2ca675a5df/tenor.gif",
                                   "https://media.tenor.com/images/36abbff599f86aab54091acac7a8963e/tenor.gif", "https://media.tenor.com/images/26ef0d2415fc11417f4f89ef045cdab0/tenor.gif", "https://media.tenor.com/images/724c8840225ba4ab1a186a8dd417da78/tenor.gif", "https://media.tenor.com/images/fd30ea94fe84698ce7c23e8aae8df0bc/tenor.gif", "https://media.tenor.com/images/a3fe0c1e21c930c5dadf14d9c0ffe892/tenor.gif"]

            url = random.choice(Entschuldigungsgifs)
            embed = discord.Embed(
                description=f"😔{ctx.author.mention} entschuldigt sich bei {member.mention}😔\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)

        elif command == "18":
            if member == None:
                member = ctx.author
            alter = random.randint(0, 100)
            if alter == 7:
                alter = 561561894651849681456468944684486468468468445645645616548945616519841651654968134984650498460654798465165749841549878941521567894652146886925885848484848444564564
            await ctx.respond(f'{member.mention} ist {alter} Jahre alt!\n{message}')

        elif command == "19":
            Brunnengifs = ["https://iruntheinternet.com/lulzdump/images/girl-posing-picture-falls-in-fountain-falls-in-water-1418165994V.gif",
                           "https://botacademy.com/wp-content/uploads/2018/02/2018-02-26-fountain-crop-compressed.gif", "https://i.gifer.com/CJsh.gif", "https://memeguy.com/photos/images/woman-falls-into-fountain-while-texting-123588.gif"]

            url = random.choice(Brunnengifs)
            if member.id == 766350321638309958:
                embed = discord.Embed(
                    description=f"😲{ctx.author.mention} versuchte {member.mention} in den Brunnen zu werfen, ist aber selbst rein gefallen!😲\n{message}", color=0xbd24e7)
            else:
                embed = discord.Embed(
                    description=f"😲{ctx.author.mention} wirft {member.mention} in den Brunnen!😲\n{message}", color=0xbd24e7)
            embed.set_image(url=url)
            embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed=embed)


        elif command == "20":

            para = textwrap.wrap(message, width=15)
            if member == None:
                member = ctx.author
            asset = member.avatar.with_size(128)
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
            Bild = Image.open("Images/ripbg.jpg").convert("RGB")
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
            Bild = Image.open("Images/ripbg.jpg")
            pfp = Image.open("Images/result.png")
            Bild.paste(pfp, (480, 250), pfp)
            font_type = ImageFont.truetype("Fonts/rip.ttf", 30)
            draw = ImageDraw.Draw(Bild)
            today = date.today()
            todaystr = f"{today.strftime('%d')}.{today.strftime('%m')}.{today.strftime('%Y')}"
            draw.text((577, 474), f"{member.display_name} *{random.randint(1, 28)}.{random.randint(0, 13)}.{random.randint(1900, 2022)} †{todaystr}", fill ="black", font = font_type, align ="left", anchor="mm") 
            para = textwrap.wrap(message, width=35)
            MAX_W, MAX_H = 850, 950
            current_h, pad = 530, 10
            for line in para:
                w, h = draw.textsize(line, font=font_type)
                draw.text((580, current_h), line, font=font_type, fill ="black",anchor="mm")
                current_h += h + pad
            Bild.save("temp2.jpg")
            channel = self.client.get_channel(966970651162312775)
            mes = await channel.send(file=discord.File('temp2.jpg'))
            link = mes.attachments[0].url
            embed = discord.Embed(title='RIP', description = f"** **", color=0xbd24e7,url = link)
            embed.set_image(url = link)
            embed.set_footer(text=f"Tanjun fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)


        elif command == "21":

            para = textwrap.wrap(message, width=15)
            if member == None:
                member = ctx.author
            Bild = Image.open("Images/Urkundebg.jpg")
            font_type = ImageFont.truetype("Fonts/Urkundemembername.ttf", 50)
            draw = ImageDraw.Draw(Bild)
            draw.text((355, 210), member.display_name, font=font_type, fill ="black",anchor="mm")
            para = textwrap.wrap(message, width=30)
            MAX_W, MAX_H = 530, 350
            current_h, pad = 220, 10
            font_type = ImageFont.truetype("Fonts/BASKVILL.ttf", 23)
            for line in para:
                w, h = draw.textsize(line, font=font_type)
                draw.text((180, current_h), line, font=font_type, fill ="black")
                current_h += h + pad
            font_type = ImageFont.truetype("Fonts/Urkundeauthorname.ttf", 60)
            draw.text((242, 352), ctx.author.display_name, font=font_type, fill ="black",anchor="mm")
            font_type = ImageFont.truetype("Fonts/Urkundeownername.ttf", 30)
            draw.text((470, 360), "EntchenEric", font=font_type, fill ="black",anchor="mm")
            Bild.save("temp2.jpg")
            channel = self.client.get_channel(966970651162312775)
            mes = await channel.send(file=discord.File('temp2.jpg'))
            link = mes.attachments[0].url
            embed = discord.Embed(title='Urkunde', description = f"** **", color=0xbd24e7,url = link)
            embed.set_image(url = link)
            embed.set_footer(text=f"Tanjun fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)


        elif command == "22":

            para = textwrap.wrap(message, width=15)
            if member == None:
                member = ctx.author
            Bild = Image.open("Images/Anzeigebg.jpg")
            font_type = ImageFont.truetype("Fonts/times.ttf", 55)
            draw = ImageDraw.Draw(Bild)
            draw.text((555, 75), f"Anzeige an: {member.display_name}", font=font_type, fill ="black",anchor="mm")
            anzeige = f'Sehr geehrte(r) Herr/Frau {member.display_name}, Aufgrund Verstoßes gegen §135aGG Abs. 1 Nr. 1, 2, 5 und wiederwilliger wiederholender Verstoß gegen §73GG Abs. 1 Nr. 4 Werden Sie, {member.display_name} angezeigt. "{message}", so sagt es {ctx.author.display_name}. Wir stimmen dem zu und bitten sie, kommenden Freitag vor Gericht. Dort wird der Richter über sie und ihr Leben entscheiden.                                                                            Mit freundlichen Grüßen,                                                Ihr Kolles Gericht Kollhdxdlpistan.'
            para = textwrap.wrap(anzeige, width=50)
            MAX_W, MAX_H = 1105, 1350
            current_h, pad = 130, 10
            font_type = ImageFont.truetype("Fonts/times.ttf", 50)
            for line in para:
                w, h = draw.textsize(line, font=font_type)
                draw.text((20, current_h), line, font=font_type, fill ="black")
                current_h += h + pad
            Bild.save("temp2.jpg")
            channel = self.client.get_channel(966970651162312775)
            mes = await channel.send(file=discord.File('temp2.jpg'))
            link = mes.attachments[0].url
            embed = discord.Embed(title='Anzeige', description = f"** **", color=0xbd24e7,url = link)
            embed.set_image(url = link)
            embed.set_footer(text=f"Tanjun fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)


        elif command == "23":
            if member == None:
                member = ctx.author
            asset = member.avatar.with_size(128)
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
            Bild = Image.open("Images/ripbg.jpg").convert("RGB")
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
            Bild = Image.open("Images/chipsbg.jpg")
            pfp = Image.open("Images/result.png")
            Bild.paste(pfp, (195, 228), pfp)
            font_type = ImageFont.truetype("Fonts/Font.ttf", 50)
            draw = ImageDraw.Draw(Bild)
            draw.text((304, 143), member.display_name, font=font_type, fill ="black",anchor="mm")
            Bild.save("temp2.jpg")
            channel = self.client.get_channel(966970651162312775)
            mes = await channel.send(file=discord.File('temp2.jpg'))
            link = mes.attachments[0].url
            embed = discord.Embed(title='Chips Tüte', description = f"** **", color=0xbd24e7,url = link)
            embed.set_image(url = link)
            embed.set_footer(text=f"Tanjun fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)


        elif command == "24":
            asset = ctx.author.avatar.with_size(128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)
            pfp = pfp.resize((45, 45))
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
            Bild = Image.open("Images/tweetbg.jpg").convert("RGB")
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
            Bild = Image.open("Images/tweetbg.jpg")
            pfp = Image.open("Images/result.png")
            Bild.paste(pfp, (19, 15), pfp)
            font_type = ImageFont.truetype("Fonts/arial.ttf", 20)
            draw = ImageDraw.Draw(Bild)
            draw.text((78, 19), ctx.author.display_name, font=font_type, fill ="white")
            draw.text((78, 40), f"@{ctx.author}", font=font_type, fill ="gray")

            para = textwrap.wrap(message, width=50)
            MAX_W, MAX_H = 345, 82
            current_h, pad = 83, 10
            font_type = ImageFont.truetype("Fonts/arial.ttf", 20)
            for line in para:
                w, h = draw.textsize(line, font=font_type)
                draw.text((19, current_h), line, font=font_type, fill ="white")
                current_h += h + pad

            today = datetime.today()
            todaystr = f"{today.strftime('%I')}:{today.strftime('%M')} {today.strftime('%p')} · {today.strftime('%d')}. {today.strftime('%b')} {today.strftime('%y')} · Tanjun"
            draw.text((20, 209), todaystr, font=font_type, fill ="gray")
            draw.line((18,240, 585, 240), fill="gray", width=1)
            draw.text((23, 255), f'{random.randint(4, 100000)} "Gefällt mir"-Angaben', font=font_type, fill ="gray")
            draw.line((18,294, 585, 294), fill="gray", width=1)
            Bild.save("temp2.jpg")
            channel = self.client.get_channel(966970651162312775)
            mes = await channel.send(file=discord.File('temp2.jpg'))
            link = mes.attachments[0].url
            embed = discord.Embed(title='Tweet', description = f"** **", color=0xbd24e7,url = link)
            embed.set_image(url = link)
            embed.set_footer(text=f"Tanjun fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)


        elif command == "25":
            if member == None:
                member = ctx.author
            asset = member.avatar.with_size(128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)
            pfp = pfp.resize((300, 300))
            Bild = Image.open("Images/wantedbg.jpg")
            Bild.paste(pfp, (83, 218))
            Bild.save("temp2.jpg")
            channel = self.client.get_channel(966970651162312775)
            mes = await channel.send(file=discord.File('temp2.jpg'))
            link = mes.attachments[0].url
            embed = discord.Embed(title='Wanted', description = f"** **", color=0xbd24e7,url = link)
            embed.set_image(url = link)
            embed.set_footer(text=f"Tanjun fun Cmds ⬝ {ctx.author}")
            await ctx.respond(embed = embed)
    # Ausmachen Befehl


    reddits = [
        discord.OptionChoice(name = "Katzen.", value = "cats"),
        discord.OptionChoice(name = "Hunde.", value = "DOG"),
        discord.OptionChoice(name = "ENTEN 🦆🦆🦆🦆🦆🦆🦆🦆", value = "DUCK"),
        discord.OptionChoice(name = "Wölfe.", value = "wolves"),
        discord.OptionChoice(name = "Wenn du nix kannst 🙄", value = "onejob"),
        discord.OptionChoice(name = "Panda.", value = "panda"),
        discord.OptionChoice(name = "🥺🥺🥺", value = "aww"),
        discord.OptionChoice(name = "Zu sehr ich 😩", value = "2meirl4meirl"),
        discord.OptionChoice(name = "Kein Meme.", value = "antimeme"),
        discord.OptionChoice(name = "🙂", value = "MadeMeSmile"),
        discord.OptionChoice(name = "Ich 🎅", value = "meirl"),
        discord.OptionChoice(name = "Selbstgemacht!", value = "DiWHY")
    ]

    @slash_command(name='reddit', description='Bekomme einen der Top 30 Posts aus Reddit!')
    async def reddit(self, ctx, command : Option(str, "Welchen Command möchtest du ausführen?", required = True, choices = reddits)):
        await ctx.defer()

        value = randint(1, 30)
        zahl = 0
        submissions = reddit.subreddit('command').hot(limit=30)
        for submission in submissions:
            zahl += 1
            url = submission.url
            if zahl == value:
                if url.endswith(('.jpg', '.png', '.gif', ".jpeg")):
                    embed = discord.Embed(
                        description=f':cat: Eine süße Katzi :cat:',
                        color=discord.Color.dark_blue())
                    embed.set_image(url=url)
                    embed.add_field(name="Quelle:",
                                    value="https://www.reddit.com" +
                                    submission.permalink)
                    embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
                    await ctx.respond(embed=embed)
                else:
                  await redditor(self, ctx, command)


    @slash_command(name='witz', description='Lass dir einen superlustigen Witz erzählen!')
    async def witz(self, ctx):
            await ctx.defer()
            Witze = ["Der einzige Witz, den ich sehe bist du :P", "Wie nennt man ein Paar Steine in Minecraft?\nCouplestone", "Ich wollte Spiderman anrufen, aber er hatte kein Netz", "Patient: Ich bin so nervös. Das ist meine erste Operation.\nChirurg: Keine Sorge, meine auch.", "Warum nimmt eine Blondine trockenes Brot mit aufs WC?\nSie möchte die WC-Ente füttern.", "Meine Schwester ist Einzelkind.", "Deine Uhr fällt auf den Boden. Du darfst sie aber nicht aufheben, denn du hast kein Uhrheberrechtsgesetz xD", 
            "Der Lehrer fragt die Schüler: Wie heißt die Mehrzahl von Sandkorn?\nEin Schüler antwortet: Wüste.", "Was tut ein Cheater im tiefen Wald? Hacken.", "Warum klaute Robin Hood Deo?\nEr wollte es unter den Armen verteilen.", "Polizist hält einen betrunkenen Autofahrer an: Haben Sie was getrunken?\nFahrer säuselt angeschwipst: Nur Tee.\nPolizist: Dann haben Sie bestimmt 1,9 Kamille.", "Was sagt der große Stift zum kleinen Stift?\nWachs-mal-stift", "Treffen sich 2 Jäger - beide tot", "Was steht aus dem Grab eines Mathelehrers?\nDamit hat er nicht gerechnet xD",
            "Was trinken Chefs?\nLeitungswasser", "Was ist grün und steht vor der Tür?\nEin Klopfsalat"]
            await ctx.respond(random.choice(Witze))

    @slash_command(name='weisheit', description='Lass dir eine weise Weisheit erzählen!')
    async def weisheit(self, ctx):
        #Weisheiten = ["Aber Toastbrot ist schon schwer zu verdauen ~ Alex aka Muab aka aswa.ae", "Einer von uns soll verhaftet werden, obwohl er nichts gemacht hat; aber wir halten zusammen 🤝 ~ A\_€×",
        #"Alex ist Alex und Alex ist Alex ~ Eric aka EntchenEric", "Ich habe mich selber eingeladen ~ A\_€×", "also was fa? ~ Eric aka EntchenEric", "Alles was in und um mein Bettchen passiert ist privat ~ Alex aka Muab aka aswa.ae",
        #"Ich will Eric aber nicht mit mir teilen ~ Birki", "birki ist mir ~ Eric aka EntchenEric", "deutschland is aber nt die ganze welt ~ Azur aka Lollyweeny aka AzuredFlower aka Stygian Zin", "Einer von uns soll verhaftet werden, obwohl er nichts gemacht hat; aber wir halten zusammen 🤝 <:P_crazypanda:831638166456107108> ~ Alex und Alex aka Muab und Klon", "BBBIIIRRRKKKCCCHHHEEENNN :Wolf_excited::Wolf_excited::Wolf_excited::Wolf_excited::Wolf_excited::Wolf_excited::Wolf_excited::Wolf_excited: ~ Mew aka Pegi", "Tanuun ~ Birki", "Da will wohl wer meinen Finger anzünden👀 ~ Eric", "Feilst du auch oder sägst du nur an meiner Haut rum?👀 ~ Eric", "Die Lernlandschaftskooperationsteamgruppensektionsmafia hat die Aluminiumminimumimmunität auf dem Lernlandschaftskooperationsteamgruppensektionsstarkstormmasten mit Dreißig Rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetzen und Grundstücksverkehrsgenehmigungszuständigkeitsübertragungsverordnung und fünfzig Donauerdampfschifffartsunternehmenkapitänskahütenreinigungsunternehmenrechnungsfälschungsprüfungsbeauftragten. ~ *Aus* <#923324344799748117>",
        #"dieses brot ist aber auch echt 24/7 am lachen <:P_SUPERFUNNYBREAD:867370461931372544> ~ Arion", "Hier random Weisheiten ~ Arion", "Der eine hat Nitro der andere nicht ~ UniverseEvoli", "Alle sind extrem alt und wenn das mal nicht der Fall ist, könnte sich ihr Alter in wenigen Sekunden ändern. ~ __**Alle**__ ||*wirklich alle...*||", "Tanjun denkt nach … ~ Tanjun ||bzw. Discords Slash Commands||", "Eric lügen und Member umbringen, deshalb böses Eric Diktator sein ~ Alex Klon ||aka Diktator <:P_SUPERFUNNYBREAD:867370461931372544>||", "eric hat doch keine türkisen haare.. xd ~ Azur aka Lollyweeny aka AzuredFlower aka Stygian Zin",
        #"Wir sind halt krass ~ Eric", "Aber das sind die einlafinren ~ Eric", "porifeammiet rbtzuf ~ Eric"]
        await ctx.defer()
        channel = self.client.get_channel(934414657811267594)
        messages = await channel.history(limit=5000).flatten()

        weisheit = random.choices(messages)

        weisheit = weisheit[0]

        print(weisheit)

        myEmbed = discord.Embed(title = "eine Weisheit!", description = f"{weisheit.content}",  color=0xbd24e7)

        await ctx.respond(embed = myEmbed)

    # slap Befehl
    # Übernachten Befehl

    # Husten Befehl

    # Niesen Befehl




    möglichkeitenRPS = [
        discord.OptionChoice(name = "Stein", value = "r"),
        discord.OptionChoice(name = "Scheere", value = "s"),
        discord.OptionChoice(name = "Papier", value = "p")
    ]

    #rps Befehl
    @slash_command(name='rps', description='Spiele Stein Scheere Papier.')
    async def rps(self, ctx, answer : Option(str, "Was wählst du?", required = True, choices = möglichkeitenRPS)):
        await ctx.defer()
        answers = ["r", "p", "s"]
    
        yourEmote = ""
        botEmote = ""
        global stringAnswer
        global respond
        respond = "0"

        botAnswer = random.choice(answers)
        if str(botAnswer) == "s":
            botEmote = "✂️"
        if str(botAnswer) == "r":
            botEmote = "<:Stone:944883014956114000>"
        if str(botAnswer) == "p":
            botEmote = "📰"

        if answer == "s":
            yourEmote = "✂️"
            if answer == botAnswer:
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nUnentschieden"
            elif answer == "s" and botAnswer == "p":
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nSieg für dich - Glückwunsch :c"
            else:
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nDu hast verloren - beim nächsten Mal gewinnst du bestimmt"
            respond = "1"

        elif answer == "r":
            yourEmote = "<:Stone:944883014956114000>"
            if answer == botAnswer:
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nUnentschieden"
            elif answer == "r" and botAnswer == "s":
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nSieg für dich - Glückwunsch :c"
            else:
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nDu hast verloren - beim nächsten Mal gewinnst du bestimmt"
            respond = "1"
        elif answer == "p":
            yourEmote = "📰"
            if answer == botAnswer:
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nUnentschieden"
            elif answer == "p" and botAnswer == "r":
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nSieg für dich - Glückwunsch :c"
            else:
                stringAnswer = f"Du: {yourEmote}\nIch: {botEmote}\n\nDu hast verloren - beim nächsten Mal gewinnst du bestimmt"
            respond = "1"
        
        if str(respond) == "1":
            await ctx.respond(stringAnswer)
        else:
            await ctx.respond("Hmm deine Antwort stimmt wohl nicht. Probiere es bitte nochmal!")
        

                


            
        

        # weinen Befehl

    @slash_command(name='cry', description='Weine.')
    async def cry(self, ctx):
        await ctx.defer()
        weinengifs = ["https://media.tenor.com/images/2705fc9ca49876e7b65834509d1d9aed/tenor.gif", "https://media.tenor.com/images/0e8274cd916e003927cfd5f6bf6d7ca8/tenor.gif", "https://media.tenor.com/images/663d64cb093223c7a8ccd03d2d7577c8/tenor.gif", "https://media.tenor.com/images/cb7028f24e9a9391d606a3fee863b6f7/tenor.gif",
                      "https://media.tenor.com/images/b6aa13ef42baa403e0472e350a4eb9ed/tenor.gif", "https://media.tenor.com/images/bac30aa4eeaa9130fd5d0f72301c561b/tenor.gif", "https://media.tenor.com/images/c20ed85fdfe2efe4165f8525108a31bb/tenor.gif", "https://media.tenor.com/images/a8328f4f68451e45e3af67577896c721/tenor.gif", "https://media.tenor.com/images/7e1004ebf8f71e76967d865d7738f204/tenor.gif"]

        url = random.choice(weinengifs)
        embed = discord.Embed(
            description=f"😭{ctx.author.mention} Weint grade!😭", color=0xbd24e7)
        embed.set_image(url=url)
        embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
        await ctx.respond(embed=embed)
    # Trösten Befehl


    # Gemeinsam den Sonnenuntergang anschauen Befehl

    @slash_command(name='sonnenuntergang', description='Schaue dir mit jemandem gemeinsam den Sonnenuntergang an.')
    async def sonnenuntergang(self, ctx, member : Option(discord.Member, "mit wen möchtest du ihn anschauen?", required = True)):
        await ctx.defer()
        Sonnenunterganggif = ["https://media.tenor.com/images/4711cd412982491d2d687c511a066a0b/tenor.gif", "https://media.tenor.com/images/a5c05cd98e2f8ea35c9c60a4cd52d9af/tenor.gif",
                              "https://media.tenor.com/images/351cb8986d2fc9c1ff02d0c7ccb6d63b/tenor.gif", "https://media.tenor.com/images/fb886626e4d8b455f1b213c98094156b/tenor.gif", "https://media.tenor.com/images/2677c9392657b9da56d61ba437f606ba/tenor.gif"]

        url = random.choice(Sonnenunterganggif)
        embed = discord.Embed(
            description=f"🔆{ctx.author.mention} Schaut gemeinsam mit {member.mention} denmSonnenuntergang zu!🔆", color=0xbd24e7)
        embed.set_image(url=url)
        embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
        await ctx.respond(embed=embed)
    # Händchen halten Befehl



async def redditor(self, ctx, subreddit):
    value = randint(1, 30)
    zahl = 0
    submissions = reddit.subreddit(subreddit).hot(limit=100)
    for submission in submissions:
        zahl += 1
        url = submission.url
        if zahl == value:
            if url.endswith(('.jpg', '.png', '.gif', ".jpeg")):
                embed = discord.Embed(
                    description=f'** **',
                    color=0xbd24e7)
                embed.set_image(url=url)
                embed.add_field(name="Quelle:",
                                value="https://www.reddit.com" +
                                submission.permalink)
                embed.set_footer(text=f"Tanjun Fun Cmds ⬝ {ctx.author}")
                await ctx.respond(embed=embed)
            else:
              await redditor(self, ctx, subreddit)
    

def setup(client):
    client.add_cog(Funcmds(client))