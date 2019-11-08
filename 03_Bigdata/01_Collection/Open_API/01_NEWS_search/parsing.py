import json

with open("코스피 _naver_news.json", 'r', encoding='utf-8') as json_file:
    json_date = json.load(json_file)
print(json_date)