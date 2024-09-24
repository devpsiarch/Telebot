import requests
import sys
import json

WEA_API = "api goes here"
TYPE =  sys.argv[1]
LOC = sys.argv[2] 

response = requests.get(f'http://api.weatherapi.com/v1/{TYPE}.json?key={WEA_API}&q={LOC}')
if response.status_code == 200:
    string = str(response.json()) 
    data = json.loads(string)
    print(data)
else:
    print("bad request ...")

