import os
import discord
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
    target_channel = guild.get_channel(940719313638293544)
    role_1 = guild.get_role(940612391819939840)
    role_2 = guild.get_role(940731429426434069)
    role_3 = guild.get_role(940731660440326154)
    roles = [role_1, role_2, role_3]

    if any(role in roles for role in message.role_mentions):
        embed = discord.Embed(
            title=message.content,
            description=message.author.display_name,
            color=0xFFFF00,
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await target_channel.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    bot.run(TOKEN)
