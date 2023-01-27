import requests

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
for i in res.values():
    print(i)
print(res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value'])
