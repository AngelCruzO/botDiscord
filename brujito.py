import asyncio
import datetime
import discord
import os
import platform
import random
import time
#import vt
import requests

from colorama import Back, Fore, Style
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from Global.Global import Global
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

gbInstance = Global()

@client.event
async def on_ready():
    synced = await client.tree.sync()
    print(f"{str(len(synced))}")

#Scanear URL
@client.command(aliases=['scan', 'scanner'])
async def virus(ctx, url="www.google.com"):
    result = gbInstance.analisysURL(url,VT_TOKEN)

    embed = discord.Embed(title="Analisis completado", description=f"Estos son los resultados para **{url}**", color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.UTC))

    embed.add_field(name="Maliciosos", value=f"{result['malicious']}")
    embed.add_field(name="Sospechosos", value=f"{result['suspicious']}")
    embed.add_field(name="No detectados", value=f"{result['undetected']}")
    embed.add_field(name="Inofensivo", value=f"{result['harmless']}")

    await ctx.send(embed=embed) 

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
