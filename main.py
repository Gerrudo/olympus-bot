import discord

TOKEN = 'NzI3OTk2MTkwMDkxNzcyMDY3.Xvz-gQ.q6hxill_x1G_GvzF_ePo9F3jfig'

client = discord.Client()

botReady = False

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.user.name+' is ready')
    print('------')
    botReady = True
    return botReady

client.run(TOKEN)

channel = discord.utils.get(client.get_all_channels(), name='general')

@client.event
async def readyCheck(botReady):

    if botReady == True:
        readyMsg = client.user.name + 'is online!'
        channel = client.get_channel(12324234183172)
        await channel.send(readyMsg)
        print ('botready = true')

