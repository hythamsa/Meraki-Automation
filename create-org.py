import sys, json, requests, csv, datetime


def readme():
    print("******************************************************************************************************************")
    print("")
    print("Create an orgnization or multiple organizations by reading input from a JSON file")
    print("")
    print("Prior to script execution please be sure to correctly fill in the orgID.json file with the correct key value pairng")
    print("You will find the necessary file to be modified in the current working directory")
    print("")
    print("******************************************************************************************************************")

if __name__ == '__main__':
    try:
        import input
        key = input.key
    except ImportError:
        key = str(raw_input('Enter your Meraki API key: '))

    head = {
            'Content-type': 'application/json',
            'X-Cisco-Meraki-API-Key': key
           }

    uri = "https://api.meraki.com/api/v0/organizations/"
    data = json.load(open('orgID.json', 'r'))
        
    
    #######################################################
    # Create New Organizations
    #######################################################
    try:
        for i in data:
            org = requests.post(uri,params=i,headers=head)
    except:
        sys.exit(readme())
