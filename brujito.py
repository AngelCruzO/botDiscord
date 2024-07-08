import asyncio
import datetime
import discord
import os
import platform
import random
import time
import vt
import requests

from colorama import Back, Fore, Style
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from UI.Modals import AnunciosModal
from UI.Selects.PremiosSelect import PremiosSelect

#Cargar variables de entorno
load_dotenv()

#Discord
DC_TOKEN = os.getenv('TOKEN_DISCORD')

#Virus Total
VT_TOKEN = os.getenv('TOKEN_VT')

#Variables globales
prefix = "!"

#Variable ciente de discord
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

#Variable cliente Virus Total
clientVT = vt.Client(VT_TOKEN)

async def scanner(url):
    async with clientVT:
        analysis = await clientVT.scan_url_async(url)
        while True:
            analysis = await clientVT.get_object_async(f"/analyses/{analysis.id}")
            if analysis.status == "completed":
                break
    
        url_id = vt.url_id(url)
        urlScan = await clientVT.get_object_async(f"/urls/{url_id}")

        return urlScan.last_analysis_stats

#async def result():
#    result = await  scanner("www.googlw.com")
#    print(result)

@client.event
async def on_ready():
    synced = await client.tree.sync()
    print(f"{str(len(synced))}")

#id 1233611453253156926 name testbot
@client.command(aliases=['hi'])
async def hola(ctx):
    if ctx.channel.name == 'testbot':
        print(adminRoles)
        await ctx.send("Hello Magic World")
    else:
        await ctx.send("Lo siento mis poderes no sirven en este reino")

#Scanear URL
@client.command(aliases=['scan', 'scanner'])
async def virus(ctx, url="www.google.com"):
    if ctx.channel.name == 'testbot':
        result = await scanner(url)
        await ctx.send(f"Hola Mundo: {result}")
    else:
        await ctx.send("Lo siento mis poderes no sirven en este reino")

#Status web
@client.command(aliases=['status','down'])
async def estado(ctx, url="https://www.google.com"):
    if ctx.channel.name == 'testbot':
        response = requests.get(url)
        if response.status_code != 200:
            await ctx.send(f"El servicio para {url} esta teniendo problemas")
        else:
            await ctx.send(f"{url} tiene su servicio con normalidad")
    else:
        await ctx.send("Lo siento mis poderes no sirven en este reino")

#Comandos slash

#Recompensas

#Soporte
@client.tree.command(name="soporte", description="Proporciona ayuda sobre algun bug o contacto personal")
async def soporte(interaction:discord.Interaction):
    if interaction.channel.name == 'testbot':
        await interaction.response.send_message(content="En que puedo ayudarte")
    else:
        await interaction.response.send_message(content="Lo siento mis poderes no sirven en este reino")

#Creación channel_voice

#Anuncios
@client.tree.command(name="anuncio", description="Manda un anunción al canal de anuncios")
async def anuncio(interaction:discord.Interaction, member:discord.Member=None):
    if member == None:
        member = interaction.user
    if interaction.channel.name == '・🔈・anuncios':
        roles = [role.name for role in member.roles]
        guildRoles = [role.name for role in interaction.guild.roles]
        adminRoles = [guildRoles[25], guildRoles[26]]
 
        if roles[1] in adminRoles:
            await interaction.response.send_modal(AnunciosModal())
        else: await interaction.response.send_message(content="Alto ahi, no cuentas con el pase de viajero")
    else:
        await interaction.response.send_message(content="Los siento mis poderes no sirven en este reino")

#Recompensas
@client.tree.command(name="premios", description="Canje de recompensas de twitch y sorteos")
async def premios(interaction: discord.Interaction):
    if interaction.channel.name == "testbot":
        await interaction.response.send_message(content="Selecciona una categoria", view=PremiosSelect(),ephemeral=True)
    else:
        await interaction.response.send_message(content="Lo siento mis poderes no sirven en este reino")

client.run(DC_TOKEN)

clientVT.close()
