import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# .env 파일에 있는 환경변수 로드
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# 봇 인텐트 설정(권한 관련)
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 확인이 필요한 경우 활성화

# 봇 생성
bot = commands.Bot(command_prefix="!", intents=intents)

# 봇 이벤트: 준비 완료 시 콘솔에 표시
@bot.event
async def on_ready():
    print(f"봇이 로그인되었습니다. 사용자명: {bot.user}")

# Cog 로드 예시
initial_extensions = [
    "cogs.example_cog"
]

if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

    # 디스코드 봇 실행
    bot.run(DISCORD_TOKEN)
