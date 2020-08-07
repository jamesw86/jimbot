import discord
import image
import os
import TestScript
import datetime

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
    if message.content.startswith('$birthday'):
        try:
            name = message.content.split()[1]
            try:
                birthday = TestScript.getBirthday(name)
                birthday = birthday[0]
            except Exception as err:
                print(err)
            if birthday == None:
                await message.channel.send(name + " doesn't have a birthday listed in the database.")
            elif isinstance(birthday, datetime.date):
                birthday = str(birthday.month) + "/" + str(birthday.day)
                await message.channel.send(name + "'s birthday is " + str(birthday))
        except Exception as err:
           await message.channel.send("Type ```$birthday <name>``` to see if they have a birthday.")
        
        

    

client.run(os.environ['BOT_TOKEN'])
