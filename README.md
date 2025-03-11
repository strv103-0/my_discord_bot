1. cogs 폴더
- 디스코드 봇의 기능을 모듈별로 관리(cog)하기 위한 폴더
- example_cog.py에는 예시 명령어를 담은 Cog 클래스를 구현
- 향후 기능이 늘어날 때마다 파일을 추가(예: music_cog.py, moderation_cog.py 등)

2. main.py
- 봇의 진입점(엔트리 포인트)
- 디스코드 봇의 기본 구동 로직과 Cog 로드 등을 포함

3. requirements.txt
- pip install -r requirements.txt 명령어로 필요한 라이브러리를 설치하기 위해 사용
- 예: discord.py==2.1.0, python-dotenv==1.0.0 등


git test