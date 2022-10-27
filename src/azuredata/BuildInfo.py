import base64
import json
import requests
import csv

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
BuildResponse = requests.get(
        ORGANIZATION_URL + RESOURCE_PATH, headers=HEADERS).json()

with open('buildInfo.json', 'w') as output_file:
    json.dump(BuildResponse, output_file)
print(output_file)

with open('buildInfo.json') as input_file:
    data = json.load(input_file)

BuildInfoList = []

for item in data['value']:
    buildId = item['id']
    buildNumber = item['buildNumber']
    definitionId = item['definition']['id']
    definitionName = item['definition']['name']
    startTime = item['startTime']
    status = item['status']

    BuildInfo_item = {
        'id': buildId,
        'buildNumber': buildNumber,
        'definitionId': definitionId,
        'definitionName': definitionName,
        'startTime': startTime,
        'status': status
        }
    BuildInfoList.append(BuildInfo_item)
print(BuildInfoList)

csv_data = BuildInfoList
out = csv.writer(open('BuildInfoData.csv', 'w'), delimiter=';', quoting=csv.QUOTE_ALL)
out.writerow(csv_data)
