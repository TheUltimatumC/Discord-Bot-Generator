import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="IgnitionCTRL"))

@client.event
async def on_message(message):
    if message.content == "!gen roblox":
        with open("roblox.txt", "r") as f:
            accounts = f.readlines()
        
        if not accounts:
            await message.channel.send("Sorry, no accounts are available at this time.")
            return
        
        import random
        account = random.choice(accounts)
        accounts.remove(account)
        
        with open("roblox.txt", "w") as f:
            f.writelines(accounts)
        
        await message.author.send("Here is your Boblox account: " + account)
        await message.channel.send("Account received, check your DMs.")
    
    elif message.content == "!gen spotify":
        with open("spotify.txt", "r") as f:
            accounts = f.readlines()
        
        if not accounts:
            await message.channel.send("Sorry, no accounts are available at this time.")
            return
        
        import random
        account = random.choice(accounts)
        accounts.remove(account)
        
        with open("spotify.txt", "w") as f:
            f.writelines(accounts)
        
        await message.author.send("Here is your Spotify account: " + account)
        await message.channel.send("Account received, check your DMs.")

      
    elif message.content == "!gen valorant":
        with open("valorant.txt", "r") as f:
            accounts = f.readlines()
        
        if not accounts:
            await message.channel.send("Sorry, no accounts are available at this time.")
            return
        
        import random
        account = random.choice(accounts)
        accounts.remove(account)
        
        with open("valorant.txt", "w") as f:
            f.writelines(accounts)
        
        await message.author.send("Here is your Valorant account: " + account)
        
        await message.channel.send("Account received, check your DMs.")

    elif message.content == "!gen help":
       
      
        await message.channel.send("**You can use the !gen command to generate valorant, spotify, roblox and we are adding more every now an then. How to generate? Use !gen {what do you want to genearte} , it's as easy as that.**")
      
client.run(TOKEN)


