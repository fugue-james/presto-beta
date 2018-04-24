try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

import requests

credentials = 'jamesm@fugue.co' + '/token', 'b1aZ2eAuTC6dFtSsIPgV2eqVaXwt6aO3DnSZbqJ1'
session = requests.Session()
session.auth = credentials

params = {
    'query': 'type:ticket status<=pending',    
#    'sort_by': 'created_at',
#    'sort_order': 'asc'
}

url = 'https://fugue.zendesk.com/api/v2/search.json?' + urlencode(params)
response = session.get(url)
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Print the subject of each ticket in the results
data = response.json()
#for result in data['results']:
#     print(result['id'])
#     print('Ticket Subject: '+result['subject'])
#     print('Ticket Description: '+result['description'])

def lambda_handler(event, context):
    for result in data['results']:
        # iD = str(result['id'])
        # print (iD) + ' - ' + (result['subject'])
        numTix = str(len(data['results']))
        returnStr = ("The number of active Support tickets is : " + (numTix))
        return returnStr