# Modals/SorteosModal.py

import discord

class SorteosModal(discord.ui.Modal, title="Sorteos generales"):

   username = discord.ui.TextInput(label="Usuario", placeholder="Usuario de Twitch o Instagram", style=discord.TextStyle.short)
   reward = discord.ui.TextInput(label="Premio", placeholder="Premio que se gano", style=discord.TextStyle.short)
   data = discord.ui.TextInput(label="Datos requeridos", placeholder="Datos de contacto (dirección, telefono, nombre, etc.)", style=discord.TextStyle.paragraph)

   async def on_submit(self, interaction:discord.Interaction):

       await interaction.response.send_message(content="Datos enviados")
