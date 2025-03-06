# Jackson Hauley - Battle Simulator

import random
from essentials import *
from characters import *

# Main Function
def main(): # Main function that runs a bunch of crap through it
    while True:
        cs()
        choice = int_input("BATTLE SIMULATOR\n\n1. BATTLE\n2. INVENTORY\n3. SHOP\n4. CHARACTER MANAGEMENT\n5. EXIT\n\nChoose a stupid option: ")
        if choice == 1: # Battle
            pass
        elif choice == 2: # Inventory Management
            pass
        elif choice == 3: # Shop
            pass
        elif choice == 4: # Character Management Menu
            while True:
                cs()
                choice = int_input("CHARACTER MANAGEMENT\n\n1. Create Character\n2. View Character\n3. Exit\n\nChoose a stupid option: ")
                if choice == 1: # Create Character
                    create_character(characters)
                elif choice == 2: # View Character
                    pass
                elif choice == 3: # Exit
                    pass
        elif choice == 5: # Exits
            cs(),print("Bye"),quit()

main()