import requests
import sys
import json

WEA_API = "1dd7aed643704c2cbd0153349242409"
TYPE =  sys.argv[1]
LOC = sys.argv[2] 

response = requests.get(f'http://api.weatherapi.com/v1/{TYPE}.json?key={WEA_API}&q={LOC}')
if response.status_code == 200:
    string = str(response.json()) 
    data = json.loads(string)
    print(data)
else:
    print("bad request ...")

