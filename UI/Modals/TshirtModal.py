# Modals/TshirtModal.py

import discord

class TshirtModal(discord.ui.Modal, title="Playera de Github"):

    username = discord.ui.TextInput(label="Usuario",placeholder="Usuario de Twitch",style=discord.TextStyle.short)
    name = discord.ui.TextInput(label="Nombre",placeholder="Nombre completo",style=discord.TextStyle.long)
    phone = discord.ui.TextInput(label="Telefono",placeholder="Numero de telefono",style=discord.TextStyle.short)
    address = discord.ui.TextInput(label="Dirección",placeholder="Dirección completa",style=discord.TextStyle.paragraph)
    link = discord.ui.TextInput(label="Playera",placeholder="Enlace del producto",style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction:discord.Interaction):

        await interaction.response.send_message(content="Datos enviados")
