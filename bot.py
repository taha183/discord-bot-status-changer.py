import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

PREFIX = ("!")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@bot.event
async def on_ready():
    activity = discord.Game(name="Join Light Riders https://discord.gg/e8eQJhCawM")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("bot is ready")

bot.run('token')
