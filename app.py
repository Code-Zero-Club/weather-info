# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
import json
from datetime import datetime
from utils import get_weather_json, get_news_json
from config import load_config

app = Flask(__name__)

@app.route('/')
def index():
    weather_info = get_weather_json()
    news_info = get_news_json()
    return render_template('index.html', weather=weather_info, news=news_info)

if __name__ == '__main__':
    load_config()
    
    app.run(debug=True)
