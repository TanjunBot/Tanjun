from pickletools import read_string1
from random import choices
import discord
from datetime import timedelta
import time
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command


class ModCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    möglichkeiten = [
        discord.OptionChoice(name = "Keine Nachrichten löschen.", value = "0"),
        discord.OptionChoice(name = "Nachrichten der letzten 7 Tage löschen.", value = "7"),
        discord.OptionChoice(name = "Nachrichten der letzten 24 Stunden löschen", value = "1")
    ]

    @has_permissions(ban_members=True)
    @slash_command(name='ban', description='Banne jemanden.')
    async def ban(self, ctx, member : Option(discord.Member, "Wen möchtest du Bannen?", required = True), nachrichten_löschen : Option(str, "Möchtest du die Nachrichten löschen?", required = True, choices = möglichkeiten), grund : Option(str, "Wieso möchtest du ihn Bannen?", required = True)):
        await ctx.defer()
        try:
            await member.send(f"Du wurdest von {ctx.guild.name} wegen `{grund}` gebannt.")
        except:
            pass
        try:
            await member.ban(reason = grund, delete_message_days = int(nachrichten_löschen))
            await ctx.respond(f"{member.mention} wurde erfolgreich gebannt.")
        except Exception as e:
            await ctx.respond(f"*Ich habe einen Error*😵\n\n{e}")

    @has_permissions(kick_members=True)
    @slash_command(name='kick', description='Kicke jemanden.')
    async def kick(self, ctx, member : Option(discord.Member, "Wen möchtest du Kicken?", required = True), grund : Option(str, "Wieso möchtest du ihn Kicken?", required = True)):
        await ctx.defer()
        try:
            await member.send(f"Du wurdest von {ctx.guild.name} wegen `{grund}` gekickt.")
        except:
            pass
        try:
            await member.kick(reason = grund)
            await ctx.respond(f"{member.mention} wurde erfolgreich gekickt.")
        except Exception as e:
            await ctx.respond(f"*Ich habe einen Error*😵\n\n{e}")
        
    möglichkeiten2 = [
        discord.OptionChoice(name = "10 Minuten Timeouten", value = "600"),
        discord.OptionChoice(name = "1 Stunde Timeouten", value = "3600"),
        discord.OptionChoice(name = "1 Tag Timeouten", value = "86400"),
        discord.OptionChoice(name = "1 Woche Timeouten", value = "604800")
    ]        

    @has_permissions(moderate_members=True)
    @slash_command(name='mute', description='Mute jemanden.')
    async def mute(self, ctx, member : Option(discord.Member, "Wen möchtest du Muten?", required = True), grund : Option(str, "Wieso möchtest du ihn muten?", required = True), muten_bis : Option(str, "Wie lange möchtest du ihn muten?", required = True, choices = möglichkeiten2)):
        await ctx.defer()
        try:
            timestamp = time.time()
            await member.send(f"Du wurdest von {ctx.guild.name} wegen `{grund}` bis <t:{int(timestamp + int(muten_bis))}:F> gemuted.")
        except:
            pass
        try:
            delta = timedelta(seconds = int(muten_bis))
            await member.timeout_for(reason = grund, duration = delta)
            await ctx.respond(f"{member.mention} wurde erfolgreich bis <t:{int(timestamp + int(muten_bis))}:F> gemuted.")
        except Exception as e:
            await ctx.respond(f"*Ich habe einen Error*😵\n\n{e}")

    @has_permissions(moderate_members=True)
    @slash_command(name='unmute', description='Entmute jemanden.')
    async def unmute(self, ctx, member : Option(discord.Member, "Wen möchtest du entmuten?", required = True), grund : Option(str, "Wieso möchtest du ihn unmuten?", required = True)):
        await ctx.defer()
        try:
            await member.timeout(reason = grund, until = None)
            await ctx.respond(f"{member.mention} wurde erfolgreich entmuted.")
        except Exception as e:
            await ctx.respond(f"*Ich habe einen Error*😵\n\n{e}")

    @has_permissions(moderate_members=True)
    @slash_command(name='timeout', description='Timeoute jemanden.')
    async def timeout(self, ctx, member : Option(discord.Member, "Wen möchtest du timeouten?", required = True), grund : Option(str, "Wieso möchtest du ihn timeouten?", required = True), muten_bis : Option(str, "Wie lange möchtest du ihn timeouten?", required = True, choices = möglichkeiten2)):
        await ctx.defer()
        try:
            timestamp = time.time()
            await member.send(f"Du wurdest von {ctx.guild.name} wegen `{grund}` bis <t:{int(timestamp + int(muten_bis))}:F> in Timeout geschickt.")
        except:
            pass
        try:
            delta = timedelta(seconds = int(muten_bis))
            await member.timeout_for(reason = grund, duration = delta)
            await ctx.respond(f"{member.mention} wurde erfolgreich bis <t:{int(timestamp + int(muten_bis))}:F> in Timeout geschickt.")
        except Exception as e:
            await ctx.respond(f"*Ich habe einen Error*😵\n\n{e}")

    @has_permissions(moderate_members=True)
    @slash_command(name='timeout_remove', description='Ent-timeoute jemanden.')
    async def timeout_remove(self, ctx, member : Option(discord.Member, "Wen möchtest du ent-timeouten?", required = True), grund : Option(str, "Wieso möchtest du ihn ent-timeouten?", required = True)):
        await ctx.defer()
        try:
            await member.timeout(reason = grund, until = None)
            await ctx.respond(f"Der Timeout von {member.mention} wurde erfolgreich gelöscht.")
        except Exception as e:
            await ctx.respond(f"*Ich habe einen Error*😵\n\n{e}")


    @has_permissions(manage_messages=True)
    @slash_command(name='purge', description='Lösche Nachrichten (massenweise).')
    async def purge(self, ctx, amount : Option(int, "Wie viele Nachrichten sollen gelöscht werden?", required = True), user : Option(discord.Member, "Von wen sollen die Nachrichten gelöscht werden?", required = False, default = None)):
        await ctx.defer()
        amount = round(amount)
        if amount > 0:
            if amount <= 10000:
                if user == None:
                    await ctx.channel.purge(limit=amount)
                else:
                    def check(m):
                        return m.author.id == user.id
                    await ctx.channel.purge(limit=amount, check = check)

                embed = discord.Embed(title='Erfolgreich gelöscht!',
                                      color=discord.Color.green())
                embed.add_field(
                    name="Nachrichten gelöscht!",
                    value=
                    f"{amount} Nachrichten wurden von {ctx.author.mention} gelöscht"
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title='❌Fehler beim Löschen der Nachrichten!❌',
                    color=discord.Color.red())
                embed.add_field(name="Anzahl zu hoch!",
                                value="Bitte gebe eine Zahl unter 10000 an!")
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='❌Fehler beim Löschen der Nachrichten!❌',
                                  color=discord.Color.red())
            embed.add_field(
                name="Anzahl ist zu gering!",
                value="Bitte gebe eine positive Zahlan!")
            await ctx.send(embed=embed)

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
    client.add_cog(ModCog(client))