import asyncio
import linecache
import math
import random
import string
from random import choices
from typing import List, Optional
from urllib.request import urlopen

import discord
from discord import app_commands
from discord.ext import commands
import requests

from champions import champions_specs
from config import TOKEN

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

tymczasowe_ankiety = {}
supported = ["USD", "AUD", "HKD", "CAD", "NZD", "SGD", "EUR", "CHF", "GBP", "UAH", "CZK", "DKK", "NOK", "SEK", "RON", "BGN", "TRY", "ILS", "PHP", "MXN", "ZAR", "BRL", "MYR", "CNY", "XDR"]
curr_helper = [
    app_commands.Choice(name="USD", value="usd"),
    app_commands.Choice(name="EUR", value="eur"),
    app_commands.Choice(name="HKD", value="hkd"),
    app_commands.Choice(name="CAD", value="cad"),
    app_commands.Choice(name="NZD", value="nzd"),
    app_commands.Choice(name="SGD", value="sgd"),
    app_commands.Choice(name="AUD", value="aud"),
    app_commands.Choice(name="CHF", value="chf"),
    app_commands.Choice(name="GBP", value="gbp"),
    app_commands.Choice(name="UAH", value="uah"),
    app_commands.Choice(name="CZK", value="czk"),
    app_commands.Choice(name="DKK", value="dkk"),
    app_commands.Choice(name="NOK", value="nok"),
    app_commands.Choice(name="SEK", value="sek"),
    app_commands.Choice(name="RON", value="ron"),
    app_commands.Choice(name="BGN", value="bgn"),
    app_commands.Choice(name="TRY", value="try"),
    app_commands.Choice(name="ILS", value="ils"),
    app_commands.Choice(name="PHP", value="php"),
    app_commands.Choice(name="MXN", value="mxn"),
    app_commands.Choice(name="ZAR", value="zar"),
    app_commands.Choice(name="BRL", value="brl"),
    app_commands.Choice(name="MYR", value="myr"),
    app_commands.Choice(name="CNY", value="cny"),
    app_commands.Choice(name="XDR", value="xdr")
]
linecache.clearcache()
@bot.event
async def on_ready():
    print("bot gud")
    try:
        synced=await bot.tree.sync()
        print(f"{len(synced)} komend powinno działać")
    except Exception as e:
        print(e)

@bot.tree.command(name="help", description="Podaje listę komend")
async def help(interaction:discord.Integration):
    embed=discord.Embed(title="Lista komend", color=0x009999)
    embed.add_field(name="Różne", value="**/hello** - Wita się z użytkownikiem\n **/generujhaslo** - Generuje bezpieczne hasło z losowych znaków", inline=False)
    embed.add_field(name="Kostki", value="**/kostka** - Prosty rzut kostką\n **/rzutpro** - Rzuca kostką z dodatkowymi funkcjami", inline=False)
    embed.add_field(name="Generacja", value="**/dungeon** - Generuje loch z emotikon\n **/customdung** - Generuje loch z wybranych emotikon\n **/presetdung** - Generuje loch z wybranego zestawu emotikon\n **/roadgen** - Generuje dróżkę z emotikon", inline=False)
    embed.add_field(name="Losowanie imion", value="**/namegen** - Generuje losowe imię z wybranej listy\n **/addname** - Dodaje imię do listy\n **/remname** - Usuwa imię z listy\n **/namelist** - Wyświetla wszystkie imiona z wybranej listy", inline=False)
    embed.add_field(name="Karty postaci", value="**/createcharacter** - Tworzy kartę postaci\n **/karta** - Wyświetla kartę postaci wybranego użytkownika\n **/modkarty** - Modyfikuje wybrany element karty", inline=False)
    embed.add_field(name="Ekwipunek", value="**/pokazeq** - Pokazuje ekwipunek wybranego gracza\n **/modyfikujeq** - Modyfikuje ekwipunek\n **/przedmiot** - Pokazuje informacje o wybranym przedmiocie", inline=False)
    embed.add_field(name="Kalkulator", value="**/dodaj** - Dodaje do siebie dwie liczby\n **/odejmij** - Odejmuje jedną liczbę od drugiej\n **/pomnoz** - Mnoży przez siebie dwie liczby\n **/podziel** - Dzieli jedną liczbę przez drugą\n **/pierwiastek** - Pierwiastkuje podaną liczbę", inline=False)
    embed.add_field(name="Waluty", value="**/waluta** - Sprawdza obecny kurs wybranej waluty\n **/zamiana** - Zamienia wybraną walutę na dowolną inną", inline=False)
    embed.add_field(name="Ligo Lego", value="**/build** - Pokazuje build wybranego bohatera\n **/losujbohatera** - Losuje bohatera", inline=False)
    
    
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="generujhaslo", description="Generuje bezpieczne hasło specjalnie dla Ciebie")
@app_commands.describe(dlugosc="Długość hasła, domyślna wartość to 12")
async def generujhaslo(interaction:discord.Integration, dlugosc:int=12):
    if dlugosc < 8:
        await interaction.response.send_message(f'Długość hasła musi wynosić co najmniej 8 znaków.', ephemeral=True)
        return

    haslo = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=dlugosc))
    await interaction.response.send_message(f'Oto wygenerowane hasło: `{haslo}`', ephemeral=True)

