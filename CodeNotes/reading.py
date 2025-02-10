# Reading Files Notes - Jackson Hauley

import csv

# TEXT FILES COME THROUGH AS STRINGS

file = open("CodeNotes/test.txt","r").read()

users = {}

with open("CodeNotes\Class CSV sample - Sheet1.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        users.update({row[0]:row[1]})

print(users)