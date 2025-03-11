# src/cogs/example_cog.py
from discord.ext import commands

class ExampleCog(commands.Cog):
    """기본 테스트용 Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """!hello 명령어"""
        await ctx.send("안녕하세요! ExampleCog에서 온 메시지입니다.")

    @commands.command()
    async def repeat(self, ctx, *, text: str):
        """!repeat [문자열] → 입력받은 문자열을 반복 응답"""
        await ctx.send(f"반복 요청: {text}")

def setup(bot):
    bot.add_cog(ExampleCog(bot))

