# src/cogs/admin.py
import discord
from discord.ext import commands

class AdminCog(commands.Cog):
    """관리자 권한 관련 명령어 모음"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """멤버를 킥하는 예시 명령어입니다."""
        try:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention}님을 킥했습니다. 사유: {reason}")
        except discord.Forbidden:
            await ctx.send("권한이 부족하거나, 이 사용자를 킥할 수 없습니다.")
        except Exception as e:
            await ctx.send("알 수 없는 오류가 발생했습니다.")
            print(e)

def setup(bot):
    bot.add_cog(AdminCog(bot))
