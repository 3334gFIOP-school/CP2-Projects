# Change Calculator - Jackson Hauley

from essentials import *

def calculate_change(country): # Change Calculator
    while True:
        amount = input("Enter the amount of money you want change of: ")
        try:
            amount = float(amount.strip()) 
            amount = round(amount, 2)
            break
        except ValueError: input("Invalid Input! Enter any amount of money (e.g. 19.20, 35000)\nPress enter to continue")
    