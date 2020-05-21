import requests
import os


url = "http://127.0.0.1:8000/api/v0/tag/"
TAG = '97/'
URL_GET_TOKEN = "http://127.0.0.1:8000/api_token/"
# auth = ('___', '_____')
#
# response = requests.get(URL_GET_TOKEN, auth=auth)
# print(response.status_code)

'''
curl -X POST -d "username=_____&password=_________" http://127.0.0.1:8000/api_token/
'''

# auth = ('___', '___')
# response = requests.delete(url, auth=auth)
# print(response.status_code)

URL = 'http://127.0.0.1:8000/api/test_drive/v0/pushkin/970/'
URL = 'http://127.0.0.1:8000/api/test_drive/v0/akhmadulina/1975/'
URL = 'http://127.0.0.1:8000/api/test_drive/v0/lermontov/1596/'


TOKEN = '8d1d971216b22ac28bd51b85c7d603ae5fe900a3'
headers = {'Authorization': f'Token {TOKEN}'}
response = requests.get(URL, headers=headers)
print(response.text)
