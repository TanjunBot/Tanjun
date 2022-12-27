from random import choices
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
from discord.ui import Button, View
import asyncio

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @slash_command(name='help', description='Lass mich dir Helfen', guild_ids = [831161440705839124, 907216584341348373])
    async def help(self, ctx):

        print("Ich helfe!")

        


        async def utility_callback(interaction):
            view = View()
            if ctx.author.guild_permissions.view_audit_log == True:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/settings`\nRichte den Server ein.\n\n`/me`\nBekomme Informationen �ber dich als User.\n\n`/addticket [channel] [titel] [beschreibung] (logchannel)`\nF�ge dem Server ein Ticket-Supportsystem hinzu.\n\n`/setslowmode [channel] [seconds]`\nSetze den Slowmodus f�r einen Channel.\n\n`/embed [channel]`Sende ein Embed.\n\n`/editembed [messageid] [channel]`\nBearbeite ein bereits bestehendes Embed.\n\n`/avatar [member]`\nSchaue dir den Avatar eines Users an.\n\n`/benchmark [memeber]`\nSchaue dir den Banner eines Users an.\n\n`/google [message]`\nGoogle etwas bestimmtes.\n\n`/reddit [command]`\nSuche etwas zuf�lliges auf Reddit aus vorgegebenen Commands.\n\n`/invite`\nBekomme eine Einladung des Bots.")
            else:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/me`\nBekomme Informationen �ber dich als User.\n\n`/avatar [member]`\nSchaue dir den Avatar eines Users an.\n\n`/benchmark [memeber]`\nSchaue dir den Banner eines Users an.\n\n`/google [message]`\nGoogle etwas bestimmtes.\n\n`/reddit [command]`\nSuche etwas zuf�lliges auf Reddit aus vorgegebenen Commands.\n\n`/invite`\nBekomme eine Einladung des Bots.",color=0xbd24e7)
            await ctx.send(embed = myEmbed, view = view)
        
        
        
        
        
        async def minigames_callback(interaction):
            view = View()
            if ctx.author.guild_permissions.view_audit_log == True:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="**Economy:**\n\n\n`/start`\nStarte das Economy System.\n\n`/insertjob`\nF�ge ein Job dem Arbeitsamt hinzu.\n\n`/arbeitsamt`\nHole dir einen (neuen) Job um Economy-Geld zu verdienen.\n\n`/work`\nArbeite und verdiene Economy-Geld.\n\n`/insertspaziergang`\nF�ge ein bezahlten Spaziergang hinzu.\n\n`/antrag [member]`\nMache jemandem einen Antrag und besitzt ein gemeinsames Konto.\n\n`/erh�hung`\nFrage nach einer Gehaltserh�hung.\n\n`/additem`\nF�ge ein Item dem Economy-Shop hinzu.\n\n`/shop`\nGehe in den Economy Shop und kaufe dir etwas.\n\n`/use`\nBenutze ein Shopitem.\n\n`/gift [member]`\nSchenke jemandem etwas aus dem Economy-Shop\n\n\n\n**Counting:**\n\n\n`/setcountingchannel [channel]`\nLege einen Channel fest, in dem Counting gespielt werden darf.\n\n`/setcount`\nLege den Countingfortschritt fest.\n\n\n\n**Schere, Stein, Papier:**\n\n\n`/rps\nSpiele Schere, Stein, Papier.",color=0xbd24e7)
            else:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="**Economy:**\n\n\n`/arbeitsamt`\nHole dir einen (neuen) Job um Economy-Geld zu verdienen.\n\n`/work`\nArbeite und verdiene Economy-Geld.\n\n`/spazieren`\nGehe spazieren und verdiene Economy-Geld.\n\n`/antrag [member]`\nMache jemandem einen Antrag und besitzt ein gemeinsames Konto.\n\n`/erh�hung`\nFrage nach einer Gehaltserh�hung.\n\n`/shop`\nGehe in den Economy Shop und kaufe dir etwas.\n\n`/use`\nBenutze ein Shopitem.\n\n`/gift [member]`\nSchenke jemandem etwas aus dem Economy-Shop\n\n\n\n**Schere, Stein, Papier:**\n\n\n`/rps\nSpiele Schere, Stein, Papier.",color=0xbd24e7)
            await ctx.send(embed = myEmbed, view = view)
        
        
        

        async def roleplay_callback(interaction):
            view = View()
            if ctx.author.guild_permissions.view_audit_log == True:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/action [command] [member] [message]`\nBenutze einen Roleplay Command an einer Person mit einer Nachricht.\n\n`/cry`\nTue so als ob du weinst\n\n`/lovetester`\nTeste deine Liebe zu einem anderen User\n\n`/mball`\nStelle eine Frage und bekomme eine Antwort.\n\n`/sonnenuntergang [member]`\nSchaue dir den Sonnenuntergang mit einer Person gemeinsam an.\n\n`/weisheit`\nLasse dir eine Weisheit erz�hlen.\n\n`/witz`\nLasse dir einen Witz erz�hlen.",color=0xbd24e7)
            else:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/action [command] [member] [message]`\nBenutze einen Roleplay Command an einer Person mit einer Nachricht.\n\n`/cry`\nTue so als ob du weinst\n\n`/lovetester`\nTeste deine Liebe zu einem anderen User\n\n`/mball`\nStelle eine Frage und bekomme eine Antwort.\n\n`/sonnenuntergang [member]`\nSchaue dir den Sonnenuntergang mit einer Person gemeinsam an.\n\n`/weisheit`\nLasse dir eine Weisheit erz�hlen.\n\n`/witz`\nLasse dir einen Witz erz�hlen.",color=0xbd24e7)
            await ctx.send(embed = myEmbed, view = view)
        
        
        
        
        
        async def giveaway_callback(interaction):
            view = View()
            if ctx.author.guild_permissions.view_audit_log == True:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/nachrichten (optional user)`\nSehe die Nachrichten von jemandem oder dir selbst.\n\n`/removenachrichten`\nEntferne Nachrichten von jemandem.\n\n`/einladungen (optional user)`\nSehe die Einladungen von jemandem oder dir selbst\n\n`/reset`\nSetze die Nachrichten und Einladungen f�r den Server zur�ck.\n\n`/chance (optional user) (optional Gewinnspielid)`\nSehe die Gewinnchance von jemandem f�r die Gewinnspiele.\n\n`/gwend [giveawayid]`\nBeende ein Giveaway\n\n`/greroll [giveawayid]`\nloose einen neuen Gewinner f�r ein Gewinnspiel aus.\n\n`/gstart [channel] [l�nge] [gewinner] [gewinn]`\nStarte ein Gewinnspiel.\n\n`/setchance [user] [chance] (optional giveawayid)`\nErh�he die Chance f�r jemandem auf ein Gewinnspiel.\n\n`/reset`\nSetze Die Nachrichten und/oder die Invites zur�ck.",color=0xbd24e7)
            else:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/nachrichten (optional user)`\nSehe die Nachrichten von jemandem oder dir selbst.\n\n`/einladungen (optional user)`\nSehe die Einladungen von jemandem oder dir selbst\n\n`/chance (optional user) (optional Gewinnspielid)`\nSehe die Gewinnchance von jemandem f�r die Gewinnspiele.",color=0xbd24e7)
            await ctx.send(embed = myEmbed, view = view)





        async def levelsystem_callback(interaction):
            view = View()
            if ctx.author.guild_permissions.view_audit_log == True:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/boost (optional user)`\nErfahre, was f�r einen XP-Boost du hast.\n\n`/setxpboost [user] [boost] [role]`\nLege den XP-Boost f�r jemanden Fest.\n\n`/rank (optional user)`\nErfahre dein level.\n\n`/changecolor`\n�ndere die Farbe deiner Rank-Card.\n\n`/top`\nErfahre das top 10 Ranking des Servers.\n\n`/purgelevel [user] [level]`\nNehme jemandem bestimmt viele Level weg.\n\n`/givelevel [user] [level]`\nGebe jemandem Level.\n\n`/addlevelrank [rolle] [level]`\nF�ge eine Rolle Hinzu, die man bei einem bestimmten Level bekommen kann.\n\n`/disablelevelsystem`\nSchalte das Levelsystem aus.\n\n`/enablelevelsystem`Schalte das Levelsystem ein.",color=0xbd24e7)
            else:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/boost (optional user)`\nErfahre, was f�r einen XP-Boost du hast.\n\n`/rank (optional user)`\nErfahre dein level.\n\n`/changecolor`\n�ndere die Farbe deiner Rank-Card.\n\n`/top`\nErfahre das top 10 Ranking des Servers.",color=0xbd24e7)
            await ctx.send(embed = myEmbed, view = view)





        async def mod_callback(interaction):
            view = View()
            if ctx.author.guild_permissions.view_audit_log == True:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`/logs [Kategorie]`\nAktiviere die Logs auf dem Server.\n\n`/mute [user] (optional Grund) (optional dauer)`\nMute jemanden f�r bis zu eine Woche.\n\n`unmute [user]`\nUnmute jemanden.\n\n`/timeout [member] [grund] [dauer]`\nTimeoute jemanden mit einem bestimmten Grund.\n\n`timeout_remove [member] [grund]`\nHebe das Timeout f�r eine Person auf.\n\n`/ban [member] [nachrichten l�schen] [grund]`\nBanne jemanden mit einem bestimmten Grund von dem Server\n\n`/kick [member] [grund]`\nKicke jemanden mit einem bestimmten Grund von dem Server\n\n`/purge [menge]`\nL�sche bestimmt viele Nachrichten\n\n`/deleteallselfroles`\nL�sche alle Selfroles.",color=0xbd24e7)
            else:
                myEmbed = discord.Embed(title = f"Tanjun Hilfe",description="`Du hast keine Rechte um die Mod Befehle auszuf�hren.",color=0xbd24e7)
            await ctx.send(embed = myEmbed, view = view)



        utility = Button(label = "Utility Help", style = discord.ButtonStyle.green, emoji = "??")
        utility.callback = utility_callback

        minigames = Button(label = "Minigames Help", style = discord.ButtonStyle.green, emoji = "??")
        minigames.callback = minigames_callback

        roleplay = Button(label = "Roleplay Help", style = discord.ButtonStyle.green, emoji = "??")
        roleplay.callback = roleplay_callback

        giveaway = Button(label = "Giveaway Help", style = discord.ButtonStyle.green, emoji = "??")
        giveaway.callback = giveaway_callback

        levelsystem = Button(label = "Levelsystem Help", style = discord.ButtonStyle.green, emoji = "??")
        levelsystem.callback = levelsystem_callback

        mod = Button(label = "Mod Help", style = discord.ButtonStyle.green, emoji = "?????")
        mod.callback = mod_callback


        view = View()

        view.add_item(giveaway)
        view.add_item(levelsystem)
        if ctx.author.guild_permissions.view_audit_log == True:
            view.add_item(mod)


        
        modhelp = f"Wof�r m�chtest du deine Hilfe erhalten?"
        myEmbed = discord.Embed(title = f"Tanjun Hilfe",description=modhelp,color=0xbd24e7)

        print("Ich helfe?")

        try:
            await ctx.respond(embed = myEmbed)
        except:
            await ctx.send(embed = myEmbed)

    #für reporterror
    error_categories = [
        discord.OptionChoice(name="Fehler(meldung) beim Ausführen eines Commands", value="Fehler(meldung) beim Ausführen eines Commands"),
        discord.OptionChoice(name="Bot macht beim Ausführen eines Commands nicht das richtige", value="Bot macht beim Ausführen eines Commands nicht das richtige"),
        discord.OptionChoice(name="Es werden durch Ausführen des Commands unerwünscht Leute gepingt", value="Es werden durch Ausführen des Commands unerwünscht Leute gepingt"),
        discord.OptionChoice(name="Ungünstige/Unverständliche Beschreibung/Angabe(n)", value="Ungünstige/Unverständliche Beschreibung/Angabe(n)"),
        discord.OptionChoice(name="Rechtschreibfehler / Grammatikfehler / Logikfehler", value="Rechtschreibfehler / Grammatikfehler / Logikfehler"),
        discord.OptionChoice(name="Sonstiges", value="Sonstiges")
    ]
    
    @slash_command(name='reporterror', description='Melde einen Fehler')
    async def sm(self, ctx, message : Option(str,"Deine Fehlermeldung", required = True), category : Option(str,"In welche Kategorie würdest du diesen Fehler einordnen?", required = True, choices = error_categories)):
        cd = self.client.get_channel(968178149902913567)
        try:
            await ctx.respond("✅ | Vielen Dank! Der Fehler wurde an das Tanjun Team gesendet.", ephemeral=True)
            await cd.send(f'<@&923324120949735484>\n**⚠️ Jemand hat einen Fehler gemeldet!**\n\n**Fehlermeldung:**\n```\n{message}\n```\nFehlerkategorie: **`{category}`**\n\n**Melder:** <@{ctx.author.id}> (`{ctx.author.id}`)')
        except:
            await ctx.respond(f"❌ | **ERROR:** Ich konnte keinen Bericht an das Tanjun Team senden.\nBitte melde den Fehler bei einem Tanjun Developer per DM.", ephemeral=True)

def setup(client):
    client.add_cog(help(client))