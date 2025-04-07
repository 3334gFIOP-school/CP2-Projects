# Jackson Hauley - main Portifolio
from essentials import *
from personal_library import *
from personal_library import main as personal_library

def main(): # Main Functions
    cs()
    input("This is the COMPUTER SCIENCE portifolio for JACKSON HAULEY\nThis is a collection of some of my best computer science projects!\nSelect the project by typing the number next to the name to run\nPress enter to continue")
    while True:
        choice = int_input("Project Navigator\n\n1. Personal Library\n2. Morse Code Translator\n3. Reaction Test\n4. To Do List Manager\n5. Word Counter\n6. Movie Recommender\n7. Exit Terminal\n\nChoose one (1-7): ")
        if choice == 1: # Personal Library
            cs(), input("This is a personal library manager I made to manage books and authors with an ID searching system!\nIts also really fun adding random books!\nPress enter to start")
            cs(), personal_library(id,library_name,library)
        elif choice == 2: # Morse Code Translator
            pass
        elif choice == 3: # Reaction Tst
            pass
        elif choice == 4: # To Do List Manager
            pass
        elif choice == 5: # Word Counter 
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            cs(),print("Bye!"),exit()

main() # Running main function