# Modals/ChangeModal.py

import discord

class ChangeModal(discord.ui.Modal, title="Cambio de premio"):

    username = discord.ui.TextInput(label="Usuario",placeholder="Usuario de Twitch",style=discord.TextStyle.short)
    name = discord.ui.TextInput(label="Nombre",placeholder="Nombre completo",style=discord.TextStyle.long)
    reward = discord.ui.TextInput(label="Premio",placeholder="Playera o Alexa",style=discord.TextStyle.long)
    paypal = discord.ui.TextInput(label="Paypal",placeholder="Cuenta de Paypal",style=discord.TextStyle.long)

    async def on_submit(self, interaction:discord.Interaction):
        
        await interaction.response.send_message(content="Datos enviados")
