import discord
from config import config_channelid, config_token

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channels = client.guilds[0].text_channels
    for i in channels:
        if i.id == config_channelid:
            break
    
    await i.send(f'sent to {i.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
client.run(config_token)