import discord
import os

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="IgnitionCTRL"))

@client.event
async def on_message(message):
    if message.content == "!gen roblox":
        # Read the accounts from the file
        with open("roblox.txt", "r") as f:
            accounts = f.readlines()
        
        # Make sure there are accounts available
        if not accounts:
            await message.channel.send("Sorry, no accounts are available at this time.")
            return
        
        # Choose a random account and remove it from the list
        import random
        account = random.choice(accounts)
        accounts.remove(account)
        
        # Save the remaining accounts back to the file
        with open("roblox.txt", "w") as f:
            f.writelines(accounts)
        
        # Send the account to the user through DM
        await message.author.send("Here is your Boblox account: " + account)
        
        # Let the user know that the account was sent through DM
        await message.channel.send("Account received, check your DMs.")
    
    elif message.content == "!gen spotify":
        # Read the accounts from the file
        with open("spotify.txt", "r") as f:
            accounts = f.readlines()
        
        # Make sure there are accounts available
        if not accounts:
            await message.channel.send("Sorry, no accounts are available at this time.")
            return
        
        # Choose a random account and remove it from the list
        import random
        account = random.choice(accounts)
        accounts.remove(account)
        
        # Save the remaining accounts back to the file
        with open("spotify.txt", "w") as f:
            f.writelines(accounts)
        
        # Send the account to the user through DM
        await message.author.send("Here is your Spotify account: " + account)
        
        # Let the user know that the account was sent through DM
        await message.channel.send("Account received, check your DMs.")

      
    elif message.content == "!gen valorant":
        # Read the accounts from the file
        with open("valorant.txt", "r") as f:
            accounts = f.readlines()
        
        # Make sure there are accounts available
        if not accounts:
            await message.channel.send("Sorry, no accounts are available at this time.")
            return
        
        # Choose a random account and remove it from the list
        import random
        account = random.choice(accounts)
        accounts.remove(account)
        
        # Save the remaining accounts back to the file
        with open("valorant.txt", "w") as f:
            f.writelines(accounts)
        
        # Send the account to the user through DM
        await message.author.send("Here is your Valorant account: " + account)
        
        # Let the user know that the account was sent through DM
        await message.channel.send("Account received, check your DMs.")

    elif message.content == "!gen help":
       
      
        await message.channel.send("**You can use the !gen command to generate valorant, spotify, roblox and we are adding more every now an then. How to generate? Use !gen {what do you want to genearte} , it's as easy as that.**")
      
# get the bot token from Replit Secrets
TOKEN = os.environ["TOKEN"]
client.run(TOKEN)


