from discord.ext import commands
import json, os

# json file setup
with open('config.json') as f:
    config = json.load(f)
    token = config.get('token')
    prefix = config.get('prefix')

# bot setup 
bot = commands.Bot(command_prefix = prefix)

# cogs setup
if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

# bot source code
@bot.event
async def on_ready():
    print(f'''{bot.user.name} #{bot.user.discriminator} is connected !''')





bot.run(token)
