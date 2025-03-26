# Jackson Hauley - Coin Change Problem - Main File

from filehandling import *
from essentials import *
from change_calculator import *

def main(): # Main Function
    while True:
        cs() # Clears the screen every iteration
        choice = int_input("Coin Change\n\n1. Get Change\n2. Exit\n\nPick one (1-2): ")
        if choice == 1: # Coin Change
            calculate_change() # Coin change function
        elif choice == 2: # Exits Program
            cs(),print("Bye bye!"),exit()
        else: input("Invalid Input! Pick a number from 1 to 2!\nPress enter to continue")

main()