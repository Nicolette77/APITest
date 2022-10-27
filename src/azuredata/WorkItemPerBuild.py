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
BUILDNUMBER = '9839'
ORGANIZATION_URL = f'https://dev.azure.com/{COLLECTION}/{PROJECT}'
RESOURCE_PATH = f'/_apis/build/builds/{BUILDNUMBER}/workitems?api-version=6.0'
HEADERS = {
    'Authorization': 'Basic %s' % B64USERPASS
}
WorkItemResponse = requests.get(
        ORGANIZATION_URL + RESOURCE_PATH, headers=HEADERS).json()

with open('workItem.json') as workItem_file:
    data = json.load(workItem_file)

WorkItemList = data['value']

DetailFile = open('WorkItemData.csv', 'w')

csv_writer = csv.writer(DetailFile)
# Counter variables used for writing headers to the csv file
count = 0
for workItemId in WorkItemList:
    if count == 0:
        # Writing header to csv
        header = workItemId.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(workItemId.values())

DetailFile.close()
