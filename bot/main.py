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
#SPY Channel
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    target1_channel = guild.get_channel(882606056184897536)
    role_1 = guild.get_role(942052888333676634)
    roles = [role_1]

    for role in roles:
        if role in message.role_mentions:
            msg = message.content.strip(f'<@&{role.id}>')
            embed = discord.Embed(title="Market Commentary", description=msg, color=0x0be60b, timestamp=datetime.now())
            embed.add_field(name='Index:', value=role.mention)
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            await target1_channel.send(embed=embed)
            await message.channel.send(embed=embed)
            
@bot.listen()
#intraday
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    target2_channel = guild.get_channel(879466084116336660)
    role_2 = guild.get_role(942051860167159819)
    roles = [role_2]

    for role in roles:
        if role in message.role_mentions:
            msg = message.content.strip(f'<@&{role.id}>')
            embed = discord.Embed(title=msg, color=0x349434, timestamp=datetime.now())
            embed.add_field(name='Trade Type:', value=role.mention)
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            await target2_channel.send(embed=embed)
            await message.channel.send(embed=embed)

@bot.listen()
#scalp
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    target3_channel = guild.get_channel(879466084116336660)
    role_3 = guild.get_role(942052324615004250)
    roles = [role_3]

    for role in roles:
        if role in message.role_mentions:
            msg = message.content.strip(f'<@&{role.id}>')
            embed = discord.Embed(title=msg, color=0x782ea6, timestamp=datetime.now())
            embed.add_field(name='Trade Type:', value=role.mention)
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            await target3_channel.send(embed=embed)
            await message.channel.send(embed=embed)
            
@bot.listen()
#risky
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    target4_channel = guild.get_channel(879466084116336660)
    role_4 = guild.get_role(942052501228777493)
    roles = [role_4]

    for role in roles:
        if role in message.role_mentions:
            msg = message.content.strip(f'<@&{role.id}>')
            embed = discord.Embed(title=msg, color=0xc45a25, timestamp=datetime.now())
            embed.add_field(name='Trade Type:', value=role.mention)
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            await target4_channel.send(embed=embed)
            await message.channel.send(embed=embed)
            
@bot.listen()
#lotto
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    target5_channel = guild.get_channel(879466084116336660)
    role_5 = guild.get_role(942052699921321984)
    roles = [role_5]

    for role in roles:
        if role in message.role_mentions:
            msg = message.content.strip(f'<@&{role.id}>')
            embed = discord.Embed(title=msg, color=0xe31e87, timestamp=datetime.now())
            embed.add_field(name='Trade Type:', value=role.mention)
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            await target5_channel.send(embed=embed)
            await message.channel.send(embed=embed)
            
@bot.listen()
#futures
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    target5_channel = guild.get_channel(879466084116336660)
    role_5 = guild.get_role(942052789100617728)
    roles = [role_5]

    for role in roles:
        if role in message.role_mentions:
            msg = message.content.strip(f'<@&{role.id}>')
            embed = discord.Embed(title=msg, color=0xe0dd12, timestamp=datetime.now())
            embed.add_field(name='Trade Type:', value=role.mention)
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            await target5_channel.send(embed=embed)
            await message.channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    bot.run(TOKEN)
