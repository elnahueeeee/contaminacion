import discord
from mi_token import Token
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    try:
        print(f'We have logged in as {bot.user}')
    except Exception as e:
        print(f"Error en evento inicio: error {e}")

@bot.command()
async def hello(ctx):
    try:
        await ctx.send(f'Hola, soy un bot {bot.user}!')
    except Exception as e:
        print(f"Error en comando hello: error {e}")

@bot.command()
async def ayuda(ctx):
    try:
        await ctx.send('Comandos disponibles:')
        await ctx.send('$hello: Muestra un saludo')
        await ctx.send('$ayuda: Muestra los comandos disponibles')
        await ctx.send('$pags: Muestra las paginas de informacion confiable')
        await ctx.send('$basureros: Muestra los significados de los colores de los basureros')
    except Exception as e:
        print(f"Error en comando help: error {e}")

lista = {
    "OMS": "https://www.who.int/",
    "PNUMA": "https://www.unep.org/",
    "IEA": "https://www.iea.org/",
    "EPA": "https://www.greenpeace.org/",
    "España": "https://www.wri.org/",
    "INECC": "https://earthjustice.org/",
    "Greenpeace": "https://www.nature.com/",
    "Science": "https://www.sciencemag.org/",
    "WRI": "https://www.wri.org/",
    "Our_World_in_Data": "https://ourworldindata.org/",
    "IQAir": "https://www.iqair.com/"
}

@bot.command()
async def pags(ctx):
    try:
        await ctx.send('Paginas de informacion confiable:')
        for name, url in lista.items():
            await ctx.send(f'{name}: {url}')
    except Exception as e:
        print(f"Error en comando pags: error {e}")

@bot.command()
async def basureros(ctx):
    try:
        File = discord.File("image.png")
        await ctx.send('Basureros:', file=File)
    except Exception as e:
        print(f"Error en comando basureros: error {e}")

@bot.command()
async def evitar(ctx):
    try:
        await ctx.send('Formas de evitar contaminar:')
    except Exception as e:
        print(f"Error en comando basureros: error {e}")

bot.run(Token)