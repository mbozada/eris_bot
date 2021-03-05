#!/usr/bin/env python3
import random

from discord.ext import commands


def setup(bot):
    bot.add_cog(Fun_Stuff(bot))

class Fun_Stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fun(self, ctx):
        await ctx.send(f'Fun Stuff Test')

    @commands.command()
    async def quote(self, ctx):
        outputs = ["You look great, by the way. Very healthy.",
                    "Look at you. Sailing through the air majestically. Like an eagle. Piloting a blimp.",
                    "This next test involves turrets. You remember them, right? They're the pale spherical things that are full of bullets. Oh wait. That's you in five seconds. Good luck.",
                    "So. How are you holding up?",
                    "BECAUSE I'M A POTATO.",
                    "Say, you're good at murder. Could you - ow - murder this bird for me?",
                    "Agh! Bird! Bird! Kill it! It's evil!"]

        # Select random quote
        quote = random.choice(outputs)
        await ctx.send(quote)
