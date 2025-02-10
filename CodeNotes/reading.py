# Reading Files Notes - Jackson Hauley

import csv

# TEXT FILES COME THROUGH AS STRINGS

file = open("CodeNotes/test.txt","r").read()
print(file)

with open("CodeNotes\Class CSV sample - Sheet1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)