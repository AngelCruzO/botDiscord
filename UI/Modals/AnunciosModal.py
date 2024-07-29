# Modals/AnunciosModal.py

import discord
import datetime
import time

class AnunciosModal(discord.ui.Modal, title="Anuncio a la comunidad"):
    
    name = discord.ui.TextInput(label="Evento", placeholder="Cual es el nombre del anunció", style=discord.TextStyle.long)
    description = discord.ui.TextInput(label="Descripción", placeholder="Describe el anuncio que enviaras", style=discord.TextStyle.long)

    async def on_submit(self, interaction:discord.Interaction):

        member = interaction.user
        

        embed = discord.Embed(title=f"{self.name}", description="Atención Comunidad", color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.UTC))
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Usuario", value=f"{member.name}#{member.discriminator}\n")
        embed.add_field(name="Anuncio", value=f"Buen día comunidad, tenemos el siguiente anuncio: \n {self.description}\n")
        #embed.add_field(name="Mention", value=f"@everyone")

        await interaction.response.send_message(embed=embed)

