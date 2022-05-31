import discord
from discord.ext import commands
prefix = "?"
bot = commands.Bot(command_prefix=prefix)

@bot.command()
async def ping(ctx):
    await ctx.reply('@everyone Creative Handhakee')

@bot.command()
async def ping3(ctx):
    await ctx.reply('@everyone im a test bot lol')

@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)

@bot.command()
async def ping2(ctx):
    await ctx.reply('@here Hi there, im a new bot that can say hello to you and add number to use me start your sentence with "?" qnd then hello or add and then your numbers')


bot.run('OTgwODkwNzE0MTc3MTQyNzg0.GUixMM.xwuOFreOv2xm1w-kSp0gP53ymqi2dqH8D3JzU8')

  