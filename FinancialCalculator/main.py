# Jackson Hauley - Financial Calculator

'''
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
'''

def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError: 
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output
    
def invalid(): 
    print("Invalid Input!")
    input("Press enter to continue")

def cs(): # Clear Screen
    print("\033c",end="")

def main():
    cs()
    choice = int_input("Financial Calculator\n\n1. Goal Setting\n2. Interest Calculator\n3. Budget Calculator\n4. Sale Price Calculator\n5. Tip Calculator\n\nWhat would you like to do? (1-5): ")
    if choice == 1:
        goal = int_input("How much money do you want to save?: ")
        while True:
            choice2 = input("Do you want to deposit monthly or weekly?: ")
            if choice2 == "monthly": 
                deposit = int_input("How much would you like to deposit monthly?: ")
            elif choice2 == "weekly": 
                deposit = int_input("How much would you like to deposit weekly?: ")
            else:
                invalid()
main()