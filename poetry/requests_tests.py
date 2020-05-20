import requests
import os


url = "http://127.0.0.1:8000/api/v0/tag/"
TAG = '5/'


# auth = ('___', '___')
# response = requests.delete(url, auth=auth)
# print(response.status_code)



TOKEN = 'f6751669f207ac95ccedbadaf0d6f8ca1d6aeb3f'
headers = {'Authorization': f'Token {TOKEN}'}
response = requests.delete(os.path.join(url, TAG), headers=headers)
print(response.status_code)