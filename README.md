# weather-info
2024 Code : Zero 동아리 프로젝트의 일부인 영단어 학습 웹사이트의 저장소입니다.
## 프로젝트 개요
- 목표: 사용자가 오늘의 날씨를 확인하고 날씨 관련 뉴스를 볼 수 있는 웹사이트 제작
- 주요 기능: 오늘의 날씨, 날씨 관련 뉴스
<hr/>

## Tech Stack
- Flask 3.1.0
## Getting Started
.env 파일을 생성하고 다음과 같이 환경변수를 설정해주세요.
```
WEATHER_API_KEY="" # OpenWeatherMap API 사용을 위한 API KEY

NAVER_CLIENT_ID="" # 네이버 API 사용을 위한 클라이언트 ID
NAVER_CLIENT_SECRET="" # 네이버 API 사용을 위한 클라이언트 시크릿
```
.env 설정이 끝나면 다음과 같이 실행해주세요.
```
python -m venv 가상환경이름
source 가상환경이름/Scripts/activate
pip install -r requirements.txt
python app.py
```
