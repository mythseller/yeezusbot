import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.listen()
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.listen()
async def on_message(message):  
    if message.author.bot: return
    guild = message.guild  
    target_channel = guild.get_channel(940719313638293544)  
# set list of role IDs and the empty list for the role objects
    role_ids = [940612391819939840, 940731429426434069, 940731660440326154]
    role_objs = []  

# iterate through role IDs and get role objects - append to role_objs list
    for role in role_ids:
    role_objs.append(guild.get_role(role))  

# check if any of the roles in message.role_mentions exists in the role_objs list
    if any(role in message.role_mentions for role in roles_objs): 
        await target_channel.send(message.author.name + " -- " + message.content)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)

