import asyncio
from os import read
from typing import overload
import discord
from discord.abc import _Overwrites
from discord.ext import commands, tasks
import logging
import asyncio
import json
from pathlib import Path

class Security(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        if member.bot == True:
            async for entry in member.guild.audit_logs(limit=1):
                if entry.action == discord.AuditLogAction.bot_add:
                    if not entry.user == member.guild.owner:
                        await member.guild.kick(entry.target, reason = "Ein Bot wurde von jemanden, der nicht der Owner ist eingeladen.")
                        user = entry.user
                        try:
                            await user.send("Nur der Owner des Servers darf Bots einladen.")
                        except:
                            pass
                        try:
                            await member.guild.owner.send(f"{user} hat grade versucht, {entry.target} auf den Server einzuladen. Ich habe den Bot vorsorglich gekickt. Du als Owner musst Bots hinzufügen.")
                        except:
                            raise


def setup(client):
    client.add_cog(Security(client))