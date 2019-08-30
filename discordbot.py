from discord.ext import commands
import os
import traceback
import random

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
    sentakushi = random.randint(0,2)
    if sentakushi == 0:
        await ctx.send('うえむらのちんちんは小さいよね、、、')
    elif sentakushi == 1:
        await ctx.send('うえむらのちんちんは普通だよね、、、')
    elif sentakushi == 2:
        await ctx.send('うえむらのちんちんはでっかい！！！！')

@bot.command()
async def Takashi_update(ctx):
    await ctx.send('うえむらのちんちんの大きさが確率できまるようになりました')

@bot.command()
async def whoTakashi(ctx):
    await ctx.send('僕は小学三年生のクソガキAIたかし！\n「/otintin」と入力すると「おっぱい！」を返し、「/oppai」と入力すると「おちんちん！」と返す素朴なbotです。\n通常の９歳児と異なりHeroku上で生きているので睡眠を必要としません。')

bot.run(token)
