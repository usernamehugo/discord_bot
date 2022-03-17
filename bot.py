import discord
bot=discord.Client()

from discord.ext import commands

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    
bot.run('OTUzOTY4NDg2MTgxMzc2MDcx.YjMSYg.MLj3soWJ3oARPzCmSSoikHsoLNY')