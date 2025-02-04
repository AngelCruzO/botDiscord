import discord

from UI.Modals import ProblemModal

class SupportSelect(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(MenuSupport())

class MenuSupport(discord.ui.Select):

    def __init__(self):
        options = [discord.SelectOption(label="No puedo ver contenido", description="Solucionar falta de visualización del server"), discord.SelectOption(label="Problema en server", description="Envia un mensaje privado a moderación para solucionar un problema")]

        super().__init__(placeholder="Selecciona una opción", options=options)

    async def callback(self, interaction: discord.Interaction):

        value = self.values[0]

        if value == "No puedo ver contenido":
            
            print("Lo sentimos")

        elif value == "Problema en server":

            await interaction.response.send_modal(ProblemModal())

