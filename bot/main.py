import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.listen()
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.listen()
async def on_message(message):  
    guild = message.guild  
    target_channel = guild.get_channel(920900596117155860)  
    target_role = guild.get_role(940612391819939840) 
    role_mentions = message.role_mentions

    if target_role in role_mentions:
        await target_channel.send(message.content)
    if (message.author.bot) return;

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)

