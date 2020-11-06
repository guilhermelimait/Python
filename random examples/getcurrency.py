import requests 
import urllib, json

r = requests.get('https://api.exchangeratesapi.io/history?start_at=2020-10-30&end_at=2020-11-06&symbols=BRL')
print (r.text)
