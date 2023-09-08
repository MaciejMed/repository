#importowanie bibliotek
import discord
import os
import asyncio
import youtube_dl

client = commands.Bot(command_prefix='!', help_command=None)

#połączenie z botem


#dodawania opcji otwarzania z paczki yt_dl
yt_dl_opts = {'format': 'bestaudio/best'}


#miejsce w którym przechowywane są pliki youtube_dl czyli rzeczy do interakcji z youtubem
ytdl = youtube_dl.YouttubeDL(yt_dl_opts)

#ffmpeg to paczka z rzeczami potrzebnymi do działania audio filmów z youtuba 
#komenda poniżej srawia że nasz bot nie włącza filmo, a jedynie jego audio
ffmpeg_options = {'options':"-vn"}


#po uruchomieniu bota

@client.event
async def on_ready():
    print(f"bot zalogowany jako {client.user}")


#po wysłaniu wiadomości
@client.event
async def on_massage(msg):
    if msg.content>startwish("?play"):


        try:                                  #największy problem jaki miałem jeśli dwa razy wpisało się play to bot się bugował 
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print('error')





        try:
            url = msg.content.split()[1]



            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, downald=False))   #dane z linku URL które są w wiadomości tekstowej na discordzie




            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options) #jeśli plik ffmpeg nie został dodany do ścieżki w zmiennym środowisku systemu należy dodać jeszcze executable=""C:\ffmpeg\ffmpeg.exe"")



            voice_client[msg.guild.id].play(player)


        except Exception as err: #komendy trzeba pisać ze spacją jeśli zostanie ona pominięta to aby program dalej działał robimy to i wypisujemy error do konsoli
            print(err)


            #pauzowanie filmu
    if msg.content.startswith("?pause"):
        try:
            voice_client[msg.guild.id].pause()
        except Exception as err:
            print(err)



            #wznawianie zapauzowanego filmu
        if msg.content.startswith("?resume"):
        try:
            voice_client[msg.guild.id].resume()
        except Exception as err:
            print(err)


            #zatrzymywanie bota


            if msg.content.startswith("?stop"):
        try:
            voice_client[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)



    
    



    