# Jackson Hauley - Word Counter

from writeandread import *
from essentials import *

# Functions

def main(): # Main function
    while True:
        cs()
        choice = int_input("Word Counter\n\n1. Write to file\n2. Read from file\n3. Exit\n\nWhat would you like to do? (1-3): ")
        if choice == 1: # Write to file
            write()
        elif choice == 2: # Read from file
            read()
        elif choice == 3: # Exit
            cs()
            print("Thanks for using Jacksons Amazing Word Counter!")
            exit()
        else:
            input("Invalid Input!\nPress enter to continue")
