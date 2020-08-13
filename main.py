import discord

client = discord.Client()


@client.event
async def on_ready():
    gc = client.get_channel(yourchannelid)
    await gc.send('hello discord')


client.run('your bot token')
