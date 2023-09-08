import discord
import requests

from discord.ext import commands
from riotwatcher import LolWatcher

bot = commands.Bot(command_prefix='/')

TOKEN = ''

RIOT_API_KEY = 'RGAPI-30e37ca4-b13f-45a6-a663-49172d6201de'

lol_watcher = LolWatcher(RIOT_API_KEY)

ITEMS_API_URL = 'https://na1.api.riotgames.com/lol/static-data/v4/items'

def get_item_info(item_id):
    headers = {
        'X-Riot-Token': RIOT_API_KEY
    }
    params = {
        'itemListData': 'from'
    }
    response = requests.get(f'{ITEMS_API_URL}/{item_id}', headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

#/runy
@bot.command()
async def runy(ctx, champion_name):
    try:
        champion_data = lol_watcher.data_dragon.champions('en_US')
        champion_id = None
        for champion_key, champion_info in champion_data['data'].items():
            if champion_info['name'].lower() == champion_name.lower():
                champion_id = champion_key
                break

        if champion_id:
            runes = lol_watcher.champion.runes(champion_id)
            await ctx.send(f'Runy dla {champion_name}:\n{runes}')
        else:
            await ctx.send('Zła nazwa postaci')

    except Exception as e:
        print(e)
        await ctx.send('Wystąpił błąd podczas pobierania danych.')

bot.run(TOKEN)

