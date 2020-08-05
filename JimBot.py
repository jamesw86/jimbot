import discord
import image
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='with numbers'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if "COVID" in message.content:
        days = image.getDays()
        try:
            f = discord.File("Day" + str(days) + ".jpg")
            await message.channel.send(file=f)
        except Exception as err:
            await message.channel.send("Error! Please contact Jim.")
            print(err)
    

client.run(os.environ['BOT_TOKEN'])
