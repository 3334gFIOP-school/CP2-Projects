# Character Managment File - Jackson Hauley
from essentials import *
import csv

characters = []

def load_characters(characters):
    with open("CP2-Projects/BattleSystem/characters.csv","r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            characters.update({
                "name":row[0],
                "age":row[1],
                "class":row[2],
                "ability":row[3],
                "super":row[4],
                "level":row[5],
                "xp":row[6],
                "inventory":row[7:]
                               })

def view_character(characters): # Views Characters
    cs()
    found = False
    def print_inventory():
        string2 = []
        for i in x["inventory"]: 
            string2.append(i)
        return "".join(string2)
    name_search = input("Name: ")
    for x in characters:
        if x["name"].lower() == name_search.strip().lower():
            found = True
            print(f"Name: {x["name"]}\nAge: {x["age"]}\nClass: {x["class"]}\nAbility {x["ability"]}\nSuper: {x["super"]}\nLevel: {x["level"]}\nXP: {x["xp"]}\nInventory: {print_inventory()}")
    if found == False:
        print("No character found")
    input("Press enter to continue")

def create_character(characters): # Creates a character
    cs()
    while True:
        name = input("Name: ")
        for x in characters:
            if x["name"].lower() == name.strip().lower():
                input("Name already taken!\nPress enter to continue")
                continue
        break
    age = int_input("Age: ")
    while True:
        classes = int_input("\nCLASSES\n1. Human\n2. Elf\n3. Goblin\n4. Troll\n5. Jackson\n\nClass Number: ")
        if classes == 1: class2 = "Human"
        elif classes == 2: class2 = "Elf"
        elif classes == 3: class2 = "Goblin"
        elif classes == 4: class2 = "Troll"
        elif classes == 5: class2 = "Jackson"
        else:
            print("Invalid input!")
            input("Press enter to continue")
            continue
        break
    while True:
        ability = int_input("\nABILITIES\n1. Heal\n2. Charge\n3. Mega Block\n4. War Cry\n5. Redistillificationalism\n\nAbility Number: ")
        if ability == 1: ability2 = "Heal"
        elif ability == 2: ability2 = "Charge"
        elif ability == 3: ability2 = "Mega Block"
        elif ability == 4: ability2 = "War Cry"
        elif ability == 5: ability2 = "Redistillificationalism"
        else:
            print("Invalid input!")
            input("Press enter to continue")
            continue
        break
    while True:
        super = int_input("\nSUPERS\n1. Mega Heal\n2. Shielded\n3. Crystal Slam\n4. Summon\n5. Undistillificationalism\n\nSuper Number: ")
        if super == 1: super2 = "Mega Heal"
        elif super == 2: super2 = "Shielded"
        elif super == 3: super2 = "Crystal Slam"
        elif super == 4: super2 = "Summon"
        elif super == 5: super2 = "Undistillificationalism"
        else:
            print("Invalid input!")
            input("Press enter to continue")
            continue
        break
    new_character = {
        "name":name,
        "age":age,
        "class":class2,
        "ablilty":ability2,
        "super":super2,
        "level":1,
        "xp":0
    }
    characters.append(new_character)

    with open("CP2-Projects/BattleSystem/characters.csv", "w", newline='') as file:
        fieldnames = characters[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)

    input("Character Created!\nPress enter to continue")