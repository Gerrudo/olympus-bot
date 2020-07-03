import discord

client = discord.Client()

@client.event
async def on_ready(client):
    print('We have logged in as {0.user}'.format(client))

    for server in client.servers:
        if server.name == "Mini Chicken Kievs":
            break
    
    for channel in server.channels:
        if channel.name == "general":
            break

    botReady = True
    if botReady == True:
        await channel.send('Ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
client.run('NzI3OTk2MTkwMDkxNzcyMDY3.Xvz-gQ.q6hxill_x1G_GvzF_ePo9F3jfig')