@bot.tree.command(name="waluta", description="Sprawdź kurs")
@app_commands.describe(curr_code="Kod waluty np. USD, GBP", quantity="kwota w złotówkach do wymiany")
@app_commands.choices(curr_code=curr_helper)
async def waluta(interaction:discord.Integration, curr_code: app_commands.Choice[str], quantity: float):
    curr_code = curr_code.value.upper()
    # url = f"https://api.nbp.pl/api/exchangerates/rates/a/{curr_code}/today/?format=json"
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{curr_code}/2023-09-01/?format=json"

    if curr_code not in supported:
        await interaction.response.send_message(f"Waluta {curr_code} nie jest obsługiwana. Wybierz jedną z {', '.join(supported)}")
        return
    res = requests.get(url)
    table = res.json()

    result = quantity * table.get("rates")[0].get("mid")
    await interaction.response.send_message(f"{quantity:.2f} PLN to {result:.2f} {curr_code.upper()}")

@bot.tree.command(name="zamiana", description="Zamień dowolną kwotę z wybranej waluty na inną.")
@app_commands.describe(
        curr_from ="Kod waluty np. USD, GBP, z której zmieniamy",
        curr_to="Kod waluty np. USD, GBP, na którą zmieniamy ",
        num="kwota"
    )
@app_commands.choices(curr_from=curr_helper, curr_to=curr_helper)
async def zamiana(interaction:discord.Integration, curr_from: app_commands.Choice[str], num:float, curr_to:app_commands.Choice[str] ):
    curr_from = curr_from.value.upper()
    curr_to = curr_to.value.upper()

    # url1 = f"https://api.nbp.pl/api/exchangerates/rates/a/{curr_from}/today/"
    url1 = f"https://api.nbp.pl/api/exchangerates/rates/a/{curr_from}/2023-09-01//?format=json"

    # url2 = f"https://api.nbp.pl/api/exchangerates/rates/a/{curr_to}/today/"
    url2 = f"https://api.nbp.pl/api/exchangerates/rates/a/{curr_to}/2023-09-01//?format=json"



    if curr_from not in supported or curr_to not in supported: 
        await interaction.response.send_message(f"waluta nie jest obsługiwana wybierz jedną z {', '.join(supported)}")
        return
    res1 = requests.get(url1)
    res2 = requests.get(url2)
    table1 = res1.json()
    table2 = res2.json()
    curr1 = table1.get("rates")[0].get("mid") # 5 EUR
    curr2 = table2.get("rates")[0].get("mid") # 3 USD
                                        # num = 10
    result = curr1 * num / curr2
    await interaction.response.send_message(f"{num:.2f} {curr_from} = {result:.2f} {curr_to}")

@bot.tree.command(name="hello", description="Wita się z użytkownikiem")
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"hello {interaction.user.mention}")

@bot.tree.command(name="kostka", description="Prosta komenda do rzucania kostkami")
@app_commands.describe(liczba_kosci="iloma kostkami chcesz rzucić?", liczba_scian="ile ścian ma mieć twoja kostka?")
async def kostka(interaction: discord.Integration, liczba_kosci: int, liczba_scian: int):
    if liczba_scian>1:
        if liczba_kosci==1:
            rand_num=random.randint(1,liczba_scian)
            if rand_num==1:
                await interaction.response.send_message(f":game_die: Użytkownik {interaction.user.mention} wylosował **1** rzucając **{liczba_kosci}d{liczba_scian}** XDDDD")
            elif rand_num==liczba_scian:
                await interaction.response.send_message(f":game_die: Użytkownik {interaction.user.mention} wylosował **{rand_num}** rzucając **{liczba_kosci}d{liczba_scian}**! To critical :tada:")
            else:
                await interaction.response.send_message(f":game_die: Użytkownik {interaction.user.mention} wylosował **{rand_num}** rzucając **{liczba_kosci}d{liczba_scian}**!")
        elif liczba_kosci>1:
            num_list=[]
            for x in range(liczba_kosci):
                num_list.extend([random.randint(1,liczba_scian)])
            
            await interaction.response.send_message(f":game_die: Użytkownik {interaction.user.mention} wylosował: **{str(num_list)[1:-1]}** (łącznie **{sum(num_list)}**:small_blue_diamond:) rzucając **{liczba_kosci}d{liczba_scian}**!")    
    else:
        await interaction.response.send_message(f"Co ty sobą bambusie reprezentujesz")



