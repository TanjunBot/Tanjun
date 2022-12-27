from functools import cmp_to_key
import discord
from discord.commands import Option, slash_command
from discord.ext.commands import has_permissions
from discord.ext import commands, tasks
import json
import asyncio
from pymongo import MongoClient

cluster = MongoClient("")

db = cluster["Main"]
supportsettingscollection = db["supportsettings"]






class Support(commands.Cog):



    def __init__(self, client):
        self.client = client

    @has_permissions(manage_webhooks=True)
    @slash_command(name='addticket', description='Füge ein Ticketsystem hinzu, bei dem Ticket erstellt werden können!')
    async def addticket(self, ctx, channel : Option(discord.TextChannel, "Wo soll ich das Ticket erstellen?", required = True), titel : Option(str, "Worum geht es in dem Ticket?", required = True), beschreibung : Option(str, "Worum geht es genau in dem Ticket?", required = True), logchannel : Option(discord.TextChannel, "Wo sollen die Tickets abgespeichert werden?", required = True)):
        await ctx.defer()
        try:
            supportsaves = supportsettingscollection.find_one({"_id" : ctx.guild.id})
            if supportsaves == None:
                supportsaves = {}
        except:
            supportsaves = {}
        
        supportsaves[str(ctx.guild.id)] = dict(supportsaves)


        await ctx.send("Bitte schreibe nun eine Nachricht, die Gesendet werden soll, wenn jemand ein Ticket erstellt. Wenn du den Ticket ersteller pingen möchtest, schreibe uuu")
        try:
            startnachricht = await self.client.wait_for('message', timeout=120, check=lambda message: message.author == ctx.author)
            myEmbed = discord.Embed(title=titel, description=f"{beschreibung}\nReagiere jetzt mit 📩 um ein Ticket zu erstellen.",color=0xbd24e7)
            ticketmsg = await channel.send(embed = myEmbed)
            await ticketmsg.add_reaction("📩")
            try:
                supportsaves[str(ctx.guild.id)]
            except:
                supportsaves[str(ctx.guild.id)] = {}
            
            try:
                supportsaves[str(ctx.guild.id)][str(ticketmsg.id)]
            except:
                supportsaves[str(ctx.guild.id)][str(ticketmsg.id)] = {}
            supportsaves[str(ctx.guild.id)][str(ticketmsg.id)] = {"titel" : titel, "beschreibung" : beschreibung, "categoryid" : channel.category.id, "startnachricht" : startnachricht.content, "logchannel" : logchannel.id}
            await ctx.send("Erfolgreich")
        except asyncio.TimeoutError:
            await ctx.send("Timeout. Die eingabe wurde abgebrochen.")
            return

        
        try:
            supportsettingscollection.update_one({"_id" : ctx.guild.id}, {"$set" : supportsaves[str(ctx.guild.id)]}, upsert=True)
        except:
            supportsaves[str(ctx.guild.id)]["_id"] = ctx.guild.id
            supportsettingscollection.insert_one(supportsaves[str(ctx.guild.id)])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot == True:
            return


        try:
            supportsaves = supportsettingscollection.find_one({"_id" : payload.guild_id})
            if supportsaves == None:
                supportsaves = {}
        except:
            supportsaves = {}
        
        supportsaves[str(payload.guild_id)] = dict(supportsaves)
            
        for s in supportsaves[str(payload.guild_id)]:
            try:
                if int(s) == payload.message_id:
                    chan = self.client.get_channel(payload.channel_id)
                    msg = await chan.fetch_message(payload.message_id)
                    await msg.remove_reaction(payload.emoji, payload.member)
                    channel = self.client.get_channel(supportsaves[str(payload.guild_id)][s]["categoryid"])
                    ticketchan = await channel.create_text_channel(name = f"{supportsaves[str(payload.guild_id)][s]['titel']} Ticket {payload.member}", topic = f"{payload.member.id} {supportsaves[str(payload.guild_id)][s]['logchannel']}")
                    await ticketchan.edit(sync_permissions = True)
                    await ticketchan.set_permissions(payload.member,read_messages=True,send_messages=True)
                    myEmbed = discord.Embed(description="❌ = Ticket Schließen\n",color=0xbd24e7)
                    msg = await ticketchan.send(content = supportsaves[str(payload.guild_id)][s]["startnachricht"].replace("uuu", payload.member.mention), embed =  myEmbed)
                    
                    supportsaves[str(payload.guild_id)]["messages"].append(msg.id)
                    await msg.add_reaction("❌")
                    try:
                        supportsettingscollection.update_one({"_id" : payload.guild_id}, {"$set" : supportsaves[str(payload.guild_id)]}, upsert=True)
                    except:
                        supportsaves[str(payload.guild_id)]["_id"] = payload.guild_id
                        supportsettingscollection.insert_one(supportsaves[str(payload.guild_id)])
                    return
            except:
                pass
        try:
            supportsaves[str(payload.guild_id)]
        except:
            supportsaves[str(payload.guild_id)] = {}
        
        try:
            supportsaves[str(payload.guild_id)]["messages"]
        except:
            supportsaves[str(payload.guild_id)]["messages"] = []

        for s in supportsaves[str(payload.guild_id)]["messages"]:
            try:
                if int(s) == payload.message_id:
                    if payload.emoji.name == "❌":
                        channel = self.client.get_channel(payload.channel_id)
                        await channel.set_permissions(payload.member,read_messages=False,send_messages=False)
                        myEmbed = discord.Embed(description="Das Ticket kann jetzt abgespeichert werden.\n♻️ = Ticket Speichern\n",color=0xbd24e7)
                        msg = await channel.send(embed = myEmbed)
                        supportsaves[str(payload.guild_id)]["messages"].append(msg.id)
                        await msg.add_reaction("♻️")
                    if payload.emoji.name == "♻️":
                        channel = self.client.get_channel(payload.channel_id)
                        x = channel.topic.split(" ")
                        creator = x[0].replace(" ", "")
                        logchannelid = x[1].replace(" ", "")
                        user = self.client.get_user(int(creator))
                        file = await createhtml(channel, user)
                        logchannel = self.client.get_channel(int(logchannelid))
                        await logchannel.send(file=discord.File(f'{file}'), content = f"Hier ist eine Zusammenfassung des Tickets mit {user.mention}.")
                        await channel.delete()
            except:
                pass
        try:
            supportsettingscollection.update_one({"_id" : payload.guild_id}, {"$set" : supportsaves[str(payload.guild_id)]}, upsert=True)
        except:
            supportsaves[str(payload.guild_id)]["_id"] = payload.guild_id
            supportsettingscollection.insert_one(supportsaves[str(payload.guild_id)])

                    




