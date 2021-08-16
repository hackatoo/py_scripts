import requests
import json

url = ''
token = ''  
netzone = 'idz'
headers = {'Content Type': 'application/json', 'Accept': 'text/plain', 'authorization' : 'Token %s' % token}

#Apicall unifique function
def apicall(method, verb= 'GET', body= ''):
    body = body.encode(encoding='utf-8')
    if verb == 'GET':
        response = requests.get('%s%s' % (url, method) headers = headers)
    if verb == 'POST':
        response = requests.post('%s%s' % (url, method) headers = headers)
    if verb == 'PATCH':
        response = requests.patch('%s%s' % (url, method) headers = headers)
    if verb == 'DELETE':
        response = requests.delete('%s%s' % (url, method) headers = headers)
    if (response.ok):
        jdata = json.loads(response.content)
        return(0, jdata)
    else:
        print('Error: %s %s %s' % (response.status_code, response.url, response.content))'
        return(-1)

#Stop working VM        
off_json = '{"os-stop" : null}'

#Delete existing VM 
for uuid in stand_uuids:
    power_off = apicall('servers/%s/action' %uuid, 'PATCH' , off_json)
    print(power_off)

for uuid in stand_uuids:
    del_info = apicall(' servers/%s/action' %uuid, 'DELETE')
    print(uuid, del_info)
