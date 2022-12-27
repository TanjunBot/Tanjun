from dis import disco
import logging
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
import time
from numpy import imag
from pymongo import MongoClient

cluster = MongoClient("")

db = cluster["Main"]
serverstatscluster = MongoClient("")
logcluster = db["logs"]
serverstatsdb = serverstatscluster["Main"]
loggingcluster = serverstatsdb["logs"]
blacklistcollection = db["blacklist"]



useractions = {}
serverupdates = {}
channelupdates = {}
memberupdates = {}
threadupdates = {}
rollenupdates = {}
emojiupdates = {}
messageupdates = {}



class Logcog(commands.Cog):
    global messagelogembeds 

    def __init__(self, client):
        self.client = client

    actions = [
        discord.OptionChoice(name = "Nachrichten Logs.", value = "Message"),
        discord.OptionChoice(name = "Mitglieder Logs.", value = "Member"),
        discord.OptionChoice(name = "Server Logs", value = "Server")
    ]

    @slash_command(name='logs', description='Sehe die Logs!')
    async def logs(self, ctx, action : Option(str, "nach welcher Aktion möchtest du filtern?", required = False, choices = actions, default = "Message"), user : Option(discord.Member, "Möchtest du nach einen bestimmten user filtern?", required = False, default = None)):
        await ctx.defer()
        print("Ich fang jetzt an")
        tic = time.perf_counter()

        logs = loggingcluster.find_one({"_id" : ctx.guild.id})
        toc = time.perf_counter()
        print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

        if user == None:
            logswithtype = logs["actions"][action]
        else:
            logswithtype = logs["fromuser"][str(user.id)]

        logswithtype = logswithtype[::-1]

        page = 0

        embeds = []

        entry = logswithtype[page]

        x = logs[str(entry)]
        txt = f"**{x['action']}**\n\n"
        try:
            txt += f"`author:` <@{x['author']}>\n"
        except:
            pass
        try:
            txt += f"`member:` <@{x['member']}>\n"
        except:
            pass
        try:
            txt += f"`channel:` <#{x['channel']}>\n"
        except:
            pass
        try:
            txt += f"`channelname:` <#{x['channelname']}>\n"
        except:
            pass
        try:
            if not x["content"] == "":
                txt += f"`content:` {x['content']}\n"
        except:
            pass
        try:
            if not x["embeds"] == []:
                txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                for emb in x["embeds"]:
                    print(emb)
                    if not emb["title"] == "Embed.Empty":
                        title = emb["title"]
                    else:
                        title = discord.Embed.Empty
                    if not emb["image"] == "Embed.Empty":
                        image = emb["image"]
                    else:
                        image = None
                    if not emb["thumbnail"] == "Embed.Empty":
                        thumbnail = emb["thumbnail"]
                    else:
                        thumbnail = None
                    if not emb["description"] == "Embed.Empty":
                        description = emb["description"]
                    else:
                        description = discord.Embed.Empty

                    embed = discord.Embed(title = title, description= description, color = discord.Colour.green())
                    if image != None:
                        embed.set_image(image)
                    if thumbnail != None:
                        embed.set_thumbnail(thumbnail)
                    for field in emb["fields"]:
                        print(field)
                        if not field["inline"] == "Embed.Empty":
                            inline = field["inline"]
                        else:
                            inline = discord.Embed.Empty
                        if not field["name"] == "Embed.Empty":
                            name = field["name"]
                        else:
                            name = discord.Embed.Empty
                        if not field["value"] == "Embed.Empty":
                            value = field["value"]
                        else:
                            value = discord.Embed.Empty

                        embed.add_field(inline = inline, name = name, value = value)
                    embeds.append(embed)
        except:
            pass
        try:
            txt += f"`messageid:` {x['msgid']}\n"
        except:
            pass
        try:
            txt += f"`url:` {x['jump_url']}\n"
        except:
            pass
        try:
            txt += f"`gelöscht von ||nicht zu 100% akkurat!||:` <@{x['deleter']}>\n"
        except:
            pass
        try:
            if x["vorher"]["content"] != x["nachher"]["content"]:
                txt += f"`content vorher:` {x['vorher']['content']}\n`content nachher:` {x['nachher']['content']}\n"
        except:
            pass
        try:
            if x["vorher"]["embeds"] != x["nachher"]["embeds"]:
                txt += f"`Embeds Vorher oben in Rot`\n`Embeds Nachher oben in blau`\n"
                try:
                    if not x["vorher"]["embeds"] == []:
                        txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                        for emb in x["vorher"]["embeds"]:
                            print(emb)
                            if not emb["title"] == "Embed.Empty":
                                title = emb["title"]
                            else:
                                title = discord.Embed.Empty
                            if not emb["image"] == "Embed.Empty":
                                image = emb["image"]
                            else:
                                image = None
                            if not emb["thumbnail"] == "Embed.Empty":
                                thumbnail = emb["thumbnail"]
                            else:
                                thumbnail = None
                            if not emb["description"] == "Embed.Empty":
                                description = emb["description"]
                            else:
                                description = discord.Embed.Empty

                            embed = discord.Embed(title = title, description= description, color = discord.Colour.green())
                            if image != None:
                                embed.set_image(image)
                            if thumbnail != None:
                                embed.set_thumbnail(thumbnail)
                            for field in emb["fields"]:
                                print(field)
                                if not field["inline"] == "Embed.Empty":
                                    inline = field["inline"]
                                else:
                                    inline = discord.Embed.Empty
                                if not field["name"] == "Embed.Empty":
                                    name = field["name"]
                                else:
                                    name = discord.Embed.Empty
                                if not field["value"] == "Embed.Empty":
                                    value = field["value"]
                                else:
                                    value = discord.Embed.Empty

                                embed.add_field(inline = inline, name = name, value = value)
                            embeds.append(embed)
                except:
                    pass
                try:
                    if not x["nachher"]["embeds"] == []:
                        txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                        for emb in x["nachher"]["embeds"]:
                            print(emb)
                            if not emb["title"] == "Embed.Empty":
                                title = emb["title"]
                            else:
                                title = discord.Embed.Empty
                            if not emb["image"] == "Embed.Empty":
                                image = emb["image"]
                            else:
                                image = None
                            if not emb["thumbnail"] == "Embed.Empty":
                                thumbnail = emb["thumbnail"]
                            else:
                                thumbnail = None
                            if not emb["description"] == "Embed.Empty":
                                description = emb["description"]
                            else:
                                description = discord.Embed.Empty

                            embed = discord.Embed(title = title, description= description, color = discord.Colour.blue())
                            if image != None:
                                embed.set_image(image)
                            if thumbnail != None:
                                embed.set_thumbnail(thumbnail)
                            for field in emb["fields"]:
                                print(field)
                                if not field["inline"] == "Embed.Empty":
                                    inline = field["inline"]
                                else:
                                    inline = discord.Embed.Empty
                                if not field["name"] == "Embed.Empty":
                                    name = field["name"]
                                else:
                                    name = discord.Embed.Empty
                                if not field["value"] == "Embed.Empty":
                                    value = field["value"]
                                else:
                                    value = discord.Embed.Empty

                                embed.add_field(inline = inline, name = name, value = value)
                            embeds.append(embed)
                except:
                    pass
        except:
            pass
        try:
            if x["vorher"]["pinned"] != x["nachher"]["pinned"]:
                if x["vorher"]["pinned"] == True:
                    txt += f"`Nachricht ist jetzt angepinnt.`\n"
                else:
                    txt += f"`Nachricht ist jetzt nicht mehr angepinnt.`\n"
        except:
            pass
        try:
            txt += f"`emoji:` {x['Emoji']}\n"
        except:
            pass
        try:
            txt += f"`user:` <@{x['user']}>\n"
        except:
            pass
        try:
            if x["vorher"]["channelname"] != x["nachher"]["channelname"]:
                txt += f"`name vorher:` {x['vorher']['channelname']}\n`name nachher:` {x['nachher']['channelname']}\n"
        except:
            pass
        try:
            if x["vorher"]["position"] != x["nachher"]["position"]:
                txt += f"`position vorher:` {x['position']['channelname']}\n`position nachher:` {x['position']['channelname']}\n"
        except:
            pass
        try:
            if x["vorher"]["position"] != x["nachher"]["position"]:
                txt += f"`position vorher:` {x['position']['channelname']}\n`position nachher:` {x['position']['channelname']}\n"
        except:
            pass
        try:
            txt += f"`name:` {x['membername']}\n"
        except:
            pass
        try:
            txt += f"`name:` {x['name']}\n"
        except:
            pass
        try:
            txt += f"`{x['change']}`\n"
        except:
            pass
        try:
            txt += f"`mention:` {x['mention']}\n"
        except:
            pass
        try:
            txt += f"`position:` {x['position']}\n"
        except:
            pass
        try:
            txt += f"`gebannt von:` <@{x['banner']}>\n"
        except:
            pass
        try:
            txt += f"`entbannt von:` <@{x['unbanner']}>\n"
        except:
            pass
        
        if len(txt) >= 4000:
            while len(txt) >= 4000:
                myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt[0:4000], color=0xbd24e7)
                txt = txt[4000:]
                embeds.append(myEmbed)
            myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt, color=0xbd24e7)
            embeds.append(myEmbed)
        else:
            myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt, color=0xbd24e7)
            embeds.append(myEmbed)
        
        async def pagenext(interaction):
            embeds = []
            nonlocal view
            nonlocal page
            nonlocal message
            page += 1
            entry = logswithtype[page]
            x = logs[str(entry)]
            txt = f"**{x['action']}**\n\n"
            try:
                txt += f"`author:` <@{x['author']}>\n"
            except:
                pass
            try:
                txt += f"`member:` <@{x['member']}>\n"
            except:
                pass
            try:
                txt += f"`channel:` <#{x['channel']}>\n"
            except:
                pass
            try:
                txt += f"`channelname:` <#{x['channelname']}>\n"
            except:
                pass
            try:
                if not x["content"] == "":
                    txt += f"`content:` {x['content']}\n"
            except:
                pass
            try:
                if not x["embeds"] == []:
                    txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                    for emb in x["embeds"]:
                        print(emb)
                        if not emb["title"] == "Embed.Empty":
                            title = emb["title"]
                        else:
                            title = discord.Embed.Empty
                        if not emb["image"] == "Embed.Empty":
                            image = emb["image"]
                        else:
                            image = None
                        if not emb["thumbnail"] == "Embed.Empty":
                            thumbnail = emb["thumbnail"]
                        else:
                            thumbnail = None
                        if not emb["description"] == "Embed.Empty":
                            description = emb["description"]
                        else:
                            description = discord.Embed.Empty
    
                        embed = discord.Embed(title = title, description= description, color = discord.Colour.green())
                        if image != None:
                            embed.set_image(image)
                        if thumbnail != None:
                            embed.set_thumbnail(thumbnail)
                        for field in emb["fields"]:
                            print(field)
                            if not field["inline"] == "Embed.Empty":
                                inline = field["inline"]
                            else:
                                inline = discord.Embed.Empty
                            if not field["name"] == "Embed.Empty":
                                name = field["name"]
                            else:
                                name = discord.Embed.Empty
                            if not field["value"] == "Embed.Empty":
                                value = field["value"]
                            else:
                                value = discord.Embed.Empty
    
                            embed.add_field(inline = inline, name = name, value = value)
                        embeds.append(embed)
            except:
                pass
            try:
                txt += f"`messageid:` {x['msgid']}\n"
            except:
                pass
            try:
                txt += f"`url:` {x['jump_url']}\n"
            except:
                pass
            try:
                txt += f"`gelöscht von ||nicht zu 100% akkurat!||:` <@{x['deleter']}>\n"
            except:
                pass
            try:
                if x["vorher"]["content"] != x["nachher"]["content"]:
                    txt += f"`content vorher:` {x['vorher']['content']}\n`content nachher:` {x['nachher']['content']}\n"
            except:
                pass
            try:
                if x["vorher"]["embeds"] != x["nachher"]["embeds"]:
                    txt += f"`Embeds Vorher oben in Rot`\n`Embeds Nachher oben in blau`\n"
                    try:
                        if not x["vorher"]["embeds"] == []:
                            txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                            for emb in x["vorher"]["embeds"]:
                                print(emb)
                                if not emb["title"] == "Embed.Empty":
                                    title = emb["title"]
                                else:
                                    title = discord.Embed.Empty
                                if not emb["image"] == "Embed.Empty":
                                    image = emb["image"]
                                else:
                                    image = None
                                if not emb["thumbnail"] == "Embed.Empty":
                                    thumbnail = emb["thumbnail"]
                                else:
                                    thumbnail = None
                                if not emb["description"] == "Embed.Empty":
                                    description = emb["description"]
                                else:
                                    description = discord.Embed.Empty
    
                                embed = discord.Embed(title = title, description= description, color = discord.Colour.green())
                                if image != None:
                                    embed.set_image(image)
                                if thumbnail != None:
                                    embed.set_thumbnail(thumbnail)
                                for field in emb["fields"]:
                                    print(field)
                                    if not field["inline"] == "Embed.Empty":
                                        inline = field["inline"]
                                    else:
                                        inline = discord.Embed.Empty
                                    if not field["name"] == "Embed.Empty":
                                        name = field["name"]
                                    else:
                                        name = discord.Embed.Empty
                                    if not field["value"] == "Embed.Empty":
                                        value = field["value"]
                                    else:
                                        value = discord.Embed.Empty
    
                                    embed.add_field(inline = inline, name = name, value = value)
                                embeds.append(embed)
                    except:
                        pass
                    try:
                        if not x["nachher"]["embeds"] == []:
                            txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                            for emb in x["nachher"]["embeds"]:
                                print(emb)
                                if not emb["title"] == "Embed.Empty":
                                    title = emb["title"]
                                else:
                                    title = discord.Embed.Empty
                                if not emb["image"] == "Embed.Empty":
                                    image = emb["image"]
                                else:
                                    image = None
                                if not emb["thumbnail"] == "Embed.Empty":
                                    thumbnail = emb["thumbnail"]
                                else:
                                    thumbnail = None
                                if not emb["description"] == "Embed.Empty":
                                    description = emb["description"]
                                else:
                                    description = discord.Embed.Empty
    
                                embed = discord.Embed(title = title, description= description, color = discord.Colour.blue())
                                if image != None:
                                    embed.set_image(image)
                                if thumbnail != None:
                                    embed.set_thumbnail(thumbnail)
                                for field in emb["fields"]:
                                    print(field)
                                    if not field["inline"] == "Embed.Empty":
                                        inline = field["inline"]
                                    else:
                                        inline = discord.Embed.Empty
                                    if not field["name"] == "Embed.Empty":
                                        name = field["name"]
                                    else:
                                        name = discord.Embed.Empty
                                    if not field["value"] == "Embed.Empty":
                                        value = field["value"]
                                    else:
                                        value = discord.Embed.Empty
    
                                    embed.add_field(inline = inline, name = name, value = value)
                                embeds.append(embed)
                    except:
                        pass
            except:
                pass
            try:
                if x["vorher"]["pinned"] != x["nachher"]["pinned"]:
                    if x["vorher"]["pinned"] == True:
                        txt += f"`Nachricht ist jetzt angepinnt.`\n"
                    else:
                        txt += f"`Nachricht ist jetzt nicht mehr angepinnt.`\n"
            except:
                pass
            try:
                txt += f"`emoji:` {x['Emoji']}\n"
            except:
                pass
            try:
                txt += f"`user:` <@{x['user']}>\n"
            except:
                pass
            try:
                if x["vorher"]["channelname"] != x["nachher"]["channelname"]:
                    txt += f"`name vorher:` {x['vorher']['channelname']}\n`name nachher:` {x['nachher']['channelname']}\n"
            except:
                pass
            try:
                if x["vorher"]["position"] != x["nachher"]["position"]:
                    txt += f"`position vorher:` {x['position']['channelname']}\n`position nachher:` {x['position']['channelname']}\n"
            except:
                pass
            try:
                if x["vorher"]["position"] != x["nachher"]["position"]:
                    txt += f"`position vorher:` {x['position']['channelname']}\n`position nachher:` {x['position']['channelname']}\n"
            except:
                pass
            try:
                txt += f"`name:` {x['membername']}\n"
            except:
                pass
            try:
                txt += f"`name:` {x['name']}\n"
            except:
                pass
            try:
                txt += f"`{x['change']}`\n"
            except:
                pass
            try:
                txt += f"`mention:` {x['mention']}\n"
            except:
                pass
            try:
                txt += f"`position:` {x['position']}\n"
            except:
                pass
            try:
                txt += f"`gebannt von:` <@{x['banner']}>\n"
            except:
                pass
            try:
                txt += f"`entbannt von:` <@{x['unbanner']}>\n"
            except:
                pass
            
            if len(txt) >= 4000:
                while len(txt) >= 4000:
                    myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt[0:4000], color=0xbd24e7)
                    txt = txt[4000:]
                    embeds.append(myEmbed)
                myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt, color=0xbd24e7)
                embeds.append(myEmbed)
            else:
                myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt, color=0xbd24e7)
                embeds.append(myEmbed)

            view = discord.ui.View()

            lastpage = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=page == 0, row = 1)
            lastpage.callback = pagebefore

            nextpage = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=page + 1 == len(logswithtype), row = 1)
            nextpage.callback = pagenext

            view.add_item(lastpage)
            view.add_item(nextpage)

            await message.edit(embeds = embeds, view = view)

        async def pagebefore(interaction):
            nonlocal view
            nonlocal page
            nonlocal message
            embeds = []
            page -= 1
            entry = logswithtype[page]
            x = logs[str(entry)]
            txt = f"**{x['action']}**\n\n"
            try:
                txt += f"`author:` <@{x['author']}>\n"
            except:
                pass
            try:
                txt += f"`member:` <@{x['member']}>\n"
            except:
                pass
            try:
                txt += f"`channel:` <#{x['channel']}>\n"
            except:
                pass
            try:
                txt += f"`channelname:` <#{x['channelname']}>\n"
            except:
                pass
            try:
                if not x["content"] == "":
                    txt += f"`content:` {x['content']}\n"
            except:
                pass
            try:
                if not x["embeds"] == []:
                    txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                    for emb in x["embeds"]:
                        print(emb)
                        if not emb["title"] == "Embed.Empty":
                            title = emb["title"]
                        else:
                            title = discord.Embed.Empty
                        if not emb["image"] == "Embed.Empty":
                            image = emb["image"]
                        else:
                            image = None
                        if not emb["thumbnail"] == "Embed.Empty":
                            thumbnail = emb["thumbnail"]
                        else:
                            thumbnail = None
                        if not emb["description"] == "Embed.Empty":
                            description = emb["description"]
                        else:
                            description = discord.Embed.Empty
    
                        embed = discord.Embed(title = title, description= description, color = discord.Colour.green())
                        if image != None:
                            embed.set_image(image)
                        if thumbnail != None:
                            embed.set_thumbnail(thumbnail)
                        for field in emb["fields"]:
                            print(field)
                            if not field["inline"] == "Embed.Empty":
                                inline = field["inline"]
                            else:
                                inline = discord.Embed.Empty
                            if not field["name"] == "Embed.Empty":
                                name = field["name"]
                            else:
                                name = discord.Embed.Empty
                            if not field["value"] == "Embed.Empty":
                                value = field["value"]
                            else:
                                value = discord.Embed.Empty
    
                            embed.add_field(inline = inline, name = name, value = value)
                        embeds.append(embed)
            except:
                pass
            try:
                txt += f"`messageid:` {x['msgid']}\n"
            except:
                pass
            try:
                txt += f"`url:` {x['jump_url']}\n"
            except:
                pass
            try:
                txt += f"`gelöscht von ||nicht zu 100% akkurat!||:` <@{x['deleter']}>\n"
            except:
                pass
            try:
                if x["vorher"]["content"] != x["nachher"]["content"]:
                    txt += f"`content vorher:` {x['vorher']['content']}\n`content nachher:` {x['nachher']['content']}\n"
            except:
                pass
            try:
                if x["vorher"]["embeds"] != x["nachher"]["embeds"]:
                    txt += f"`Embeds Vorher oben in Rot`\n`Embeds Nachher oben in blau`\n"
                    try:
                        if not x["vorher"]["embeds"] == []:
                            txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                            for emb in x["vorher"]["embeds"]:
                                print(emb)
                                if not emb["title"] == "Embed.Empty":
                                    title = emb["title"]
                                else:
                                    title = discord.Embed.Empty
                                if not emb["image"] == "Embed.Empty":
                                    image = emb["image"]
                                else:
                                    image = None
                                if not emb["thumbnail"] == "Embed.Empty":
                                    thumbnail = emb["thumbnail"]
                                else:
                                    thumbnail = None
                                if not emb["description"] == "Embed.Empty":
                                    description = emb["description"]
                                else:
                                    description = discord.Embed.Empty
    
                                embed = discord.Embed(title = title, description= description, color = discord.Colour.green())
                                if image != None:
                                    embed.set_image(image)
                                if thumbnail != None:
                                    embed.set_thumbnail(thumbnail)
                                for field in emb["fields"]:
                                    print(field)
                                    if not field["inline"] == "Embed.Empty":
                                        inline = field["inline"]
                                    else:
                                        inline = discord.Embed.Empty
                                    if not field["name"] == "Embed.Empty":
                                        name = field["name"]
                                    else:
                                        name = discord.Embed.Empty
                                    if not field["value"] == "Embed.Empty":
                                        value = field["value"]
                                    else:
                                        value = discord.Embed.Empty
    
                                    embed.add_field(inline = inline, name = name, value = value)
                                embeds.append(embed)
                    except:
                        pass
                    try:
                        if not x["nachher"]["embeds"] == []:
                            txt += f"`Embeds wurden oben in grün mitgesendet`\n"
                            for emb in x["nachher"]["embeds"]:
                                print(emb)
                                if not emb["title"] == "Embed.Empty":
                                    title = emb["title"]
                                else:
                                    title = discord.Embed.Empty
                                if not emb["image"] == "Embed.Empty":
                                    image = emb["image"]
                                else:
                                    image = None
                                if not emb["thumbnail"] == "Embed.Empty":
                                    thumbnail = emb["thumbnail"]
                                else:
                                    thumbnail = None
                                if not emb["description"] == "Embed.Empty":
                                    description = emb["description"]
                                else:
                                    description = discord.Embed.Empty
    
                                embed = discord.Embed(title = title, description= description, color = discord.Colour.blue())
                                if image != None:
                                    embed.set_image(image)
                                if thumbnail != None:
                                    embed.set_thumbnail(thumbnail)
                                for field in emb["fields"]:
                                    print(field)
                                    if not field["inline"] == "Embed.Empty":
                                        inline = field["inline"]
                                    else:
                                        inline = discord.Embed.Empty
                                    if not field["name"] == "Embed.Empty":
                                        name = field["name"]
                                    else:
                                        name = discord.Embed.Empty
                                    if not field["value"] == "Embed.Empty":
                                        value = field["value"]
                                    else:
                                        value = discord.Embed.Empty
    
                                    embed.add_field(inline = inline, name = name, value = value)
                                embeds.append(embed)
                    except:
                        pass
            except:
                pass
            try:
                if x["vorher"]["pinned"] != x["nachher"]["pinned"]:
                    if x["vorher"]["pinned"] == True:
                        txt += f"`Nachricht ist jetzt angepinnt.`\n"
                    else:
                        txt += f"`Nachricht ist jetzt nicht mehr angepinnt.`\n"
            except:
                pass
            try:
                txt += f"`emoji:` {x['Emoji']}\n"
            except:
                pass
            try:
                txt += f"`user:` <@{x['user']}>\n"
            except:
                pass
            try:
                if x["vorher"]["channelname"] != x["nachher"]["channelname"]:
                    txt += f"`name vorher:` {x['vorher']['channelname']}\n`name nachher:` {x['nachher']['channelname']}\n"
            except:
                pass
            try:
                if x["vorher"]["position"] != x["nachher"]["position"]:
                    txt += f"`position vorher:` {x['position']['channelname']}\n`position nachher:` {x['position']['channelname']}\n"
            except:
                pass
            try:
                if x["vorher"]["position"] != x["nachher"]["position"]:
                    txt += f"`position vorher:` {x['position']['channelname']}\n`position nachher:` {x['position']['channelname']}\n"
            except:
                pass
            try:
                txt += f"`name:` {x['membername']}\n"
            except:
                pass
            try:
                txt += f"`name:` {x['name']}\n"
            except:
                pass
            try:
                txt += f"`{x['change']}`\n"
            except:
                pass
            try:
                txt += f"`mention:` {x['mention']}\n"
            except:
                pass
            try:
                txt += f"`position:` {x['position']}\n"
            except:
                pass
            try:
                txt += f"`gebannt von:` <@{x['banner']}>\n"
            except:
                pass
            try:
                txt += f"`entbannt von:` <@{x['unbanner']}>\n"
            except:
                pass

            
            if len(txt) >= 4000:
                while len(txt) >= 4000:
                    myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt[0:4000], color=0xbd24e7)
                    txt = txt[4000:]
                    embeds.append(myEmbed)
                myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt, color=0xbd24e7)
                embeds.append(myEmbed)
            else:
                myEmbed = discord.Embed(title=f'Tanjun Audit Log Seite {page + 1} / {len(logswithtype)}', description=txt, color=0xbd24e7)
                embeds.append(myEmbed)
            view = discord.ui.View()

            lastpage = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=page == 0, row = 1)
            lastpage.callback = pagebefore

            nextpage = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=page + 1 == len(logswithtype), row = 1)
            nextpage.callback = pagenext

            view.add_item(lastpage)
            view.add_item(nextpage)

            await message.edit(embeds = embeds, view = view)

        view = discord.ui.View()

        lastpage = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=page == 0, row = 1)
        lastpage.callback = pagebefore

        nextpage = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=page + 1 == len(logswithtype), row = 1)
        nextpage.callback = pagenext

        view.add_item(lastpage)
        view.add_item(nextpage)

        message = await ctx.send(embeds = embeds, view = view)

        #print(logs)

        

    

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        timestamp = int(str(time.time()).replace(".", ""))
        loggingcluster.update_one({"_id" : channel.guild.id}, {"$set" : {str(timestamp) : {"action" : "Jemand hat getippt", "user" : user.id, "channel" : channel.id}}}, upsert=True)


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild == None:
            return


        timestamp = int(str(time.time()).replace(".", ""))
        embeds = []
        if not message.embeds == None:
            for embed in message.embeds:
                fields = []
                if embed.fields != None:
                    for field in embed.fields:
                        fields.append({"inline" : field.inline, "name" : str(field.name), "value" : str(field.value)})

                dictonary = {"description" : str(embed.description), "fields" : fields,"title" : str(embed.title)}  
                try:
                    dictonary["image"] = str(embed.image.proxy_url)
                except:
                    pass
                try:
                    dictonary["thumbnail"] = str(embed.thumbnail.proxy_url)
                except:
                    pass
                embeds.append(dictonary)

        
        loggingcluster.update_one({"_id" : message.guild.id}, {"$set" : {str(timestamp) : {"action" : "Nachricht geschrieben", "author" : message.author.id, "channel" : message.channel.id, "content" : message.content, "embeds" : embeds, "msgid" : message.id, "jump_url" : message.jump_url}}}, upsert=True)
        loggingcluster.update_one({"_id" : message.guild.id}, {"$addToSet" : {f"fromuser.{message.author.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : message.guild.id}, {"$addToSet" : {f"actions.Message" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild == None:
            return


        async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
            deleter = entry.user
        timestamp = int(str(time.time()).replace(".", ""))
        embeds = []
        if not message.embeds == None:
            for embed in message.embeds:
                fields = []
                if embed.fields != None:
                    for field in embed.fields:
                        fields.append({"inline" : field.inline, "name" : str(field.name), "value" : str(field.value)})

                dictonary = {"description" : str(embed.description), "fields" : fields,"title" : str(embed.title)}  
                try:
                    dictonary["image"] = str(embed.image.proxy_url)
                except:
                    pass
                try:
                    dictonary["thumbnail"] = str(embed.thumbnail.proxy_url)
                except:
                    pass
                embeds.append(dictonary)

        
        loggingcluster.update_one({"_id" : message.guild.id}, {"$set" : {str(timestamp) : {"action" : "Nachricht gelöscht", "author" : message.author.id, "channel" : message.channel.id, "content" : message.content, "embeds" : embeds, "msgid" : message.id, "jump_url" : message.jump_url, "deleter" : deleter.id}}}, upsert=True)
        loggingcluster.update_one({"_id" : message.guild.id}, {"$addToSet" : {f"fromuser.{message.author.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : message.guild.id}, {"$addToSet" : {f"fromuser.{deleter.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : message.guild.id}, {"$addToSet" : {f"actions.Message" : timestamp}}, upsert=True)


    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        if message.guild == None:
            return
        timestamp = int(str(time.time()).replace(".", ""))

        messagess = []

        for message in messages:
            embeds = []
            if not message.embeds == None:
                for embed in message.embeds:
                    fields = []
                    if embed.fields != None:
                        for field in embed.fields:
                            fields.append({"inline" : field.inline, "name" : str(field.name), "value" : str(field.value)})

                    dictonary = {"description" : str(embed.description), "fields" : fields,"title" : str(embed.title)}  
                    try:
                        dictonary["image"] = str(embed.image.proxy_url)
                    except:
                        pass
                    try:
                        dictonary["thumbnail"] = str(embed.thumbnail.proxy_url)
                    except:
                        pass
                    embeds.append(dictonary)
            messages.append({"author" : message.author.id, "channel" : message.channel.id, "content" : message.content, "embeds" : embeds, "id" : message.id, "jump_url" : message.jump_url, "pinned" : message.pinned, "tts" : message.tts, "created_at" : message.created_at})


        loggingcluster.update_one({"_id" : messages[0].guild.id}, {"$set" : {str(timestamp) : {"action" : "Nachrichten Massengelöscht", "Nachrichten" : messagess}}}, upsert=True)
        loggingcluster.update_one({"_id" : message.guild.id}, {"$addToSet" : {f"actions.Message" : timestamp}}, upsert=True)


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.guild == None:
            return


        timestamp = int(str(time.time()).replace(".", ""))
        
        embeds = []
        if not before.embeds == None:
            for embed in before.embeds:
                fields = []
                if embed.fields != None:
                    for field in embed.fields:
                        fields.append({"inline" : field.inline, "name" : str(field.name), "value" : str(field.value)})
                dictonary = {"description" : str(embed.description), "fields" : fields,"title" : str(embed.title)}  
                try:
                    dictonary["image"] = str(embed.image.proxy_url)
                except:
                    pass
                try:
                    dictonary["thumbnail"] = str(embed.thumbnail.proxy_url)
                except:
                    pass
                embeds.append(dictonary)
        bef = {"content" : before.content, "embeds" : embeds, "id" : before.id, "pinned" : before.pinned}

        embeds = []
        if not after.embeds == None:
            for embed in after.embeds:
                fields = []
                if embed.fields != None:
                    for field in embed.fields:
                        fields.append({"inline" : field.inline, "name" : str(field.name), "value" : str(field.value)})
                dictonary = {"description" : str(embed.description), "fields" : fields,"title" : str(embed.title)}  
                try:
                    dictonary["image"] = str(embed.image.proxy_url)
                except:
                    pass
                try:
                    dictonary["thumbnail"] = str(embed.thumbnail.proxy_url)
                except:
                    pass
                embeds.append(dictonary)
        aft = {"content" : after.content, "embeds" : embeds, "msgid" : after.id, "pinned" : after.pinned}


        loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "Nachricht bearbeitet", "vorher" : bef, "nachher" : aft, "author" : before.author.id, "channel" : before.channel.id}}}, upsert=True)
        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"fromuser.{before.author.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"actions.Message" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        timestamp = int(str(time.time()).replace(".", ""))

        embeds = []
        if not reaction.message.embeds == None:
            for embed in reaction.message.embeds:
                fields = []
                if embed.fields != None:
                    for field in embed.fields:
                        fields.append({"inline" : field.inline, "name" : str(field.name), "value" : str(field.value)})
                dictonary = {"description" : str(embed.description), "fields" : fields,"title" : str(embed.title)}  
                try:
                    dictonary["image"] = str(embed.image.proxy_url)
                except:
                    pass
                try:
                    dictonary["thumbnail"] = str(embed.thumbnail.proxy_url)
                except:
                    pass
                embeds.append(dictonary)

        loggingcluster.update_one({"_id" : reaction.message.guild.id}, {"$set" : {str(timestamp) : {"action" : "Reagiert", "author" : reaction.message.author.id, "channel" : reaction.message.channel.id, "Emoji" : str(reaction.emoji), "user" : user.id, "content" : reaction.message.content, "embeds" : embeds}}}, upsert=True)

        loggingcluster.update_one({"_id" : reaction.message.guild.id}, {"$addToSet" : {f"fromuser.{user.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : reaction.message.guild.id}, {"$addToSet" : {f"actions.Message" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        timestamp = int(str(time.time()).replace(".", ""))

        embeds = []
        if not reaction.message.embeds == None:
            for embed in reaction.message.embeds:
                fields = []
                if embed.fields != None:
                    for field in embed.fields:
                        fields.append({"inline" : field.inline, "name" : str(field.name), "value" : str(field.value)})
                dictonary = {"description" : str(embed.description), "fields" : fields,"title" : str(embed.title)}  
                try:
                    dictonary["image"] = str(embed.image.proxy_url)
                except:
                    pass
                try:
                    dictonary["thumbnail"] = str(embed.thumbnail.proxy_url)
                except:
                    pass
                embeds.append(dictonary)

        loggingcluster.update_one({"_id" : reaction.message.guild.id}, {"$set" : {str(timestamp) : {"action" : "Reaktion entfernt", "author" : reaction.message.author.id, "content" : reaction.message.content, "embeds" : embeds, "Emoji" : str(reaction.emoji), "user" : user.id}}}, upsert=True)
        loggingcluster.update_one({"_id" : reaction.message.guild.id}, {"$addToSet" : {f"fromuser.{user.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : reaction.message.guild.id}, {"$addToSet" : {f"actions.Message" : timestamp}}, upsert=True)


    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        timestamp = int(str(time.time()).replace(".", ""))
        loggingcluster.update_one({"_id" : channel.guild.id}, {"$set" : {str(timestamp) : {"action" : "Kanal gelöscht", "channelname" : channel.name}}}, upsert=True)
        loggingcluster.update_one({"_id" : channel.guild.id}, {"$addToSet" : {f"actions.Channel" : timestamp}}, upsert=True)
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        timestamp = int(str(time.time()).replace(".", ""))
        loggingcluster.update_one({"_id" : channel.guild.id}, {"$set" : {str(timestamp) : {"action" : "Kanal erstellt", "channelname" : channel.name, "channel" : channel.id}}}, upsert=True)
        loggingcluster.update_one({"_id" : channel.guild.id}, {"$addToSet" : {f"actions.Channel" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        timestamp = int(str(time.time()).replace(".", ""))
        loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "Kanal bearbeitet", "vorher" : {"channelname" : before.name, "position" : before.position}, "nachher" : {"channelname" : after.name, "position" : after.position}}}}, upsert=True)
        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"actions.Channel" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        timestamp = int(str(time.time()).replace(".", ""))

        loggingcluster.update_one({"_id" : member.guild.id}, {"$set" : {str(timestamp) : {"action" : "User Gejoint", "isbot" : member.bot, "created_at" : member.created_at, "user" : member.id}}}, upsert=True)
        loggingcluster.update_one({"_id" : member.guild.id}, {"$addToSet" : {f"fromuser.{member.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : member.guild.id}, {"$addToSet" : {f"actions.Member" : timestamp}}, upsert=True)
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        timestamp = int(str(time.time()).replace(".", ""))

        loggingcluster.update_one({"_id" : member.guild.id}, {"$set" : {str(timestamp) : {"action" : "User Geleaved", "isbot" : member.bot, "created_at" : member.created_at,"membername" : str(member), "joined_at" : member.joined_at}}}, upsert=True)
        loggingcluster.update_one({"_id" : member.guild.id}, {"$addToSet" : {f"fromuser.{member.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : member.guild.id}, {"$addToSet" : {f"actions.Member" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        timestamp = int(str(time.time()).replace(".", ""))

        change1 = list(set(before.roles) - set(after.roles))
        change2 = list(set(after.roles) - set(before.roles))

        if change1 != []:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User bearbeitet", "member" : before.id, "change" : f"rollle Entfernt: {change1[0].mention}"}}}, upsert=True)

        if change2 != []:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User bearbeitet", "member" : before.id, "change" : f"rollle Hinzugefüht: {change2[0].mention}"}}}, upsert=True)

        if before.nick != after.nick:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User bearbeitet", "member" : before.id, "change" : f"Nickname geändert: {before.nick} ➡️ {after.nick}"}}}, upsert=True)

        if before.timed_out != after.timed_out:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User bearbeitet", "member" : before.id, "change" : f"timeout geändert: {before.timed_out} ➡️ {after.timed_out}"}}}, upsert=True)


        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"fromuser.{before.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"actions.Member" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        timestamp = int(str(time.time()).replace(".", ""))

        if before.status != after.status:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User bearbeitet", "member" : before.id, "change" : f"Status geändert: {before.status} ➡️ {after.status}"}}}, upsert=True)

        if before.activity != after.activity:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User bearbeitet", "member" : before.id, "change" : f"activity geändert: {before.activity} ➡️ {after.activity}"}}}, upsert=True)


        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"fromuser.{before.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"actions.Member" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        timestamp = int(str(time.time()).replace(".", ""))
        loggingcluster.update_one({"_id" : role.guild.id}, {"$set" : {str(timestamp) : {"action" : "Rolle erstellt", "position" : role.position, "mention" : role.mention}}}, upsert=True)
        loggingcluster.update_one({"_id" : role.guild.id}, {"$addToSet" : {f"actions.Server" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        timestamp = int(str(time.time()).replace(".", ""))
        loggingcluster.update_one({"_id" : role.guild.id}, {"$set" : {str(timestamp) : {"action" : "Rolle gelöscht", "position" : role.position, "name" : role.name}}}, upsert=True)
        loggingcluster.update_one({"_id" : role.guild.id}, {"$addToSet" : {f"actions.Server" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        timestamp = int(str(time.time()).replace(".", ""))

        if before.name != after.name:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User Rolle bearbeitet", "mention" : before.mention, "change" : f"Name geändert: {before.name} ➡️ {after.name}"}}}, upsert=True)
  
        if before.position != after.position:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "User Rolle bearbeitet", "mention" : before.mention, "change" : f"position geändert: {before.position} ➡️ {after.position}"}}}, upsert=True)


        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"actions.Server" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        timestamp = int(str(time.time()).replace(".", ""))

        change1 = list(set(before) - set(after))
        change2 = list(set(after) - set(before))

        if change1 != []:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "Emojis bearbeitet", "change" : f"Emoji Entfernt: {change1[0]}"}}}, upsert=True)

        if change2 != []:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "Emojis bearbeitet", "change" : f"Emoji Hinzugefüht: {change2[0]}"}}}, upsert=True)

        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"actions.Server" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_guild_stickers_update(self, guild, before, after):
        timestamp = int(str(time.time()).replace(".", ""))

        change1 = list(set(before.roles) - set(after.roles))
        change2 = list(set(after.roles) - set(before.roles))

        if change1 != []:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "Sticker bearbeitet", "change" : f"Sticker Entfernt: {change1[0].name}"}}}, upsert=True)

        if change2 != []:
            loggingcluster.update_one({"_id" : before.guild.id}, {"$set" : {str(timestamp) : {"action" : "Sticker bearbeitet", "change" : f"Sticker Hinzugefüht: {change2[0].name}"}}}, upsert=True)

        loggingcluster.update_one({"_id" : before.guild.id}, {"$addToSet" : {f"actions.Server" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        timestamp = int(str(time.time()).replace(".", ""))
        async for entry in guild.audit_logs(limit=1,action=discord.AuditLogAction.ban):
            banner = entry.user
        loggingcluster.update_one({"_id" : guild.id}, {"$set" : {str(timestamp) : {"action" : "User gebannt", "membername" : user, "banner" : banner.id}}}, upsert=True)
        loggingcluster.update_one({"_id" : guild.id}, {"$addToSet" : {f"fromuser.{user.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : guild.id}, {"$addToSet" : {f"actions.Member" : timestamp}}, upsert=True)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        timestamp = int(str(time.time()).replace(".", ""))
        async for entry in guild.audit_logs(limit=1,action=discord.AuditLogAction.unban):
            banner = entry.user
        loggingcluster.update_one({"_id" : guild.id}, {"$set" : {str(timestamp) : {"action" : "User unbanned", "membername" : user, "unbanner" : banner.id}}}, upsert=True)
        loggingcluster.update_one({"_id" : guild.id}, {"$addToSet" : {f"fromuser.{user.id}" : timestamp}}, upsert=True)
        loggingcluster.update_one({"_id" : guild.id}, {"$addToSet" : {f"actions.Member" : timestamp}}, upsert=True)


def setup(client):
    client.add_cog(Logcog(client))