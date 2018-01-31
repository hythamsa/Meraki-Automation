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
EG: key = '<your Meraki API key here'

Revisions actively being made:
- read input from a CSV file
- create Orgs, retrieve Org IDs
- create VLANS, assign ports to VLANs, create firewall rules

# get_fwrules.py (Python 2.x)

Retrieve firweall rules from an organization and an associated network to be dumped into a CSF file:w
. A secondary support file (input.py) accepts the following parameters:
- key = <Meraki API Key>
- org_name = Organization Name where network resides
- net_name = Network Name to retrieve

If you do not wish to define the variables into the file, input validation is performed and will kick it back to a raw_input for the necessary data. Some additional error correction will be put into place shortly.
