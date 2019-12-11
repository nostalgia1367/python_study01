import csv

with open('parks.csv', 'r') as file:
    reader = csv.reader(file)
    park_list = list(reader)

pprint.pprint(park_list)
