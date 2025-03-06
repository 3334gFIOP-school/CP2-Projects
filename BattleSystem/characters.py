# Character Managment File - Jackson Hauley
from essentials import *

characters = []

def load_characters(characters):
    pass


def create_character(characters): # Creates a character
    cs()
    name = input("Name: ")
    age = int_input("Age: ")
    classes = int_input("\nCLASSES\n1. Human\n2. Elf\n3. Goblin\n4. Troll\n5. Jackson\n\nClass Number: ")
    if classes == 1: class2 = "Human"
    elif classes == 2: class2 = "Elf"
    elif classes == 3: class2 = "Goblin"
    elif classes == 4: class2 = "Troll"
    elif classes == 5: class2 = "Jackson"
    ability = int_input("\nABILITIES\n1. Heal\n2. Charge\n3. Mega Block\n4. War Cry\n5. Redistillificationalism\n\nAbility Number: ")
    if ability == 1: ability2 = "Heal"
    elif ability == 2: ability2 = "Elf"
    elif ability == 3: ability2 = "Goblin"
    elif ability == 4: ability2 = "Troll"
    elif ability == 5: ability2 = "Jackson"
    super = int_input("\nSUPERS\n1. Mega Heal\n2. Shielded\n3. Crystal Slam\n4. Summon\n5. Undistillificationalism\n\nAbility Number: ")
    if super == 1: super2 = "Mega Heal"
    elif super == 2: super2 = "Shielded"
    elif super == 3: super2 = "Crystal Slam"
    elif super == 4: super2 = "Summon"
    elif super == 5: super2 = "Undistillificationalism"
    characters.append({
        "name":name,
        "age":age,
        "class":class2,
        "abliity":ability2,
        "super":super2
    })


