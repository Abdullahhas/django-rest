import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

#READ
def get_data(id = None):
    params = {}
    if id is not None:
        params['id'] = id
    
    r = requests.get(url=URL , params=params)

    data = r.json()

    print(data)




#WRITE
def create_data():

    data = {
    'name': "mughal",
    'roll' : 1,
    'city' : 'shkp'
}

    json_data = json.dumps(data)

    r = requests.post(url=URL , data=json_data)

    data = r.json()

    print(data)


# UPDATE
def update_data():
    data = {
    'id' : 4,
    'name': "ali naqi khan",
    'roll' : 32,
    'city' : 'lahore'
}

    json_data = json.dumps(data)

    r = requests.put(url=URL , data=json_data)

    data = r.json()

    print(data)


# DELETE
def delete_data():

    data = {'id' : 4}
    json_data = json.dumps(data)
    r = requests.delete(url=URL , data= json_data)
    data = r.json()
    print(data)

# delete_data()


    
get_data()
# get_data(1)

# create_data()

# update_data()

