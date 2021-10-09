import discord

client = discord.Client()

client.run("ODk2MzA3Njc0ODQzNjExMTQ2.YWFNkg.ebv5P12l---U7zaexwgTsPQH71w")


@client.event
async def on_ready():
    await print("Odysseus est prêt !")


@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")

