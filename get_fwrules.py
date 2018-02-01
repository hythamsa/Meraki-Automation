import csv, json, requests, datetime, sys

try:
    import input
    key = input.key
    org_name = input.org_name
    net_name = input.net_name
except ImportError:
    print('Looks like there was an error inputting your variables. Please enter the correct information now: ')
    key = str(raw_input('Enter your Meraki API key: '))
    org_name = str(raw_input('Enter the organization name you would like to search: '))
    net_name = str(raw_input('Enter the network name you are searching for: '))
except AttributeError:
    print('Looks like there was an error inputting your variables. Please enter the correct information now: ')
    key = str(raw_input('Enter your Meraki API key: '))
    org_name = str(raw_input('Enter the organization name you would like to search: '))
    net_name = str(raw_input('Enter your network name you are searching for: '))

head = {
        'content-type': 'application/json',
        'x-cisco-meraki-api-key': key
        }

today = datetime.date.today()
baseuri = 'https://api.meraki.com/api/v0/'

def getorgid():
    try:
        getorgid = json.loads(requests.get(baseuri + 'organizations/',headers=head).content)

        for orgname in getorgid:
            if orgname['name'] == org_name:
                return orgname['id']
    except:
        sys.exit(2)


def getnetid():
    try:
        getnetid = json.loads(requests.get(baseuri + 'organizations/' + `orgid` + '/networks/',headers=head).content)

        for netname in getnetid:
            if netname['name'] == net_name:
                return netname['id']
    except:
        sys.exit(2)



if __name__ == '__main__':
    orgid = getorgid()
    netid = getnetid()


        # Define CSV file write paramters
    with open (net_name + '_' 'FWRules_' + str(today) + '.csv', 'w') as csvfile:
        fieldnames = ['Comment', 'Policy', 'Protocol(s)', 'Source Port(s)', 'Source Address(es)', 'Destination Port(s)', 'Destination Address(es)', 'Syslog']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    # Grab firewall rules
        getfwrules = json.loads(requests.get(baseuri + 'networks/' + netid + '/l3FirewallRules/',headers=head).content)

        for i in getfwrules:
            comment = i['comment']
            policy = i['policy']
            protocol = i['protocol']
            destport = i['destPort']
            destcidr = i['destCidr']
            srcport = i['srcPort']
            srccidr = i['srcCidr']
            syslog = i['syslogEnabled']

            writer.writerow({'Comment': comment, 'Policy': policy, 'Protocol(s)': protocol, 'Source Port(s)': srcport, 'Source Address(es)': srccidr, 'Destination Port(s)': destport, 'Destination Address(es)': destcidr, 'Syslog': syslog})
