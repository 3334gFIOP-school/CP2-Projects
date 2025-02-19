# Writing Notes - Jackson Hauley

import csv

"""
r = to read the file
w = write on the file (REPLACES OLD CONTENT)
w+ = read and write
a = append (does not delete)
x = create a file
a+ = append and read (creates file if it doesnt exist)
"""

# This is for writing to a text file

#with open("CodeNotes/test.txt","w") as file:
#    file.write("Computer science is the best!\nEspecially Programming Classes")
    
data = [
    {"username":"larose","color":"blue"},
    {"username":"maxwell","color":"green"},
    {"username":"kode_runner","color":"orange"}
]

data2 = [
    {"username":"larose2","color":"blue2"},
    {"username":"maxwell2","color":"green2"},
    {"username":"kode_runner2","color":"orange2"}
]

with open("CodeNotes/Class CSV sample - Sheet1.csv","a",newline="") as file:
    fieldnames = ["username","color"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data2)

with open("CodeNotes/Class CSV sample - Sheet1.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"---------\nUsername: {row[0]} \nColor: {row[1]}")