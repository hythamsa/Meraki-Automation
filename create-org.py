import sys, json, requests, csv, datetime


def readme():
    print("*************************************************************************************************************************")
    print("")
    print("Create an orgnization or multiple organizations by reading input from a CSV file named "org.csv")
    print("")
    print("Prior to script execution please be sure to correctly fill in the "with open" statement with the correct name of your csv")
    print("The CSV file must be located in the same working directory as the python script to execute properly.")
    print("If you disire to change the location of the CSV, please be sure to reflect this change in the script.")
    print("")
    print("*************************************************************************************************************************")


try:
    import input
    key = input.key
except ImportError:
    key = str(raw_input('Enter your Meraki API key: '))
except AttributeError:
    key = str(raw_input('Enter your Meraki API key: '))


head = {
        'Content-type': 'application/json',
        'x-cisco-meraki-api-key': key
        }

baseuri = "https://api.meraki.com/api/v0/organizations/"


def main():
    try:

        orgs = []
        with open('org.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                orgs.append(row)

        for i in orgs:
            create = requests.post(baseuri,data=json.dumps(i),headers=head)
            print create.status_code
            print create.content

    except:
        sys.exit(readme())



if __name__ == '__main__':
    main()
