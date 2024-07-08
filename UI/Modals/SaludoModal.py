# Modals/SaludoModal.py

import discord

class SaludoModal(discord.ui.Modal, title="Personaliza tu saludo"):

    username = discord.ui.TextInput(label="Usuario",placeholder="Usuario de Twitch",style=discord.TextStyle.short)
    social = discord.ui.TextInput(label="Red social",placeholder="Usuario de la red social donde se subira el saludo",style=discord.TextStyle.short)
    saludo = discord.ui.TextInput(label="Saludo",placeholder="Escribe el saludo que deseas recibir",style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction:discord.Interaction):

        await interaction.response.send_message(content="Datos enviados")
