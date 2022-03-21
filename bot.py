import discord
from discord.ext import commands

intents=discord.Intents.all()


bot=commands.Bot(command_prefix='[',intents=intents)

@bot.event
async def on_ready():
    print('目前登入身份:',bot.user)
    
@bot.event
async def on_ready():
    print('目前登入身份：',bot.user)
    game = discord.Game('coding')
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.event
async def on_member_join(member):
    channel=bot.get_channel(955473394978160702)
    await channel.send(f'{member} join!')
    
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(955473418625613854)
    await channel.send(f'{member} leave!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == '早晨':
        await message.channel.send('早晨>.<')
        
    if message.author == bot.user:
        return
    if message.content == '沒人？':
        await message.channel.send('我在')
        
    if message.author == bot.user:
        return
    if message.content == '?':
        await message.channel.send('wtf you doing')
        
    if message.author == bot.user:
        return
    if message.content == '嗨':
        await message.channel.send('嗨sb')
        
    if message.author == bot.user:
        return
    if message.content == '早':
        await message.channel.send('早')
        
    if message.author == bot.user:
        return
    if message.content == '早安':
        await message.channel.send('早安')
        
    if message.author == bot.user:
        return
    if message.content == '笑死了':
        await message.channel.send('死了沒')
        
    if message.author == bot.user:
        return
    if message.content == '七仔robot':
        await message.channel.send('有什麼事快說')
        
    if message.author == bot.user:
        return
    if message.content == 'yes':
        await message.channel.send('great')
        
    if message.author == bot.user:
        return
    if message.content == 'no':
        await message.channel.send('why no')
        
    if message.author == bot.user:
        return
    if message.content == '88':
        await message.channel.send('88')
    
    if message.author == bot.user:
            return
    if message.content == 'hi':
        await message.channel.send('helloooo')
        
    if message.author == bot.user:
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
            await bot.change_presence(status=discord.Status.idle, activity=game)
            

bot.run('OTUzOTY4NDg2MTgxMzc2MDcx.YjMSYg.V6nvu3rAwqK9TgW-jB7dfeqVtSw')