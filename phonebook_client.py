
#%%

import requests

def myphonebook():
    request = requests.get("http://127.0.0.1:5000/myphonebook")
    return request.json()


def add_contact(name,phone):
    
    request = requests.put("http://127.0.0.1:5000/add-contact/{}/{}".format(name,phone))
    return request.json()


def get_phone(name):
    request = requests.get("http://127.0.0.1:5000/get-phone/{}".format(name))
    return request.json()


def delete_phone(name):
    request = requests.delete("http://127.0.0.1:5000/delete-phone/{}".format(name))
    return request.json()


def update_phone(name, phone):
    request = requests.post("http://127.0.0.1:5000/update-phone/{}/{}".format(name,phone))
    return request.json()
