import os
import discord
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents = intents)
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
    callout_channel = guild.get_channel(879466084116336660)
    spy_channel = guild.get_channel(882606056184897536)
    futures_channel = guild.get_channel(879468481492447254)
    shitposting_channel = guild.get_channel(879467246953570305)
    # Fetch target roles
    spy_role = guild.get_role(942052888333676634)
    intraday_role = guild.get_role(942051860167159819)
    scalp_role = guild.get_role(942052324615004250)
    risky_role = guild.get_role(942052501228777493)
    lotto_role = guild.get_role(942052699921321984)
    futures_role = guild.get_role(942052789100617728)
    goblin_role = guild.get_role(950706317482410015)

    if spy_role in message.role_mentions:
        msg = message.content.strip(f"<@&{spy_role.id}>")
        embed = discord.Embed(
            title="Market Commentary",
            description=msg,
            color=0x0be60b,
            timestamp=datetime.now(),
        )
        # embed.add_field(name="Index:", value=spy_role.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        embed2 = discord.Embed(
            title=msg,
            color=0x0be60b,
            timestamp=datetime.now(),
        )
        embed2.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await spy_channel.send("<@&942052888333676634>")
        await spy_channel.send(embed=embed)
        await futures_channel.send(embed=embed2)
        await message.channel.send(embed=embed)

    elif intraday_role in message.role_mentions:
        # intraday
        msg = message.content.strip(f"<@&{intraday_role.id}>")
        embed = discord.Embed(title=msg, color=0x349434, timestamp=datetime.now())
        # embed.add_field(name="Risk level:", value=intraday_role.mention)
        embed.add_field(name="Risk level:", value="Intraday")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        noti = await callout_channel.send(msg + f"<@&{intraday_role.id}>")
        await noti.delete()
        targetEmoji = await callout_channel.send(embed=embed)
        messageEmoji = await message.channel.send(embed=embed)
        await messageEmoji.add_reaction("👍")
        await messageEmoji.add_reaction("❌")
        # await targetEmoji.add_reaction("👍")
        # await targetEmoji.add_reaction("❌")


    elif scalp_role in message.role_mentions:
        #scalp
        msg = message.content.strip(f"<@&{scalp_role.id}>")
        embed = discord.Embed(title=msg, color=0x782ea6, timestamp=datetime.now())
        # embed.add_field(name="Risk level:", value=scalp_role.mention)
        embed.add_field(name="Risk level:", value="Scalp")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        noti = await callout_channel.send(msg + f"<@&{scalp_role.id}>")
        await noti.delete()
        targetEmoji = await callout_channel.send(embed=embed)
        messageEmoji = await message.channel.send(embed=embed)
        await messageEmoji.add_reaction("👍")
        await messageEmoji.add_reaction("❌")
        # await targetEmoji.add_reaction("👍")
        # await targetEmoji.add_reaction("❌")
        
    elif risky_role in message.role_mentions:
        #risky
        msg = message.content.strip(f"<@&{risky_role.id}>")
        embed = discord.Embed(title=msg, color=0xc45a25, timestamp=datetime.now())
        # embed.add_field(name="Risk level:", value=risky_role.mention)
        embed.add_field(name="Risk level:", value="Risky")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        noti = await callout_channel.send(msg + f"<@&{risky_role.id}>")
        await noti.delete()
        targetEmoji = await callout_channel.send(embed=embed)
        messageEmoji = await message.channel.send(embed=embed)
        await messageEmoji.add_reaction("👍")
        await messageEmoji.add_reaction("❌")
        # await targetEmoji.add_reaction("👍")
        # await targetEmoji.add_reaction("❌")
        
    elif lotto_role in message.role_mentions:
        #lotto
        msg = message.content.strip(f"<@&{lotto_role.id}>")
        embed = discord.Embed(title=msg, color=0xe31e87, timestamp=datetime.now())
        # embed.add_field(name="Risk level:", value=lotto_role.mention)
        embed.add_field(name="Risk level:", value="Lotto")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        noti = await callout_channel.send(msg + f"<@&{lotto_role.id}>")
        await noti.delete()
        targetEmoji = await callout_channel.send(embed=embed)
        targetEmoji = await message.channel.send(embed=embed)
        await messageEmoji.add_reaction("👍")
        await messageEmoji.add_reaction("❌")
        # await targetEmoji.add_reaction("👍")
        # await targetEmoji.add_reaction("❌")
        
    elif futures_role in message.role_mentions:
        # futures
        msg = message.content.strip(f"<@&{futures_role.id}>")
        embed = discord.Embed(title=msg, color=0xe0dd12, timestamp=datetime.now())
        # embed.add_field(name="Trade Type:", value=futures_role.mention)
        # embed.add_field(name="Risk level:", value="Futures")
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await futures_channel.send(embed=embed)
   
    elif goblin_role in message.role_mentions:
        # goblin mode
        msg = message.content.strip(f"<@&{goblin_role.id}>")
        embed = discord.Embed(title="said some dumb shit", description=msg, color=0xe31e87, timestamp=datetime.now())
        # embed.add_field(name="we goin", value=goblin_role.mention)
        embed.add_field(name="we goin", value=goblin_role.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )

        targetEmoji = await shitposting_channel.send(embed=embed)
        messageEmoji = await message.channel.send(embed=embed)
        await messageEmoji.add_reaction("😩")
        await targetEmoji.add_reaction("😩")

@bot.listen()
async def on_message(message):
  '''simple on message to respond if a message containing "hello" is sent'''
  # prevent bot from answering other bots, including self
  if message.author.bot:
     return
  # create message content and channel variables
  content = message.content.lower()
  channel = message.channel
  # check if message includes "hello"
  if 'did we do today' in content:
    msg = await channel.send('yeah, you bank on these dank callouts or fuck it up?')
    await msg.add_reaction("🟢")
    await msg.add_reaction("🔴")
@bot.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    bot.run(TOKEN)
