import json, os

import requests


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

image_path = os.path.join(os.getcwd(), "readyplayeronejpg.jpg")

headers = {
    "Content-Type": "application/json"
}

data = {
    'username': 'test96',
    'password': 'admin3004'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)


ENDPOINT = "http://127.0.0.1:8000/api/status/15/"


headers2 = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token
}

data2 = {
    'content': 'This is new content post'
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }   
    r = requests.get(ENDPOINT, headers=headers2)
    print(r.text)



# ENDPOINT = "http://127.0.0.1:8000/api/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

# image_path = os.path.join(os.getcwd(), "readyplayeronejpg.jpg")

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNSwidXNlcm5hbWUiOiJ0ZXN0OTYiLCJleHAiOjE1Nzg0MjE3NjksImVtYWlsIjoidGVzdEB0ZXN0OTYuY29tIiwib3JpZ19pYXQiOjE1Nzg0MjE0Njl9.OwigHbcC4WgtUqlA55AyH2_HJx9FJPWD0nSzwN1psfo'
# }

# data = {
#     'username': 'test96',
#     'email': 'test@test96.com',
#     'password': 'admin3004',
#     'password2': 'admin3004'
# }

# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()#['token']
# print(token)



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

