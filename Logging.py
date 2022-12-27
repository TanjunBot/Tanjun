import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
import time
from pymongo import MongoClient

cluster = MongoClient("")

db = cluster["Main"]
serverstatscluster = MongoClient("")
logcluster = db["logs"]
serverstatsdb = serverstatscluster["Main"]
loggingcluster = serverstatsdb["logs"]



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
        discord.OptionChoice(name = "Server Updates", value = "guild_update"),
        discord.OptionChoice(name = "Kanal Erstellungen", value = "channel_create"),
        discord.OptionChoice(name = "Kanal Bearbeitungen", value = "channel_update"),
        discord.OptionChoice(name = "Kanal Löschungen", value = "channel_delete"),
        discord.OptionChoice(name = "Kanalberechtigungen erstellt", value = "overwrite_create"),
        discord.OptionChoice(name = "Kanalberechtigungen bearbeitet", value = "overwrite_update"),
        discord.OptionChoice(name = "Kanalberechtigungen Gelöscht", value = "overwrite_delete"),
        discord.OptionChoice(name = "Kicks", value = "kick"),
        discord.OptionChoice(name = "banns", value = "ban"),
        discord.OptionChoice(name = "Entbannungen", value = "unban"),
        discord.OptionChoice(name = "User Updates", value = "member_update"),
        discord.OptionChoice(name = "Rollen von Usern geändert", value = "member_role_update"),
        discord.OptionChoice(name = "Rollen Erstellungen", value = "role_create"),
        discord.OptionChoice(name = "Rollen Bearbeitungenm", value = "role_update"),
        discord.OptionChoice(name = "Rollen Löschungen", value = "role_delete"),
        discord.OptionChoice(name = "Emoji Erstellungen", value = "emoji_create"),
        discord.OptionChoice(name = "Emoji Bearbeitungen", value = "emoji_update"),
        discord.OptionChoice(name = "Emoji Löschungen", value = "emoji_delete"),
        discord.OptionChoice(name = "Nachrichten Löschungem", value = "message_delete"),
        discord.OptionChoice(name = "Massenlöschungen von Nachrichten", value = "message_bulk_delete"),
        discord.OptionChoice(name = "Anpinnen von Nachrichten", value = "message_pin"),
        discord.OptionChoice(name = "Sticker Erstellungen", value = "sticker_create"),
        discord.OptionChoice(name = "Sticker Updates", value = "sticker_update"),
        discord.OptionChoice(name = "Sticker Löschungen", value = "sticker_delete")
    ]

    @has_permissions(manage_channels=True)
    @slash_command(name='foo', description='Stelle die Logs ein', guild_ids = [831161440705839124])
    async def foo(self, ctx, user : Option(discord.Member, "Möchtest du nach einen User Filtern?", required = False, default = None), action : Option(str, "Möchtest du nach einer action filtern?", required = False, choices = actions, default = None)):
        print("Die Logs mach ich jetzt!")
        entries = await ctx.guild.audit_logs(limit=1000, user=user, action = action).flatten()
        print("Hab die Logs! Hier sind sie:")
        print(entries)

        page = 1
        embed = discord.Embed(title = f"Tanjun Audit Log Seite {page}", description="Hier ist der Audit Log :o")
        for entry in entries[0 + (page * 5) : 5 + (page * 5)]:
            embed.add_field(name = f"{entry.action}", value = f"`user`: {entry.user}\n`reason`: {entry.reason}\n`before`: {entry.before.name}\n`after`: {entry.after.name}\n`extra`: {entry.extra}", inline=False)

        

        async def pagenext(interaction):
            nonlocal view
            nonlocal page
            nonlocal message
            page += 1
            embed = discord.Embed(title = f"Tanjun Audit Log Seite {page}", description="Hier ist der Audit Log :o")
            for entry in entries[0 + (page * 5) : 5 + (page * 5)]:
                embed.add_field(name = f"{entry.action}", value = f"`user`: {entry.user}\n`reason`: {entry.reason}\n`before`: {entry.before}\n`after`: {entry.after}\n`extra`: {entry.extra}", inline=False)

            view = discord.ui.View()

            lastpage = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=page == 1, row = 1)
            lastpage.callback = pagebefore

            nextpage = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1)
            nextpage.callback = pagenext

            view.add_item(lastpage)
            view.add_item(nextpage)

            await message.edit(embed = embed, view = view)

        async def pagebefore(interaction):
            nonlocal view
            nonlocal page
            nonlocal message
            page -= 1
            embed = discord.Embed(title = f"Tanjun Audit Log Seite {page}", description="Hier ist der Audit Log :o")
            for entry in entries[0 + (page * 5) : 5 + (page * 5)]:
                embed.add_field(name = f"{entry.action}", value = f"`user`: {entry.user}\n`reason`: {entry.reason}\n`before`: {entry.before}\n`after`: {entry.after}\n`extra`: {entry.extra}", inline=False)

            view = discord.ui.View()

            lastpage = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=page == 1, row = 1)
            lastpage.callback = pagebefore

            nextpage = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1)
            nextpage.callback = pagenext

            view.add_item(lastpage)
            view.add_item(nextpage)

            await message.edit(embed = embed, view = view)

        view = discord.ui.View()

        lastpage = discord.ui.Button(label = "◀", style = discord.ButtonStyle.blurple, disabled=page == 1, row = 1)
        lastpage.callback = pagebefore

        nextpage = discord.ui.Button(label = "▶", style = discord.ButtonStyle.blurple, disabled=False, row = 1)
        nextpage.callback = pagenext

        view.add_item(lastpage)
        view.add_item(nextpage)

        message = await ctx.send(embed = embed, view = view)



def setup(client):
    client.add_cog(Logcog(client))