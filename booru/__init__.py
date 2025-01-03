from .booru import Booru


async def setup(bot):
    n = Booru(bot)
    await bot.add_cog(n)
