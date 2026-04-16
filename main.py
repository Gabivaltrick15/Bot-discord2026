import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_class(model_path, labels_path, image_path): # Seu código de processamento aqui 
    resultado = "Exemplo" 
    return resultado

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attacments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./(attachment.filename)")
            await ctx.send (get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path= f"./{attachment.filename}"))
    else:
        await ctx.send("Você esqueceu de enviar a imagem :)")

bot.run("TOKEN")

