
import requests
import json


url = 'https://www.random.org/quota/'

params = {'format': 'plain'}

response = requests.get(url, params=params)


print(response.json())


url = 'https://www.random.org/quota/'
params = {'ip': '134.226.36.80', 'format': 'plain'}

response = requests.get(url, params=params)
print(response.json())


url = 'https://www.virustotal.com/vtapi/v2/file/scan'

params = {
    'apikey': '7286be80269965ada62cf29801212542466967cb216655985be01b7e2cec68ab'}

files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}


response = requests.post(url, files=files, params=params)
print(response.json())
