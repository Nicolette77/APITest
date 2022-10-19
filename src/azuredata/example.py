import base64
import csv
import json
import pandas as pd
import requests
from requests import Response
import pprint as pp

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

try:
    ADO_RESPONSE: Response = requests.get(
        ORGANIZATION_URL + RESOURCE_PATH, headers=HEADERS)

    # pp.pprint(ADO_RESPONSE)
    # pp.pprint(ADO_RESPONSE.text)
    ADO_RESPONSE.raise_for_status()
except requests.exceptions.HTTPError as err:
    pp.pprint(err)

# with open('output.json') as file:
#     for line in file:
#         print(line.rstrip())

with open('output.json') as output:
    output = json.load(output)
    # build_data = output['value']
    print(output['value'][0]['id'])
    print(output['value'][0]['buildNumber'])
    print(output['value'][0]['definition']['name'])
    print(output['value'][0]['startTime'])
    print(output['value'][0]['finishTime'])
    # file.write(json.dumps(output.json(), indent=4))
    # file.close()
    BuildInfoData = open('BuildInfoData.csv', 'w')
    csv_writer = csv.writer(open('BuildInfoData.csv', 'w'))

    count = 0
    for item in output:
        if count == 0:
            header = output.keys()
            csv_writer.writerow(header)
            count += 1
    csv_writer.writerow(output.values())
BuildInfoData.close()

