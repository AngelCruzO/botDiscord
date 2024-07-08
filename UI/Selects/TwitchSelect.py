import discord

from UI.Modals import * 

class TwitchSelect(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(MenuTwitch())

class MenuTwitch(discord.ui.Select):    

    def __init__(self):
        options = [discord.SelectOption(label="Saludo personalizado",description="Te mando un saludo con el mensaje que gustes"),discord.SelectOption(label="Follow Instagram",description="Te sigo en Instagram"),discord.SelectOption(label="Follow Tiktok",description="Te sigo en Tiktok"),discord.SelectOption(label="Playera Github",description="Te compro una playera de Github de la tienda oficial"),discord.SelectOption(label="Echo Dot (Alexa)",description="Te compro una Alexa de ultima generación"),discord.SelectOption(label="Cambio de premio",description="Te puedo cambiar el valor equivalente del premio por otra cosa")]
        super().__init__(placeholder="Selecciona una opción",options=options)

    async def callback(self, interaction:discord.Interaction):

        self.disabled = True
        value = self.values[0]


        if value == "Saludo personalizado":
            await interaction.response.send_modal(SaludoModal())
        elif value == "Follow Instagram":
            await interaction.response.send_modal(IGModal())
        elif value == "Follow Tiktok":
            await interaction.response.send_modal(TiktokModal())
        elif value == "Playera Github":
            await interaction.response.send_modal(TshirtModal())
        elif value == "Echo Dot (Alexa)":
            await interaction.response.send_modal(EchoModal())
        elif value == "Cambio de premio":
            await interaction.response.send_modal(ChangeModal())
