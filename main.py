from distutils.command.config import config
from json import load
import discord
from cogs.settings import bot_token
from discord.ext import commands

intents = discord.Intents.default()

client = commands.Bot(command_prefix='!', help_command=None)

load_cogs = [
    'cogs.report',
    'cogs.warn',
    'cogs.social',
    'cogs.fun',
    'cogs.voice',
    'cogs.mute',
    'cogs.verify',
    'cogs.ban'
]
for cog in load_cogs:
    client.load_extension(cog)


@client.event
async def on_ready():
    print(f"Logged in as bot {client.user.name}")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help", description="Here are the commands you can use", color=0x00ff00)
    embed.add_field(name="!ping", value="Pong!", inline=False)
    embed.add_field(
        name="!invite", value="Invite the bot to your server", inline=False)
    embed.add_field(name="!github", value="GitHub link", inline=False)
    embed.add_field(name="!insta", value="Instagram link", inline=False)
    embed.add_field(name="!yt", value="YouTube channel link", inline=False)
    embed.add_field(name="!report {REASON}",
                    value="Report a user", inline=False)
    embed.add_field(name="!bring [coffee, tea, water, mate]",
                    value="Get a drink", inline=False)
    embed.add_field(name="!help", value="Shows this message", inline=False)
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='coding around'))


client.run(bot_token)
