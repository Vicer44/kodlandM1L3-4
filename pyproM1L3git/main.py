import random

import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user} i raczej nic nie zepsuliśmy!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send("Do widzenia!")
    await ctx.send("\U0001f642")

# "pass" jest słowem kluczowym Pythona, więc nazwę podajemy osobno
@bot.command(name='pass')
async def pass_(ctx, pass_length: int = 8):
    password = gen_pass(pass_length)
    await ctx.send(f"Twoje hasło: {password}")

@bot.command()
async def roll(ctx):
    await ctx.send(random.randint(1, 6))

@bot.command()
async def coin(ctx):
    await ctx.send(random.choice(['Orzeł', 'Reszka']))
@bot.command(name='help')
async def help_(ctx):
    await ctx.send(
        "**Lista poleceń:**\n"
        "`$hello` - bot się przedstawia\n"
        "`$heh [liczba]` - śmiech, domyślnie 5 razy, np. `$heh 3`\n"
        "`$bye` - pożegnanie\n"
        "`$pass [długość]` - generuje hasło, domyślnie 8 znaków, np. `$pass 12`\n"
        "`$help` - pokazuje tę listę"
    )

bot.run("TOKEN")  # Replace TOKEN with your actual bot token