import base64
import json
import pprint as pp
import requests
from requests import Response

# API Get(....
with open('ado_pat.txt', 'r') as file:
    PERSONAL_AUTHENTICATION_TOKEN = file.read().replace('\n', '')

USERNAME = ""
USER_PASS = USERNAME + ":" + PERSONAL_AUTHENTICATION_TOKEN
B64USERPASS = base64.b64encode(USER_PASS.encode()).decode()

COLLECTION = 'atworkiss'
PROJECT = 'AW6'
ORGANIZATION_URL = f'https://dev.azure.com/{COLLECTION}/{PROJECT}'
RESOURCE_PATH = '/_apis/build/builds?api-version=6.0'
HEADERS = {
    'Authorization': 'Basic %s' % B64USERPASS
}

Response = requests.get(
        ORGANIZATION_URL + RESOURCE_PATH, headers=HEADERS).json()

with open('ouput.json', 'w') as output_file:
    json.dump(Response, output_file)
print(output_file)