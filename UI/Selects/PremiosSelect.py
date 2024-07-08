import discord

from UI.Modals import SorteosModal
from UI.Selects.TwitchSelect import TwitchSelect

class PremiosSelect(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(MenuPremios())

class MenuPremios(discord.ui.Select):

    def __init__(self):
        options = [discord.SelectOption(label="Recompensas Twitch", description="Canje de puntos de canal de Twitch"), discord.SelectOption(label="Premios sorteos", description="Sorteos realizados para la comunidad")]
        super().__init__(placeholder="Selecciona una opción", options=options)

    async def callback(self, interaction: discord.Interaction):

        self.disabled = True
        value = self.values[0]

        if value == "Recompensas Twitch":
            await interaction.response.send_message(content="Selecciona tu premio", view=TwitchSelect())
        elif value == "Premios sorteos":
            await interaction.response.send_modal(SorteosModal())

