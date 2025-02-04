# Modals/ProblemModal.py

import discord

class ProblemModal(discord.ui.Modal, title="Hay algun problema en el server?"):

    section = discord.ui.TextInput(label="Sección",placeholder="Canal de voz o texto, donde se origina el problema",style=discord.TextStyle.short)
    description = discord.ui.TextInput(label="Descripción",placeholder="Menciona a detalle que problema hay",style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction:discord.Interaction):

       #Colocar logica de DM, mods o admins
       await interaction.response.send_message(content="Gracias por informar el problema, en breve analizaremos lo que esta pasando")

