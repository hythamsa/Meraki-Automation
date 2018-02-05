import json, requests, json, sys, csv

try:
    import input
    key = input.key
except ImportError:
    key = str(raw_input('Enter your Meraki API key: '))
except AttributeError:
    key = str(raw_input('Enter your Meraki API key: '))

baseuri = 'https://api.meraki.com/api/v0/'

head = {
        'content-type': 'application/json',
        'x-cisco-meraki-api-key': key
        }


# Read CSV file to obtain parameters to be passed to API
with open('firewall-rules.csv', 'r')as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        orgname = row['org name']
        netname = row['network name']
        

        # Obtain Org ID for each organization defined in CSV
        getorgid = json.loads(requests.get(baseuri + 'organizations/',headers=head).content)


        for org in getorgid:
            if org['name'] == orgname:
                orgid = org['id']


# Obtain Network ID for each network name defined in CSV
getnetid = json.loads(requests.get(baseuri + 'organizations/' + `orgid` + '/networks/',headers=head).content)

for net in getnetid:
    if net['name'] == netname:
        netid = net['id']

# Push security policy to device

try:
    data = []
    with open('firewall-rules.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
            
    pushpolicy = requests.put('https://api.meraki.com/api/v0/networks/%s/l3FirewallRules/' % netid, headers=head, data=json.dumps({'rules': data})) 
    print pushpolicy.status_code
    print pushpolicy.content
except:
    sys.exit(2)
