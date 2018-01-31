import sys
import csv

def get_message_type(argument):
    switcher = {
        'I': 'Info',
        'W': 'Warning',
        'E': 'Error',
        'S': 'Security'
    }
    return switcher.get(argument, 'Null')

def main(argv):

    if (len(argv) != 2 and len(argv) != 3):
        print('Invalid number of arguments.\nUsage:', argv[0], 'SW1 SW2(optional)')
        return 0

    with open('apdu_responses.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            if (row[0] == argv[1]):
                if (len(argv) == 2 and (row[1]=='--')) or (row[1] == argv[2] or row[1] == 'XX'):
                    print('Type:', get_message_type(row[2]))
                    print('Description:', row[3])
                    return 0

    print('Response codes not found.')

main(sys.argv)