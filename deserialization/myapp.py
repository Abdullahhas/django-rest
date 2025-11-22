import requests
import json

URL = "http://127.0.0.1:8000/studentcreate/"

data = {
    'name' : 'abdullah',
    'roll' : 7,
    'city' : 'kasur'
}

json_data = json.dumps(data)

r = requests.post(url=URL  , data=json_data)

data = r.json()

print(data)