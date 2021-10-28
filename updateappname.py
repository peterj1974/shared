import json
import requests

## Variables
host=morpheus['morpheus']['applianceHost']
token=morpheus['morpheus']['apiAccessToken']
foundinstance=""
foundapp=""

## Request headers
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}

## Functions
def makeGetRequest(endpoint, headers):
    method = 'get'
    r = getattr(requests, method)(
        endpoint,
        headers = headers,
        verify = False
        )
    return json.loads(r.text)
    
def makePutRequest(endpoint, headers, payload):
    method = 'put'
    r = getattr(requests, method)(
        endpoint,
        headers = headers,
        verify = False,
        data = payload
        )
    return json.loads(r.text)
    
## Get instance name
instname = morpheus['instance']['name']

## Test instance name is QASP server
result = instname.startswith('QASP')
if result == True:
    apiUrl = 'https://%s/api/apps?type=morpheus' % (host)
    try:
        ## API call to GET list of Morpheus apps
        apps=makeGetRequest(apiUrl, headers)
    except:
        print(apps)
        sys.exit("Attempting to get apps")

## Iterate through list of apps to find app that contains instname, and then get the appid that it belongs to
    for app in apps["apps"]:
        for tier in app["appTiers"]:
            for ins in tier["appInstances"]:
                instnamenew = ins["instance"]["name"]
                if instnamenew == instname:
                    foundinstance=instnamenew
                    foundapp=app["id"]
    
    ## If we find an instance and app id, update the app name to be the same as the instance name
    if foundinstance != "" and foundapp != "":
        print(foundinstance,foundapp)
        apiUrl = 'https://%s/api/apps/%s' % (host, foundapp)
        print(apiUrl)
        appBody = {
            "app": {
                "name": foundinstance
                }
            }
        try:    
            updateappname=makePutRequest(apiUrl, headers, json.dumps(appBody))
        except:
            print(updateappname)
            sys.exit("Attempting to update app name")
