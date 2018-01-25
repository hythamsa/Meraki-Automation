# Meraki-Automation
A collection of scripts automating the Meraki Dashboard

# multi-org-inventory.py (Python 2.x)
Reaches out to the Meraki Dashboard collecting inventory on each Organization you are permitted access into and then dumping the data into a CSV file. A secondary support python script ( input.py ... or whatever you'd like to name it, but be sure to modify the relevant import line under def main(): ) is used for authentication purposes. 

There is only one line in input.py in the format of:
EG: key = '<your Meraki API key here'

For now the script collects Organization Name, Organization ID, Model, Serial and MAC addresses. This will be expanded upon to further include additonal data over time.

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
