import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
from urllib.parse import quote_plus as qp

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
async def pep(ctx):
    response = random.choice(pep20)
    await ctx.send(response)

@bot.command(name='pep20', help='Sends the link for the PEP20 page on python.org')
async def pep20(ctx):
    response = full_pep20
    await ctx.send(response)

@bot.command(name='sign', help='Reminds everyone to sign the attendance popup in Odyssey')
async def sign(ctx):
    response = '@everyone Émargement disponible !'
    await ctx.send(response)

@bot.command(name='scrum', help='Sends the Scrum 2020 guide')
async def scrum(ctx):
    response = "https://drive.google.com/file/d/1vnhynIyVQZuWVEuPnnW_kMJpu93QUZZ7/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='py_basics', help='Sends the Python basics cheat sheet')
async def py_basics(ctx):
    response = "https://drive.google.com/file/d/1-tror16uiEhs-OdWffP6wWo-OpcNRNGe/view?usp=sharing"
    await ctx.send(response)

# @bot.command(name='pandas', help='Sends the Pandas cheat sheet')
# async def pandas(ctx):
#     response = "https://drive.google.com/file/d/1-9yVz9DAc5VcxTkQga7FgAkQhijFl6xB/view?usp=sharing"
#     await ctx.send(response)

@bot.command(name='numpy', help='Sends the Numpy cheat sheet')
async def numpy(ctx):
    response = "https://drive.google.com/file/d/1-Lv2tPRtlFBYfsXlrFmuASdoW4ndaDYJ/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='pandas', help='Sends the Pandas cheat sheets')
async def pandas(ctx):
    response = "https://drive.google.com/file/d/1-9yVz9DAc5VcxTkQga7FgAkQhijFl6xB/view?usp=sharing"
    response_2 = "https://drive.google.com/file/d/1-6krx82wcV6VbqFz8JmRDxPp0mfByoGN/view?usp=sharing"
    response_3 = "https://drive.google.com/file/d/12ItEPc-KZkdFdxa5faAB6vCxN2_PV-W5/view?usp=sharing"
    await ctx.send(response)
    await ctx.send(response_2)
    await ctx.send(response_3)

@bot.command(name='importing', help='Sends the cheat sheet regarding importing data in Python')
async def importing(ctx):
    response = "https://drive.google.com/file/d/1-Zm5TKQWCGNjSyhNXddO7ers3Uoq3lpF/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='jupyter', help='Sends the Jupyter cheat sheet')
async def jupyter(ctx):
    response = "https://drive.google.com/file/d/1-WClDt40g0URb_oQGPMvYoL4BNvZmlPS/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='matplotlib', help='Sends the Matplotlib cheat sheet')
async def matplotlib(ctx):
    response = "https://drive.google.com/file/d/1-NHhWnRP9ArqhW7UvzsawICv-8_uv1KM/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='seaborn', help='Sends the Seaborn cheat sheet')
async def seaborn(ctx):
    response = "https://drive.google.com/file/d/1-heZX97Qod46F_IcINi4ybJGP6Yh-xLk/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='bokeh', help='Sends the Bokeh cheat sheet')
async def bokeh(ctx):
    response = "https://drive.google.com/file/d/1-_sQeRcvzdxjdsgO73vGvAhDHpUa3XNw/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='scipy', help='Sends the SciPy cheat sheet')
async def scipy(ctx):
    response = "https://drive.google.com/file/d/1-oVJgPoXC8TyUkw0QLJ8pCU04rivnu8U/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='sklearn', help='Sends the scikit-learn cheat sheet')
async def sklearn(ctx):
    response = "https://drive.google.com/file/d/1-d-cTfrI7jHZEY105CoDJCHyEpPg1znz/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='pyspark', help='Sends the PySpark cheat sheets')
async def pyspark(ctx):
    response = "https://drive.google.com/file/d/1-1Iii9lNTD4ggGTdD4OfYYBQzBcXsbz1/view?usp=sharing"
    response_2 = "https://drive.google.com/file/d/1-3KL5vDxgnrc7-XJMQBGwQnx64nTqpxo/view?usp=sharing"
    await ctx.send(response)
    await ctx.send(response_2)

@bot.command(name='keras', help='Sends the Keras cheat sheet')
async def keras(ctx):
    response = "https://drive.google.com/file/d/1-VFhfQoR0YF_hLUAjKlpf_Lt1NNUnlK8/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='spacy', help='Sends the Spacy cheat sheet')
async def spacy(ctx):
    response = "https://drive.google.com/file/d/1-bXWgfZCP9s4uLFeifwlFmGHLLzCCp39/view?usp=sharing"
    await ctx.send(response)

@bot.command(name='knime', help='Sends the KNIME cheat sheets')
async def knime(ctx):
    response = "https://drive.google.com/file/d/11vUPxy7oPT0Os5TZpYp-HJGLIVaWPlvG/view?usp=sharing"
    response_2 = "https://drive.google.com/file/d/12A8USMYUfDXqh44WHipJHUubb-WYS3Uh/view?usp=sharing"
    response_3 = "https://drive.google.com/file/d/122e1VIxHH6mv8O8GsjfuHzyerxbfAL8X/view?usp=sharing"
    await ctx.send(response)
    await ctx.send(response_2)
    await ctx.send(response_3)

@bot.command(name='sql', help='Sends the SQL cheat sheet')
async def sql(ctx):
    response = "https://drive.google.com/file/d/12B_qS1VnqMwWvZE2Ig5_gzOzKWdhq9ay/view?usp=sharing"
    await ctx.send(response)

bot.run(TOKEN)





