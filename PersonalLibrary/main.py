# Jackson Hauley - Personal Library Program

# Initializing Variables
library_name = "My Library"

library = set({})

# Essential Functions
def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError:
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output
def str_input(text): # Only takes in string
    while True:
        try: output = str(input(text))
        except ValueError:
            print("String Input! (only strings accepted)")
            input("Press enter to try again")
            continue
        return output
def float_input(text): # Only takes in floats
    while True:
        try: output = float(input(text))
        except ValueError:
            print("Invalid Input! (only floats accepted)")
            input("Press enter to try again")
            continue
        return output
def cs(): # Clear Screen
    print("\033c",end="")

# Main Funcitons
def main():
    while True:
        cs()
        choice = int_input("Personal Library\n\n1. Search Library\n2. Add Item\n3. Remove Item\n4. Erase Library\n5. Generate Random Library\n6. Rename Library\n7. View Library\n8. Exit Library\n\nWhat do you want to do? (1-8): ")
        if choice == 1:
            pass
        elif choice == 2: # Adding item choice
            cs()
            print("Adding Item")
            book = str_input("What is the title of the book?: ")
            author = str_input("What is the authors name?: ")
            adding = (book,author) # Ordered Tuple for adding to library set
            library.add(adding) # Adds book and title 
            input("Press enter to continue")
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7: # Print out the entire library
            cs()
            print(f"======= {library_name} =======")
            for x in library:
                print(x)
                input('Press enter to continue')
        elif choice == 8: # Exit Choice
            print(f"\nExiting {library_name}! See you next time!")
            exit()



main()