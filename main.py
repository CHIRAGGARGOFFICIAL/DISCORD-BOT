import discord

client = discord.Client()


@client.event
async def on_ready():
    gc = client.get_channel(743480942278082581)
    await gc.send('hello discord')


client.run('NzQzNDk5NDA5NzI3MjkxMzkz.XzVjyA.DwGLjtgkzlNdx8fksfu4VqO-EsQ')
