# from discord.ext import commands
import discord
import os
# import traceback
import random

# bot = commands.Bot(command_prefix='/')
# token = os.environ['DISCORD_BOT_TOKEN']
token = 'NjE2OTMxMjQxNTg0NzU0Njg4.XWkylQ.CoZ6ZNZm1Y279-5a6GAl7qqeLuE'
client = discord.Client()


@client.event
async def on_ready():
    CHANNEL_ID = 615880185136545792
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おれが帰ってきたぞ！')


# @bot.event
# async def on_command_error(ctx, error):
#     await ctx.send(str(error))


# @bot.command()
# async def otintin(ctx):
#     await ctx.send('おっぱい！')


# @bot.command()
# async def oppai(ctx):
#     await ctx.send('おちんちん！')


# @bot.command()
# async def manko(ctx):
#     await ctx.send('まんこ！')


# @bot.command()
# async def debug_sako(ctx):
#     method_dir = dir()
#     for i in method_dir:
#         await ctx.send(i)


# @bot.command()
# async def uemura(ctx):
#     sentakushi = random.randint(0, 2)
#     if sentakushi == 0:
#         await ctx.send('うえむらのちんちんは小さいよね、、、')
#     elif sentakushi == 1:
#         await ctx.send('うえむらのちんちんは普通だよね、、、')
#     elif sentakushi == 2:
#         await ctx.send('うえむらのちんちんはでっかい！！！！')


# @bot.command()
# async def Takashi_update(ctx):
#     await ctx.send('うえむらのちんちんの大きさが確率できまるようになりました')


# @bot.command()
# async def whoTakashi(ctx):
#     await ctx.send('僕は小学三年生のクソガキAIたかし！\n' +
#                    '「/ otintin」と入力すると「おっぱい！」を返し、' +
#                    '「/oppai」と入力すると「おちんちん！」と返す素朴なbotです。\n' +
#                    '通常の９歳児と異なりHeroku上で生きているので睡眠を必要としません。')


@client.event
async def on_message(message):
    if message.content.startwith("help"):
        m = ('たかしの持っている関数は以下の通りだよ！\n /otintin(), ' +
             '/oppai(), /manko(), /uemura() /whoTakashi()' +
             'うえむらのちんちんはたしかに小さいよね...')
        await message.channel.send(m)

# bot.run(token)
client.run(token)
