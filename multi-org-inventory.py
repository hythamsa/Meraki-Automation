import csv, sys, json, datetime, requests

try:
    import input
    key = input.key
except ImportError:
    key = str(raw_input('Enter your Meraki API key: '))
except AttributeError:
    key = str(raw_input('Enter your Meraki API key: '))

head = {
        'content-type': 'applicaton/json',
        'x-cisco-meraki-api-key': key
        }

baseuri = 'https://api.meraki.com/api/v0/'
today = datetime.date.today()

def main():
    try:
        # Define CSV file write parameters
        with open ('Inventory_' + str(today) + '.csv', 'w') as csvfile:
            fieldnames = ['Organization Name', 'Organization ID', 'Model', 'Serial', 'MAC', 'Licensed Devices', 'Expiration Date', 'Status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Retrieve Organization Names and IDs
            ret_org_data= json.loads(requests.get(baseuri + 'organizations/',headers=head).content)

            for a in ret_org_data:
                name = a['name']
                orgid = a['id']

                # Retrieve Inventory for the Org ID
                ret_org_inventory = json.loads(requests.get(baseuri + 'organizations/' + `orgid` + '/inventory/',headers=head).content)

                for b in ret_org_inventory:
                    model = b['model']
                    serial = b['serial']
                    mac = b['mac']
                    # Write to CSV File
                    writer.writerow({'Organization Name': name, 'Organization ID': orgid, 'Model': model, 'Serial': serial, 'MAC': mac})


                # Retrieve License Data
                ret_org_lic = json.loads(requests.get(baseuri + 'organizations/' + `orgid` + '/licenseState/',headers=head).content)
                licdev = ret_org_lic['licensedDeviceCounts']
                expdate = ret_org_lic['expirationDate']
                stat = ret_org_lic['status']

                # Write to CSV File
                writer.writerow({'Organization Name': name, 'Licensed Devices': licdev, 'Expiration Date': expdate, 'Status': stat})

    except:
        sys.exit(2)


if __name__ == '__main__':
    main()
