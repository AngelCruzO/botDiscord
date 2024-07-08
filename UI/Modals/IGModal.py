# Modals/IGModal.py

import discord

class IGModal(discord.ui.Modal, title="Seguir en Instagram"):

    username = discord.ui.TextInput(label="Usuario",placeholder="Usuario de Twitch",style=discord.TextStyle.short)
    igUser = discord.ui.TextInput(label="Instagram",placeholder="Usuario de Instagram a seguir",style=discord.TextStyle.short)

    async def on_submit(self, interaction:discord.Interaction):

        await interaction.response.send_message(content="Datos enviados")
