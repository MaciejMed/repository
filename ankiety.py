import discord
from discord.ext import commands
import asyncio

TOKEN = ''

bot = commands.Bot(command_prefix='/')

tymczasowe_ankiety = {}

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def ankieta(ctx, pytanie, *odpowiedzi):
    odpowiedzi = list(odpowiedzi)
    pytanie = pytanie.capitalize()
    tresc_ankiety = f'**Ankieta**: {pytanie}\n\n'
    
    for i, odpowiedz in enumerate(odpowiedzi):
        tresc_ankiety += f'{i+1}. {odpowiedz}\n'
    
    tresc_ankiety += 'Aby zagłosować, użyj komendy /glosuj [numer odpowiedzi].'
    ankieta_msg = await ctx.send(tresc_ankiety)
    
    tymczasowe_ankiety[ankieta_msg.id] = {'autor': ctx.author, 'pytanie': pytanie, 'odpowiedzi': odpowiedzi, 'wyniki': [0] * len(odpowiedzi)}
    
    for i in range(len(odpowiedzi)):
        emoji = chr(127462 + i) 
        await ankieta_msg.add_reaction(emoji)

@bot.command()
async def glosuj(ctx, numer_odpowiedzi):
    try:
        numer_odpowiedzi = int(numer_odpowiedzi) - 1
        ankieta_msg = ctx.message.reference.resolved 

        if ankieta_msg.id in tymczasowe_ankiety:
            autor_ankiety = tymczasowe_ankiety[ankieta_msg.id]['autor']
            pytanie = tymczasowe_ankiety[ankieta_msg.id]['pytanie']
            odpowiedzi = tymczasowe_ankiety[ankieta_msg.id]['odpowiedzi']

            if 0 <= numer_odpowiedzi < len(odpowiedzi):
                tymczasowe_ankiety[ankieta_msg.id]['wyniki'][numer_odpowiedzi] += 1
                await ctx.send(f'{ctx.author.mention} zagłosował na opcję {odpowiedzi[numer_odpowiedzi]} w ankiecie "{pytanie}" autorstwa {autor_ankiety.mention}.')

            else:
                await ctx.send('Podano nieprawidłowy numer odpowiedzi.')
        else:
            await ctx.send('Nie znaleziono aktywnej ankiety.')

    except ValueError:
        await ctx.send('Podano nieprawidłowy numer odpowiedzi.')

@bot.command()
async def zakoncz_ankiete(ctx):
    if ctx.message.reference and ctx.message.reference.message_id in tymczasowe_ankiety:
        ankieta_msg = ctx.message.reference.resolved 
        wyniki = tymczasowe_ankiety[ankieta_msg.id]['wyniki']
        pytanie = tymczasowe_ankiety[ankieta_msg.id]['pytanie']
        odpowiedzi = tymczasowe_ankiety[ankieta_msg.id]['odpowiedzi']

        tresc_wynikow = f'**Wyniki ankiety "{pytanie}":**\n\n'
        for i, odpowiedz in enumerate(odpowiedzi):
            tresc_wynikow += f'{odpowiedz}: {wyniki[i]}\n'

        await ctx.send(tresc_wynikow)
        del tymczasowe_ankiety[ankieta_msg.id]
    else:
        await ctx.send('Nie znaleziono aktywnej ankiety.')

bot.run(TOKEN)
