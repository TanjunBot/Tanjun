import discord
from discord.ext import commands, tasks
import datetime
from discord.ext.commands import has_permissions
from discord.commands import Option, slash_command
from datetime import datetime
from pymongo import MongoClient
from discord.ext import tasks
from discord.utils import get
from datetime import date

#cluster = MongoClient("")

db = cluster["Main"]
bdaycollection = db["bdays"]


class VorlageCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    möglichkeitenMonat = [
        discord.OptionChoice(name = "Januar", value = "01"),
        discord.OptionChoice(name = "Februar", value = "02"),
        discord.OptionChoice(name = "März", value = "03"),
        discord.OptionChoice(name = "April", value = "04"),
        discord.OptionChoice(name = "Mai", value = "05"),
        discord.OptionChoice(name = "Juni", value = "06"),
        discord.OptionChoice(name = "Juli", value = "07"),
        discord.OptionChoice(name = "August", value = "08"),
        discord.OptionChoice(name = "September", value = "09"),
        discord.OptionChoice(name = "Oktober", value = "10"),
        discord.OptionChoice(name = "November", value = "11"),
        discord.OptionChoice(name = "Dezember", value = "12")
    ]


    @slash_command(name='addbirthday', description='Lass mich deinen Geburtstag wissen.')
    async def addbirthday(self, ctx, monat : Option(str, "In welchem Monat hast du Geburtstag?", required = True, choices = möglichkeitenMonat), tag : Option(int, "An welchen Tag hast du Geburtstag?", required = True), jahr : Option(int, "In welchem Jahr hast du Geburtstag?", required = False, default = None)):
        await ctx.defer()
        if len(str(tag)) == 1:
            tag = str(tag)
            tag = f"0{tag}"
        bdaycollection.insert_one({"_id" : ctx.author.id, "date" : f"{monat}-{tag}", "Jahr" : jahr})
        await ctx.respond("Ich weiß jetzt deinen Geburtstag")

    @slash_command(name='removebirthday', description='Lass mich deinen Geburtstag vergessen.')
    async def removebirthday(self, ctx):
        await ctx.defer()
        bdaycollection.delete_one({"_id" : ctx.author.id})
        await ctx.respond("Oh je... was war nochmal dein Geburtstag? 😵")
    


    @slash_command(name='showbirthday', description='Lass dir den Geburtstag von jemandem anzeigen.')
    async def showbirthday(self, ctx, member : Option(discord.Member, "Wessen Geburtstag soll gezeigt werden?", required = False)):
        await ctx.defer()
        if(member == None):
            bday = bdaycollection.find_one({"_id" : ctx.author.id})
            dt = bday['date']
            month = dt[0:2]
            day = dt[3:]
            todaymonth = datetime.today().strftime('%m')
            todayday = datetime.today().strftime('%d')
            todayyear = datetime.today().strftime('%y')
            hasbirthday = True
            if int(month) > int(todaymonth):
                hasbirthday = False
            elif int(month) == int(todaymonth):
                if int(day) > int(todayday):
                    hasbirthday = False

            daystillbday = 0
            year = 0

            if hasbirthday == True:
                year = int(todayyear) + 1
            else:
                year = int(todayyear)

            daystillbday = date(int(year), int(month), int(day)) - date(int(todayyear), int(todaymonth), int(todayday))
        
            await ctx.respond(f"Dein Geburtstag ist am {day}.{month}. (in {daystillbday.days} Tagen!)")
        else:
            bday = bdaycollection.find_one({"_id" : member.id})
            dt = bday['date']
            month = dt[0:2]
            day = dt[3:]

            todaymonth = datetime.today().strftime('%m')
            todayday = datetime.today().strftime('%d')
            todayyear = datetime.today().strftime('%y')
            hasbirthday = True
            if int(month) > int(todaymonth):
                hasbirthday = False
            elif int(month) == int(todaymonth):
                if int(day) > int(todayday):
                    hasbirthday = False

            daystillbday = 0
            year = 0

            if hasbirthday == True:
                year = int(todayyear) + 1
            else:
                year = int(todayyear)

            daystillbday = date(int(year), int(month), int(day)) - date(int(todayyear), int(todaymonth), int(todayday))
        
            await ctx.respond(f"{member.mention} hat am {day}.{month}. Geburtstag. (in {daystillbday.days} Tagen!)")
    
    @slash_command(name='changebirthday', description='Ändere deinen bereits eingetragenen Geburtstag.')
    async def changebirthday(self, ctx, monat : Option(str, "In welchem Monat hast du Geburtstag?", required = True, choices = möglichkeitenMonat), tag : Option(int, "An welchen Tag hast du Geburtstag?", required = True), jahr : Option(int, "In welchem Jahr hast du Geburtstag?", required = False, default = None)):
        await ctx.defer()
        if len(str(tag)) == 1:
            tag = str(tag)
            tag = f"0{tag}"
        bdaycollection.update_one({"_id" : ctx.author.id}, {"$set":{"date" : f"{monat}-{tag}", "Jahr" : jahr}})
        await ctx.respond("Ich werde mich nun an deinen **neuen** Geburtstag erinnern!")
    
    @slash_command(name='showallbirthdays', description='Lass dir alle Geburtstage anzeigen.')
    async def showallbirthday(self, ctx):
        await ctx.defer()
        message = ""
        allbdays = {}
        todaymonth = datetime.today().strftime('%m')
        todayday = datetime.today().strftime('%d')
        todayyear = datetime.today().strftime('%y')
        for member in ctx.guild.members:
            dt = None
            try:
                bday = bdaycollection.find_one({"_id" : member.id})
                dt = bday['date']
                month = dt[0:2]
                day = dt[3:]
                
                hasbirthday = True
                if int(month) > int(todaymonth):
                    hasbirthday = False
                elif int(month) == int(todaymonth):
                    if int(day) > int(todayday):
                        hasbirthday = False

                daystillbday = 0
                year = 0

                if hasbirthday == True:
                    year = int(todayyear) + 1
                else:
                    year = int(todayyear)

                daystillbday = date(int(year), int(month), int(day)) - date(int(todayyear), int(todaymonth), int(todayday))

                allbdays[member.id] = {"Anzahl" : int(daystillbday.days), "membermention" : member.mention, "bday" : f"{day}.{month}."}
            except:
                pass

        


        ranking = sorted(allbdays.items(),key=lambda x: x[1]["Anzahl"],reverse=False)

        for rank in ranking:

            try:
                rank = rank[1]
                message += f"{rank['membermention']} hat am {rank['bday']} Geburtstag (in {rank['Anzahl']} Tagen)\n\n" 
            except:
                pass
        if len(message) >= 4000:
            while len(message) >= 4000:
                embed = discord.Embed(title='Geburtstagsliste', description=message[0:4000], color=0xbd24e7)
                message = message[4000:]
                await ctx.respond(embed=embed)
            embed = discord.Embed(title='Geburtstagsliste', description=message, color=0xbd24e7)
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title='Geburtstagsliste', description=message, color=0xbd24e7)
            await ctx.respond(embed=embed)

    @slash_command(name='setbirthdayrole', description='Setze die Geburtstagsrolle fest')
    async def setbirthdayrole(self, ctx, role : Option(discord.Role, "Welche Rolle sollen Geburtstagsleute bekommen?", required = True)):
        await ctx.defer()
        await ctx.respond(f"{role.mention} wurde als Geburtstagsrolle gesetzt")
        bdaycollection.insert_one({"_id" : 1, "role" : role.id})

    @slash_command(name='sayhappybirthday', description='Sag jemandem herzlichen Glückwunsch')
    async def sayhappybirthday(self, ctx, member : Option(discord.Member, "Wer hat Geburtstag?", required = True), role : Option(discord.Role, "Welche Rolle sollen der User bekommen?", required = True)):
        await ctx.defer()
        channelBirthday = self.client.get_channel(int(923324287522324602))
        await channelBirthday.send(f"**HAPPY BIRTHDAY**\n{member.mention} hat heute Geburtstag. 🥳 Wir wünschen dir Alles Gute zum Geburtstag und einen tollen Tag :)")
        await member.add_roles(role)
        
    @tasks.loop(seconds = 60)
    async def checkforbirthday(self):
        today = datetime.today().strftime('%m-%d')
        x = datetime.now()
        print(x.hour)
        if x.hour == 0 and x.minute == 0:
            for guild in self.client.guilds:
                for member in guild.members:
                    try:
                        x = bdaycollection.find_one({"_id" : member.id})
                        roleCollect = bdaycollection.find_one({"_id" : 1})
                        role = get(guild.roles, id=roleCollect["role"])
                        if x['date'] == today:
                            try:
                                channelBirthday = self.client.get_channel(int(923324287522324602))
                                await channelBirthday.send(f"**HAPPY BIRTHDAY**\n{member.mention} hat heute Geburtstag. 🥳 Wir wünschen dir Alles Gute zum Geburtstag und einen tollen Tag :)")
                                await member.add_roles(role)
                            except:
                                raise
                        elif role in member.roles:
                            await member.remove_roles(role)
                    except:
                        if x == None:
                            pass
                        else:
                            raise



    @commands.Cog.listener()
    async def on_ready(self):
        self.checkforbirthday.start()


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
    client.add_cog(VorlageCog(client))