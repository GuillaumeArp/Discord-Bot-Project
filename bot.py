import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)


    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
          )

@client.event
async def on_member_join(member):
    await member.create_dm
    await member.dm_channel.send(f'Hey {member.name}, bienvenue dans la promo Wild Data Green !')

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

full_pep20 = "https://www.python.org/dev/peps/pep-0020/"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!pep':
        response = random.choice(pep20)
        await message.channel.send(response)

    if message.content == '!pep20':
        response = full_pep20
        await message.channel.send(response)
        # await member.create_dm
        # await member.dm_channel.send(
        #     f"Content de voir que tu veux connaître le Zen de Python {member.name} !"
        # )
        # await member.dm_channel.send(
        #     "Lance la commande `import this` dans une cellule de notebook ou une console Python ^^"
        # )


client.run(TOKEN)