@bot.tree.command(name="dungeon", description="Generuje loch o wybranych wymiarach")
@app_commands.describe(length="długość twojego lochu", width="szerokość twojego lochu")
async def dungeon(interaction: discord.Integration, length: int, width: int):
    floor=":black_large_square:"
    rat=":rat:"
    wiz=":man_mage:"
    pop=[floor, rat, wiz]
    wei=[0.9, 0.09, 0.01]
    tiles=[]
    if (width % 2) == 0:
        door_pos1 = random.randint(1,width)
        door_pos2 = random.randint(1,width)


        for x in range(door_pos1):
            tiles.extend([":white_square_button:"])
        tiles.extend([":door:"])
        for x in range(width-door_pos1):
            tiles.extend([":white_square_button:"])
        tiles.extend([":white_square_button:","\n"])
        
    
        for x in range(length):
            tiles.extend([":white_square_button:"])
            for x in range(width):
                tiles.extend(random.choices(pop, wei))
            tiles.extend([":white_square_button:"])
            tiles.extend(["\n"])
    
        for x in range(door_pos2):
            tiles.extend([":white_square_button:"])
        tiles.extend([":door:"])
        for x in range(width-door_pos2):
            tiles.extend([":white_square_button:"])
        tiles.extend([":white_square_button:","\n"])
        await interaction.response.send_message(''.join(tiles))
    else:
        tiles.extend([":white_square_button:"])
        for x in range(int(width/2)):
            tiles.extend([":white_square_button:"])
        tiles.extend([":door:"])
        for x in range(int(width/2)):
            tiles.extend([":white_square_button:"])
        tiles.extend([":white_square_button:","\n"])
        
    
        for x in range(length):
            tiles.extend([":white_square_button:"])
            for x in range(width):
                tiles.extend(random.choices(pop, wei))
            tiles.extend([":white_square_button:"])
            tiles.extend(["\n"])

        tiles.extend([":white_square_button:"])
        for x in range(int(width/2)):
            tiles.extend([":white_square_button:"])
        tiles.extend([":door:"])
        for x in range(int(width/2)):
            tiles.extend([":white_square_button:"])
        tiles.extend([":white_square_button:","\n"])
        await interaction.response.send_message(''.join(tiles))


@bot.tree.command(name="customdung", description="Generuje loch o wybranych wymiarach i parametrach")
@app_commands.describe(length="długość twojego lochu", width="szerokość twojego lochu", emotki="emotki użyte do generacji lochu w formacie [:cat: :dog: :tea:]", szanse="szanse pojawienia się kolejnych emotek w formacie [1 14 2.2]", wall_emote="emotka użyta jako ściany", door_emote="emotka użyta jako drzwi")
async def customdung(interaction: discord.Integration, length: int, width: int, emotki: str, szanse: str, wall_emote: str, door_emote: str):
    pop=emotki.split()
    szanse2=szanse.split()
    wei=[float(i) for i in szanse2]
    tiles=[]
    if (width % 2) == 0:
        door_pos1 = random.randint(1,width)
        door_pos2 = random.randint(1,width)


        for x in range(door_pos1):
            tiles.extend([wall_emote])
        tiles.extend([door_emote])
        for x in range(width-door_pos1):
            tiles.extend([wall_emote])
        tiles.extend([wall_emote,"\n"])
        
    
        for x in range(length):
            tiles.extend([wall_emote])
            for x in range(width):
                tiles.extend(random.choices(pop, wei))
            tiles.extend([wall_emote])
            tiles.extend(["\n"])
    
        for x in range(door_pos2):
            tiles.extend([wall_emote])
        tiles.extend([door_emote])
        for x in range(width-door_pos2):
            tiles.extend([wall_emote])
        tiles.extend([wall_emote,"\n"])
        await interaction.response.send_message(''.join(tiles))
    else:
        tiles.extend([wall_emote])
        for x in range(int(width/2)):
            tiles.extend([wall_emote])
        tiles.extend([door_emote])
        for x in range(int(width/2)):
            tiles.extend([wall_emote])
        tiles.extend([wall_emote,"\n"])
        
    
        for x in range(length):
            tiles.extend([wall_emote])
            for x in range(width):
                tiles.extend(random.choices(pop, wei))
            tiles.extend([wall_emote])
            tiles.extend(["\n"])

        tiles.extend([wall_emote])
        for x in range(int(width/2)):
            tiles.extend([wall_emote])
        tiles.extend([door_emote])
        for x in range(int(width/2)):
            tiles.extend([wall_emote])
        tiles.extend([wall_emote,"\n"])
        await interaction.response.send_message(''.join(tiles))

