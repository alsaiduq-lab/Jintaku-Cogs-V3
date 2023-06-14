from .xkcd import XKCD


async def setup(bot):
    n = XKCD()
    await bot.add_cog(n)
