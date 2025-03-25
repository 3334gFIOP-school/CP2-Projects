# Jackson Hauley - Coin Change Problem - Main File

from filehandling import *
from essentials import *
from change_calculator import *

country = "us" # Default Country
currency = get_money()

def main(): # Main Function
    while True:
        cs() # Clears the screen every iteration
        choice = int_input("Coin Change\n\n1. Get Change\n2. Select Country\n3. Exit\n\nPick one (1-3): ")
        if choice == 1: # Coin Change
            pass
        elif choice == 2: # Country Choice
            cs()
            country_choice = int_input("Select Country\n1. United States\n2. Europe\n3. Cancel\n\nPick one (1-3): ")
            if country_choice == 1: country = "us"
            elif country_choice == 2: country = "eu"
            elif country_choice == 3: continue
            else: print("Invalid Input! Pick a number from 1 to 3!")
        elif choice == 3: # Exits Program
            cs(),print("Bye bye!"),exit()
        else: input("Invalid Input! Pick a number from 1 to 3!\nPress enter to continue")
