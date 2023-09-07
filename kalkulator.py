import math
from discord.ext import commands
import discord

client = commands.Bot(command_prefix='!', help_command=None)

##funkcje

def sub(x: float, y:float):
    return x - y


def add(x: float, y: float):
    return x + y


def div(x: float, y: float):
    return x / y

def rando(x: float, y: float):
    return random.randint(x,y)

def sqrt(x: float):
    return math.sqrt(x)

##wszystkie funkcje


@client.event
async def on_ready():
    print(f'{bot.user.name} is online')




##komendy
@client.command()
async def mathadd(ctx, x: float, y: float ):
    res = add(x,y) #użycie komendy add
    await ctx.send(res)


@client.commamd()
async  def mathsub(ctx, x: float, y: float ):
    res = sub(x, y)
    await ctx.send(res)


@client.commamd()
async  def mathadd(ctx, x: float, y: float ):
    res = add(x, y)
    await ctx.send(res)

@client.commamd()
async  def mathdiv(ctx, x: float, y: float ):
    res = div(x, y)
    await ctx.send(res)



@client.commamd()
async  def mathrandom(ctx, x: float, y: float ):
    res = rando(x, y)
    await ctx.send(res)


@client.commamd()
async  def mathsqrt(ctx, x: float, y: float ):
    res = sqrt(x)
    await ctx.send(res)


##wszystkie komendy

client.run ('')



