import os
import discord
from datetime import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.listen()
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    # Fetch target channels
    target1_channel = guild.get_channel(940719313638293544)
    target2_channel = guild.get_channel(940719313638293544)
    target3_channel = guild.get_channel(942055833720750081)
    # Fetch target roles
    role_1 = guild.get_role(940612391819939840)
    role_2 = guild.get_role(940731429426434069)
    role_3 = guild.get_role(940731660440326154)

    if role_1 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_1.id}>")
        embed = discord.Embed(
            title="Market Commentary",
            description=msg,
            color=0x0BE60B,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Index:", value=role_1.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target1_channel.send(embed=embed)
        await message.channel.send(embed=embed)

    elif role_2 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_2.id}>")
        embed = discord.Embed(title=msg, color=0x0000FF, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_2.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target2_channel.send(embed=embed)
        await message.channel.send(embed=embed)

    elif role_3 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_3.id}>")
        embed = discord.Embed(title=msg, color=0xFF0000, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_3.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target3_channel.send(embed=embed)
        await message.channel.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    bot.run(TOKEN)
