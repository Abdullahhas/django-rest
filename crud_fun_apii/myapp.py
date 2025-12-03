import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

#READ
def get_data(id = None):
    data = {}
    if id is not None:

        data = {'id' : id}
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r = requests.get(url=URL , headers= headers , data=json_data)

    data = r.json()

    print(data)




#WRITE
def create_data():

    data = {
    'name': "zaidy",
    'roll' : 15,
    'city' : 'shkp'
}

    json_data = json.dumps(data)

    headers = {'content-Type' : 'application/json'}
    r = requests.post(url=URL , headers= headers,  data=json_data)

    data = r.json()

    print(data)


# UPDATE
def update_data():
    data = {
    'id' : 3,
    'name': "zaidy mughal",
    'roll' : 16,
    'city' : 'shkp'
}

    json_data = json.dumps(data)

    headers = {'content-Type' : 'application/json'}
    r = requests.put(url=URL , headers= headers,  data=json_data)

    data = r.json()

    print(data)


# DELETE
def delete_data():

    data = {'id' : 4}
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r = requests.delete(url=URL , headers= headers,  data=json_data)
    data = r.json()
    print(data)

delete_data()


    
# get_data(2)
# get_data(1)

# create_data()

# update_data()

