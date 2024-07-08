# Modals/TiktokModal.py

import discord

class TiktokModal(discord.ui.Modal, title="Seguir en Tiktok"):

    username = discord.ui.TextInput(label="Usuario", placeholder="Usuario de Twitch",style=discord.TextStyle.short)
    tkUser = discord.ui.TextInput(label="Tiktok", placeholder="Usuario de Tiktok",style=discord.TextStyle.short)

    async def on_submit(self, interaction:discord.Interaction):

        await interaction.response.send_message(content="Datos enviados")