async def createhtml(channel, ticketcreator):
    filecontent = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <style type = "text/css">

body{
    background-color: black;
    color: white;

    font-family: Arial, Helvetica, sans-serif;

    font-size: 16px;
    font-weight: normal;
    /* Same as above */
    font: normal 16px Arial, Helvetica, sans-serif;

    line-height: 1.6em;
    margin: 0;
}



.container{
    width: 90%;
    margin: auto;
    margin-bottom: 10;
}


img {
  border-radius: 50%;
}

.block{
    float:left;
    width: 100%;
    border: 1px solid #ccc;
    padding: 10px;
    box-sizing: border-box;
    border: 1px lightgray solid;
    border-radius: 15px;
}

#Main-Footer{
                text-align: center;
                font-size: 18px;
            }


.pfpleft{
    float: left;
}
.Textleft{
    float: left;
    font-size: 40px;
}

.pfpright{
    float: right;
}
.Textright{
    float: right;
    font-size: 40px;
}

.inhaltleft{
    float: left;
    font-size: 25px;
}

.fix-me{
    position: fixed;
    bottom:10;
    align-self: center;
    color: white;
    background-color: black;
    border: 1px solid black;
    border-radius: 15px;
}

.inhalright{
    float: right;
    font-size: 25px;
}
    </style>
    <title>Ticket</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <a class = "fix-me button"href="https://waa.ai/qe7K">Tanjun Discord Bot Support</a>
    <div class = "container">

    """

    messages = await channel.history(limit=1000).flatten()
    messages.reverse()
    for message in messages:
        content = message.content
        if not content == "":
            text = ""
            inhalt = ""
            if message.author == ticketcreator:
                text = "Textleft"
                inhalt = "inhaltleft"
                pfp = "pfpleft"
            else:
                text = "Textright"
                inhalt = "inhalright"
                pfp = "pfpright"

            filecontent += f'''
            <div class="block">
            <div>
                <div class = "mleft">
                    <img src="{message.author.avatar.url}" alt="My Sample Image" width="60" class = "{pfp}">
                    <br>
                    <br>
                    <br>
                    <div class = "{str(text)}">{str(message.author)}</div>
                    <br>
                    <p class = "{str(inhalt)}">{str(message.content)}</p>
                    <br>
                </div>
            </div>
            <br>
            <br>
            <br>
                
        </div>
        <br>
        <br>
            '''
            


    filecontent += """

        </div>
    
    </div>


</body>
</html>
    """
    f = open("Ticket.html","w")
    f.close()
    f = open("Ticket.html", "a", encoding="utf-8")
    f.write(filecontent)
    f.close()
    return "Ticket.html"
            





def setup(client):
    client.add_cog(Support(client))