from ast import Await
import discord
client=discord.Client()

@client.event
async def on_ready():
    print('目前登入身份:',client.user)
    
@client.event
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('努力學習py中')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'yo':
        await message.channel.send('yo 87')
        
    if message.author == client.user:
        return
    if message.content == '嗨':
        await message.channel.send('嗨sb')
        
    if message.author == client.user:
        return
    if message.content == '早':
        await message.channel.send('早')
        
    if message.author == client.user:
        return
    if message.content == '早安':
        await message.channel.send('早安')
        
    if message.author == client.user:
        return
    if message.content == '笑死了':
        await message.channel.send('死了沒')
        
    if message.author == client.user:
        return
    if message.content == '七仔robot':
        await message.channel.send('有什麼事快說')
        
    if message.author == client.user:
        return
    if message.content == 'yes':
        await message.channel.send('great')
        
    if message.author == client.user:
        return
    if message.content == 'no':
        await message.channel.send('why no')
        
    if message.author == client.user:
        return
    if message.content == '88':
        await message.channel.send('88')
    
    if message.author == client.user:
            return
    if message.content == 'hi':
        await message.channel.send('helloooo')
        
    if message.author == client.user:
        return
    if message.content.startswith('say'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("你要我說什麼啦？")
        else:
            await message.channel.send(tmp[1])
    
    if message.content.startswith('更改狀態'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            await client.change_presence(status=discord.Status.idle, activity=game)
            

client.run('OTUzOTY4NDg2MTgxMzc2MDcx.YjMSYg.WRpmGv4S65WGtceFWAYzIJGf3Mo')