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


def getorgname():
    try:

        # Open CSV, retrieve org/net name, and get org ID
        with open('firewall-rules.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return row['org name']
    except:
        sys.exit(2)


def getorgid():
    try:
        getorgid = json.loads(requests.get(baseuri + 'organizations/', headers=head).content)

        for org in getorgid:
            if org['name'] == orgname:
                return org['id']
    except:
        sys.exit(2)


def getnetname():
    try:
        with open('firewall-rules.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return row['network name']
    except:
        sys.exit(2)


def getnetid():
    try:
        getnetid = json.loads(requests.get(baseuri + 'organizations/' + `orgid` + '/networks/',headers=head).content)

        for net in getnetid:
            if net['name'] == netname:
                return net['id']
    except:
        sys.exit(2)


def pushfwrules():
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


if __name__ == '__main__':
    orgname = getorgname()
    orgid = getorgid()
    netname = getnetname()
    netid = getnetid()

    pushfwrules()
