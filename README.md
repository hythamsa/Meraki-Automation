# Meraki-Automation
A collection of scripts automating the Meraki Dashboard

# multi-org-inventory.py (Python 2.x)
Reaches out to the Meraki Dashboard collecting inventory on each Organization you are granted access and then dumping the data into a CSV file. A secondary support python script ( input.py ... or whatever you'd like to name it, but be sure to modify the relevant import line under def main(): ) is used for authentication purposes to fully automate the data collection.

There is only one line in input.py in the format of:
- EG: key = '<your Meraki API key here'

Once the above has been configured, the script will then collect and output the following:

- Organization Name, Organization ID, Model, Serial, MAC addresses, Licensed Devices (count), Expiration and Status.

# create-org.py (Python 2.x)
An incredibly rudimentary (v0.1) script written to create new organizations within the Meraki dashboard. For now the script accepts a JSON formatted input file (orgID.json) with multiple key:value pairings.

EG:
[
        {
                "name": "org-test1"
        },
        {
                "name": "org-test2"
        },
        {
                "name": "org-test3"
        }
]

create-org.py leverages a secondary input.py script that houses your Meraki API key which is used to authenticate you for API use.

There is only one line found within input.py in the format of:
- key = 'your Meraki API key here'

Revisions actively being made:
- read input from a CSV file
- create Orgs, retrieve Org IDs
- create VLANS, assign ports to VLANs, create firewall rules

# get_fwrules.py (Python 2.x)

Retrieve firweall rules from an organization and an associated network to be dumped into a CSV file.

A secondary support file (input.py) accepts the following parameters:
- key = Meraki API Key
- org_name = Organization Name where network resides (This is case sensitive!)
- net_name = Network Name to retrieve (This is case sensitive!)

If you do not wish to define the variables into the file, input validation is performed and will kick it back to a raw_input prompting the user for required information.

# push_fwrules.py (Python 2.x)
Automate the deployment of a single organization and a single network via a user generated CSV file. A supplied example CSV file has been provided to better understand the data required for a successful deployment. Please note that the organization name AND the network name are case sensitive and MUST be typed exactly as they are found within your Meraki Dashboard... this is where the additional error handling will come in to play.

Like the other Python scripts I have written, a secondary support python script holding your authorization is required.

There is only one line found within input.py in the format of:
- key = 'your Meraki API key here'

If you do not wish to use this file, you may comment out the following lines of code by enclosing them with ''' like so:

'''
try:
    import input
    key = input.key
except ImportError:
    key = str(raw_input('Enter your Meraki API key: '))
except AttributeError:
    key = str(raw_input('Enter your Meraki API key: '))
'''

Be sure to modify the "head" variable and input your Meraki API key.

head = {
        'content-type': 'application/json',
        'x-cisco-meraki-api-key': <PUT YOUR MERAKI API KEY HERE>
        }


Future revisions will include:
- Multi organization and multi network deployments
- Improved error handling







