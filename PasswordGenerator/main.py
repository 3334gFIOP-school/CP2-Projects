# Jackson Hauley - Password Generator

import random
import time

num = "1234567890"
symbol = "!@#$%^&*_-"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
current_pass = "N/A"

def main():
    while True:
        cs()
        global current_pass
        try:
            choice = int(input(f"Password Generator\nCurrent password: {current_pass}\n\n 1. Generate Password\n 2. Set Password\n 3. Test Strength\n\nWhat do you want to do? (1-3): "))
        except ValueError:
            print("Only integers accepted")
            input("Press enter to continue")
            cs()

        if choice == 1:
            cs()
            print("Generate Password")
            global length
            length = int_input("How long of a password do you want?: ")
            global password
            password = []
            number = "no"
            symbol = "no"
            lowercase = "no"
            capital = "no"
            for x in range(length):
                password.append("")
            while True:
                pass_choice = input("Do you want capital letters in your password? (y/n): ")
                if pass_choice == "y":
                    capital = "yes"
                    password = add_capital(password)
                    break
                else: break
            while True:
                pass_choice = input("Do you want symbols in your password? (y/n): ")
                if pass_choice == "y":
                    symbol = "yes"
                    password = add_symbol(password)
                    break
                else: break
            
            while True:
                pass_choice = input("Do you want numbers in your password? (y/n): ")
                if pass_choice == "y":
                    number = "yes"
                    password = add_num(password)
                    break
                else: break
            while True:
                pass_choice = input("Do you want lowercase letters in your password? (y/n): ")
                if pass_choice == "y":
                    lowercase = "yes"
                    password = add_lowercase(password)
                    break
                else: break
            while "" in password:
                rand = random.randint(1,4)
                if rand == 1 and lowercase == "yes": password = add_lowercase(password)
                elif rand == 2 and number == "yes" : password = add_num(password)
                elif rand == 3 and symbol == "yes" : password = add_symbol(password)
                elif rand == 4 and capital == "yes": password = add_capital(password)
                else: continue
            current_pass = assemble()
            print(f"\nYour generated password was {current_pass}\n")
            print(f"Capitals: {capital}")
            print(f"Symbols: {symbol}")
            print(f"Numbers: {number}")
            print(f"Lowercases: {lowercase}")
            print(f"Length: {length} characters\n")
            input("Press enter to continue")

        elif choice == 2:
            cs()
            print("Setting password, press enter to cancel")
            choosing_pass = input("Password: ")
            if choosing_pass == "":
                input("Canceled, press enter to continue")
            else:
                confirm = input("Confirm Password: ")
                if choosing_pass == confirm:
                    current_pass = confirm
                    print("Password successfully changed!")
                    input("Press enter to continue")
                else:
                    while choosing_pass != confirm:
                        confirm = input("Confirm Password: ")
                    current_pass = confirm
                    print("Password successfully changed!")
                    input("Press enter to continue ")

        elif choice == 3:
            hash = ["-","-","-","-","-","-","-","-","-","-"]
            for x in range(10):
                cs()
                printhash = "".join(hash)
                hash.pop(x)
                hash.insert(x,"#")
                print(f"[{printhash}]")
                time.sleep(1)
            print(f"[{printhash}]")
            strength = random.randint(1,10)
            print(f"The password {current_pass} strength level is: {strength}")
            if strength == 1:
                print("So weak like that actually sucks")
            elif strength == 2:
                print("Weak")
            elif strength == 3:
                print("Lincoln could crack that in 0.0002405 miliseconds")
            elif strength == 4:
                print("Decent...")
            elif strength == 5:
                print("Mid")
            elif strength == 6:
                print("My password is probably about this")
            elif strength == 7:
                print("Strength = 7")
            elif strength == 8:
                print("Vincent does not stamp that with approval")
            elif strength == 9:
                print("STRONG")
            elif strength == 10:
                print("G I G A C H A D    P A S S W O R D")
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
