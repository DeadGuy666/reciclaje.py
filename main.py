import discord
from discord.ext import commands
import os
# Configuracion del bot
intents = discord.Intents.default
bot = commands.Bot(command_prefix="!",intents=intents)

info = {
    "Plastico": {
        "descripcion": "El plastico es un material reciclable usado en envases, botellas, bolsas, etc."
        "consejos": [
            "lava y seca los envases antes de reciclarlos,",
            "Reutiliza botellas y bolsas plasticas cuando sea posible"
        ]
    }
}
