import base64
import json
import pprint as pp

import fp as fp
import pandas as pd
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

try:
    ADO_RESPONSE: Response = requests.get(
        ORGANIZATION_URL + RESOURCE_PATH, headers=HEADERS)

    pp.pprint(ADO_RESPONSE)
    pp.pprint(ADO_RESPONSE.text)
    ADO_RESPONSE.raise_for_status()
except requests.exceptions.HTTPError as err:
    pp.pprint(err)

# Read response and write to output.json (Does not write file yet)
with open('output.json', 'w') as ResponseOutput:
    ResponseOutput.write('output.json')
    print(ResponseOutput)

# BuildInformation_list = []
#
# with open('output.json') as BuildInfoCollect:
#     BuildInfo = json.load(BuildInfoCollect)
#     for item in BuildInfo:
#         buildId = item['id']
#         buildNumber = item['buildNumber']
#         buildName = item['definition']['name']
#         startTime = item['startTime']
#         finishTime = item['finishTime']
#
#         BuildInfo = {
#             'id': buildId,
#             'buildNumber': buildNumber,
#             'name': buildName,
#             'startTime': startTime,
#             'finishTime': finishTime
#         }
#     print(data[0])
#     print(ResponseOutput['value'][0]['buildNumber'])
#     print(ResponseOutput['value'][0]['definition']['name'])
#     print(ResponseOutput['value'][0]['startTime'])
#     print(ResponseOutput['value'][0]['finishTime'])
#     file.write(json.dumps(output.json(), indent=4))
#     file.close()
#     BuildInformation_list.append(BuildInfo)
#     BuildInfo = open('BuildInfoData.csv', 'w')
#     csv_writer = csv.writer(open('BuildInfoData.csv', 'w'))
#
#     count = 0
#     for item in ResponseOutput:
#         if count == 0:
#             header = ResponseOutput.keys()
#             csv_writer.writerow(header)
#             count += 1
#     csv_writer.writerow(ResponseOutput.values())
# BuildInfo.close()
