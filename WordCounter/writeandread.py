# Writing and reading file

import time

def cs(): # Clear Screen
    print("\033c",end="")

def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError:
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output

def write(): # Write to a file menu
    cs()
    choice = int_input("1. File 1\n2. File 2\n3. Exit\n\nWhat would you like to do? (1-3): ")
    if choice == 1: # File 1
        file = "WordCounter/text.txt"
        write_to(file)
    elif choice == 2: # File 2
        file = "WordCounter/text2.txt"
        write_to(file)
    elif choice == 3:
        pass

def read(): # Read a file menu
    cs()
    choice = int_input("1. File 1\n2. File 2\n3. Exit\n\nWhat would you like to do? (1-3): ")
    if choice == 1: # File 1
        file = "WordCounter/text.txt"
        read_from(file)
    elif choice == 2: # File 2
        file = "WordCounter/text2.txt"
        read_from(file)
    elif choice == 3:
        pass

def write_to(file): # Writes to a file
    write = input("What do you want to write to the file: ")
    with open(file, "w") as file:
        file.writelines([write,"\n",time.ctime()])
        input("\nFile Overwriten!\nPress enter to continue")

def read_from(file): # Reads from a file
    contents = []
    with open(file, "r") as file:
        contents = file.readlines()
        print(f"\nYour file says:\n{contents[0]}\nWritten on:\n{contents[1]}\n")
        input("Press enter to continue")