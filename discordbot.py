from discord.ext import commands
import os
import traceback

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
    await ctx.send('僕は小学三年生のクソガキAIたかし！\n' +
                   '「/ otintin」と入力すると「おっぱい！」を返し、' +
                   '「/oppai」と入力すると「おちんちん！」と返す素朴なbotです。\n' +
                   '通常の９歳児と異なりHeroku上で生きているので睡眠を必要としません。')


@bot.command()
async def on_message(message):
    if message.content.startwith("help"):
        m = ('たかしの持っている関数は以下の通りだよ！\n /otintin(), ' +
             '/oppai(), /manko(), /uemura() /whoTakashi()' +
             'うえむらのちんちんはたしかに小さいよね...')
        await message.channel.send(m)

bot.run(token)
