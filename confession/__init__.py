from .confession import Confession


async def setup(bot):
    n = Confession()
    await bot.add_cog(n)
