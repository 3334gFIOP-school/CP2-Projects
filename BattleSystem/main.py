# Jackson Hauley - Battle Simulator

from stats import *
from essentials import *
from characters import *
from battling import *
import random
import time
import os
import keyboard
import matplotlib
import pandas
import faker

with open("CP2-Projects/BattleSystem/characters.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            characters.append(row)

# Main Function
def main(): # Main function that runs a bunch of crap through it
    while True:
        cs()

        choice = int_input("BATTLE SIMULATOR\n\n1. BATTLE\n2. CHARACTER MANAGEMENT\n3. GENERATE CHARACTER\n4. SEE STATS\n5. EXIT\n\nChoose an option: ")
        if choice == 1: # Battle
            battle()
        elif choice == 2: # Character Management Menu
            while True:
                cs()
                choice = int_input("CHARACTER MANAGEMENT\n\n1. Create Character\n2. View Character\n3. Exit\n\nChoose an option: ")
                if choice == 1: # Create Character
                    create_character(characters)
                elif choice == 2: # View Character
                    view_character(characters)
                elif choice == 3: # Exit
                    break
        elif choice == 3: # make a random character
            rand_character(characters)
        elif choice == 4: # See Stats
            pass
        elif choice == 5: # Exits
            cs(),print("Bye"),quit()

main()