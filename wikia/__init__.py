from .wikia import Wikia


async def setup(bot):
    n = Wikia()
    await bot.add_cog(n)
