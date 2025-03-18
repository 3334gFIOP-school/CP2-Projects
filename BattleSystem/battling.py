# Battling functions
from characters import *
from characters import *

def battle(): # Starts the battle
    character1 = input("Name of defending character: ")
    character2 = input("Name of attacking character: ")
    while True:
        if character1.lower().strip() == character2.lower().strip():
            print("Characters cannot be the same!")
            character2 = input("Name of attacking character: ")
        else:
            break
    check = False
    for x in characters:
        if x["name"].lower().strip() == character1.lower().strip():
            character1 = x
            check = True
            break
    if check == False:
        input("Character not found, press enter to continue")
        return False
    check = False
    for x in characters:
        if x["name"].lower().strip() == character2.lower().strip():
            character2 = x
            check = True
            break
    if check == False:
        input("Character not found, press enter to continue")
        return False

    def check_death(): # Checks if any1 died
        if int(character1["health"]) <= 0 or int(character2["health"]) <= 0:
            going = False
            running = False
            return True
    running = True
        
    def use_power(character,power): # This returns what a power does
        if power == 1: # Super
            if character["super"] == "Mega Heal":
                return "heal",200
            elif character["super"] == "Shielded":
                return "block",300
            elif character["super"] == "Crystal Slam":
                return "block",300
            elif character["super"] == "Summon":
                return "attack",100
            elif character["super"] == "Undistillificationalism":
                return "power",500
        elif power == 2: # Ability
            if character["ability"] == "Heal":
                return "heal",100
            elif character["ability"] == "Charge":
                return "attack",50
            elif character["ability"] == "Mega Block":
                return "block",50
            elif character["ability"] == "War Cry":
                return "attack",100
            elif character["ability"] == "Redistillificationalism":
                return "power",300
            
    def round(): # THIS WHOLE CHUNK IS THE ATTACKING SYSTEM, AND IT IS ALL SELF EXPLANATORY SO IT DOESNT NEED COMMENTS
            cs()
            going = True
            while going:
                print(f"{character1["name"]} is attacking {character2["name"]}!")
                while True:
                    choice = int_input("1. Normal Attack\n2. Use Ability\n3. Use Super\nWhat to do: ")
                    if choice == 1:
                        character2["health"] = int(character2["health"])-20
                        print(f"{character1["name"]} attacked {character2["name"]} for 20 damage!")
                        break
                    elif choice == 2:
                        type,amount = use_power(character1,2)
                        if type == "heal":
                            character1["health"] = int(character1["health"])+amount
                            print(f"{character1["name"]} Healed {amount}")
                        elif type == "attack":
                            character2["health"] = int(character2["health"])-amount+char2block
                            char2block = 0
                            print(f"{character1["name"]} attacked {character2["name"]} for {amount} damage!")
                        elif type == "block":
                            char1block = amount
                        elif type == "power":
                            character2["health"] = int(character2["health"])-amount+char2block
                            char2block = 0
                            print(f"{character1["name"]} attacked {character2["name"]} for {amount} damage!")
                            character1["health"] = int(character1["health"])+amount
                            print(f"{character1["name"]} Healed {amount}")
                            char1block = amount
                        break
                    elif choice == 2:
                        type,amount = use_power(character1,1)
                        if type == "heal":
                            character1["health"] = int(character1["health"])+amount
                            print(f"{character1["name"]} Healed {amount}")
                        elif type == "attack":
                            character2["health"] = int(character2["health"])-amount+char2block
                            char2block = 0
                            print(f"{character1["name"]} attacked {character2["name"]} for {amount} damage!")
                        elif type == "block":
                            char1block = amount
                        elif type == "power":
                            character2["health"] = int(character2["health"])-amount+char2block
                            char2block = 0
                            print(f"{character1["name"]} attacked {character2["name"]} for {amount} damage!")
                            character1["health"] = int(character1["health"])+amount
                            print(f"{character1["name"]} Healed {amount}")
                            char1block = amount
                        break
                    else:
                        continue
                if check_death():
                    print("Character 1 Won!")
                    character1["xp"] = character1["xp"]+10
                    character1["level"] = character1["level"]+1
                    break
                print(f"{character2["name"]} is attacking {character1["name"]}!")
                while True:
                    choice = int_input("1. Normal Attack\n2. Use Ability\n3. Use Super\nWhat to do: ")
                    if choice == 1:
                        character1["health"] = int(character1["health"])-20
                        print(f"{character2["name"]} attacked {character1["name"]} for 20 damage!")
                        break
                    elif choice == 2:
                        type,amount = use_power(character2,2)
                        if type == "heal":
                            character2["health"] = int(character2["health"])+amount
                            print(f"{character2["name"]} Healed {amount}")
                        elif type == "attack":
                            character2["health"] = int(character2["health"])-amount+char1block
                            char1block = 0
                            print(f"{character2["name"]} attacked {character1["name"]} for {amount} damage!")
                        elif type == "block":
                            char2block = amount
                        elif type == "power":
                            character1["health"] = int(character1["health"])-amount+char1block
                            char1block = 0
                            print(f"{character2["name"]} attacked {character1["name"]} for {amount} damage!")
                            character2["health"] = int(character2["health"])+amount
                            print(f"{character1["name"]} Healed {amount}")
                            char2block = amount
                        break
                    elif choice == 2:
                        type,amount = use_power(character2,1)
                        if type == "heal":
                            character2["health"] = int(character2["health"])+amount
                            print(f"{character2["name"]} Healed {amount}")
                        elif type == "attack":
                            character2["health"] = int(character2["health"])-amount+char1block
                            char1block = 0
                            print(f"{character2["name"]} attacked {character1["name"]} for {amount} damage!")
                        elif type == "block":
                            char2block = amount
                        elif type == "power":
                            character1["health"] = int(character1["health"])-amount+char1block
                            char1block = 0
                            print(f"{character2["name"]} attacked {character1["name"]} for {amount} damage!")
                            character2["health"] = int(character2["health"])+amount
                            print(f"{character2["name"]} Healed {amount}")
                            char2block = amount
                        break
                    else:
                        continue
                if check_death():
                    print("Character 2 Won!")
                    character2["xp"] = character2["xp"]+10
                    character2["level"] = character2["level"]+1
                    break

    while running:
        round()

    character1["health"] = 100+(character1["level"]*10) # Restoring Health
    character2["health"] = 100+(character2["level"]*10)

    with open("CP2-Projects/BattleSystem/characters.csv", "w", newline='') as file: # Saving the new characters stats
        fieldnames = characters[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)
