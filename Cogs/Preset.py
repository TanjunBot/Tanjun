import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
          
    @commands.Cog.listener()
    async def on_ready(self):
        print("ich bin bereit!")

    @slash_command(name='Hallo', description='Sage hallo!')
    async def Hallo(self, ctx, channel : Option(discord.TextChannel, "Ein Channel, weil wieso nicht lolo", required = True)):
        await ctx.send("Hallo!")


def setup(client):
    client.add_cog(Help(client))