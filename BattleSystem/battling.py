# Battling functions
from characters import *

def battle():
    character1 = input("Name of defending character: ")
    character2 = input("Name of attacking character: ")
    while True:
        if character1.lower().strip() == character2.lower().strip():
            print("Characters cannot be the same!")
            character2 = input("Name of attacking character: ")
        else:
            break
    for x in characters:
        if x["name"].lower().strip() == character1.lower().strip():
            character1 = x
            break
    for x in characters:
        if x["name"].lower().strip() == character2.lower().strip():
            character2 = x
            break
    running = True
    def round():
            cs()
            print(f"{character1["name"]}")
    while running:
        round()