@bot.tree.command(name="presetdung", description="Generuje loch o wybranych wymiarach")
@app_commands.describe(length="długość twojego lochu", width="szerokość twojego lochu")
@app_commands.choices(preset=[
    app_commands.Choice(name="Sci-Fi", value="scifi"),
    app_commands.Choice(name="Mroczny", value="dark"),
    app_commands.Choice(name="Mglisty", value="foggy")
])
async def presetdung(interaction: discord.Integration, length: int, width: int, preset: app_commands.Choice[str]):
    if preset.value == "scifi":
        floor=":stop_button:"
        rat=":diamond_shape_with_a_dot_inside:"
        wiz=":free:"
        door=":cyclone:"
        wall=":white_large_square:"

    elif preset.value == "dark":
        floor=":black_large_square:"
        rat=":spider_web:"
        wiz=":spider:"
        door=":new_moon:"
        wall=":milky_way:"
    
    elif preset.value == "foggy":
        floor=":fog:"
        rat=":foggy:"
        wiz=":cloud_tornado:"
        door=":face_in_clouds:"
        wall=":cloud:"
    
    pop=[floor, rat, wiz]
    wei=[0.9, 0.09, 0.01]
    tiles=[]
    if (width % 2) == 0:
        door_pos1 = random.randint(1,width)
        door_pos2 = random.randint(1,width)


        for x in range(door_pos1):
            tiles.extend([wall])
        tiles.extend([door])
        for x in range(width-door_pos1):
            tiles.extend([wall])
        tiles.extend([wall,"\n"])
        
    
        for x in range(length):
            tiles.extend([wall])
            for x in range(width):
                tiles.extend(random.choices(pop, wei))
            tiles.extend([wall])
            tiles.extend(["\n"])
    
        for x in range(door_pos2):
            tiles.extend([wall])
        tiles.extend([door])
        for x in range(width-door_pos2):
            tiles.extend([wall])
        tiles.extend([wall,"\n"])
        await interaction.response.send_message(''.join(tiles))
    else:
        tiles.extend([wall])
        for x in range(int(width/2)):
            tiles.extend([wall])
        tiles.extend([door])
        for x in range(int(width/2)):
            tiles.extend([wall])
        tiles.extend([wall,"\n"])
        
    
        for x in range(length):
            tiles.extend([wall])
            for x in range(width):
                tiles.extend(random.choices(pop, wei))
            tiles.extend([wall])
            tiles.extend(["\n"])

        tiles.extend([wall])
        for x in range(int(width/2)):
            tiles.extend([wall])
        tiles.extend([door])
        for x in range(int(width/2)):
            tiles.extend([wall])
        tiles.extend([wall,"\n"])
        await interaction.response.send_message(''.join(tiles))



@bot.tree.command(name="roadgen", description="Generuje planszę z drogą o wybranych wymiarach")
@app_commands.describe(length="długość planszy", width="szerokość planszy")
async def roadgen(interaction: discord.Integration, length: int, width: int):
    tiles=[]
    current_pos=random.randint(1,width)
    pop=[":green_square:", ":deciduous_tree:", ":house:"]
    wei=[30, 1, 1]
    num_list=[0,1]
    for x in range(length):
        for x in range(current_pos-1):
            tiles.extend(random.choices(pop, wei))
        tiles.extend([":brown_square:"])
        for x in range(width-current_pos):
            tiles.extend(random.choices(pop, wei))
        tiles.extend(["\n"])
        if current_pos==1:
            added=random.choices(num_list,weights=(1,7))
            current_pos=current_pos+added[0]
        elif current_pos==width:
            added=random.choices(num_list,weights=(1,7))
            current_pos=current_pos-added[0]
        else:
            current_pos=current_pos+random.randint(-1,1)

    await interaction.response.send_message(''.join(tiles))


@bot.tree.command(name="rzutpro", description="Zaawansowana komenda do rzucania kośćmi, używa notacji typu 1d6+1")
@app_commands.describe(parametry="Parametry rzutu w notacji 1d6+1")
async def rzutpro(interaction: discord.Integration, parametry: str):
    lista=parametry.split("+")
    dodana=lista[1]
    rzut=lista[0]
    rzut1=rzut.split("d")
    num_list=[]
    for x in range(int(rzut1[0])):
        num_list.extend([random.randint(1,int(rzut1[1]))])
    await interaction.response.send_message(f":game_die: Użytkownik {interaction.user.mention} wylosował: **{str(num_list)[1:-1]}** (łącznie **{int(sum(num_list))+int(dodana)}**:small_blue_diamond:) rzucając **{parametry}**!")



