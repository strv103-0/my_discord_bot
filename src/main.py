# src/main.py
import os
import logging

# py-cord 관련 임포트
import discord
from discord.ext import commands

from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,  # 로그 레벨: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),  # 파일에 로그 저장
        logging.StreamHandler()  # 콘솔에도 로그 출력
    ]
)

# py-cord Intents 설정
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
# 필요한 경우 intents.message_content = True 등 권장

# 명령어 접두사(prefix)는 예시로 "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# 초기 로드할 Cog 목록
initial_extensions = [
    "cogs.admin",
    "cogs.example_cog",
]

if __name__ == "__main__":
    # 확장(Cog) 로드
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f"봇이 로그인했습니다. 사용자명: {bot.user}")
    logging.info("Bot is ready.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("존재하지 않는 명령어입니다.")
    else:
        logging.error(f"Unhandled command error: {error}")
        await ctx.send("오류가 발생했습니다. 관리자에게 문의하세요.")

# 봇 실행
bot.run(TOKEN)
