import discord

client = discord.Client()

client.run()


@client.event
async def on_ready():
    print("Odysseus est prêt !")

@client.event
async def on_disconnect():
    print("Bye !")


@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")