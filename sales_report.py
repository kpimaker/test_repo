import requests
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data.json()