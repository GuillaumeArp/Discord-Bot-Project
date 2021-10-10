import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)


    print(f'{bot.user.name} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
          )

emoji_python = "<:python:896781436948975646>"
emoji_sql = "<:sql:896781407052001320>"
emoji_tableau = "<:tableau:896780976745775104>"
emoji_powerbi = "<:powerbi:896781226185195620>"
emoji_windows = "<:windows:896781323312693369>"
emoji_linux = "<:linux:896781371744338041>"
emoji_macos = "<:macos:896782073770147840>"
emoji_jetbrains = "<:jetbrains:896782108486434877>"
emoji_vscode = "<:vscode:896782141386526741>"
emoji_knime = "<:knime:896780876770340914>"
emoji_dataiku = "<:dataiku:896780823829811270>"
emoji_git = "<:git:896786303683801098>"

pep20 = [
    'Beautiful is better than ugly. (PEP 20 -- The Zen of Python)',
    'Explicit is better than implicit. (PEP 20 -- The Zen of Python)',
    'Simple is better than complex. (PEP 20 -- The Zen of Python)',
    "Complex is better than complicated. (PEP 20 -- The Zen of Python)",
    "Flat is better than nested. (PEP 20 -- The Zen of Python)",
    "Sparse is better than dense. (PEP 20 -- The Zen of Python)",
    "Readability counts. (PEP 20 -- The Zen of Python)",
    "Special cases aren't special enough to break the rules. (PEP 20 -- The Zen of Python)",
    "Although practicality beats purity. (PEP 20 -- The Zen of Python)",
    "Errors should never pass silently. (PEP 20 -- The Zen of Python)",
    "Unless explicitly silenced. (PEP 20 -- The Zen of Python)",
    "In the face of ambiguity, refuse the temptation to guess. (PEP 20 -- The Zen of Python)",
    "There should be one-- and preferably only one --obvious way to do it. (PEP 20 -- The Zen of Python)",
    "Although that way may not be obvious at first unless you're Dutch. (PEP 20 -- The Zen of Python)",
    "Now is better than never. (PEP 20 -- The Zen of Python)",
    "Although never is often better than *right* now. (PEP 20 -- The Zen of Python)",
    "If the implementation is hard to explain, it's a bad idea. (PEP 20 -- The Zen of Python)",
    "If the implementation is easy to explain, it may be a good idea. (PEP 20 -- The Zen of Python)",
    "Namespaces are one honking great idea -- let's do more of those! (PEP 20 -- The Zen of Python)"
]

full_pep20 = f"https://www.python.org/dev/peps/pep-0020/ {emoji_python}"


@bot.command(name='pep', help='Responds with one random Zen of Python statement')
async def pep_python(ctx):
    response = random.choice(pep20)
    await ctx.send(response)

@bot.command(name='pep20', help='Sends the link for the PEP20 page on python.org')
async def pep_python(ctx):
    response = full_pep20
    await ctx.send(response)

@bot.command(name='sign', help='Reminds everyone to sign the attendance popup in Odyssey')
async def pep_python(ctx):
    response = '@everyone Émargement disponible !'
    await ctx.send(response)


bot.run(TOKEN)





