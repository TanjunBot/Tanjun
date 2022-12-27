from pydoc import describe
import discord
from discord.ext import commands, tasks
from discord.commands import Option, slash_command
import random
import json

from pymongo import MongoClient


cluster = MongoClient("")

db = cluster["Main"]
snakecollection = db["cate"]
quizcollection = db["Quiz"]
tanjunocollection = db["Tanjuno"]
tanjnitecollection = db["Tanjnite"]



class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
          

    möglichkeitenArt = [
        discord.OptionChoice(name = "Hintergrund Skin kaufen", value = "0"),
        discord.OptionChoice(name = "Katzen Skin kaufen", value = "1"),
        discord.OptionChoice(name = "Essen Skin kaufen", value = "2"),
        discord.OptionChoice(name = "Hintergrund Skin ändern", value = "3"),
        discord.OptionChoice(name = "Katzen Skin ändern", value = "4"),
        discord.OptionChoice(name = "Essen Skin ändern", value = "5"),

    ]

    @slash_command(name='cateshop', description='Kaufe neue Skins und ändere deine Aktuellen Skins!')
    async def cateshop(self, ctx, mode : Option(str, "Möchtest du die Nachrichten löschen?", required = True, choices = möglichkeitenArt)):
        await ctx.defer()
        x = snakecollection.find_one({"_id" : ctx.author.id})

        if x == None:
            await ctx.respond("Bitte spiele zuerst mindestens eine Runde cate. Benutze dazu den `/cate` Befehl!", ephemeral=True)
            return

        if mode == "0":
            class Dropdown(discord.ui.Select):
                def __init__(self):
                    options = [
                        discord.SelectOption(label = "Kosten: 10", emoji = "🟫", value="🟫"),
                        discord.SelectOption(label = "Kosten: 50", emoji = "🟦", value="🟦"),
                        discord.SelectOption(label = "Kosten: 100", emoji = "🟧", value="🟧"),
                        discord.SelectOption(label = "Kosten: 300", emoji = "🔲", value="🔲"),
                        discord.SelectOption(label = "Kosten: 500", emoji = "⬛", value="⬛"),
                        discord.SelectOption(label = "Premium Only", emoji = "❎", value="❎"),
                        discord.SelectOption(label = "Premium Only", emoji = "🟪", value="🟪"),
                        discord.SelectOption(label = "Premium Only", emoji = "⏹", value="⏹")
                    ]
                
                    super().__init__(
                        placeholder="Wähle den Skin aus, den du kaufen möchtest.",
                        min_values=1,
                        max_values=1,
                        options=options
                    )

                async def callback(select, interaction : discord.Interaction):

                    if interaction.user.id != ctx.author.id:
                        await interaction.response.send_message("Du kannst das hier nicht tun. Bitte gehe selbst mit den `/cateshop` Befhel einkaufen!", ephemeral=True)
                        return

                    if select.values[0] == "🟫":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 10:
                            if "🟫" not in inventory:
                                coins -= 10
                                inventory.append("🟫")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🟦":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 50:
                            if "🟦" not in inventory:
                                coins -= 50
                                inventory.append("🟦")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🟧":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 100:
                            if "🟧" not in inventory:
                                coins -= 100
                                inventory.append("🟧")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🔲":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 300:
                            if "🔲" not in inventory:
                                coins -= 300
                                inventory.append("🔲")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "⬛":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 500:
                            if "⬛" not in inventory:
                                coins -= 500
                                inventory.append("⬛")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()


                    self.add_item(Dropdown())

            view = DropdownView()

            await ctx.respond(content = f"Bitte wähle aus, was du Kaufen möchtest!\nDu hast momentan {x['coins']} Coins!", view = view, ephemeral=True)

        if mode == "1":
            class Dropdown(discord.ui.Select):
                def __init__(self):
                    options = [
                        discord.SelectOption(label = "Kosten: 15", emoji = "😸", value="😸"),
                        discord.SelectOption(label = "Kosten: 35", emoji = "😳", value="😳"),
                        discord.SelectOption(label = "Kosten: 75", emoji = "😍", value="😍"),
                        discord.SelectOption(label = "Kosten: 150", emoji = "🐶", value="🐶"),
                        discord.SelectOption(label = "Kosten: 500", emoji = "🤡", value="🤡"),
                        discord.SelectOption(label = "Premium Only", emoji = "🤖", value="🤖"),
                        discord.SelectOption(label = "Premium Only", emoji = "🦊", value="🦊"),
                        discord.SelectOption(label = "Premium Only", emoji = "🥶", value="🥶"),
                        discord.SelectOption(label = "Premium Only", emoji = "😨", value="😨"),
                        discord.SelectOption(label = "Premium Only", emoji = "👾", value="👾"),
                        discord.SelectOption(label = "Premium Only", emoji = "💀", value="💀")
                    ]
                
                    super().__init__(
                        placeholder="Wähle den Skin aus, den du kaufen möchtest.",
                        min_values=1,
                        max_values=1,
                        options=options
                    )

                async def callback(select, interaction : discord.Interaction):

                    if interaction.user.id != ctx.author.id:
                        await interaction.response.send_message("Du kannst das hier nicht tun. Bitte gehe selbst mit den `/cateshop` Befhel einkaufen!", ephemeral=True)
                        return

                    if select.values[0] == "😸":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 15:
                            if "😸" not in inventory:
                                coins -= 15
                                inventory.append("😸")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "😳":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 35:
                            if "😳" not in inventory:
                                coins -= 35
                                inventory.append("😳")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "😍":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 75:
                            if "😍" not in inventory:
                                coins -= 75
                                inventory.append("😍")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🐶":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 150:
                            if "🐶" not in inventory:
                                coins -= 150
                                inventory.append("🐶")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🤡":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 500:
                            if "🤡" not in inventory:
                                coins -= 500
                                inventory.append("🤡")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()


                    self.add_item(Dropdown())

            view = DropdownView()

            await ctx.respond(content = f"Bitte wähle aus, was du Kaufen möchtest!\nDu hast momentan {x['coins']} Coins!", view = view, ephemeral=True)

        if mode == "2":
            class Dropdown(discord.ui.Select):
                def __init__(self):
                    options = [
                        discord.SelectOption(label = "Kosten: 20", emoji = "🍕", value="🍕"),
                        discord.SelectOption(label = "Kosten: 35", emoji = "🍤", value="🍤"),
                        discord.SelectOption(label = "Kosten: 75", emoji = "🎂", value="🎂"),
                        discord.SelectOption(label = "Kosten: 150", emoji = "🧀", value="🧀"),
                        discord.SelectOption(label = "Kosten: 500", emoji = "🍙", value="🍙"),
                        discord.SelectOption(label = "Premium Only", emoji = "🍇", value="🍇"),
                        discord.SelectOption(label = "Premium Only", emoji = "🌭", value="🌭"),
                        discord.SelectOption(label = "Premium Only", emoji = "🥐", value="🥐"),
                        discord.SelectOption(label = "Premium Only", emoji = "🌮", value="🌮"),
                        discord.SelectOption(label = "Premium Only", emoji = "🥓", value="🥓"),
                        discord.SelectOption(label = "Premium Only", emoji = "🍑", value="🍑"),
                        discord.SelectOption(label = "Premium Only", emoji = "🥩", value="🥩") 
                    ]
                
                    super().__init__(
                        placeholder="Wähle den Skin aus, den du kaufen möchtest.",
                        min_values=1,
                        max_values=1,
                        options=options
                    )

                async def callback(select, interaction : discord.Interaction):

                    if interaction.user.id != ctx.author.id:
                        await interaction.response.send_message("Du kannst das hier nicht tun. Bitte gehe selbst mit den `/cateshop` Befhel einkaufen!", ephemeral=True)
                        return

                    if select.values[0] == "🍕":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 20:
                            if "🍕" not in inventory:
                                coins -= 20
                                inventory.append("🍕")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🍤":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 35:
                            if "🍤" not in inventory:
                                coins -= 35
                                inventory.append("🍤")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🎂":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 75:
                            if "🎂" not in inventory:
                                coins -= 75
                                inventory.append("🎂")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🧀":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 150:
                            if "🧀" not in inventory:
                                coins -= 150
                                inventory.append("🧀")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)

                    elif select.values[0] == "🍙":
                        coins = x["coins"]
                        inventory = x["inventory"]
                        if coins >= 500:
                            if "🍙" not in inventory:
                                coins -= 500
                                inventory.append("🍙")
                                snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"cons" : coins, "inventory" : inventory}})
                                await interaction.response.send_message("Du hast das Item erfolgreich gekauft! Rüste es doch gleich aus, indem du erneut den `/cateshop` Befehl ausführst!", ephemeral=True)
                            else:
                                await interaction.response.send_message("Du hast dieses Item bereits. Bitte wähle ein anderes aus.", ephemeral=True)
                        else:
                            await interaction.response.send_message("Du hast nicht genug Geld für dieses Item.", ephemeral=True)



            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()


                    self.add_item(Dropdown())

            view = DropdownView()

            await ctx.respond(content = f"Bitte wähle aus, was du Kaufen möchtest!\nDu hast momentan {x['coins']} Coins!", view = view, ephemeral=True)

        if mode == "3":
            class Dropdown(discord.ui.Select):
                def __init__(self):
                    options = [
                    ]

                    inv = x["inventory"]

                    if "🟫" in inv:
                        options.append(discord.SelectOption(label = "🟫", value="🟫"))
                    if "🟦" in inv:
                        options.append(discord.SelectOption(label = "🟦", value="🟦"))
                    if "🟧" in inv:
                        options.append(discord.SelectOption(label = "🟧", value="🟧"))
                    if "🔲" in inv:
                        options.append(discord.SelectOption(label = "🔲", value="🔲"))
                    if "⬛" in inv:
                        options.append(discord.SelectOption(label = "⬛", value="⬛"))
                    if "❎" in inv:
                        options.append(discord.SelectOption(label = "❎", value="❎"))
                    if "🟪" in inv:
                        options.append(discord.SelectOption(label = "🟪", value="🟪"))
                    if "⏹" in inv:
                        options.append(discord.SelectOption(label = "⏹", value="⏹"))
                    

                
                    super().__init__(
                        placeholder="Wähle den Skin aus, den du Auswählen möchtest.",
                        min_values=1,
                        max_values=1,
                        options=options
                    )

                async def callback(select, interaction : discord.Interaction):

                    if interaction.user.id != ctx.author.id:
                        await interaction.response.send_message("Du kannst das hier nicht tun. Bitte gehe selbst mit den `/cateshop` Befhel einkaufen!", ephemeral=True)
                        return
                    
                    snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"backgroundskin" : select.values[0]}})

                    await interaction.response.send_message(f"Du hast erfolgreich {select.values[0]} als Hintergrundskin ausgewählt!", ephemeral=True)

            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()


                    self.add_item(Dropdown())

            view = DropdownView()

            await ctx.respond(content = f"Bitte wähle aus, was du benutzen möchtest!", view = view, ephemeral=True)

        if mode == "4":
            class Dropdown(discord.ui.Select):
                def __init__(self):
                    options = [
                    ]

                    inv = x["inventory"]

                    if "😸" in inv:
                        options.append(discord.SelectOption(label = "😸", value="😸"))
                    if "😳" in inv:
                        options.append(discord.SelectOption(label = "😳", value="😳"))
                    if "😍" in inv:
                        options.append(discord.SelectOption(label = "😍", value="😍"))
                    if "🐶" in inv:
                        options.append(discord.SelectOption(label = "🐶", value="🐶"))
                    if "🤡" in inv:
                        options.append(discord.SelectOption(label = "🤡", value="🤡"))
                    if "🤖" in inv:
                        options.append(discord.SelectOption(label = "🤖", value="🤖"))
                    if "🦊" in inv:
                        options.append(discord.SelectOption(label = "🦊", value="🦊"))
                    if "🥶" in inv:
                        options.append(discord.SelectOption(label = "🥶", value="🥶"))
                    if "😨" in inv:
                        options.append(discord.SelectOption(label = "😨", value="😨"))
                    if "👾" in inv:
                        options.append(discord.SelectOption(label = "👾", value="👾"))
                    if "💀" in inv:
                        options.append(discord.SelectOption(label = "💀", value="💀"))
                    

                
                    super().__init__(
                        placeholder="Wähle den Skin aus, den du Auswählen möchtest.",
                        min_values=1,
                        max_values=1,
                        options=options
                    )

                async def callback(select, interaction : discord.Interaction):

                    if interaction.user.id != ctx.author.id:
                        await interaction.response.send_message("Du kannst das hier nicht tun. Bitte gehe selbst mit den `/cateshop` Befhel einkaufen!", ephemeral=True)
                        return
                    
                    snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"catskin" : select.values[0]}})

                    await interaction.response.send_message(f"Du hast erfolgreich {select.values[0]} als Katzenskin ausgewählt!", ephemeral=True)

            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()


                    self.add_item(Dropdown())

            view = DropdownView()

            await ctx.respond(content = f"Bitte wähle aus, was du benutzen möchtest!", view = view, ephemeral=True)

        if mode == "5":
            class Dropdown(discord.ui.Select):
                def __init__(self):
                    options = [
                    ]

                    inv = x["inventory"]

                    if "🍕" in inv:
                        options.append(discord.SelectOption(label = "🍕", value="🍕"))
                    if "🍤" in inv:
                        options.append(discord.SelectOption(label = "🍤", value="🍤"))
                    if "🎂" in inv:
                        options.append(discord.SelectOption(label = "🎂", value="🎂"))
                    if "🧀" in inv:
                        options.append(discord.SelectOption(label = "🧀", value="🧀"))
                    if "🍙" in inv:
                        options.append(discord.SelectOption(label = "🍙", value="🍙"))
                    if "🍇" in inv:
                        options.append(discord.SelectOption(label = "🍇", value="🍇"))
                    if "🌭" in inv:
                        options.append(discord.SelectOption(label = "🌭", value="🌭"))
                    if "🥐" in inv:
                        options.append(discord.SelectOption(label = "🥐", value="🥐"))
                    if "🌮" in inv:
                        options.append(discord.SelectOption(label = "🌮", value="🌮"))
                    if "🥓" in inv:
                        options.append(discord.SelectOption(label = "🥓", value="🥓"))
                    if "🍑" in inv:
                        options.append(discord.SelectOption(label = "🍑", value="🍑"))
                    if "🥩" in inv:
                        options.append(discord.SelectOption(label = "🥩", value="🥩"))
                    

                
                    super().__init__(
                        placeholder="Wähle den Skin aus, den du Auswählen möchtest.",
                        min_values=1,
                        max_values=1,
                        options=options
                    )

                async def callback(select, interaction : discord.Interaction):

                    if interaction.user.id != ctx.author.id:
                        await interaction.response.send_message("Du kannst das hier nicht tun. Bitte gehe selbst mit den `/cateshop` Befhel einkaufen!", ephemeral=True)
                        return
                    
                    snakecollection.update_one({"_id" : ctx.author.id}, {"$set" : {"Foodskin" : select.values[0]}})

                    await interaction.response.send_message(f"Du hast erfolgreich {select.values[0]} als Essensskin ausgewählt!", ephemeral=True)

            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()


                    self.add_item(Dropdown())

            view = DropdownView()

            await ctx.respond(content = f"Bitte wähle aus, was du benutzen möchtest!", view = view, ephemeral=True)


    @slash_command(name='tic-tac-toe', description='Spiele Tic-Tac-Toe gegen jemanden!')
    async def TicTacToe(self, ctx, user : Option(discord.Member, "Gegen wen möchtest du spielen?", required = False, default = None)):
        await ctx.defer()
        message = None
        movenow = ctx.author.id
        if user.bot ==True:
            user = None
        if user != None:
            x = random.randint(1, 2)
            if x == 1:
                movenow = ctx.author.id#
            else:
                movenow = user.id

        async def printBoard(board, mes = None):
            if mes == None:
                view = discord.ui.View()
                btn = discord.ui.Button(label = board[1], style = discord.ButtonStyle.blurple, disabled=board[1] != " ", row = 1, custom_id = str(0))
                btn.callback = playerMove
                btn2 = discord.ui.Button(label = board[2], style = discord.ButtonStyle.blurple, disabled=board[2] != " ", row = 1, custom_id = str(1))
                btn2.callback = playerMove
                btn3 = discord.ui.Button(label = board[3], style = discord.ButtonStyle.blurple, disabled=board[3] != " ", row = 1, custom_id = str(2))
                btn3.callback = playerMove
                btn4 = discord.ui.Button(label = board[4], style = discord.ButtonStyle.blurple, disabled=board[4] != " ", row = 2, custom_id = str(3))
                btn4.callback = playerMove
                btn5 = discord.ui.Button(label = board[5], style = discord.ButtonStyle.blurple, disabled=board[5] != " ", row = 2, custom_id = str(4))
                btn5.callback = playerMove
                btn6 = discord.ui.Button(label = board[6], style = discord.ButtonStyle.blurple, disabled=board[6] != " ", row = 2, custom_id = str(5))
                btn6.callback = playerMove
                btn7 = discord.ui.Button(label = board[7], style = discord.ButtonStyle.blurple, disabled=board[7] != " ", row = 3, custom_id = str(6))
                btn7.callback = playerMove
                btn8 = discord.ui.Button(label = board[8], style = discord.ButtonStyle.blurple, disabled=board[8] != " ", row = 3, custom_id = str(7))
                btn8.callback = playerMove
                btn9 = discord.ui.Button(label = board[9], style = discord.ButtonStyle.blurple, disabled=board[9] != " ", row = 3, custom_id = str(8))
                btn9.callback = playerMove
                view.add_item(btn)
                view.add_item(btn2)
                view.add_item(btn3)
                view.add_item(btn4)
                view.add_item(btn5)
                view.add_item(btn6)
                view.add_item(btn7)
                view.add_item(btn8)
                view.add_item(btn9)
            else:
                view = discord.ui.View()
                btn = discord.ui.Button(label = board[1], style = discord.ButtonStyle.blurple, disabled=True, row = 1, custom_id = str(0))
                btn.callback = playerMove
                btn2 = discord.ui.Button(label = board[2], style = discord.ButtonStyle.blurple, disabled=True, row = 1, custom_id = str(1))
                btn2.callback = playerMove
                btn3 = discord.ui.Button(label = board[3], style = discord.ButtonStyle.blurple, disabled=True, row = 1, custom_id = str(2))
                btn3.callback = playerMove
                btn4 = discord.ui.Button(label = board[4], style = discord.ButtonStyle.blurple, disabled=True, row = 2, custom_id = str(3))
                btn4.callback = playerMove
                btn5 = discord.ui.Button(label = board[5], style = discord.ButtonStyle.blurple, disabled=True, row = 2, custom_id = str(4))
                btn5.callback = playerMove
                btn6 = discord.ui.Button(label = board[6], style = discord.ButtonStyle.blurple, disabled=True, row = 2, custom_id = str(5))
                btn6.callback = playerMove
                btn7 = discord.ui.Button(label = board[7], style = discord.ButtonStyle.blurple, disabled=True, row = 3, custom_id = str(6))
                btn7.callback = playerMove
                btn8 = discord.ui.Button(label = board[8], style = discord.ButtonStyle.blurple, disabled=True, row = 3, custom_id = str(7))
                btn8.callback = playerMove
                btn9 = discord.ui.Button(label = board[9], style = discord.ButtonStyle.blurple, disabled=True, row = 3, custom_id = str(8))
                btn9.callback = playerMove
                view.add_item(btn)
                view.add_item(btn2)
                view.add_item(btn3)
                view.add_item(btn4)
                view.add_item(btn5)
                view.add_item(btn6)
                view.add_item(btn7)
                view.add_item(btn8)
                view.add_item(btn9)

        

            
            nonlocal message
            nonlocal movenow
            if mes == None:
                if message == None:
                    if user == None:
                        message = await ctx.send(f"Klicke um zu spielen {ctx.author.mention}.", view = view)
                    else:
                        if movenow == ctx.author.id:
                            movenow = user.id
                        else:
                            movenow = ctx.author.id
                        if movenow == ctx.author.id:
                            message = await ctx.send(f"Klicke um zu spielen!\n <@{movenow}> ist dran! Dein Zeichen: {player}", view = view)
                        else:
                            message = await ctx.send(f"Klicke um zu spielen!\n <@{movenow}> ist dran! Dein Zeichen: {bot}", view = view)
                else:
                    if user != None:
                        if movenow == ctx.author.id:
                            await message.edit(f"Klicke um zu spielen!\n <@{movenow}> ist dran! Dein Zeichen: {player}", view = view)
                        else:
                            await message.edit(f"Klicke um zu spielen!\n <@{movenow}> ist dran! Dein Zeichen: {bot}", view = view)
                    else:
                        await message.edit(f"Klicke um zu spielen {ctx.author.mention}.", view = view)
            else:
                await message.edit(content = mes, view = view)

        def spaceIsFree(position):
            if board[position] == ' ':
                return True
            else:
                return False


        async def insertLetter(letter, position):
            nonlocal movenow
            if spaceIsFree(position):
                nonlocal message
                board[position] = letter
                await printBoard(board)
                if (checkDraw()):
                    
                    view = discord.ui.View()
                    await printBoard(board=board, mes = "Unentschieden <:P_Shrug:959817497882808342>")
                if checkForWin():
                    if letter == 'X':
                        view = discord.ui.View()
                        if user == None:
                            await printBoard(board=board, mes = "Ich habe gewonnen! <a:P_Dabb:967358076099375154>")
                        else:
                            await printBoard(board=board, mes = "Ich habe gewonnen! <a:P_Dabb:967358076099375154>")

                    else:
                        view = discord.ui.View()
                        if user == None:
                            await printBoard(board=board, mes = "Ich habe gewonnen! <a:P_Dabb:967358076099375154>")
                        else:
                            if movenow == ctx.author.id:
                                movenow = user.id
                            else:
                                movenow = ctx.author.id
                            await printBoard(board=board, mes = f"<@{movenow}> hat gewonnen <:P_Squirrel:954472809084620800>")

                return


            else:
                await message.edit("Öhm..")
                return


        def checkForWin():
            if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
                return True
            elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
                return True
            elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
                return True
            elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
                return True
            elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
                return True
            elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
                return True
            elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
                return True
            elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
                return True
            else:
                return False


        def checkWhichMarkWon(mark):
            if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
                return True
            elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
                return True
            elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
                return True
            elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
                return True
            elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
                return True
            elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
                return True
            elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
                return True
            elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
                return True
            else:
                return False


        def checkDraw():
            for key in board.keys():
                if (board[key] == ' '):
                    return False
            return True


        async def playerMove(interaction):
            if user == None:
                if interaction.user.id == ctx.author.id:
                    print(interaction)
                    print(interaction.custom_id)
                    position = int(interaction.custom_id) + 1
                    print(position)
                    await insertLetter(player, position)
                    await compMove()
                    return
                else:
                    await interaction.response.send_message("Nicht dein Spiel! Benutze den /tic-tac-toe Befehl um selbst zu spielen!", ephemeral = True)
            else:
                nonlocal movenow
                if interaction.user.id == movenow:
                    if movenow == user.id:
                        if movenow == ctx.author.id:
                            movenow = user.id
                        else:
                            movenow = ctx.author.id
                        print(interaction)
                        print(interaction.custom_id)
                        position = int(interaction.custom_id) + 1
                        print(position)
                        await insertLetter(bot, position)
                    else:
                        if movenow == ctx.author.id:
                            movenow = user.id
                        else:
                            movenow = ctx.author.id
                        print(interaction)
                        print(interaction.custom_id)
                        position = int(interaction.custom_id) + 1
                        print(position)
                        await insertLetter(player, position)

                else:
                    await interaction.response.send_message("Du bist nicht dran!", ephemeral = True)


        async def compMove():
            bestScore = -800
            bestMove = 0
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = bot
                    score = minimax(board, 0, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
                        bestMove = key

            await insertLetter(bot, bestMove)
            return


        def minimax(board, depth, isMaximizing):
            if (checkWhichMarkWon(bot)):
                return 1
            elif (checkWhichMarkWon(player)):
                return -1
            elif (checkDraw()):
                return 0

            if (isMaximizing):
                bestScore = -800
                for key in board.keys():
                    if (board[key] == ' '):
                        board[key] = bot
                        score = minimax(board, depth + 1, False)
                        board[key] = ' '
                        if (score > bestScore):
                            bestScore = score
                return bestScore

            else:
                bestScore = 800
                for key in board.keys():
                    if (board[key] == ' '):
                        board[key] = player
                        score = minimax(board, depth + 1, True)
                        board[key] = ' '
                        if (score < bestScore):
                            bestScore = score
                return bestScore


        board = {1: ' ', 2: ' ', 3: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 7: ' ', 8: ' ', 9: ' '}

        player = '⭕'
        bot = '❌'

        await printBoard(board)
        await ctx.respond("Du hast erfolgreich Tic-Tac-Toe gestartet!", ephemeral=True)

    actions = [
        discord.OptionChoice(name = "Quiz Spielen", value = "play"),
        discord.OptionChoice(name = "Quiz auswerten (geht nur als ersteller des Quizzes)", value = "auswerten"),
        discord.OptionChoice(name = "Quiz bearbeiten (geht nur als ersteller des Quizzes)", value = "edit")
    ]

    @slash_command(name='quiz', description='Benutze das Tanjun Quiz-System')
    async def quiz(self, ctx, action : Option(str, "Was möchtest du machen?", required = True, choices = actions), quizid : Option(int, "Welche ID hat das Quiz?", required = True)):
        await ctx.defer(ephemeral = True)
        if action == "play":
            quiz = quizcollection.find_one({"_id" : quizid})
            if quiz == None:
                await ctx.respond(content = f"Es gibt kein Quiz mit dieser ID.")
                return
            try:
                playedby = quiz["playedby"]
            except:
                playedby = []
    
            if ctx.author.id in playedby:
                await ctx.respond(content = "Du hast dieses Quiz schon einmal gespielt.")
                return
            
            fragenanzahl = quiz["Fragen"]
    
            inter = None
    
            punkte = 0
    
            nextquestion = False
            message = None
            async def questioneer(fragenummer, inter = None):
            
                options = []
                c = 0
                for wrongawnser in quiz[str(fragenummer)]["wrongawnsers"]:
                    c += 1
                    options.append(discord.SelectOption(label = wrongawnser, value=f"-{c}"))
    
                for rightawnsers in quiz[str(fragenummer)]["rightawnsers"]:
                    c += 1
                    options.append(discord.SelectOption(label = rightawnsers, value=f"+{c}"))
    
                class Dropdown(discord.ui.Select):
                    def __init__(self):
                        random.shuffle(options)
                        super().__init__(
                            placeholder="Bitte wähle deine Antwort aus",
                            min_values=1,
                            max_values=1,
                            options=options
                        )
    
                    async def callback(select, interaction):
                        nonlocal punkte
                        if fragenummer + 1 == fragenanzahl:
                            if select.values[0][0] == "+":
                                punkte += 1
                            await ctx.send(content = f"{ctx.author.mention} hat das Quiz {quiz['title']} Erfolgreich gespielt und hat {punkte} / {fragenummer + 1} Punkte erreicht!")
                            quizcollection.update_one({"_id" : quizid}, {"$addToSet" : {"playedby" : ctx.author.id}}, upsert = True)
                            quizcollection.update_one({"_id" : quizid}, {"$set" : {f"points.{ctx.author.id}" : punkte}}, upsert = True)
                        else:
                            if select.values[0][0] == "+":
                                punkte += 1
                            await questioneer(fragenummer=fragenummer + 1, inter = interaction)
    
                class DropdownView(discord.ui.View):
                    def __init__(self):
                        super().__init__()
    
                        self.add_item(Dropdown())
    
                view = DropdownView()
                nonlocal message
                if message == None:
                    message = await ctx.respond(content = quiz[str(fragenummer)]["question"], view = view)
                else:
                    await message.edit(content = quiz[str(fragenummer)]["question"], view = view)
    
            await questioneer(0)

        if action == "auswerten":
            quiz = quizcollection.find_one({"_id" : quizid})
            if quiz == None:
                await ctx.respond(content = f"Es gibt kein Quiz mit dieser ID.", ephemeral=True)
                return
    
            if quiz["ersteller"] != ctx.author.id:
                await ctx.respond(content = f"Du hast dieses Quiz nicht erstellt.", ephemeral=True)
                return
            
            txt = ""
    
            awnsers = quiz["points"]
    
            txt += f"Das Quiz wurde `{len(awnsers)}` mal gespielt.\n\n"
    
            sort_orders = sorted(awnsers.items(), key=lambda x: x[1], reverse=True)
    
            c = 0
            for i in sort_orders:
                c += 1
                txt += f"`platz {c}`: <@{i[0]}> mit {i[1]} Punkten\n"
    
    
            myEmbed = discord.Embed(title = f"Auswertung des Quizzes {quiz['title']}", description=txt, color=0xbd24e7)
    
            await ctx.respond(embed = myEmbed, ephemeral=True)

        if action == "edit":
            quiz = quizcollection.find_one({"_id" : quizid})
            if quiz == None:
                await ctx.respond(content = f"Es gibt kein Quiz mit dieser ID.", ephemeral=True)
                return
    
            if quiz["ersteller"] != ctx.author.id:
                await ctx.respond(content = f"Du hast dieses Quiz nicht erstellt.", ephemeral=True)
                return
        
            options = []
            c = 0
    
            myEmbed = discord.Embed(title = f"Quiz `{quiz['title']}` Bearbeiten",color=0xbd24e7)
            for fragenummer in range(quiz["Fragen"]):
                
                options.append(discord.SelectOption(label = quiz[str(fragenummer)]["question"], value=f"{fragenummer}"))
    
                value = "Falsche Antworten:\n"
                for awnser in quiz[str(fragenummer)]["wrongawnsers"]:
                    value += f"{awnser}\n"
                value += "\n\nRichtige Antworten:\n"
                for awnser in quiz[str(fragenummer)]["rightawnsers"]:
                    value += f"{awnser}\n"
    
    
                myEmbed.add_field(name = quiz[str(fragenummer)]["question"], value = value, inline = False)
    
            class Dropdown(discord.ui.Select):
                def __init__(self):
                    super().__init__(
                        placeholder="Welche Frage möchtest du bearbeiten?",
                        min_values=1,
                        max_values=1,
                        options=options
                    )
    
                async def callback(select, interaction):
                    fragenummer = int(select.values[0])
                    quizdict = {}
                    quizdict[str(fragenummer)] = {}
                    message = None
                    if message == None:
                        message = await ctx.send(f"Bitte gebe die {fragenummer + 1}. Frage ein")
                    else:
                        await message.edit(f"Bitte gebe die {fragenummer + 1}. Frage ein")
                    async def getquestion(Error = False):
                        if Error == True:
                            if message.content != f"Bitte gebe die {fragenummer + 1}. Frage ein\ndeine Frage darf Höchstens 100 Zeichen lang sein!":
                                await message.edit(f"Bitte gebe die {fragenummer + 1}. Frage ein\ndeine Frage darf Höchstens 100 Zeichen lang sein!")
                        else:
                            if message.content != f"Bitte gebe die {fragenummer + 1}. Frage ein":
                                await message.edit(f"Bitte gebe die {fragenummer + 1}. Frage ein")
                        def check(m):
                            return m.author.id == ctx.author.id and m.channel == ctx.channel
        
                        msg = await self.client.wait_for('message', check=check)
        
                        await msg.delete()
        
                        frage = msg.content
        
                        if not len(frage) < 100:
                            frage = await getquestion(True)
        
                        return frage
        
                    frage = await getquestion(False)
        
                    quizdict[str(fragenummer)]["question"] = frage
        
                    async def getawnseramount(Error = False):
                        if Error == True:
                            if message.content != "Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll\nDu musst Mindestens eine und Maximal 25 Antwortmöglichkeiten haben!\n`Beispiel: 7`":
                                await message.edit("Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll\nDu musst Mindestens eine und Maximal 25 Antwortmöglichkeiten haben!\n`Beispiel: 7`")
                        else:
                            if message.content != "Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll":
                                await message.edit("Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll")
                        def check(m):
                            return m.author.id == ctx.author.id and m.channel == ctx.channel
        
                        msg = await self.client.wait_for('message', check=check)
        
                        await msg.delete()
        
                        antwortenmenge = msg.content
        
                        try:
                            antwortenmenge = int(antwortenmenge)
                        except:
                            antwortenmenge = await getawnseramount(True)
        
        
                        if antwortenmenge < 0:
                            antwortenmenge = await getawnseramount(True)
        
                        if antwortenmenge > 25:
                            antwortenmenge = await getawnseramount(True)
        
                        return antwortenmenge
        
                    antwortenmenge = await getawnseramount(False)
        
                    quizdict[str(fragenummer)]["antwortenmenge"] = antwortenmenge
        
                    async def getrightawnseramount(Error = False):
                        if Error == True:
                            if message.content != f"Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll\nEine Frage muss Mindestens eine Richtige Antwort haben. Du darfst nicht mehr Richtige Antworten als {antwortenmenge} festlegen\n`Beispiel: 1`":
                                await message.edit(f"Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll\nEine Frage muss Mindestens eine Richtige Antwort haben. Du darfst nicht mehr Richtige Antworten als {antwortenmenge} festlegen\n`Beispiel: 1`")
                        else:
                            if message.content != "Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll":
                                await message.edit("Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll")
                        def check(m):
                            return m.author.id == ctx.author.id and m.channel == ctx.channel
        
                        msg = await self.client.wait_for('message', check=check)
        
                        await msg.delete()
        
                        richtigeantworten = msg.content
        
                        try:
                            richtigeantworten = int(richtigeantworten)
                        except:
                            richtigeantworten = await getrightawnseramount(True)
        
        
                        if richtigeantworten < 0:
                            richtigeantworten = await getrightawnseramount(True)
        
                        if richtigeantworten > 25:
                            richtigeantworten = await getrightawnseramount(True)
        
                        return richtigeantworten
        
                    richtigeantworten = await getrightawnseramount(False)
        
                    quizdict[str(fragenummer)]["richtigeantworten"] = richtigeantworten
        
                    awnsers = []
        
                    for questionnummer in range(antwortenmenge - richtigeantworten):
                        async def getawnseramount(Error = False):
                            if Error == True:
                                if message.content != "Bitte gebe eine der **Falschen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.":
                                    await message.edit("Bitte gebe eine der **Falschen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.")
                            else:
                                if message.content != "Bitte gebe eine der **Falschen** Antworten ein.":
                                    await message.edit("Bitte gebe eine der **Falschen** Antworten ein.")
                            def check(m):
                                return m.author.id == ctx.author.id and m.channel == ctx.channel
        
                            msg = await self.client.wait_for('message', check=check)
        
                            await msg.delete()
        
                            awnser = msg.content
        
                            if not len(awnser) < 100:
                                awnser = await getquestion(True)
        
                            return awnser
                        
                        awnser = await getawnseramount(False)
                        awnsers.append(awnser)
        
                    quizdict[str(fragenummer)]["wrongawnsers"] = list(awnsers)
        
                    
                    awnsers = []
                    for questionnumber in range(richtigeantworten):
                        async def getawnseramount(Error = False):
                            if Error == True:
                                if message.content != "Bitte gebe eine der **Richtigen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.":
                                    await message.edit("Bitte gebe eine der **Richtigen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.")
                            else:
                                if message.content != "Bitte gebe eine der **Richtigen** Antworten ein.":
                                    await message.edit("Bitte gebe eine der **Richtigen** Antworten ein.")
                            def check(m):
                                return m.author.id == ctx.author.id and m.channel == ctx.channel
        
                            msg = await self.client.wait_for('message', check=check)
        
                            await msg.delete()
        
                            awnser = msg.content
        
                            if not len(awnser) < 100:
                                awnser = await getquestion(True)
        
                            return awnser
                        
                        awnser = await getawnseramount(False)
                        awnsers.append(awnser)
    
                    quizdict[str(fragenummer)]["rightawnsers"] = list(awnsers)
    
                    quizcollection.update_one({"_id" : quizid}, {"$set" : {f"{fragenummer}" : quizdict[str(fragenummer)]}})
    
                    await message.edit(f"Die {fragenummer + 1}. Frage von dem Quiz {quiz['title']} mit der ID {quizid} wurde erfolgreich bearbeitet.")
    
            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()
    
                    self.add_item(Dropdown())
    
            view = DropdownView()
    
            await ctx.respond(embed = myEmbed, view = view, ephemeral=True)
    
            txt = ""

    @slash_command(name='createquiz', description='Erstelle ein Quiz!')
    async def createquiz(self, ctx, fragen : Option(int, "Wie viele Fragen soll dein Quiz haben?", required = True), titel : Option(str, "Was soll der Titel des Quiz sein?", required = True)):
        await ctx.defer(ephemeral=True)
        if fragen <= 0:
            await ctx.respond("Dein Qziz muss mindestens eine Frage haben!", ephemeral  = True)
            return
        elif fragen > 25:
            await ctx.respond("Dein Qziz darf nicht mehr als 25 Fragen haben!", ephemeral  = True)
            return
        await ctx.respond("Das Setup wird jetzt gestartet!", ephemeral=False)
        quizdict = {}

        generalinformations = quizcollection.find_one({"_id" : "general"})
        quizid = generalinformations["nextid"]
        quizcollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})
        message = None
        for fragenummer in range(fragen):
            quizdict[str(fragenummer)] = {}
            if message == None:
                message = await ctx.send(f"Bitte gebe die {fragenummer + 1}. Frage ein")
            else:
                await message.edit(f"Bitte gebe die {fragenummer + 1}. Frage ein")
            async def getquestion(Error = False):
                if Error == True:
                    if message.content != f"Bitte gebe die {fragenummer + 1}. Frage ein\ndeine Frage darf Höchstens 100 Zeichen lang sein!":
                        await message.edit(f"Bitte gebe die {fragenummer + 1}. Frage ein\ndeine Frage darf Höchstens 100 Zeichen lang sein!")
                else:
                    if message.content != f"Bitte gebe die {fragenummer + 1}. Frage ein":
                        await message.edit(f"Bitte gebe die {fragenummer + 1}. Frage ein")
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel

                msg = await self.client.wait_for('message', check=check)

                await msg.delete()

                frage = msg.content

                if not len(frage) < 100:
                    frage = await getquestion(True)

                return frage

            frage = await getquestion(False)

            quizdict[str(fragenummer)]["question"] = frage

            async def getawnseramount(Error = False):
                if Error == True:
                    if message.content != "Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll\nDu musst Mindestens eine und Maximal 25 Antwortmöglichkeiten haben!\n`Beispiel: 7`":
                        await message.edit("Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll\nDu musst Mindestens eine und Maximal 25 Antwortmöglichkeiten haben!\n`Beispiel: 7`")
                else:
                    if message.content != "Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll":
                        await message.edit("Bitte gebe an, wie Viele Antworten (Falsche und Richtige) deine Frage haben soll")
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel

                msg = await self.client.wait_for('message', check=check)

                await msg.delete()

                antwortenmenge = msg.content

                try:
                    antwortenmenge = int(antwortenmenge)
                except:
                    antwortenmenge = await getawnseramount(True)


                if antwortenmenge < 0:
                    antwortenmenge = await getawnseramount(True)

                if antwortenmenge > 25:
                    antwortenmenge = await getawnseramount(True)

                return antwortenmenge

            antwortenmenge = await getawnseramount(False)

            quizdict[str(fragenummer)]["antwortenmenge"] = antwortenmenge

            async def getrightawnseramount(Error = False):
                if Error == True:
                    if message.content != f"Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll\nEine Frage muss Mindestens eine Richtige Antwort haben. Du darfst nicht mehr Richtige Antworten als {antwortenmenge} festlegen\n`Beispiel: 1`":
                        await message.edit(f"Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll\nEine Frage muss Mindestens eine Richtige Antwort haben. Du darfst nicht mehr Richtige Antworten als {antwortenmenge} festlegen\n`Beispiel: 1`")
                else:
                    if message.content != "Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll":
                        await message.edit("Bitte gebe an, wie Viele Richtige Antworten deine Frage haben soll")
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel

                msg = await self.client.wait_for('message', check=check)

                await msg.delete()

                richtigeantworten = msg.content

                try:
                    richtigeantworten = int(richtigeantworten)
                except:
                    richtigeantworten = await getrightawnseramount(True)


                if richtigeantworten < 0:
                    richtigeantworten = await getrightawnseramount(True)

                if richtigeantworten > 25:
                    richtigeantworten = await getrightawnseramount(True)

                return richtigeantworten

            richtigeantworten = await getrightawnseramount(False)

            quizdict[str(fragenummer)]["richtigeantworten"] = richtigeantworten

            awnsers = []

            for questionnummer in range(antwortenmenge - richtigeantworten):
                async def getawnseramount(Error = False):
                    if Error == True:
                        if message.content != "Bitte gebe eine der **Falschen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.":
                            await message.edit("Bitte gebe eine der **Falschen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.")
                    else:
                        if message.content != "Bitte gebe eine der **Falschen** Antworten ein.":
                            await message.edit("Bitte gebe eine der **Falschen** Antworten ein.")
                    def check(m):
                        return m.author.id == ctx.author.id and m.channel == ctx.channel

                    msg = await self.client.wait_for('message', check=check)

                    await msg.delete()

                    awnser = msg.content

                    if not len(awnser) < 100:
                        awnser = await getquestion(True)

                    return awnser
                
                awnser = await getawnseramount(False)
                awnsers.append(awnser)

            quizdict[str(fragenummer)]["wrongawnsers"] = list(awnsers)

            
            awnsers = []
            for questionnumber in range(richtigeantworten):
                async def getawnseramount(Error = False):
                    if Error == True:
                        if message.content != "Bitte gebe eine der **Richtigen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.":
                            await message.edit("Bitte gebe eine der **Richtigen** Antworten ein.\nEine Antwortmöglichkeit darf nicht länger als 100 Zeichen sein.")
                    else:
                        if message.content != "Bitte gebe eine der **Richtigen** Antworten ein.":
                            await message.edit("Bitte gebe eine der **Richtigen** Antworten ein.")
                    def check(m):
                        return m.author.id == ctx.author.id and m.channel == ctx.channel

                    msg = await self.client.wait_for('message', check=check)

                    await msg.delete()

                    awnser = msg.content

                    if not len(awnser) < 100:
                        awnser = await getquestion(True)

                    return awnser
                
                awnser = await getawnseramount(False)
                awnsers.append(awnser)

            quizdict[str(fragenummer)]["rightawnsers"] = list(awnsers)

        quizdict["_id"] = quizid
        quizdict["Fragen"] = fragen
        quizdict["title"] = titel
        quizdict["ersteller"] = ctx.author.id


        quizcollection.insert_one(quizdict)

        await message.edit(f"Dein Quiz wurde erfolgreich erstellt! Es hat die ID `{quizid}`. Du kannst es mit den /playquiz befehl Spielen.")
        



    tanjuno_actions = [
        discord.OptionChoice(name = "Tanjuno spielen", value = "play"),
        discord.OptionChoice(name = "karten anschauen", value = "look"),
        discord.OptionChoice(name = "Karten spielen", value = "place"),
        discord.OptionChoice(name = "Tisch sehen", value = "table"),
        discord.OptionChoice(name = "Spiel verlassen", value = "quit"),
        discord.OptionChoice(name = "jemanden aus dem Spiel werfen", value = "kick")
    ]

    @slash_command(name='tanjuno', description='Benutze das Tanjuno Minispiel.')
    async def tanjuno(self, ctx, action : Option(str, "Was möchtest du machen?", required = True, choices = tanjuno_actions)):
        print("Ein Tanjuno Befehl :D")

        cardsingame = ["01", "02", "03", "04", "05", "06", "08", "09", "11", "12", "13", "14", "15", "16", "17", "18", "19", "110", "21", "22", "23", "24", "25", "26", "27", "28", "29", "210", "31", "32", "33", "34", "35", "36", "37", "38", "39", "310", "41", "42", "43", "44", "45", "46", "47", "48", "49", "410"]

        async def convertcardtoemoji(cardid):
            return cardid
            if cardid == "01":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "02":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "03":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "04":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "05":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "06":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "07":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "08":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "09":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "10":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "11":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "12":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "13":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "14":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "15":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "16":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "17":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "18":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "19":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "110":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "111":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "112":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "113":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "20":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "21":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "22":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "23":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "24":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "25":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "26":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "27":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "28":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "29":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "210":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "211":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "212":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "213":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "30":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "31":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "32":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "33":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "34":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "35":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "36":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "37":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "38":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "39":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "310":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "311":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "312":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "313":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "40":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "41":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "42":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "43":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "44":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "45":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "46":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "47":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "48":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "49":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "410":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "411":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "412":
                return "<:Untitled4:969651395722608640>"
            elif cardid == "413":
                return "<:Untitled4:969651395722608640>"
            else:
                return f"Beim anzeigen dieser Karte ist ein Fehler aufgetreten. Bitte gebe dem Tanjun support bescheid. ({cardid})"

        async def createwinningtable(tanjunoid):
            game = tanjunocollection.find_one({"_id" : tanjunoid})
            players = game["players"]
            nowonturn = game["turnnow"]
            hoster = game["hoster"]
            authorname = game["authorname"]
            hands = game["hands"]
            channel = game["channelid"]
            ontable = game["cardontable"]
            direction = game["direction"]
            messageid = game["msgid"]
            lastaction = game["lastaction"]
            ranking = game["ranking"]
            channel = self.client.get_channel(int(channel))
            try:
                message = await channel.fetch_message(int(messageid))
            except:
                message = None

            pls = ""
            c = 0
            for rank in ranking:
                c += 1
                pls += f"\n\nPlatz {c}: <@{rank}>"
            c += 1
            pls += f"\n\nPlatz {c}: <@{players[0]}>"

            myEmbed = discord.Embed(title = f"Tanjuno Spiel von {authorname}", description = f"Das spiel ist beendet. Ich hoffe ihr hattet Spaß am Spiel. Es folgt das Ranking. Wenn du einen Fehler im Spiel entdeckt hast oder du eine Idee für eine neue Karte hast, melde dich bitte bei EntchenEric#1002 per Dm! Vielen Dank!\n\n{pls}")
            if message != None:
                message = await message.edit(embed = myEmbed)
            else:
                message = await channel.send(embed = myEmbed)

            tanjunocollection.delete_one({"_id" : tanjunoid})

        async def tableupdate(tanjunoid):
            game = tanjunocollection.find_one({"_id" : tanjunoid})
            players = game["players"]
            nowonturn = game["turnnow"]
            hoster = game["hoster"]
            authorname = game["authorname"]
            hands = game["hands"]
            channel = game["channelid"]
            ontable = game["cardontable"]
            direction = game["direction"]
            messageid = game["msgid"]
            lastaction = game["lastaction"]
            ranking = game["ranking"]
            channel = self.client.get_channel(int(channel))
            try:
                message = await channel.fetch_message(int(messageid))
            except:
                message = None
            try:
                idofplayernow = players.index(nowonturn) + direction
            except:
                idofplayernow = 0

            if len(players) == idofplayernow:
                idofplayernow = 0

            if idofplayernow == -1:
                idofplayernow = len(players) - 1

            if len(players) == 1:
                await createwinningtable(tanjunoid)
                return

            pls = ""
            for player in players:
                hand = hands[str(player)]
                if len(hand) == 0:
                    players.remove(player)
                    ranking.append(player)
                    tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"ranking" : ranking}})
                    tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"players" : players}})
                    if len(players) == 1:
                        await createwinningtable(tanjunoid)
                        return
                if player == players[idofplayernow]:
                    pls += f"➢ <@{player}> ({len(hand)} Karten)\n"
                else:
                    pls += f"<@{player}> ({len(hand)} Karten)\n"

            if direction == 1:
                pls += f"\n\nRichtung: ⇩"
            else:
                pls += f"\n\nRichtung: ⇧"
            
            c = 0
            for rank in ranking:
                c += 1
                pls += f"\n\nPlatz {c}: <@{rank}>"




                

            myEmbed = discord.Embed(title = f"Tanjuno Spiel von {authorname}", description = f"Spieler:\n{pls}\n\nAktuelle Karte: {await convertcardtoemoji(ontable)}\n\nWas ist passiert: {lastaction}")
            if message != None:
                message = await message.edit(embed = myEmbed)
            else:
                message = await channel.send(embed = myEmbed)
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"msgid" : message.id}})


            tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"turnnow" : players[idofplayernow]}})
            
            

        if action == "play":
            await ctx.defer(ephemeral=False)
            
            async def joingame(interaction):

                nonlocal ingame

                if interaction.user.id in ingame:
                    await interaction.response.send_message(f"Du nimmst bereits an diesen Spiel teil.", ephemeral = True)
                    return

                ingame.append(interaction.user.id)
                await updatetable()
                await interaction.response.send_message(f"Du bist dem Spiel erfolgreich beigetreten. Bitte warte, bis {ctx.author.mention} das Spiel startet.", ephemeral = True)
            
            async def startgame(interaction):
                if interaction.user.id != ctx.author.id:
                    await interaction.response.send_message(f"Nur {ctx.author.mention} darf das Spiel starten.", ephemeral = True)
                else:
                    nonlocal ingame
                    nonlocal message

                    myEmbed = discord.Embed(title = f"Tanjuno Spiel von {ctx.author}", description = f"Das Spiel wurde soeben gestartet! Es werden noch einige vorkehrungen getroffen. Bitte warte noch einen kurzen Moment <a:P_Gears_Loading:960472817441329172>")
                    view = discord.ui.View()
                    message = await message.edit(embed = myEmbed, view = view)

                    hands = {}

                    for player in ingame:
                        cards = []
                        for _ in range(7):
                            cards.append(random.choice(cardsingame))
                        hands[str(player)] = cards

                    tanjunocollection.insert_one({"_id" : tanjunoid, "players" : ingame, "msgid" : message.id, "hoster" : ctx.author.id, "hands" : hands, "authorname" : str(ctx.author), "channelid" : ctx.channel.id, "turnnow" : random.choice(ingame), "direction" : 1, "cardontable" : random.choice(cardsingame), "lastaction" : f"{ctx.author} hat das Spiel gestartet.", "todraw" : 0, "ranking" : []})
                    
                    for player in ingame:
                        tanjunocollection.update_one({"_id" : "general"}, {"$set" : {str(player) : tanjunoid}}, upsert = True)

                    await tableupdate(tanjunoid)
        
            

            async def generateview():
                view = discord.ui.View()

                beitretenbutton = discord.ui.Button(label = "Spiel beitreten", style = discord.ButtonStyle.blurple, disabled=False, row = 1, custom_id = "Spiel Beitreten")
                beitretenbutton.callback = joingame
                view.add_item(beitretenbutton)

                startgamebutton = discord.ui.Button(label = "Spiel starten", style = discord.ButtonStyle.blurple, disabled=False, row = 1, custom_id = "Spiel Starten")
                startgamebutton.callback = startgame
                view.add_item(startgamebutton)

                return view

            async def updatetable():
                nonlocal message
                nonlocal ingame
                pls = ""
                for player in ingame:
                    pls += f"<@{player}> "
                myEmbed = discord.Embed(title = f"Tanjuno Spiel von {ctx.author}", description = f"Klicke auf `Spiel beitreten`, um dem Tanjuo Spiel von {ctx.author.mention} beizutreten.\nAktuell im Spiel: {pls}")
                view = await generateview()
                message = await message.edit(embed = myEmbed, view = view)

            tanjunodict = {}

            generalinformations = tanjunocollection.find_one({"_id" : "general"})
            tanjunoid = generalinformations["nextid"]
            tanjunocollection.update_one({"_id" : "general"}, {"$inc" : {"nextid" : 1}})

            myEmbed = discord.Embed(title = f"Tanjuno Spiel von {ctx.author}", description = f"Klicke auf `Spiel beitreten`, um dem Tanjuo Spiel von {ctx.author.mention} beizutreten.\nAktuell im Spiel: {ctx.author.mention}")

            ingame = [ctx.author.id]

            view = await generateview()

            message = await ctx.respond(embed = myEmbed, ephemeral = False, view = view)

        if action == "look":
            await ctx.defer()
            tanj = tanjunocollection.find_one({"_id" : "general"})
            try:
                tanjunoid = tanj[str(ctx.author.id)]
            except:
                await ctx.respond(f"Du nimmst grade an keinen Tanjuno spiel teil.")
                return
            
            tanjunogame = tanjunocollection.find_one({"_id" : tanjunoid})
            cards = tanjunogame["hands"][str(ctx.author.id)]

            cardsstr = ""
            cardontable = tanjunogame["cardontable"]

            cardsstr += "__Deine Karten:__\n"

            c = 0

            for card in cards:
                if len(cardsstr) < 3000:
                    cardsstr += f"{await convertcardtoemoji(card)} KartenID: {card}\n"
                else:
                    cardsstr += "Woah! Du hast ganz schön viele Karten. Zu viele. Ich kann nicht alle Anzeigen :c\nbenutze den /tanjuno Karten spielen Befehl, um eine Karte zu spielen."
                    myEmbed = discord.Embed(title = f"Tanjuno Spiel von {ctx.author}", description = cardsstr)
                    await ctx.respond(embed = myEmbed)
                    return

            if cardsstr == "__Karten die du legen kannst:__\n":
                cardsstr = "Du hast keine Karten die du legen kannst 😔\n"


            myEmbed = discord.Embed(title = f"Tanjuno Spiel von {ctx.author}", description = cardsstr)
            await ctx.respond(embed = myEmbed)

        if action == "place":
            await ctx.defer()
            tanj = tanjunocollection.find_one({"_id" : "general"})
            try:
                tanjunoid = tanj[str(ctx.author.id)]
            except:
                await ctx.respond(f"Du nimmst grade an keinen Tanjuno spiel teil.")
                return
            
            tanjunogame = tanjunocollection.find_one({"_id" : tanjunoid})
            print(tanjunogame)
            if tanjunogame["turnnow"] != ctx.author.id:
                await ctx.respond(f"Du bist nicht an der Reihe.")
                return

            cards = tanjunogame["hands"][str(ctx.author.id)]

            cardsstr = ""
            cardontable = tanjunogame["cardontable"]

            cardsstr += "__Karten die du legen kannst:__\n"

            c = 0

            for card in cards:
                print(card)
                print(card[0])
                print(c)
                if len(cardsstr) < 3000:
                    if cardontable == "07":
                        cardsstr += f"{await convertcardtoemoji(card)} KartenID: {card}\n"
                    elif cardontable[1:] == "12":
                        if card == "02" or card == "05" or card == "06":
                            cardsstr += f"{await convertcardtoemoji(card)} KartenID: {card}\n"
                    elif cardontable[1:] == "11":
                        if card[1:] == "11":
                            cardsstr += f"{await convertcardtoemoji(card)} KartenID: {card}\n"
                    else:
                        if card[0] == "0" or card[0] == cardontable[0] or card[1] == cardontable[1]:
                            c += 1
                            cardsstr += f"{await convertcardtoemoji(card)} KartenID: {card}\n"
                else:
                    cardsstr += "Woah! Du hast ganz schön viele Karten. Zu viele. Ich kann nicht alle Anzeigen :c\nbenutze den /tanjuno Karten spielen Befehl, um eine Karte zu spielen."
                    myEmbed = discord.Embed(title = f"Tanjuno Spiel von {ctx.author}", description = cardsstr)
                    await ctx.respond(embed = myEmbed)
                    return

            if cardsstr == "__Karten die du legen kannst:__\n":
                cardsstr = "Du hast keine Karten die du legen kannst 😔\n"


            myEmbed = discord.Embed(title = f"Tanjuno Spiel von {ctx.author}", description = cardsstr)
            
            message = await ctx.respond(f"Bitte gebe die ID der Karte ein, die du spielen möchtest.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.", embed = myEmbed)

            async def getcardid(Error = "Keiner"):
                nonlocal message
                if Error == "Keiner":
                    if message.content != f"Bitte gebe die ID der Karte ein, die du spielen möchtest.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.":
                        await message.edit(f"Bitte gebe die ID der Karte ein, die du spielen möchtest.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.")
                if Error == "Karte nicht spielbar":
                    if message.content != f"Die von dir gelegte Karte ist nicht Spielbar.\n Benutze den /tanjuno karten anschauen Befehl um zu sehen, welche Karten du spielen kannst.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.":
                        await message.edit(f"Die von dir gelegte Karte ist nicht Spielbar.\n Benutze den /tanjuno karten anschauen Befehl um zu sehen, welche Karten du spielen kannst.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.", embed = myEmbed)
                if Error == "Keine Karte":
                    if message.content != f"Die von dir eingegebene Karten ID ist keine Karte.\n Benutze den /tanjuno karten anschauen Befehl um zu sehen, welche Karten du spielen kannst.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.":
                        await message.edit(f"Die von dir eingegebene Karten ID ist keine Karte.\n Benutze den /tanjuno karten anschauen Befehl um zu sehen, welche Karten du spielen kannst.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.", embed = myEmbed)
                if Error == "Karte nicht auf Hand":
                    if message.content != f"Du besitzt diese Karte nicht.\n Benutze den /tanjuno karten anschauen Befehl um zu sehen, welche Karten du spielen kannst.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.":
                        await message.edit(f"Du besitzt diese Karte nicht.\n Benutze den /tanjuno karten anschauen Befehl um zu sehen, welche Karten du spielen kannst.\ngebe `ziehen` ein, wenn du keine Karte legen kannst.", embed = myEmbed)
                def check(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel

                msg = await self.client.wait_for('message', check=check)

                await msg.delete()
                
                if msg.content.lower() == "ziehen":
                    return "00"

                try:
                    x = int(msg.content)
                except:
                    cardid = await getcardid(Error = "Keine Karte")
                    return cardid
                
                cardid = msg.content

                cardid = str(cardid)

                hand = tanjunogame["hands"][str(ctx.author.id)]
                if not cardid in hand:
                    print(hand)
                    print(cardid)
                    cardid = await getcardid(Error = "Karte nicht auf Hand")
                    return cardid


                nowontable = tanjunogame["cardontable"]

                if cardontable[1:] == "12":
                    if cardid != "02" and cardid != "05" and cardid != "06":
                        cardid = await getcardid(Error = "Karte nicht spielbar")
                        return cardid
                elif cardontable[1:] == "11":
                    if cardid[1:] != "11":
                        cardid = await getcardid(Error = "Karte nicht spielbar")
                        return cardid
                elif cardid[0] != "0" and cardid[0] != nowontable[0] and cardid[1] != cardontable[1] and cardontable != "07":
                    cardid = await getcardid(Error = "Karte nicht spielbar")
                    return cardid


                return cardid

            cardid = await getcardid()
            print(cardid)
            if cardid == "00":
                hand = tanjunogame["hands"][str(ctx.author.id)]
                todraw = tanjunogame["todraw"]
                for _ in range(todraw):
                    hand.append( random.choice(cardsingame))
                if todraw == 0:
                    hand.append( random.choice(cardsingame))
                    tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat eine Karte gezogen."}})
                else:
                    tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat {todraw} Karten gezogen."}})
                    tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"cardontable" : f"{cardontable[0]}0"}})
                
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"todraw" : 0}})
                await tableupdate(tanjunoid)
            elif (cardid[1:] == "1" or cardid[1:] == "2" or cardid[1:] == "3" or cardid[1:] == "4" or cardid[1:] == "5" or cardid[1:] == "6" or cardid[1:] == "7" or cardid[1:] == "8" or cardid[1:] == "9") and cardid[0] != "0":
                print("Ne normal Carte")
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : cardid}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat eine Karte gelegt."}})
                await tableupdate(tanjunoid)
            elif cardid == "01":
                print("Farbe wünschen :o")
                class DropDownMenu(discord.ui.Select):
                    @discord.ui.select(placeholder="Wähle deine Farbe aus!", options=[
                        discord.SelectOption(label = "Rot", description = "Klicke, um Rot auszuwählen", emoji = "🟥", value = "Red"),
                        discord.SelectOption(label = "Blau", description = "Klicke, um Blau auszuwählen", emoji = "🟦", value = "Blue"),
                        discord.SelectOption(label = "Gelb", description = "Klicke, um Gelb auszuwählen", emoji = "🟨", value = "Yellow"),
                        discord.SelectOption(label = "Grün", description = "Klicke, um Grün auszuwählen", emoji = "🟩", value = "Green")
                    ])

                    async def callback(self, select, interaction : discord.Interaction):

                        nonlocal messhage
                        
                        if select.values[0] == "Red":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "10"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich Rot gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
                        if select.values[0] == "Blue":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "20"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich Blau gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
                        if select.values[0] == "Yellow":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "30"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich Gelb gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
                        if select.values[0] == "Green":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "40"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich Grün gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
            
                class DropdownView(discord.ui.View):
                    def __init__(self):
                        super().__init__()


                        self.add_item(DropDownMenu())

                        view = DropdownView()


                messhage = await message.channel.send(content = "Bitte wähle die Farbe aus, die du dir wünscht.", view = view)
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
            elif cardid == "03":
                print("Karten Tauschen :oha:")
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat dafür gesorgt, dass die Karten getauscht wurde. jeder hat jetzt die Karte von dem der nach ihm dran ist."}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "07"}})
                tanjunocol = tanjunocollection.find_one({"_id" : tanjunoid})
                players = tanjunocol["players"]

                hands = dict(tanjunocol["hands"])

                tmphands = dict(tanjunocol["hands"])

                c = 0
                for player in players:
                    if c + 1 == len(players):
                        c = -1
                    print("player: ", players[c + 1])
                    print("c: ", c)
                    hands[str(player)] = tmphands[str(players[c + 1])]
                    c += 1

                    tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{player}" : hands[str(player)]}})

                await tableupdate(tanjunoid)

            elif cardid == "04":
                print("Jeder +2 :hhahahah")
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat dafür gesorgt, dass jeder 2 Karten ziehen muss."}})
                tanjunocol = tanjunocollection.find_one({"_id" : tanjunoid})
                players = tanjunocol["players"]

                c = 0
                for player in players:
                    hand = tanjunogame["hands"][str(player)]
                    hand.append(random.choice(cardsingame))
                    hand.append(random.choice(cardsingame))
                    tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{player}" : hand}})

                await tableupdate(tanjunoid)
            elif cardid[0] != "0" and cardid[1:] == "10":
                print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRichtungswechelllllllllllllllllllllll")
                hand = tanjunogame["hands"][str(ctx.author.id)]
                tanjunocol = tanjunocollection.find_one({"_id" : tanjunoid})
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                direction = tanjunocol["direction"]
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"direction" : direction * -1}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat die Richtung geändert."}})
                players = tanjunocol["players"]
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : cardid}})
                idofplayernow = players.index(ctx.author.id) - direction
                if len(players) == idofplayernow:
                    idofplayernow = -1

                if len(players) == 2:
                    tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"turnnow" : players[idofplayernow]}})

                await tableupdate(tanjunoid)

            elif cardid[1:] == "11":
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$inc" : {f"todraw" : 2}})
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : cardid}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat eine +2 Karte gelegt."}})
                await tableupdate(tanjunoid)

            elif cardid == "02":
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$inc" : {f"todraw" : 4}})
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                class DropDownMenu(discord.ui.Select):
                    @discord.ui.select(placeholder="Wähle deine Farbe aus!", options=[
                        discord.SelectOption(label = "Rot", description = "Klicke, um Rot auszuwählen", emoji = "🟥", value = "Red"),
                        discord.SelectOption(label = "Blau", description = "Klicke, um Blau auszuwählen", emoji = "🟦", value = "Blue"),
                        discord.SelectOption(label = "Gelb", description = "Klicke, um Gelb auszuwählen", emoji = "🟨", value = "Yellow"),
                        discord.SelectOption(label = "Grün", description = "Klicke, um Grün auszuwählen", emoji = "🟩", value = "Green")
                    ])

                    async def callback(self, select, interaction : discord.Interaction):

                        nonlocal messhage
                        
                        if select.values[0] == "Red":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "112"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich mit einer +4 Rot gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
                        if select.values[0] == "Blue":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "212"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich mit einer +4 Blau gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
                        if select.values[0] == "Yellow":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "312"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich mit einer +4 Gelb gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
                        if select.values[0] == "Green":
                            if interaction.user.id == ctx.author.id:
                                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "412"}})
                                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich mit einer +4 Grün gewünscht."}})
                                await tableupdate(tanjunoid)
                                await messhage.delete()
                            else:
                                await interaction.response.send_message(f"Nur {ctx.author.mention} darf sich eine Farbe aussuchen.", ephemeral = True)
            
                class DropdownView(discord.ui.View):
                    def __init__(self):
                        super().__init__()


                        self.add_item(DropDownMenu())

                        view = DropdownView()


                messhage = await message.channel.send(content = "Bitte wähle die Farbe aus, die du dir wünscht.", view = view)

            elif cardid == "05":
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"todraw" : 0}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "07"}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich mit einen Schild verteidigt."}})
                await tableupdate(tanjunoid)

            elif cardid == "06":
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})

                players = tanjunogame["players"]
                direction = tanjunogame["direction"]
                idofplayernow = players.index(ctx.author.id) + direction * -1

                if len(players) == idofplayernow:
                    idofplayernow = 0

                if idofplayernow == -1:
                    idofplayernow = len(players) - 1

                hand = tanjunogame["hands"][str(players[idofplayernow])]

                todraw = tanjunogame["todraw"]
                for _ in range(todraw):
                    hand.append( random.choice(cardsingame))
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{players[idofplayernow]}" : hand}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"todraw" : 0}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "07"}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat sich mit einen Spiegel verteidigt. <@{players[idofplayernow]}> musste deshalb {todraw} Karten ziehen."}})
                await tableupdate(tanjunoid)

            elif cardid == "08":
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                handlen = len(hand)
                hand = []
                for card in range(handlen):
                    hand.append(random.choice(cardsingame))
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "07"}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} Hat seine Karten durch neue Zufällige Karten getauscht."}})
                await tableupdate(tanjunoid)

            elif cardid == "09":
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                players = tanjunogame["players"]
                random.shuffle(players)
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"players" : players}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : "07"}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat Die Reihenfolge in der Gespielt wird zufällig vertauscht."}})
                await tableupdate(tanjunoid)

            elif cardid[1:] == "13":
                hand = tanjunogame["hands"][str(ctx.author.id)]
                hand.remove(cardid)
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"hands.{ctx.author.id}" : hand}})
                tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"cardontable" : cardid}})
                tanjunocollection.update_one({"_id" :tanjunoid}, {"$set" : {f"lastaction" : f"{ctx.author} hat den nächsten der an der reihe ist aussetzen lassen."}})
                await tableupdate(tanjunoid)
                await tableupdate(tanjunoid)

        if action == "table":
            await ctx.defer()
            tanj = tanjunocollection.find_one({"_id" : "general"})
            try:
                tanjunoid = tanj[str(ctx.author.id)]
            except:
                await ctx.respond(f"Du nimmst grade an keinen Tanjuno spiel teil.")
                return
            game = tanjunocollection.find_one({"_id" : tanjunoid})
            channel = game["channelid"]
            messageid = game["msgid"]
            channel = self.client.get_channel(int(channel))
            try:
                message = await channel.fetch_message(int(messageid))
                await ctx.respond(f"Hier ist der Tisch: {message.jump_url}")
            except:
                await ctx.respond(f"Huch.. Ich hab den Tisch wohl verloren 💀 Ich hab in {channel.mention} einen neuen gemacht.")

                await tableupdate(tanjunoid)

        if action == "quit":
            await ctx.defer()
            tanj = tanjunocollection.find_one({"_id" : "general"})
            try:
                tanjunoid = tanj[str(ctx.author.id)]
            except:
                await ctx.respond(f"Du nimmst grade an keinen Tanjuno spiel teil.")
                return
            game = tanjunocollection.find_one({"_id" : tanjunoid})
            players = game["players"]
            players.remove(ctx.author.id)
            tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"players" : players}})
            print(players)
            await tableupdate(tanjunoid)

        if action == "kick":
            await ctx.defer()
            tanj = tanjunocollection.find_one({"_id" : "general"})
            try:
                tanjunoid = tanj[str(ctx.author.id)]
            except:
                await ctx.respond(f"Du nimmst grade an keinen Tanjuno spiel teil.")
                return
            game = tanjunocollection.find_one({"_id" : tanjunoid})
            players = game["players"]
            authorname = game["authorname"]
            if str(ctx.author) != authorname:
                await ctx.respond("Du bist nicht der Ersteller des Spiels.")
                return

            message = await ctx.respond("Bitte pinge den User, den du kicken möchtest.")

            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel

            msg = await self.client.wait_for('message', check=check)

            if len(msg.mentions) == 0:
                await message.edit("<:P_loading:966696817670651954>")
                return

            if len(msg.mentions) > 1:
                await message.edit("<:P_meow:880797109371166760> Bitte kicke immer nur eine Person")
                return

            try:
                mentoneduser = msg.mentions[0].id
            except:
                await message.edit("<:P_loading:966696817670651954> Entweder du hast keine Person gepingt oder die Person hat keine ID <:P_loading:966696817670651954><:P_loading:966696817670651954><:P_loading:966696817670651954>")
                return
            players.remove(mentoneduser)
            tanjunocollection.update_one({"_id" : tanjunoid}, {"$set" : {"players" : players}})
            await tableupdate(tanjunoid)


    @slash_command(name='tanjnite', description='Spiele Tanjnite.')
    async def tanjnite(self, ctx):       
        spielmodi = ["solo", "duo", "squad"]
        dropzones = ["lootlake", "tilted Towers", "Moisty Mire", "Salty springs", "Sanctunary", "Camp Cuddle"]
        async def solo(message):

            print("Jetzt in Solo :DD")

            class Dropdown_solo(discord.ui.Select):
                def __init__(self):
                    
                    options = []

                    for zone in dropzones:
                        options.append(discord.SelectOption(label = zone, description = f"Klicke, um in {zone} zu droppen", value = zone))
                
                    super().__init__(
                        placeholder="wähle aus, wo du droppen möchtest.",
                        min_values=1,
                        max_values=1,
                        options=options
                    )

            

                async def callback(select, interaction : discord.Interaction):

                    nonlocal message

                    inventory = []

                    gegner = 99

                    leben = 100

                    kills = 0

                    shield = 0

                    actions = ["kiste gefunden","kiste gefunden","kiste gefunden", "Gegner Gefunden", "von Gegner angegrifen", "Angel gefunden", "von Sniper getroffen", "Item benutzen", "Item benutzen", "Item benutzen", "Item benutzen", "Item benutzen", "Item benutzen"]#, "von anderen Angetanzt", "seilrutsche gefunden", "Busch gefunden"]

                    weapons = ["Pump", "Golden Scar", "Scar", "Sniper", "Trommelgewehr", "Raketenwerfer", "Pistole"]

                    items = ["Mini Shield", "Shield", "Bandages", "Medkit", "Chug Jug", "Splashies", "Fleisch"]



                    async def makeaction(lasthappened = f"Du hast das Tanjnite gestartet und bis in {select.values[0]} gedroppt."):
                        action = random.choice(actions)

                        nonlocal message
                        nonlocal inventory
                        nonlocal gegner
                        nonlocal leben
                        nonlocal kills
                        nonlocal shield
                        nonlocal weapons
                        nonlocal items

                        if lasthappened != f"Du hast das Tanjnite gestartet und bis in {select.values[0]} gedroppt.":
                            gegner -= random.randint(5, 15)

                        if shield > 0:
                            shield = 0

                        if leben <= 0:
                            txt = ""

                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            view = discord.ui.View()

                            message = await message.edit("<a:LDance:970044151842353183>", view = view, embed = myEmbed)
                            return

                        if gegner <= 0:


                            txt = ""

                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            view = discord.ui.View()

                            message = await message.edit("DU HAST GEWONNEN <:P_Espeon_GG:927185863211884595>", view = view, embed = myEmbed)
                            return

                        print("Es passiert was :o")
                        print(action)

                        if action == "Item benutzen":
                            anitemisininventory = False
                            for item in inventory:
                                if item in items:
                                    anitemisininventory = True
                            
                            if anitemisininventory == False:
                                while action == "Item benutzen":
                                    action = random.choice(actions)

                        if action == "kiste gefunden":

                            class Dropdown_kiste_firstmenu(discord.ui.Select):
                                def __init__(self):

                                    options = [
                                        discord.SelectOption(label = "Öffnen", description = f"Klicke, um die Kiste zu öffnen", value = "öffnen"),
                                        discord.SelectOption(label = "nicht Öffnen", description = f"Klicke, um die Kiste nicht zu öffnen", value = "nicht Öffnen")
                                    ]

                                    super().__init__(
                                        placeholder="wähle aus, was du machen möchtest.",
                                        min_values=1,
                                        max_values=1,
                                        options=options
                                    )

            

                                async def callback(chestselect, interaction : discord.Interaction):

                                    nonlocal message
                                    nonlocal inventory
                                    nonlocal gegner
                                    nonlocal leben
                                    nonlocal kills
                                    nonlocal shield
                                    nonlocal weapons
                                    nonlocal items

                                    if chestselect.values[0] == "öffnen":
                                        möglichkeiten = ["Gegner greift an", "du hörst Gegner", "Du öffnest Kiste"]
                                        happened = random.choice(möglichkeiten)
                                        print(happened)
                                        if happened == "Gegner greift an":
                                            if gegner == 99:
                                                hits = random.randint(1, 10)
                                                hhits = hits
                                                while shield >= 20 and hits > 1:
                                                    shield -= 20
                                                    hits -= 1
                                                while hits > 1:
                                                    leben -= 20
                                                    hits -= 1
                                            elif "Pump" in inventory:
                                                damage = random.randint(10, 75)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Golden Scar" in inventory:
                                                damage = random.randint(10, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Scar" in inventory:
                                                damage = random.randint(20, 125)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Trommelgewehr" in inventory:
                                                damage = random.randint(15, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Pistole" in inventory:
                                                damage = random.randint(50, 120)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Raketenwerfer" in inventory:
                                                damage = random.randint(60, 130)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Sniper" in inventory:
                                                damage = random.randint(30, 90)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            if leben > 0:
                                                itemsinchest = []
                                                for _ in range(3):
                                                    
                                                    madeitin = False
                                                    while madeitin == False:
                                                        x  = random.choice(items)
                                                        if x not in inventory and x not in itemsinchest:
                                                            itemsinchest.append(x)
                                                            madeitin = True
                                                for _ in range(2):
                                                    
                                                    madeitin = False
                                                    while madeitin == False:
                                                        x  = random.choice(weapons)
                                                        if x not in inventory and x not in itemsinchest:
                                                            itemsinchest.append(x)
                                                            madeitin = True

                                                class DropDownMenu_Items_kiste_öffnen(discord.ui.Select):
                                                
                                                
                                                    def __init__(self):
                                                        options = []

                                                        c = 0

                                                        for item in inventory:
                                                            c += 1
                                                            options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                        for item in itemsinchest:
                                                            c += 1
                                                            options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                        super().__init__(
                                                            placeholder="Wähle die 5 Items, die du behalten möchtest.",
                                                            min_values=5,
                                                            max_values=5,
                                                            options=options
                                                        )

                                                    async def callback(select2, interaction : discord.Interaction):
                                                        nonlocal message
                                                        nonlocal inventory
                                                        nonlocal gegner
                                                        nonlocal leben
                                                        nonlocal kills
                                                        nonlocal shield
                                                        nonlocal weapons
                                                        nonlocal items
                                                        inventory = select2.values
                                                        await makeaction("Als du die Kiste öffnen wolltest, hast du einen Gegner gehört. Natürlich hast du ihn Gejagt und Elemeniert. gut gemacht")
                                                        kills += 1
                                                        return
                                                class DropdownView(discord.ui.View):
                                                    def __init__(self):
                                                        super().__init__()


                                                        self.add_item(DropDownMenu_Items_kiste_öffnen())

                                                view = DropdownView()


                                                message = await message.edit(content = "Bitte wähle die Items aus, die du behalten möchtest.", view = view)
                                            else:
                                                await makeaction("Als du die Kiste öffnen wolltest, hast du einen Gegner gehört. Du wolltest ihn Töten, hast aber versagt <a:LDance:970044151842353183>")
                                                return
                                        
                                        if happened == "du hörst Gegner":

                                            class DropDownMenu_kiste_gegnergehört(discord.ui.Select):
                                            
                                                def __init__(self):
                                                
                                                    options = []

                                                    options.append(discord.SelectOption(label = "Gegner Suchen", description = f"Klicke, um den Gegner zu suchen", value = "suchen"))

                                                    options.append(discord.SelectOption(label = "weglaufen", description = f"Klicke, um weg zu laufen", value = "laufen"))

                                                    options.append(discord.SelectOption(label = "ignorieren", description = f"Klicke, um den Gegner zu ignorieren", value = "ignorieren"))

                                                    super().__init__(
                                                        placeholder="Bitte Wähle, was du tun möchtest.",
                                                        min_values=1,
                                                        max_values=1,
                                                        options=options
                                                    )


                                                async def callback(gegnerhörenselect, interaction : discord.Interaction):

                                                    nonlocal message
                                                    nonlocal inventory
                                                    nonlocal gegner
                                                    nonlocal leben
                                                    nonlocal kills
                                                    nonlocal shield
                                                    nonlocal weapons
                                                    nonlocal items

                                                    async def gegnersuchen():
                                                        nonlocal message
                                                        nonlocal inventory
                                                        nonlocal gegner
                                                        nonlocal leben
                                                        nonlocal kills
                                                        nonlocal shield
                                                        nonlocal weapons
                                                        nonlocal items
                                                        möglichkeiten = ["Gegner gefunden", "Gegner nicht gefunden"]
                                                        happened = random.choice(möglichkeiten)
                                                        if happened == "Gegner nicht gefunden":
                                                            itemsinchest = []
                                                            for _ in range(3):
                                                                
                                                                madeitin = False
                                                                while madeitin == False:
                                                                    x  = random.choice(items)
                                                                    if x not in inventory and x not in itemsinchest:
                                                                        itemsinchest.append(x)
                                                                        madeitin = True
                                                            for _ in range(2):
                                                                
                                                                madeitin = False
                                                                while madeitin == False:
                                                                    x  = random.choice(weapons)
                                                                    if x not in inventory and x not in itemsinchest:
                                                                        itemsinchest.append(x)
                                                                        madeitin = True

                                                            class DropDownMenu_Items_kiste_gegner_nichtGefunden(discord.ui.Select):
                                                            
                                                                def __init__(self):
                                                                    options = []

                                                                    c = 0

                                                                    for item in inventory:
                                                                        c += 1
                                                                        options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                    for item in itemsinchest:
                                                                        c += 1
                                                                        options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                    super().__init__(
                                                                        placeholder="Wähle die 5 Items, die du behalten möchtest.",
                                                                        min_values=5,
                                                                        max_values=5,
                                                                        options=options
                                                                    )


                                                                async def callback(select2, interaction : discord.Interaction):
                                                                    nonlocal message
                                                                    nonlocal inventory
                                                                    nonlocal gegner
                                                                    nonlocal leben
                                                                    nonlocal kills
                                                                    nonlocal shield
                                                                    nonlocal weapons
                                                                    nonlocal items
                                                                    inventory = select2.values
                                                                    await makeaction("Du hast einen Gegner gehört. Als du ihn gesucht hast, hast du ihn leider nicht gefunden. Deshalb hast du einfach die Kiste auf gemacht.")
                                                                    return

                                                            class DropdownView(discord.ui.View):
                                                                def __init__(self):
                                                                    super().__init__()


                                                                    self.add_item(DropDownMenu_Items_kiste_gegner_nichtGefunden())

                                                            view = DropdownView()


                                                            message = await message.edit(content = "Bitte wähle die 5 Items aus, die du benutzen möchtest.", view = view)

                                                        else:
                                                            if gegner == 99:
                                                                hits = random.randint(1, 10)
                                                                hhits = hits
                                                                while shield >= 20 and hits > 1:
                                                                    shield -= 20
                                                                    hits -= 1
                                                                while hits > 1:
                                                                    leben -= 20
                                                                    hits -= 1
                                                            elif "Pump" in inventory:
                                                                damage = random.randint(10, 75)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Golden Scar" in inventory:
                                                                damage = random.randint(10, 100)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Scar" in inventory:
                                                                damage = random.randint(20, 125)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Trommelgewehr" in inventory:
                                                                damage = random.randint(15, 100)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Pistole" in inventory:
                                                                damage = random.randint(50, 120)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Raketenwerfer" in inventory:
                                                                damage = random.randint(60, 130)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Sniper" in inventory:
                                                                damage = random.randint(30, 90)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            if leben > 0:
                                                                itemsinchest = []
                                                                for _ in range(3):
                                                                    
                                                                    madeitin = False
                                                                    while madeitin == False:
                                                                        x  = random.choice(items)
                                                                        if x not in inventory and x not in itemsinchest:
                                                                            itemsinchest.append(x)
                                                                            madeitin = True
                                                                for _ in range(2):
                                                                    
                                                                    madeitin = False
                                                                    while madeitin == False:
                                                                        x  = random.choice(weapons)
                                                                        if x not in inventory and x not in itemsinchest:
                                                                            itemsinchest.append(x)
                                                                            madeitin = True
                                                                class DropDownMenu_Items_Kiste_gegner_kampf(discord.ui.Select):
                                                                
                                                                    def __init__(self):
                                                                        options = []

                                                                        c = 0

                                                                        for item in inventory:
                                                                            c += 1
                                                                            options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                        for item in itemsinchest:
                                                                            c += 1
                                                                            options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                        super().__init__(
                                                                            placeholder="Wähle die 5 Items, die du behalten möchtest.",
                                                                            min_values=5,
                                                                            max_values=5,
                                                                            options=options
                                                                        )

                                                                    async def callback(select2, interaction : discord.Interaction):
                                                                        nonlocal message
                                                                        nonlocal inventory
                                                                        nonlocal gegner
                                                                        nonlocal leben
                                                                        nonlocal kills
                                                                        nonlocal shield
                                                                        nonlocal weapons
                                                                        nonlocal items
                                                                        inventory = select2.values
                                                                        await makeaction("Als du die Kiste öffnen wolltest, hast du einen Gegner gehört. Natürlich hast du ihn Gejagt und Elemeniert. gut gemacht")
                                                                        kills += 1
                                                                        return
                                                                class DropdownView(discord.ui.View):
                                                                    def __init__(self):
                                                                        super().__init__()


                                                                        self.add_item(DropDownMenu_Items_Kiste_gegner_kampf())

                                                                view = DropdownView()


                                                                message = await message.edit(content = "Bitte wähle die 5 Items aus, die du benutzen möchtest.", view = view)
                                                            else:
                                                                    await makeaction("Du hast den Gegner, den du gehört hast als du eine Kiste öffnen wolltest, gesucht und gefunden. Er hat dich aber getötet <a:LDance:970044151842353183>")
                                                                    return

                                                    async def weglaufen():
                                                        nonlocal message
                                                        nonlocal inventory
                                                        nonlocal gegner
                                                        nonlocal leben
                                                        nonlocal kills
                                                        nonlocal shield
                                                        nonlocal weapons
                                                        nonlocal items
                                                        await makeaction("Du Wolltest eigetlich eine Kiste öffnen. Als du aber einen Gegner gehört hast, bist du weg gelaufen.")
                                                        return

                                                    async def ignorieren():
                                                        nonlocal message
                                                        nonlocal inventory
                                                        nonlocal gegner
                                                        nonlocal leben
                                                        nonlocal kills
                                                        nonlocal shield
                                                        nonlocal weapons
                                                        nonlocal items
                                                        möglichkeiten = ["Gegner findet dich", "Gegner Findet dich nicht"]
                                                        happened = random.choice(möglichkeiten)
                                                        if happened == "Gegner Findet dich nicht":
                                                            itemsinchest = []
                                                            for _ in range(3):
                                                                
                                                                madeitin = False
                                                                while madeitin == False:
                                                                    x  = random.choice(items)
                                                                    if x not in inventory and x not in itemsinchest:
                                                                        itemsinchest.append(x)
                                                                        madeitin = True
                                                            for _ in range(2):
                                                                
                                                                madeitin = False
                                                                while madeitin == False:
                                                                    x  = random.choice(weapons)
                                                                    if x not in inventory and x not in itemsinchest:
                                                                        itemsinchest.append(x)
                                                                        madeitin = True
                                                            class DropDownMenu_Items_kiste_gegner_ignorieren_nichtGefunden(discord.ui.Select):
                                                            
                                                                def __init__(self):
                                                                
                                                                    options = []

                                                                    c = 0

                                                                    for item in inventory:
                                                                        c += 1
                                                                        options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                    for item in itemsinchest:
                                                                        c += 1
                                                                        options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                    super().__init__(
                                                                        placeholder="Wähle die 5 Items, die du behalten möchtest.",
                                                                        min_values=5,
                                                                        max_values=5,
                                                                        options=options
                                                                    )


                                                                async def callback(select2, interaction : discord.Interaction):
                                                                    nonlocal message
                                                                    nonlocal inventory
                                                                    nonlocal gegner
                                                                    nonlocal leben
                                                                    nonlocal kills
                                                                    nonlocal shield
                                                                    nonlocal weapons
                                                                    nonlocal items
                                                                    inventory = select2.values
                                                                    await makeaction("Du hast zwar einen Gegner gehört, ihn aber Ignoriert. Zum Glück hat er dich nicht bemerkt. Du hast die Kiste geöffnet.")
                                                                    return

                                                            class DropdownView(discord.ui.View):
                                                                def __init__(self):
                                                                    super().__init__()


                                                                    self.add_item(DropDownMenu_Items_kiste_gegner_ignorieren_nichtGefunden())

                                                            view = DropdownView()


                                                            message = await message.edit(content = "Bitte wähle die 5 Items aus, die du benutzen möchtest.", view = view)

                                                        if happened == "Gegner findet dich":
                                                            if gegner == 99:
                                                                hits = random.randint(1, 10)
                                                                hhits = hits
                                                                while shield >= 20 and hits > 1:
                                                                    shield -= 20
                                                                    hits -= 1
                                                                while hits > 1:
                                                                    leben -= 20
                                                                    hits -= 1
                                                            elif "Pump" in inventory:
                                                                damage = random.randint(10, 75)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Golden Scar" in inventory:
                                                                damage = random.randint(10, 100)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Scar" in inventory:
                                                                damage = random.randint(20, 125)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Trommelgewehr" in inventory:
                                                                damage = random.randint(15, 100)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Pistole" in inventory:
                                                                damage = random.randint(50, 120)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Raketenwerfer" in inventory:
                                                                damage = random.randint(60, 130)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            elif "Sniper" in inventory:
                                                                damage = random.randint(30, 90)
                                                                while shield >= 0:
                                                                    shield -= 1
                                                                    damage -= 1
                                                                leben -= damage
                                                            if leben > 0:
                                                                itemsinchest = []
                                                                for _ in range(3):
                                                                    
                                                                    madeitin = False
                                                                    while madeitin == False:
                                                                        x  = random.choice(items)
                                                                        if x not in inventory and x not in itemsinchest:
                                                                            itemsinchest.append(x)
                                                                            madeitin = True
                                                                for _ in range(2):
                                                                    
                                                                    madeitin = False
                                                                    while madeitin == False:
                                                                        x  = random.choice(weapons)
                                                                        if x not in inventory and x not in itemsinchest:
                                                                            itemsinchest.append(x)
                                                                            madeitin = True

                                                                class DropDownMenu_Items_Kiste_gegner_kampf(discord.ui.Select):
                                                                
                                                                    def __init__(self):
                                                                    
                                                                        options = []

                                                                        c = 0

                                                                        for item in inventory:
                                                                            c += 1
                                                                            options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                        for item in itemsinchest:
                                                                            c += 1
                                                                            options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                                        super().__init__(
                                                                            placeholder="Wähle die 5 Items, die du behalten möchtest.",
                                                                            min_values=5,
                                                                            max_values=5,
                                                                            options=options
                                                                        )




                                                                    async def callback(select2, interaction : discord.Interaction):
                                                                        nonlocal message
                                                                        nonlocal inventory
                                                                        nonlocal gegner
                                                                        nonlocal leben
                                                                        nonlocal kills
                                                                        nonlocal shield
                                                                        nonlocal weapons
                                                                        nonlocal items
                                                                        inventory = select2.values
                                                                        await makeaction("Du hast versucht, den Gegner zu Ignorieren. Er hat dich aber bemerkt und hat dich angegriffen. Ihr habt gekämpft. Zum Glück hast du gewonnen.")
                                                                        kills += 1
                                                                        return

                                                                class DropdownView(discord.ui.View):
                                                                    def __init__(self):
                                                                        super().__init__()


                                                                        self.add_item(DropDownMenu_Items_Kiste_gegner_kampf())

                                                                view = DropdownView()


                                                                message = await message.edit(content = "Bitte wähle die 5 Items aus, die du benutzen möchtest.", view = view)
                                                            else:
                                                                    await makeaction("Du hast versucht, den Gegner zu Ignorieren. Er hat dich aber bemerkt und hat dich angegriffen. Ihr habt gekämpft. Leider hast du den kampf verloren.")
                                                                    return

                                                    if gegnerhörenselect.values[0] == "suchen":
                                                        await gegnersuchen()
                                                    elif gegnerhörenselect.values[0] == "laufen":
                                                        await weglaufen()
                                                    else:
                                                        await ignorieren()



                                            class DropdownView(discord.ui.View):
                                                def __init__(self):
                                                    super().__init__()


                                                    self.add_item(DropDownMenu_kiste_gegnergehört())

                                            view = DropdownView()


                                            message = await message.edit(content = "Du hörst Gegner. Was möchtest du tun?.", view = view)

                                        if happened == "Du öffnest Kiste":
                                            itemsinchest = []
                                            for _ in range(3):
                                                
                                                madeitin = False
                                                
                                                while madeitin == False:
                                                    x  = random.choice(items)
                                                    print(x)
                                                    if x not in inventory and x not in itemsinchest:
                                                        itemsinchest.append(x)
                                                        madeitin = True
                                            for _ in range(2):
                                                madeitin = False
                                                while madeitin == False:
                                                    x  = random.choice(weapons)
                                                    print(x)
                                                    if x not in inventory and x not in itemsinchest:
                                                        itemsinchest.append(x)
                                                        madeitin = True

                                            class DropDownMenu_Items_Kiste_öffnen_normal(discord.ui.Select):
                                            
                                                def __init__(self):
                                                
                                                    options = []

                                                    c = 0

                                                    for item in inventory:
                                                        c += 1
                                                        options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                    for item in itemsinchest:
                                                        c += 1
                                                        options.append(discord.SelectOption(label = item, description = f"Klicke, um {item} zu behalten", value = item))

                                                    super().__init__(
                                                        placeholder="Wähle die 5 Items, die du behalten möchtest.",
                                                        min_values=5,
                                                        max_values=5,
                                                        options=options
                                                    )


                                                async def callback(select2, interaction : discord.Interaction):
                                                    nonlocal message
                                                    nonlocal inventory
                                                    nonlocal gegner
                                                    nonlocal leben
                                                    nonlocal kills
                                                    nonlocal shield
                                                    nonlocal weapons
                                                    nonlocal items
                                                    inventory = select2.values
                                                    await makeaction("Du hast die Kiste geöffnet.")
                                                    return

                                            class DropdownView(discord.ui.View):
                                                def __init__(self):
                                                    super().__init__()


                                                    self.add_item(DropDownMenu_Items_Kiste_öffnen_normal())

                                            view = DropdownView()


                                            message = await message.edit(content = "Bitte wähle die 5 Items aus, die du benutzen möchtest.", view = view)

                                    else:
                                        await makeaction("Du hast die Kiste Ignoriert und bist weiter gegangen.")
                                        return

                                        view = discord.ui.View()

                                        öpnen = discord.ui.Button(label = "Kiste öffnen", style = discord.ButtonStyle.blurple, disabled=False, row = 3, custom_id = str(8))
                                        öpnen.callback = öffnen
                                        niköpnen = discord.ui.Button(label = "Kiste nicht öffnen", style = discord.ButtonStyle.blurple, disabled=False, row = 3, custom_id = str(9))
                                        niköpnen.callback = nicht_öffnen
                                        view.add_item(öpnen)
                                        view.add_item(niköpnen)

                                        myEmbed = discord.Embed(title = f"Kiste in {select.values[0]} gefunden", description = f"Du hast eine Kiste gefunden. Willst du sie öffnen?\n\n`was zuletzt geschah: `{lasthappened}")
                                        message = await message.edit(embed = myEmbed, view = view)
                    
                            class Dropdown_kiste_firstmenu_viewer(discord.ui.View):
                                def __init__(self):
                                    super().__init__()


                                    self.add_item(Dropdown_kiste_firstmenu())

                            view = Dropdown_kiste_firstmenu_viewer()


                            txt = ""

                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            message = await message.edit("Du hast eine Kiste gefunden. Möchtest du sie Öffnen?", view = view, embed = myEmbed)

                        elif action == "Gegner Gefunden":
                            class Dropdown_gegner_firstmenu(discord.ui.Select):
                                def __init__(self):

                                    options = [
                                        discord.SelectOption(label = "Angreifen", description = f"Klicke, um die Kiste zu öffnen", value = "Angreifen"),
                                        discord.SelectOption(label = "Ignorieren", description = f"Klicke, um die Kiste nicht zu öffnen", value = "Ignorieren")

                                    ]
                                    super().__init__(
                                        placeholder="wähle aus, was du machen möchtest.",
                                        min_values=1,
                                        max_values=1,
                                        options=options
                                    )

            

                                async def callback(chestselect, interaction : discord.Interaction):

                                    nonlocal message
                                    nonlocal inventory
                                    nonlocal gegner
                                    nonlocal leben
                                    nonlocal kills
                                    nonlocal shield
                                    nonlocal weapons
                                    nonlocal items

                                    if chestselect.values[0] == "Angreifen":
                                        if gegner == 99:
                                            hits = random.randint(1, 10)
                                            hhits = hits
                                            while shield >= 20 and hits > 1:
                                                shield -= 20
                                                hits -= 1
                                            while hits > 1:
                                                leben -= 20
                                                hits -= 1
                                        elif "Sniper" in inventory:
                                            damage = random.randint(0, 30)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Raketenwerfer" in inventory:
                                            damage = random.randint(0, 60)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Pump" in inventory:
                                            damage = random.randint(10, 75)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Golden Scar" in inventory:
                                            damage = random.randint(10, 100)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Scar" in inventory:
                                            damage = random.randint(20, 125)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Trommelgewehr" in inventory:
                                            damage = random.randint(15, 100)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Pistole" in inventory:
                                            damage = random.randint(50, 120)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        else:
                                            damage = random.randint(100, 250)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        if leben > 0:
                                            await makeaction("Als du einen Gegner gesehen hast, hast du ihn elemeniert.")
                                            return
                                        else:
                                            await makeaction("Als du einen Gegner gesehen hast, hast du ihn angegriffen. Wäre wohl besser gewesen, du hättest ihn auch besiegen können.")
                                            return

                                    else:
                                        möglichkeiten = ["Gegner gefunden", "Gegner nicht gefunden"]
                                        happened = random.choice(möglichkeiten)
                                        if happened == "Gegner nicht gefunden":
                                            await makeaction("Du bist ganz Normal gelaufen. Als du einen Gegner gesehen hast, hast du ihn Ignoriert. Ihr seid euch aus den Weg gegangen.")
                                            return
                                        else:
                                            if gegner == 99:
                                                hits = random.randint(1, 10)
                                                hhits = hits
                                                while shield >= 20 and hits > 1:
                                                    shield -= 20
                                                    hits -= 1
                                                while hits > 1:
                                                    leben -= 20
                                                    hits -= 1
                                            elif "Pump" in inventory:
                                                damage = random.randint(10, 75)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Golden Scar" in inventory:
                                                damage = random.randint(10, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Scar" in inventory:
                                                damage = random.randint(20, 125)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Trommelgewehr" in inventory:
                                                damage = random.randint(15, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Pistole" in inventory:
                                                damage = random.randint(50, 120)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Raketenwerfer" in inventory:
                                                damage = random.randint(60, 130)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Sniper" in inventory:
                                                damage = random.randint(30, 90)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            else:
                                                damage = random.randint(100, 275)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            if leben > 0:
                                                await makeaction("Als du einen Gegner gesehen hast, wolltest du ihn Ignorieren. Er hat dich aber gesehen und dich angegriffen. Du hast ihn aber trotzdem fertig gemacht!")
                                                return
                                            else:
                                                await makeaction("Als du einen Gegner gesehen hast, hast du ihn angegriffen. Wäre wohl besser gewesen, du hättest ihn auch besiegen können.")
                                                return
                        
                        
                            class Dropdown_gegner_firstmenu_viewer(discord.ui.View):
                                def __init__(self):
                                    super().__init__()


                                    self.add_item(Dropdown_gegner_firstmenu())

                            view = Dropdown_gegner_firstmenu_viewer()


                            txt = ""

                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            message = await message.edit("Du hast einen Gegner gefunden. Was möchtest du tun?", view = view, embed = myEmbed)

                        elif action == "von Gegner angegrifen":
                            class Dropdown_gegner_firstmenu(discord.ui.Select):
                                def __init__(self):

                                    options = [
                                        discord.SelectOption(label = "Angreifen", description = f"Klicke, um dich gegen die Angreifer zu verteidigen", value = "Angreifen"),
                                        discord.SelectOption(label = "weglaufen", description = f"Klicke, um vor deinen gegnern wegzulaufen", value = "laufen")

                                    ]
                                    super().__init__(
                                        placeholder="wähle aus, was du machen möchtest.",
                                        min_values=1,
                                        max_values=1,
                                        options=options
                                    )

            

                                async def callback(chestselect, interaction : discord.Interaction):

                                    nonlocal message
                                    nonlocal inventory
                                    nonlocal gegner
                                    nonlocal leben
                                    nonlocal kills
                                    nonlocal shield
                                    nonlocal weapons
                                    nonlocal items

                                    if chestselect.values[0] == "Angreifen":
                                        if gegner == 99:
                                            hits = random.randint(1, 10)
                                            hhits = hits
                                            while shield >= 20 and hits > 1:
                                                shield -= 20
                                                hits -= 1
                                            while hits > 1:
                                                leben -= 20
                                                hits -= 1
                                        elif "Pump" in inventory:
                                            damage = random.randint(10, 75)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Golden Scar" in inventory:
                                            damage = random.randint(10, 100)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Scar" in inventory:
                                            damage = random.randint(20, 125)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Trommelgewehr" in inventory:
                                            damage = random.randint(15, 100)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Sniper" in inventory:
                                            damage = random.randint(40, 120)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Raketenwerfer" in inventory:
                                            damage = random.randint(40, 130)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Pistole" in inventory:
                                            damage = random.randint(50, 120)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        else:
                                            damage = random.randint(100, 250)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        if leben > 0:
                                            await makeaction("Du wurdest angegriffen. Zum Glück konntest du dich gegen deine Angreifer verteidigen.")
                                            return
                                        else:
                                            await makeaction("Du wurdest angegriffen und von den Angreifern elemeniert")
                                            return

                                    else:
                                        möglichkeiten = ["erfolgreich", "nicht erfolgreich", "nicht erfolgreich"]
                                        happened = random.choice(möglichkeiten)
                                        if happened == "erfolgreich":
                                            await makeaction("Du wurdest angegriffen, konntest aber weglaufen. Deine Verfolger haben dich verloren.")
                                            return
                                        else:
                                            if gegner == 99:
                                                hits = random.randint(1, 10)
                                                hhits = hits
                                                while shield >= 20 and hits > 1:
                                                    shield -= 20
                                                    hits -= 1
                                                while hits > 1:
                                                    leben -= 20
                                                    hits -= 1
                                            elif "Pump" in inventory:
                                                damage = random.randint(10, 75)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Golden Scar" in inventory:
                                                damage = random.randint(10, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Scar" in inventory:
                                                damage = random.randint(20, 125)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Trommelgewehr" in inventory:
                                                damage = random.randint(15, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Pistole" in inventory:
                                                damage = random.randint(50, 120)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Raketenwerfer" in inventory:
                                                damage = random.randint(60, 130)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Sniper" in inventory:
                                                damage = random.randint(30, 90)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            else:
                                                damage = random.randint(100, 275)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            if leben > 0:
                                                await makeaction("Du wurdest angegriffen und hast dich dafür entschieden, wegzulaufen. Dein Verfolger hat aber nicht locker gelassen, sodass du ihn angreifen musstest. Natürlich hast du gewonnen!")
                                                return
                                            else:
                                                await makeaction("Du wurdest angegriffen und wolltest vor deinen gegner weglaufen. Leider war er schneller und hat dich Eingeholt und elemeniert.")
                                                return
                        
                        
                            class Dropdown_gegner_firstmenu_viewer(discord.ui.View):
                                def __init__(self):
                                    super().__init__()


                                    self.add_item(Dropdown_gegner_firstmenu())

                            view = Dropdown_gegner_firstmenu_viewer()



                            txt = ""

                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            message = await message.edit("Du wirst von einen Gegner angegriffen. Was möchtest du tun?", view = view, embed = myEmbed)

                        elif action == "Angel gefunden":
                            class Dropdown_gegner_firstmenu(discord.ui.Select):
                                def __init__(self):

                                    options = [
                                        discord.SelectOption(label = "Angeln", description = f"Klicke, um Die Angel zu benutzen und etwas zu angeln.", value = "angeln"),
                                        discord.SelectOption(label = "Nicht Angeln", description = f"Klicke, um Die Angel zu ignorieren und weiter zu gehen.", value = "nicht angeln")

                                    ]
                                    super().__init__(
                                        placeholder="wähle aus, was du machen möchtest.",
                                        min_values=1,
                                        max_values=1,
                                        options=options
                                    )

            

                                async def callback(chestselect, interaction : discord.Interaction):

                                    nonlocal message
                                    nonlocal inventory
                                    nonlocal gegner
                                    nonlocal leben
                                    nonlocal kills
                                    nonlocal shield
                                    nonlocal weapons
                                    nonlocal items

                                    if chestselect.values[0] == "nicht angeln":
                                        await makeaction("Du hast zwar eine Angel gesehen, dich aber dagegen Entschieden zu angeln.")
                                        return

                                    else:
                                        möglichkeiten = ["Floppers", "Slurpfish", "Jellyfish", "Shieldfish", "Spicy Fish", "Small Fry", "Hop Flopper", "gegner"]
                                        happened = random.choice(möglichkeiten)
                                        if happened == "gegner":
                                            if gegner == 99:
                                                hits = random.randint(1, 10)
                                                hhits = hits
                                                while shield >= 20 and hits > 1:
                                                    shield -= 20
                                                    hits -= 1
                                                while hits > 1:
                                                    leben -= 20
                                                    hits -= 1
                                            elif "Pump" in inventory:
                                                damage = random.randint(10, 75)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Golden Scar" in inventory:
                                                damage = random.randint(10, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Scar" in inventory:
                                                damage = random.randint(20, 125)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Trommelgewehr" in inventory:
                                                damage = random.randint(15, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Sniper" in inventory:
                                                damage = random.randint(40, 120)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Raketenwerfer" in inventory:
                                                damage = random.randint(40, 130)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Pistole" in inventory:
                                                damage = random.randint(50, 120)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            else:
                                                damage = random.randint(100, 250)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            if leben > 0:
                                                await makeaction("Eigentlich wolltest du nur Angeln, aber ein Gegner hat dich angegriffen. Du hast ihn aber natürlich besiegt <:P_Shrug:959817497882808342>")
                                                return
                                            else:
                                                await makeaction("Du wolltest nur Angeln, wurdest aber angegriffen. Leider hat dich der Angreifer besiegt.")
                                                return
                                        elif happened == "Floppers":
                                            leben += 40
                                            if leben > 100:
                                                leben = 100
                                            await makeaction("Du hast einen Floppers geangelt und ihn gegessen.")
                                            return
                                        elif happened == "Slurpfish":
                                            leben += 40
                                            if leben > 100:
                                                shield += leben - 100
                                                leben = 100
                                                if shield > 100:
                                                    shield = 100
                                            await makeaction("Du hast einen Slurpfish geangelt und ihn gegessen.")
                                            return
                                        elif happened == "Jellyfish":
                                            leben += 40
                                            if leben > 100:
                                                shield += leben - 100
                                                leben = 100
                                                if shield > 100:
                                                    shield = 100
                                            await makeaction("Du hast einen Jellyfish geangelt und ihn gegessen.")
                                            return
                                        elif happened == "Shieldfish":
                                            shield += 50
                                            if shield > 100:
                                                shield = 100
                                            await makeaction("Du hast einen Shieldfish geangelt und ihn gegessen.")
                                            return
                                        elif happened == "Spicy Fish":
                                            leben += 15
                                            if leben > 100:
                                                leben = 100
                                            await makeaction("Du hast einen Spicy Fish geangelt und ihn gegessen.")
                                            return
                                        elif happened == "Small Fry":
                                            if leben <= 75:
                                                leben += 15
                                                if leben > 75:
                                                    leben = 75
                                            await makeaction("Du hast einen Small Fry geangelt und ihn gegessen.")
                                            return
                                        else:
                                            leben += 15
                                            if leben > 100:
                                                leben = 100
                                            await makeaction("Du hast einen Hop Flopper geangelt und ihn gegessen.")
                                            return
                                        
                        
                            class Dropdown_gegner_firstmenu_viewer(discord.ui.View):
                                def __init__(self):
                                    super().__init__()


                                    self.add_item(Dropdown_gegner_firstmenu())

                            view = Dropdown_gegner_firstmenu_viewer()


                            txt = ""

                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            message = await message.edit("Du hast eine Angel gefunden! Möchtest du sie benutzen?", view = view, embed = myEmbed)

                        elif action == "von Sniper getroffen":
                            class Dropdown_gegner_firstmenu(discord.ui.Select):
                                def __init__(self):

                                    options = [
                                        discord.SelectOption(label = "Angreifen", description = f"Klicke, um anzugreifen", value = "Angreifen"),
                                        discord.SelectOption(label = "weglaufen", description = f"Klicke, um wegzulaufen", value = "Ignorieren")

                                    ]
                                    super().__init__(
                                        placeholder="wähle aus, was du machen möchtest.",
                                        min_values=1,
                                        max_values=1,
                                        options=options
                                    )

            

                                async def callback(chestselect, interaction : discord.Interaction):

                                    nonlocal message
                                    nonlocal inventory
                                    nonlocal gegner
                                    nonlocal leben
                                    nonlocal kills
                                    nonlocal shield
                                    nonlocal weapons
                                    nonlocal items

                                    if chestselect.values[0] == "Angreifen":
                                        if gegner == 99:
                                            hits = random.randint(1, 10)
                                            hhits = hits
                                            while shield >= 20 and hits > 1:
                                                shield -= 20
                                                hits -= 1
                                            while hits > 1:
                                                leben -= 20
                                                hits -= 1
                                        elif "Sniper" in inventory:
                                            damage = random.randint(0, 30)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Raketenwerfer" in inventory:
                                            damage = random.randint(0, 60)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Pump" in inventory:
                                            damage = random.randint(10, 75)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Golden Scar" in inventory:
                                            damage = random.randint(10, 100)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Scar" in inventory:
                                            damage = random.randint(20, 125)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Trommelgewehr" in inventory:
                                            damage = random.randint(15, 100)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        elif "Pistole" in inventory:
                                            damage = random.randint(50, 120)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        else:
                                            damage = random.randint(100, 250)
                                            while shield >= 0:
                                                shield -= 1
                                                damage -= 1
                                            leben -= damage
                                        if leben > 0:
                                            await makeaction("Du wurdest mit einem Scharfschützengewehr angeschossen. Dadurch warst du natürlich stark im Nachteil und bist leider gestorben.")
                                            return
                                        else:
                                            await makeaction("Du wurdest mit einem Scharfschützengewehr angeschossen. Den Angreifer hast du natürlich verfolgt und elemeniert.")
                                            return

                                    else:
                                        möglichkeiten = ["Gegner gefunden", "Gegner nicht gefunden", "Gegner nicht gefunden", "Gegner nicht gefunden"]
                                        happened = random.choice(möglichkeiten)
                                        if happened == "Gegner nicht gefunden":
                                            await makeaction("Als du von einem Scharfschützengewehr angeschossen wurdest, bist du ganz schnell weg gerannt. Der Angreifer hat dich nie wieder gesehen.")
                                            return
                                        else:
                                            if gegner == 99:
                                                hits = random.randint(1, 10)
                                                hhits = hits
                                                while shield >= 20 and hits > 1:
                                                    shield -= 20
                                                    hits -= 1
                                                while hits > 1:
                                                    leben -= 20
                                                    hits -= 1
                                            elif "Pump" in inventory:
                                                damage = random.randint(10, 75)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Golden Scar" in inventory:
                                                damage = random.randint(10, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Scar" in inventory:
                                                damage = random.randint(20, 125)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Trommelgewehr" in inventory:
                                                damage = random.randint(15, 100)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Pistole" in inventory:
                                                damage = random.randint(50, 120)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Raketenwerfer" in inventory:
                                                damage = random.randint(60, 130)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            elif "Sniper" in inventory:
                                                damage = random.randint(30, 90)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            else:
                                                damage = random.randint(100, 275)
                                                while shield >= 0:
                                                    shield -= 1
                                                    damage -= 1
                                                leben -= damage
                                            if leben > 0:
                                                await makeaction("Du wurdest von einem Scharfschützengewehr angegriffen und bist weg gerannt. Du konntest deinen Angreifer jedoch nicht entkommen. Deshalb hast du ihn angegriffen und besiegt.")
                                                return
                                            else:
                                                await makeaction("Du wurdest von einem Scharfschützengewehr angegriffen und bist weg gerannt. Du konntest deinen Angreifer jedoch nicht entkommen. Der Angreifer konnte dich besiegen.")
                                                return
                        
                        
                            class Dropdown_gegner_firstmenu_viewer(discord.ui.View):
                                def __init__(self):
                                    super().__init__()


                                    self.add_item(Dropdown_gegner_firstmenu())

                            view = Dropdown_gegner_firstmenu_viewer()

                            txt = ""
                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            message = await message.edit("auf dich wurde mit einer Sniper geschossen. Was möchtest du tun?", view = view, embed = myEmbed)

                        else:

                            class Dropdown_gegner_firstmenu(discord.ui.Select):
                                def __init__(self):

                                    options = []

                                    for item in inventory:
                                        if item in items:
                                            discord.SelectOption(label = "item", description = f"Klicke, um {item} zu benutzen", value = item),


                                    super().__init__(
                                        placeholder="wähle aus, welches item du benutzen möchtest.",
                                        min_values=1,
                                        max_values=1,
                                        options=options
                                    )

            

                                async def callback(chestselect, interaction : discord.Interaction):

                                    nonlocal message
                                    nonlocal inventory
                                    nonlocal gegner
                                    nonlocal leben
                                    nonlocal kills
                                    nonlocal shield
                                    nonlocal weapons
                                    nonlocal items

                                    if chestselect.values[0] == "Mini Shield":
                                        if shield <= 50:
                                            shield += 25
                                            if shield > 50:
                                                shield = 50
                                        await makeaction("Du hast Mini Shield benutzt.")
                                        return

                                    if chestselect.values[0] == "Shield":
                                        shield += 50
                                        if shield > 100:
                                            shield = 100
                                        await makeaction("Du hast Shield Trank benutzt.")
                                        return

                                    if chestselect.values[0] == "Bandages":
                                        if leben < 75:
                                            leben += 15
                                            if leben > 75:
                                                leben = 75
                                        await makeaction("Du hast Bandages benutzt.")
                                        return

                                    if chestselect.values[0] == "Medkit":
                                        leben = 100
                                        await makeaction("Du hast Medkit benutzt.")
                                        return

                                    if chestselect.values[0] == "Chug Jug":
                                        leben = 100
                                        shield = 100
                                        await makeaction("Du hast Chug Jug benutzt.")
                                        return

                                    if chestselect.values[0] == "Splashies":
                                        leben += 20
                                        if leben > 100:
                                            shield += leben - 100
                                            leben = 100
                                            if shield > 100:
                                                shield = 100
                                        await makeaction("Du hast Splashies benutzt.")
                                        return

                                    else:
                                        if leben < 95:
                                            leben += 15
                                            if leben > 95:
                                                leben = 95
                                        await makeaction("Du hast Fleisch benutzt.")
                                        return

                        
                        
                            class Dropdown_gegner_firstmenu_viewer(discord.ui.View):
                                def __init__(self):
                                    super().__init__()


                                    self.add_item(Dropdown_gegner_firstmenu())

                            view = Dropdown_gegner_firstmenu_viewer()


                            txt = ""

                            txt += f"\ngegner übrig: {gegner}"
                            txt += f"\nLeben: {leben}"
                            txt += f"\nShield: {shield}"
                            txt += f"\nKills: {kills}"
                            txt += f"\n\nAls letztes passiert: {lasthappened}"
                            if len(inventory) != 0:
                                txt += f"\n\n__Items in deinem Inventar__"
                            for item in inventory:
                                txt += f"\n{item}"
                                


                            myEmbed = discord.Embed(title = "Tanjnite", description= txt)

                            message = await message.edit("Es ist grade Ruhig, weshalb du ein Item benutzen solltest. Welches Item möchtest du verwenden?", view = view, embed = myEmbed)

                    await makeaction()

            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()


                    self.add_item(Dropdown_solo())

            view = DropdownView()


            message = await message.edit(content = "Bitte Wähle aus, wo du droppen möchtest.", view = view)

        async def duo():
            print("Du spielst Solo")

        async def squad():
            print("Du spielst Solo")
            # Wie kann das sein, dass bei beiden Solo ist?

        class DropDownMenu_Spielmodus(discord.ui.Select):
            def __init__(self):
                options = []

                for modi in spielmodi:
                    options.append(discord.SelectOption(label = modi, description = f"Klicke, um {modi} zu Spielen", value = modi))
            
                super().__init__(
                    placeholder="Wähle, welchen Spielmodus du spielen möchtest.",
                    min_values=1,
                    max_values=1,
                    options=options
                )


            async def callback(select, interaction : discord.Interaction):

                nonlocal message
                
                if select.values[0] == "solo":
                    print("Solo!")
                    await solo(message)
    
        class DropdownView(discord.ui.View):
            def __init__(self):
                super().__init__()


                self.add_item(DropDownMenu_Spielmodus())

        view = DropdownView()

        message = await ctx.send(content = "Bitte wähle aus, welchen Spielmodus du spielen möchtest.", view = view)




def setup(client):
    client.add_cog(Help(client))