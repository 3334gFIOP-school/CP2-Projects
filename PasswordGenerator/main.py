# Jackson Hauley - Password Generator

import random
import time

num = 1234567890
symbol = "!@#$%^&*_-"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
current_pass = N/A

def main():
    cs()
    choice = int_input(f"Password Generator\nCurrent password: {current_pass}\n\n1. Generate Password\n 2. Test Password\n 3. Exit\n\nWhat do you want to do? (1-3): ")
    if choice == 1:
        cs()
        print("Generate Password")
        global length
        length = int_input("How long of a password do you want?: ")
        global password
        password = []
        for x in range(length):
            password.append("")
        while True:
            pass_choice = input("Do you want capital letters in your password? (y/n): ")
            if pass_choice == "y":
                capital = "yes"
                password = add_capital(password)
                break
            else: continue
        while True:
            pass_choice = input("Do you want symbols in your password? (y/n): ")
            if pass_choice == "y":
                symbol = "yes"
                password = add_symbol(password)
                break
            else: continue
        number = "no"
        symbol = "no"
        lowercase = "no"
        capital = "no"
        while True:
            pass_choice = input("Do you want numbers in your password? (y/n): ")
            if pass_choice == "y":
                number = "yes"
                password = add_num(password)
                break
            else: continue
        while True:
            pass_choice = input("Do you want lowercase letters in your password? (y/n): ")
            if pass_choice == "y":
                lowercase = "yes"
                password = add_lowercase(password)
                break
            else: continue
        while "" in password:
            rand = random.randint(1,4)
            if rand == 1 and lowercase == "yes": password = add_lowercase(password)
            elif rand == 2 and number == "yes" : password = add_num(password)
            elif rand == 3: symbol == "yes" = add_symbol(password)
            elif rand == 4: capital == "yes" = add_capital(password)
            else: continue
        current_pass = assemble()
        print(f"Your generated password was {final_pass}!")
        print(f"Capitals: {capital}")
        print(f"Symbols: {symbol}")
        print(f"Numbers: {number}")
        print(f"Lowercases: {lowercase}")
        print(f"Length: {length} characters")
        input("Press enter to continue")
        
        
        


def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError: 
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output

def cs(): # Clear Screen
    print("\033c",end="")

def check_length():
    pass

def add_num(password):
    location = random.randint(0,length-1)
    password.pop(location)
    password.insert(location,random.choice(num))
    return password
    
def add_symbol(password):
    location = random.randint(0,length-1)
    password.pop(location)
    password.insert(location,random.choice(symbol))
    return password

def add_capital(password):
    location = random.randint(0,length-1)
    password.pop(location)
    password.insert(location,random.choice(capital))
    return password

def add_lowercase(password):
    location = random.randint(0,length-1)
    password.pop(location)
    password.insert(location,random.choice(lower))
    return password

def assemble():
    global password
    output = "".join(password)
    return output



main()
