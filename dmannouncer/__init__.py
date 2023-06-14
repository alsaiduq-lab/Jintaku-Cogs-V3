from .dmannouncer import Dmannouncer


async def setup(bot):
    n = Dmannouncer()
    await bot.add_cog(n)
