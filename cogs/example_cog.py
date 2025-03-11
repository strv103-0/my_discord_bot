import discord
from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 명령어 예시
    @commands.command(name="ping")
    async def ping_command(self, ctx):
        await ctx.send("pong!")

    # 명령어 확장 예시
    @commands.command(name="hello")
    async def hello_command(self, ctx):
        await ctx.send(f"안녕하세요, {ctx.author.mention}님!")

# Cog 세팅
async def setup(bot):
    await bot.add_cog(ExampleCog(bot))
