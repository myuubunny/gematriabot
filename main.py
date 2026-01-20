import discord
from discord import app_commands
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import pygematria.conv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='g!', intents=intents, allowed_contexts=discord.app_commands.AppCommandContext(guild=True, dm_channel=True, private_channel=True), allowed_installs=discord.app_commands.AppInstallationType(guild=True, user=True))

@bot.event
async def on_ready():
    print({bot.user.name})

@bot.command()
async def sync(interaction):
    print("sync command")
    if interaction.author.id == 448951760925753347:
        await bot.tree.sync()
        await interaction.send('Command tree synced.')
    else:
        await interaction.send('You must be the owner to use this command!')

@bot.tree.command(name="eq", description="English Qaballa cipher")
async def eq(interaction, *, arg: str):
    await interaction.response.send_message("English Qaballa: " + str(pygematria.conv.string_values(arg, 'eq')) + " = " + str(sum(pygematria.conv.string_values(arg, 'eq'))))
    msg = await interaction.original_response()

@bot.tree.command(name="a", description="Agrippa cipher")
async def a(interaction, *, arg: str):
    await interaction.response.send_message("Agrippa: " + str(pygematria.conv.string_values(arg, 'agrippa')) + " = " + str(sum(pygematria.conv.string_values(arg, 'agrippa'))))
    msg = await interaction.original_response()

# @bot.tree.command(name="h", description="Hebrew cipher")
# async def h(interaction, *, arg: str):
#    await interaction.response.send_message("Hebrew: " + str(pygematria.conv.string_values(arg, 'hebrew')) + " = " + str(sum(pygematria.conv.string_values(arg, 'hebrew'))))
#    msg = await interaction.original_response()

# @bot.tree.command(name="g", description="Greek isopsephy cipher")
# async def g(interaction, *, arg: str):
#    await interaction.response.send_message("Greek isopsephy:" + str(pygematria.conv.string_values(arg, 'greek')) + " = " + str(sum(pygematria.conv.string_values(arg, 'greek'))))
#    msg = await interaction.original_response()

@bot.tree.command(name="r", description="Rudolff cipher")
async def r(interaction, *, arg: str):
    await interaction.response.send_message("Rudolff: " + str(pygematria.conv.string_values(arg, 'rudolff')) + " = " + str(sum(pygematria.conv.string_values(arg, 'rudolff'))))
    msg = await interaction.original_response()

@bot.tree.command(name="fortune", description="s4s fortune")
async def fortune(interaction):
    fortune = ['Your Fortune: Reply hazy, try again', 'Your Fortune: Excellent Luck', 'Your Fortune: Good Luck', 'Your Fortune: Average Luck', 'Your Fortune: Bad Luck', 'Your Fortune: Good news will come to you by mail', 'Your Fortune: （  `_ゝ`）ﾌｰﾝ ', 'Your Fortune: ｷﾀ━━━━━━(ﾟ∀ﾟ)━━━━━━ !!!!', 'Your Fortune: You will meet a dark handsome stranger', 'Your Fortune: Better not tell you now', 'Your Fortune: Outlook good', 'Your Fortune: Very Bad Luck', 'Your Fortune: Godly Luck']
    await interaction.response.send_message(random.choice(fortune))
    msg = await interaction.original_response()

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

# סוֹד‎
