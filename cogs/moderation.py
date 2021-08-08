import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cls")
    async def delete(self, ctx, number: int):
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()


def setup(bot):
    bot.add_cog(moderation(bot))