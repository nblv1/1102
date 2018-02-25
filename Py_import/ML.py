from urllib import request


# If you are using Python 3+, import urllib instead of urllib2

import json


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["fuel-type", "curb-weight", "fuel-system"],
                    "Values": [ [ "diesel", "0", "1bbl" ], [ "diesel", "0", "1bbl" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/b479e79fbb794396b12d2bc107652fdc/services/c8f4aed0dbb147a481bbe67678b08d6d/execute?api-version=2.0&details=true'
api_key = 'qb1XKgBA/L1FD9fgHDOq/LXPaIG6ViazWRd1OR10nBFTiW4GSfdAwda0l4B/Nyn6yZFaNoCviddPRt1jcp3WVw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = request.Request(url, body, headers)

try:
    response = request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except HTTPError as error:
    print("The request failed with status code: " + str(error.code))

#Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
print(error.info())

print(json.loads(error.read()))