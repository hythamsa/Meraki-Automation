import csv, sys, json, datetime, requests

def main():
    try:
        import input
        key = input.key
    except ImportError:
        key = str(raw_input('Enter your Meraki API Key: '))

    head = {
            'content-type': 'applicaton/json',
            'x-cisco-meraki-api-key': key
            }

    baseuri = "https://api.meraki.com/api/v0/"
    
    try:
        # Define CSV file write parameters
        today = datetime.date.today()
        with open ('Inventory_' + str(today) + '.csv', 'w') as csvfile:
            fieldnames = ['Organization Name', 'Organization ID', 'Model', 'Serial', 'MAC']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Retrieve Organization Names and IDs
            ret_org_data = json.loads(requests.get(baseuri + 'organizations/',headers=head).content)

            for a in ret_org_data:
                name = a['name']
                orgid = a['id']
                
                # Retrieve Inventory for each Org ID
                ret_org_inventory = json.loads(requests.get(baseuri + 'organizations/' + `orgid` + '/inventory/',headers=head).content)

                for b in ret_org_inventory:
                    model = b['model']
                    serial = b['serial']
                    mac = b['mac']
                    writer.writerow({'Organization Name': name, 'Organization ID': orgid, 'Model': model, 'Serial': serial, 'MAC': mac})

    except:
        sys.exit(2)

if __name__ == '__main__':
    main()
