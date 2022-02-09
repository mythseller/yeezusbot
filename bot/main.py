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
    role_1 = guild.get_role(940612391819939840)  
    role_2 = guild.get_role(940731429426434069)
    role_3 = guild.get_role(940731660440326154) 

    if role_1 in message.role_mentions: 
        await target_channel.send(message.author.name + " -- " + message.content)
    elif role_2 in message.role_mentions: 
        await target_channel.send(message.author.name + " -- " + message.content)
    elif role_3 in message.role_mentions: 
        embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embed)
    


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
