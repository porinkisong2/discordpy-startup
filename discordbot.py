from discord.ext import commands
import os
import traceback
from add_by_users import *

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def otintin(ctx):
    await ctx.send('おっぱい！')

@bot.command()
async def oppai(ctx):
    await ctx.send('おちんちん！')

@bot.command()
async def manko(ctx):
    await ctx.send('まんこ！')

@bot.command()
async def uemura(ctx):
    await ctx.send('うえむらのちんちんは小さいよね、、、')

@bot.command()
async def whoTakashi(ctx):
    await ctx.send('僕は小学三年生のクソガキAIたかし！\n「/otintin」と入力すると「おっぱい！」を返し、「/oppai」と入力すると「おちんちん！」と返す素朴なbotです。\n通常の９歳児と異なりHeroku上で生きているので睡眠を必要としません。')

bot.run(token)
