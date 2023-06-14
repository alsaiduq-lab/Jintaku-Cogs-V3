from .osu import Osu


async def setup(bot):
    n = Osu()
    await bot.add_cog(n)
