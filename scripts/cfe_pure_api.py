import requests


BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    for obj in data:
        print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(dir(r2))
            print(r2.json())
    return data


def create_update():
    new_data = {
        'user': 1,
        'content': 'Another new cool update'
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=new_data)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    
    return r.text

print(create_update())
