import math
import random

import discord
from discord.ext import commands

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

#sda
@client.event
async def on_ready():
    print(f'{client.user} is online')


##komendy
@client.command()
async def mathadd(ctx, x: float, y: float ):
    res = add(x,y) #użycie funkcn add
    await ctx.send(res)


@client.command()
async def mathsub(ctx, x: float, y: float ):
    res = sub(x, y)
    await ctx.send(res)


@client.command()
async def mathadd(ctx, x: float, y: float ):
    res = add(x, y)
    await ctx.send(res)

@client.command()
async def mathdiv(ctx, x: float, y: float ):
    res = div(x, y)
    await ctx.send(res)

@client.command()
async def mathrandom(ctx, x: float, y: float ):
    res = rando(x, y)
    await ctx.send(res)

@client.command()
async def mathsqrt(ctx, x: float, y: float ):
    res = sqrt(x)
    await ctx.send(res)


##wszystkie komendy

client.run ('')
