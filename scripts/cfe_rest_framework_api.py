import json, os

import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

image_path = os.path.join(os.getcwd(), "readyplayeronejpg.jpg")

headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE1NzY2ODM4NDIsImVtYWlsIjoidGVzdEB0ZXN0LmNvbSIsIm9yaWdfaWF0IjoxNTc2NjgzNTQyfQ.RAxqE1VofW6jSO804-zQnnEtEBF4SzfGj7JPK4bBpes'
}

data = {
    'username': 'test8',
    'email': 'test@test9.com',
    'password': 'admin3004',
    'password2': 'admin3004'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()#['token']
print(token)



# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token
# }

# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }

#     data = {
#         "content": "Updated description"
#     }

#     post_data = {} #json.dumps({"content": ""})
#     posted_response = requests.put(ENDPOINT + str(21) + "/" , data=data, headers=headers, files=file_data)
#     print(posted_response.text)



# print(token)

# refresh_data = {
#     'token': token
# }

# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()['token']

# print(new_token)

# get_endpoint = ENDPOINT + str(12)
# post_data = json.dumps({"content": "Some random content"})

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers = {
#     'content-type': 'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)

# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(img_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do_img(method='put', data={"id": 14, "user": 1, "content": "Some new content"}, is_json=False, img_path=image_path)



# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do(data={'id':40})

# do(method='delete' ,data={'id':9})

# do(method='put' ,data={'id':1, 'content': 'some cool new content', 'user': 1})

# do(method='post' ,data={'content': 'some hahah cool new content', 'user': 1})

