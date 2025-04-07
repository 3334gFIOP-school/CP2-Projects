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
    choice = input("Copy the file path: ")
    path = choice.replace("\\", "/")
    write_to(path)

def read(): # Read a file menu
    cs()
    choice = input("Copy the file path: ")
    path = choice.replace("\\", "/")
    read_from(path)

def write_to(file): # Writes to a file
    write = input("What do you want to write to the file: ")
    try:
        with open(file, "w") as file:
            file.writelines([write,"\n",time.ctime()])
            input("\nFile Overwriten!\nPress enter to continue")
    except:
        input("File not found!\nPress enter to continue")

def read_from(file): # Reads from a file
    contents = []
    try:
        with open(file, "r") as file:
            contents = file.readlines()
            words = len(contents[0].split())
            print(f"\nYour file says:\n{contents[0]}\nWritten on: {contents[1]}\nWords: {words}\n")
            input("Press enter to continue")
    except:
        input("File not found!\nPress enter to continue")