import discord
from discord.ext import commands
import random
import string

TOKEN = ''

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def generujhaslo(ctx, dlugosc=12):
    if dlugosc < 4:
        await ctx.send('Długość hasła musi wynosić co najmniej 4 znaki.')
        return

    haslo = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=dlugosc))
    await ctx.send(f'Oto wygenerowane hasło: `{haslo}`')

bot.run(TOKEN)
