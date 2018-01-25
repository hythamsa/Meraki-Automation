# Meraki-Automation
A collection of scripts automating the Meraki Dashboard

# multi-org-inventory.py
Reaches out to the Meraki Dashboard collecting inventory on each Organization you are permitted access into and then dumping the data into a CSV file. A secondary support python script ( input.py ... or whatever you'd like to name it, but be sure to modify the relevant import line under def main(): ) is used for authentication purposes. 

There is only one line in input.py in the format of:
EG. key = '<your Meraki API key here'

For now the script collects Organization Name, Organization ID, Model, Serial and MAC addresses. This will be expanded upon to further include additonal data over time.
