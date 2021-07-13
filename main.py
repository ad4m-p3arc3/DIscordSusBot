import discord 
import random

client = discord.Client()

sus_list = {
    'sus',
    'sussy',
    'sussy baka',
    'amogus',
    'among us',
    'Sus',
    'Sussy',
    'Sussy baka',
    'Sussy Baka',
    'sussy Baka',
    'Amogus',
    'Among Us',
    'among Us',
    'Among us',
    'SUS',
    'AMOGUS',
    'AMONG US',
    'SUSSY BAKA',
    'SUSSY'
}

wholesome_stuff = ['<3', 'i love u', 'ily', 'i love you']

my_dict = ['sus', 'amogus', 'sussy', 'sussy baka', 'AMONG US', 'https://www.youtube.com/watch?v=Zn2v_kHkyis']

@client.event
async def on_ready():
    print("We have successfully logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return 
    msg = message.content
    
    if msg.startswith("$help"):
      await message.channel.send("list of commands: \n$troll (sends troll face gif)\n$help (Displays list of all commands")

    if any(word in msg for word in sus_list):
        await message.channel.send(random.choice(my_dict))
    
    if msg.startswith("$troll"):
      with open('trollface.gif', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(file=picture)

    if any(word in msg for word in wholesome_stuff):
      await message.channel.send("wholesome moment")
      
client.run('your_token_here')
