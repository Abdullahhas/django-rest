import requests
import json


URL = "http://127.0.0.1:8000/crud/"

def get_data(id = None):
    params = {}
    if id is not None:
        params['id'] = id
    
    r = requests.get(url=URL , params=params)
    res = r.json()
    print(res)


def create_data():
    data = {
        'id' : 3, 
        'name' : 'mateen haider',
        'roll' : 54,
        'city' : 'gojra'
    }

    json_data = json.dumps(data)
    
    r = requests.post(url=URL , data = json_data)
    res = r.json()
    print(res)

def update_data ():
    
    data ={
        'id' : 4,
        'name' : 'ali naqi khan',
        'roll' : 32,
        'city' : 'lahore'
    } 

    json_data = json.dumps(data)
    
    r = requests.put(url=URL , data = json_data)
    res = r.json()
    print(res)

def delete_data():
    data  = {'id' : 3}
    json_data = json.dumps(data)
    
    r = requests.delete(url=URL , data = json_data)
    res = r.json()
    print(res)







# delete_data()
# update_data()
# get_data()
create_data()