@bot.tree.command(name="namegen", description="Wybiera losowo imię używając wybranej listy")
@app_commands.describe(rasa="rasa Twojej postaci")
@app_commands.choices(rasa=[
    app_commands.Choice(name="Krasnolud", value="krasnolud"),
    app_commands.Choice(name="Elf", value="elf"),
    app_commands.Choice(name="Człowiek", value="czlowiek")
])
async def namegen(interaction: discord.Integration, rasa: app_commands.Choice[str]):
    if rasa.value == "czlowiek":
        with open(r"D:\tsyal\names.txt", "r") as fp:
            for count, line in enumerate(fp):
                pass
        f=open(r"D:\tsyal\names.txt","r")
        for x in range(random.randint(1,count+1)):
            name=f.readline()
        await interaction.response.send_message(name)
    elif rasa.value == "elf":
        with open(r"D:\tsyal\elves.txt", "r") as fp:
            for count, line in enumerate(fp):
                pass
        f=open(r"D:\tsyal\elves.txt","r")
        for x in range(random.randint(1,count+1)):
            name=f.readline()
        await interaction.response.send_message(name)
    elif rasa.value == "krasnolud":
        with open(r"D:\tsyal\dwarves.txt", "r") as fp:
            for count, line in enumerate(fp):
                pass
        f=open(r"D:\tsyal\dwarves.txt","r")
        for x in range(random.randint(1,count+1)):
            name=f.readline()
        await interaction.response.send_message(name)
    else:
        await interaction.response.send_message(f"Proszę wybrać dostępną opcję {rasa}")

@bot.tree.command(name="addname", description="Dodaje imię do listy używanej do losowania")
@app_commands.describe(name="imię do dodania do listy", rasa="rasa Twojej postaci")
@app_commands.choices(rasa=[
    app_commands.Choice(name="Krasnolud", value="krasnolud"),
    app_commands.Choice(name="Elf", value="elf"),
    app_commands.Choice(name="Człowiek", value="czlowiek")
])
async def addname(interaction: discord.Integration, name: str, rasa: app_commands.Choice[str]):
    if rasa.value == "czlowiek":
        f = open(r"D:\tsyal\names.txt", "a")
    elif rasa.value == "elf":
        f = open(r"D:\tsyal\elves.txt", "a")
    elif rasa.value == "krasnolud":
        f = open(r"D:\tsyal\dwarves.txt", "a")
    else:
        await interaction.response.send_message(f"Proszę wybrać dostępną opcję")
    f.write("\n")
    f.write(name)
    f.close()
    await interaction.response.send_message(f"Imię **{name}** zostało dodane do listy imion rasy **{rasa}** komendy /namegen")

