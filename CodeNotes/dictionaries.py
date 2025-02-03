# Jackson Hauley - Dictionaries

car = {
    "Make": ["Ford","Chevy","Toyota","Honda","Tesla","Volkswagen"], # Can contain lists and you can do car["Make"][2] to index lists
    "Model": "Escape xlt",
    "Year": 2008,
    "Color": 'Red', # Dont forget the comma
    "Name": "Freya"
}

 # print(car["Make"])

students = { # Dictionary with dictionaries in it PERIOD, SEAT, then it gives their name
    "first": {
        1: 'Vincent',
        2: 'Cecily',
        3: 'Evan',
        4: 'Sawyer',
        5: 'Alisha'
    },
    "sixth": {
        1: 'Nicole',
        2: 'Luke',
        3: 'Gavin',
        4: 'Jackson'
    }
}

# print(students["sixth"][2]) # Using a key from in a dictionary

# print(car.keys) this prints all the keys of a dictionary 

# print(car.get("Make"))

# car.popitem() pops the item in it from any item

# The add version of a dictionary, and it already exists then it will return the value car.setdefault("drive",2)
