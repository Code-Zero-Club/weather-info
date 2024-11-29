from datetime import datetime
import json
import requests
import os

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
NAVER_CLIENT_ID = os.environ.get('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.environ.get('NAVER_CLIENT_SECRET')

WEATHER_API_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

# 네이버 API 설정
NAVER_NEWS_URL = "https://openapi.naver.com/v1/search/news.json"

def get_weather_json() -> dict:
    now = datetime.now()
    
    params = {
        'serviceKey': WEATHER_API_KEY,
        'numOfRows': '70',
        'pageNo': '1',
        'base_date': now.strftime("%Y%m%d"),
        'base_time': '0500',
        'nx': '71',
        'ny': '71',
        'dataType': 'JSON'
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        data = json.loads(response.text)
        
        if response.status_code == 200:
            items = data['response']['body']['items']['item']
            
            weather_info = {
                'temperature': None,
                'humidity': None,
                'precipitation': None,
                'sky': None
            }
            
            for item in items:
                if item['category'] == 'TMP':
                    weather_info['temperature'] = item['fcstValue']
                elif item['category'] == 'REH':
                    weather_info['humidity'] = item['fcstValue']
                elif item['category'] == 'PCP':
                    weather_info['precipitation'] = item['fcstValue']
                elif item['category'] == 'SKY':
                    sky_code = item['fcstValue']
                    
                    sky_code_dict = {
                        '1': '맑음',
                        '3': '구름많음',
                        '4': '흐림'
                    }
                    
                    weather_info['sky'] = sky_code_dict.get(sky_code, 'None')
            
            return weather_info
        else:
            return {"error": "날씨 정보를 가져오는데 실패했습니다."}
            
    except Exception as e:
        return {"error": f"오류 발생: {str(e)}"}

def get_news_json():
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    
    params = {
        "query": "기후",
        "display": 5,
        "sort": "date"
    }
    
    try:
        response = requests.get(
            NAVER_NEWS_URL,
            headers=headers,
            params=params
        )
        
        if response.status_code == 200:
            news_data = response.json()
            return news_data.get('items', [])
        else:
            return []
            
    except Exception as e:
        print(f"뉴스 가져오기 오류: {str(e)}")
        return []