@bot.tree.command(name="remname", description="Usuwa imię z listy używanej do losowania")
@app_commands.describe(name="imię do usunięcia z listy", rasa="rasa Twojej postaci")
@app_commands.choices(rasa=[
    app_commands.Choice(name="Krasnolud", value="krasnolud"),
    app_commands.Choice(name="Elf", value="elf"),
    app_commands.Choice(name="Człowiek", value="czlowiek")
])
async def remname(interaction: discord.Integration, name: str, rasa: app_commands.Choice[str]):
    if rasa.value == "czlowiek":
        with open(r"D:\tsyal\names.txt", "r") as fp:
            lines=fp.readlines()
        with open(r"D:\tsyal\names.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != name:
                    fp.write(line)
                else:
                    line.strip
        await interaction.response.send_message(f"Imię **{name}** zostało usunięte z listy imion ludzi.")
    elif rasa.value == "elf":
        with open(r"D:\tsyal\elves.txt", "r") as fp:
            lines=fp.readlines()
        with open(r"D:\tsyal\elves.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != name:
                    fp.write(line)
                else:
                    line.strip
        await interaction.response.send_message(f"Imię **{name}** zostało usunięte z listy imion elfów.")
    elif rasa.value == "krasnolud":
        with open(r"D:\tsyal\dwarves.txt", "r") as fp:
            lines=fp.readlines()
        with open(r"D:\tsyal\dwarves.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != name:
                    fp.write(line)
                else:
                    line.strip
        await interaction.response.send_message(f"Imię **{name}** zostało usunięte z listy imion krasnoludów.")
    else:
        await interaction.response.send_message(f"Proszę wybrać dostępną opcję")

@bot.tree.command(name="namelist", description="Wyświetla zawartość listy imion z danej kategorii")
@app_commands.describe(rasa="rasa Twojej postaci")
@app_commands.choices(rasa=[
        app_commands.Choice(name="Krasnolud", value="krasnolud"),
        app_commands.Choice(name="Elf", value="elf"),
        app_commands.Choice(name="Człowiek", value="czlowiek")
    ])
async def namelist(interaction: discord.Integration, rasa: app_commands.Choice[str]):
    if rasa.value == "czlowiek":
        with open(r"D:\tsyal\names.txt", "r") as f:
            lines = [line for line in f]
        await interaction.response.send_message(' '.join(lines))
    elif rasa.value == "elf":
        with open(r"D:\tsyal\elves.txt", "r") as f:
            lines = [line for line in f]
        await interaction.response.send_message(' '.join(lines))
    elif rasa.value == "krasnolud":
        with open(r"D:\tsyal\dwarves.txt", "r") as f:
            lines = [line for line in f]
        await interaction.response.send_message(' '.join(lines))
    else:
        await interaction.response.send_message(f"Proszę wybrać dostępną opcję")

@bot.tree.command(name="createcharacter", description="Tworzy kartę postaci ze statystykami z systemu DnD")
@app_commands.describe(
    name="Imię dla Twojej postaci",
    char_class="Klasa Twojej postaci",
    portrait="Link do rysunku postaci",
    strength="Siła postaci, podaj wartość lub wpisz random",
    dexterity="Zręczność i zwinność postaci, podaj wartość lub wpisz random",
    constitution="Zdrowie postaci, podaj wartość lub wpisz random",
    intelligence="Inteligencja postaci, podaj wartość lub wpisz random",
    wisdom="Intuicja i postrzeganie postaci, podaj wartość lub wpisz random",
    charisma="Siła woli postaci, podaj wartość lub wpisz random",
    notes="Dowolne notatki i informacje na temat postaci"
    )
async def createcharacter(
    interaction: discord.Integration, name: str, char_class: str, portrait: str, strength: str, dexterity: str, constitution: str, intelligence: str, wisdom: str, charisma: str, notes: str
    ):
    filename=str(interaction.user.mention)
    with open(f"{filename[2:-1]}.txt", "w") as f:
        f.write(f"{name}\n")
        f.write(f"{char_class}\n")
        f.write(f"{portrait}\n")

        def randomstat(statname):
            if statname == "random":
                rand_str=[]
                for x in range(4):
                    rand_str.extend([random.randint(1,6)])
                rand_str.sort()
                f.write(f"{sum(rand_str[-3:])}\n")
            else:
                f.write(f"{statname}\n")

        randomstat(strength)
        randomstat(dexterity)
        randomstat(constitution)
        randomstat(intelligence)
        randomstat(wisdom)
        randomstat(charisma)    


        f.write(f"{notes}\n")
        f.close
    await interaction.response.send_message(f"Stworzono postać")

@bot.tree.command(name="karta", description="Wyświetla kartę postaci wybranego użytkownika")
@app_commands.describe(gracz="Gracz, którego kartę postaci chcesz zobaczyć (@gracz), zostaw puste jeśli chcesz zobaczyć swoją")
async def karta(interaction: discord.Integration, gracz: str=None):
    try:
        if gracz == None:
            gracz=interaction.user.mention
        file_name=gracz[2:-1]
        f=open(f"{file_name}.txt","r")
        emb_title=f.readline()
        emb_desc=f.readline()
        emb_img=f.readline()
        emb_str=f.readline()
        emb_dex=f.readline()
        emb_con=f.readline()
        emb_int=f.readline()
        emb_wis=f.readline()
        emb_cha=f.readline()
        emb_notes=f.readline()
        f.close()

        embed=discord.Embed(title=emb_title[0:-1], description=emb_desc)
        embed.set_image(url=emb_img)
        embed.add_field(name="Strength", value=emb_str, inline=True)
        embed.add_field(name="Dexterity", value=emb_dex, inline=True)
        embed.add_field(name="Constitution", value=emb_con, inline=True)
        embed.add_field(name="Intelligence", value=emb_int, inline=True)
        embed.add_field(name="Wisdom", value=emb_wis, inline=True)
        embed.add_field(name="Charisma", value=emb_cha, inline=True)
        embed.add_field(name="Notatki", value=emb_notes, inline=False)
        await interaction.response.send_message(embed=embed)
    except FileNotFoundError:
        await interaction.response.send_message(f"Użytkonik nie posiada karty postaci")

@bot.tree.command(name="modkarty", description="Modyfikuje wybrany element Twojej karty postaci")
@app_commands.describe(element="Który element swojej karty chcesz zmienić", wartosc="Nowa wartość, która ma zostać przypisana")
@app_commands.choices(element=[
        app_commands.Choice(name="Nazwa", value="name"),
        app_commands.Choice(name="Klasa", value="class"),
        app_commands.Choice(name="Obrazek", value="portrait"),
        app_commands.Choice(name="Siła", value="str"),
        app_commands.Choice(name="Zręczność", value="dex"),
        app_commands.Choice(name="Konstytucja", value="con"),
        app_commands.Choice(name="Inteligencja", value="int"),
        app_commands.Choice(name="Mądrość", value="wis"),
        app_commands.Choice(name="Charyzma", value="cha"),
        app_commands.Choice(name="Notatki", value="notes")
    ])
async def modkarty(interaction: discord.Integration, element: app_commands.Choice[str], wartosc: str):
    file_name=interaction.user.mention[2:-1]

    def changeline(linenum):
        with open(f"{file_name}.txt","r") as file:
            data = file.readlines()
        data[linenum] = f"{wartosc}\n"
        with open(f"{file_name}.txt","w") as file:
            file.writelines(''.join([str(elem) for elem in data]))

    if element.value == "name":
        changeline(0)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")
            
    elif element.value == "class":
        changeline(1)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")
    
    elif element.value == "portrait":
        changeline(2)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    elif element.value == "str":
        changeline(3)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    elif element.value == "dex":
        changeline(4)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    elif element.value == "con":
        changeline(5)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    elif element.value == "int":
        changeline(6)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    elif element.value == "wis":
        changeline(7)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    elif element.value == "cha":
        changeline(8)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    elif element.value == "notes":
        changeline(9)
        await interaction.response.send_message(f"Nowa wartość {element.value} to {wartosc}.")

    else:
        await interaction.response.send_message(f"Niepoprawna nazwa parametru")
    

@bot.tree.command(name="modyfikujeq", description="Modyfikuje ekwipunek gracza")
@app_commands.describe(akcja ="Co chcesz zrobić z ekwipunkiem", przedmiot="Przedmiot, który chcesz dodać/usunąć z ekwipunku")
@app_commands.choices(akcja=[
    app_commands.Choice(name="Dodaj", value="dodaj"),
    app_commands.Choice(name="Usuń", value="usun"),
    ],
    przedmiot=[
        app_commands.Choice(name="Miecz", value="miecz"),
        app_commands.Choice(name="Tarcza", value="tarcza"),
        app_commands.Choice(name="Tunelowy wykrywacz zakłóceń fal grawitacyjnych", value="wykrywacz"),
        app_commands.Choice(name="Przedmiot Czwarty", value="cztery")
    ])
async def modyfikujeq(interaction: discord.Integration, akcja: app_commands.Choice[str], przedmiot: app_commands.Choice[str]):
    file_name=interaction.user.mention[2:-1]
    count=0
    if akcja.value=="dodaj":
        f = open(f"ekw_{file_name}.txt", "a")
        f.write("\n")
        f.write(przedmiot.value)
        f.close()
        await interaction.response.send_message(f"Do Twojego ekwipunku dodano **{przedmiot.name}**")
    elif akcja.value=="usun":
        with open(f"ekw_{file_name}.txt", "r") as fp:
            lines=fp.readlines()
        with open(f"ekw_{file_name}.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != przedmiot.value:
                    fp.write(line)
                else:
                    if count>=1:
                        fp.write(line)
                    count = count+1

                    
            await interaction.response.send_message(f"Usunięto **{przedmiot.name}** z Twojego ekwipunku")

@bot.tree.command(name="przedmiot", description="Podaje informacje o wybranym przedmiocie")
@app_commands.describe(przedmiot="Przedmiot, o którym chcesz przeczytać")
@app_commands.choices(przedmiot=[
        app_commands.Choice(name="Miecz", value="miecz"),
        app_commands.Choice(name="Tarcza", value="tarcza"),
        app_commands.Choice(name="Tunelowy wykrywacz zakłóceń fal grawitacyjnych", value="wykrywacz"),
        app_commands.Choice(name="Przedmiot Czwarty", value="cztery")
])
async def przedmiot(interaction: discord.Integration, przedmiot: app_commands.Choice[str]):
    if przedmiot.value=="miecz":
        embed=discord.Embed(title="Miecz", description="Chyba najmniej oryginalny pomysł w historii pomysłów jeśli chodzi o broń", color=0x101010)
        embed.set_image(url="https://media.discordapp.net/attachments/1046385267071799326/1046397619750051860/sungorio_component_278b_of_the_final_magical_weapon_133e117a-2aa4-48e6-aac6-c9083ee91e3a.png?width=662&height=662")
    elif przedmiot.value=="tarcza":
        embed=discord.Embed(title="Tarcza", description="Chroni przed atakami przeciwników. Niezwykłe, co?", color=0xb79a77)
        embed.set_image(url="https://media.discordapp.net/attachments/1046385267071799326/1055104674967060550/sungorio_xenon_hyperdrive_ring_0e48c1b3-8a81-46f7-ad9f-bdc0acfae6ac.png?width=662&height=662")
    elif przedmiot.value=="wykrywacz":
        embed=discord.Embed(title="Tunelowy wykrywacz zakłóceń fal grawitacyjnych", description="Wykrywa lokalne zakłócenia w falach grawitacyjnych", color=0xb41b0a)
        embed.set_image(url="https://media.discordapp.net/attachments/1046385267071799326/1055178173089857568/sungorio_laser_viewfinder_f286b9ae-611b-46d0-ad62-f4638cf4de79.png?width=662&height=662") 
    elif przedmiot.value=="cztery":
        embed=discord.Embed(title="Przedmiot czwarty", description="Jest ostatnim z czterech przedmiotów", color=0xc7ba9a)
        embed.set_image(url="https://media.discordapp.net/attachments/1046385267071799326/1055182916784763070/sungorio_blueprint_of_an_organic_blimp_f659795f-7c39-42c0-89d1-4df464f9a309.png?width=662&height=662") 
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="pokazeq", description="Wyświetla ekwipunek wybranego użytkownika")
@app_commands.describe(gracz="Gracz, którego ekwipunek chcesz zobaczyć (@gracz), zostaw puste jeśli chcesz zobaczyć swój")
async def pokazeq(interaction: discord.Integration, gracz: str=None):
    try:
        embed=discord.Embed(title=f"Ekwipunek gracza {interaction.user}")
        if gracz == None:
            gracz=interaction.user.mention
        file_name=gracz[2:-1]
        f=open(f"ekw_{file_name}.txt","r")
        count=0
        while True:
            count += 1
            line = f.readline()
            if not line:
                break
            if line.strip("\n")=="miecz":
                embed.add_field(name=":crossed_swords: Miecz", value="", inline=False)
            elif line.strip("\n")=="tarcza":
                embed.add_field(name=":shield: Tarcza", value="", inline=False)
            elif line.strip("\n")=="wykrywacz":
                embed.add_field(name=":satellite: Tunelowy wykrywacz zakłóceń fal grawitacyjnych", value="", inline=False)
            elif line.strip("\n")=="cztery":
                embed.add_field(name=":four: Przedmiot czwarty", value="", inline=False)

        await interaction.response.send_message(embed=embed)
    except FileNotFoundError:
        await interaction.response.send_message(f"Użytkownik nie posiada ekwipunku")



@bot.tree.command(name="odejmij", description="Odejmuje odjemnik od odjemnej")
@app_commands.describe(odjemna="Liczba, od której odejmujesz", odjemnik="Liczba, którą odejmujesz")
async def odejmij(interaction: discord.Integration, odjemna: float, odjemnik: float ):
    res = odjemna - odjemnik
    await interaction.response.send_message(f"{odjemna} - {odjemnik} = {res}")

@bot.tree.command(name="dodaj", description="Sumuje dwa składniki")
@app_commands.describe(skladnik_1="Pierwsza liczba do dodania", skladnik_2="Druga liczba do dodania")
async def dodaj(interaction: discord.Integration, skladnik_1: float, skladnik_2: float ):
    res = skladnik_1 + skladnik_2
    await interaction.response.send_message(f"{skladnik_1} + {skladnik_2} = {res}")

@bot.tree.command(name="podziel", description="Dzieli dzielną przez dzielnik")
@app_commands.describe(dzielna="Liczba, która jest dzielona", dzielnik="Liczba, przez którą dzielisz")
async def podziel(interaction: discord.Integration, dzielna: float, dzielnik: float ):
    res = dzielna / dzielnik
    await interaction.response.send_message(f"{dzielna} : {dzielnik} = {res}")

@bot.tree.command(name="pierwiastek", description="Pierwiastkuje liczbę")
@app_commands.describe(liczba="Liczba, która ma zostać spierwiastkowana")
async def pierwiastek(interaction: discord.Integration, liczba: float):
    res = math.sqrt(liczba)
    await interaction.response.send_message(f"√{liczba} = {res}")

@bot.tree.command(name="pomnoz", description="Mnoży przez siebie dwa czynniki")
@app_commands.describe(czynnik_1="Pierwsza liczba do pomnożenia", czynnik_2="Druga liczba do pomnożenia")
async def pomnoz(interaction: discord.Integration, czynnik_1: float, czynnik_2: float ):
    res = czynnik_1 * czynnik_2
    await interaction.response.send_message(f"{czynnik_1} • {czynnik_2} = {res}")

@bot.tree.command(name="build", description="Wyświetla poradnik dla wybranego bohatera")
@discord.app_commands.describe(champion_name='Nazwa wybranego bohatera', lane='Linia wybrana do poradnika')
async def build(ctx, champion_name:str, lane:str):
    champion_name = champion_name.capitalize()
    lane = lane.lower()
    
    # Sprawdzenie, czy linia jest prawidłowa
    available_lanes = ['top', 'jungle', 'mid', 'bot', 'support']
    if lane not in available_lanes:
        await ctx.response.send_message(f'Podano nieprawidłową linię. Dostępne linie: {", ".join(available_lanes)}.')
        return
    
    if champion_name in champions_specs:
        if lane in champions_specs[champion_name]:
            mobafire_url = champions_specs[champion_name][lane]
            await ctx.response.send_message(f'Build dla {champion_name} na linii {lane}:\n{mobafire_url}')
        else:
            await ctx.response.send_message('Nie znaleziono danych dla podanej linii.')
    else:
        await ctx.response.send_message('Nie znaleziono danych dla podanego bohatera.')

@bot.tree.command(name="losujbohatera", description="Losuje jednego z bohaterów")
async def losujbohatera(ctx):
    available_champions = list(champions_specs.keys())
    random_champion = random.choice(available_champions)
    
    await ctx.response.send_message(f'Wylosowany bohater: {random_champion}')
    

bot.run(TOKEN)