import base64
import json
import requests
import csv

# API Get(....
with open('C:/Users/NicolettevandenHeeve/PycharmProjects/APITest/src/azuredata/ado_pat.txt', 'r') as file:
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

with open('buildDetail.json') as build_file:
    data = json.load(build_file)

BuildList = data['value']

BuildFile = open('BuildInfoData.csv', 'w')

csv_writer = csv.writer(BuildFile)

count = 0
for buildItem in BuildList:
    if count == 0:
        header = buildItem.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(buildItem.values())

BuildFile.close()
