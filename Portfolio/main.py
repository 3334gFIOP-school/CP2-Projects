# Jackson Hauley - main Portifolio
from essentials import *
from personal_library import *
from personal_library import main as personal_library
from morse_code import *
from morse_code import main as morse_translator
from reaction_game import *
from reaction_game import main as reaction_game
from todolist import *
from todolist import main as todolist_manager
from word_counter import *
from word_counter import main as word_counter
from movie_recommender import *
from movie_recommender import main as movie_recommender

def main(): # Main Functions
    cs()
    input("This is the COMPUTER SCIENCE portifolio for JACKSON HAULEY\nThis is a collection of some of my best computer science projects!\nSelect the project by typing the number next to the name to run\nPress enter to continue")
    while True:
        cs()
        choice = int_input("Project Navigator\n\n1. Personal Library\n2. Morse Code Translator\n3. Reaction Test\n4. To Do List Manager\n5. Word Counter\n6. Movie Recommender\n7. Exit Terminal\n\nChoose one (1-7): ")
        if choice == 1: # Personal Library
            cs(), input("This is a personal library manager I made to manage books and authors with an ID searching system!\nIts also really fun adding random books!\nPress enter to start")
            cs(), personal_library(id,library_name,library)
            cs()
        elif choice == 2: # Morse Code Translator
            cs(), input("This is a morse code translator, and it has morse to english and english to morse!\nCool thing for secret messages haha\nPress enter to start")
            cs(), morse_translator()
            cs()
        elif choice == 3: # Reaction Test
            cs(), input("This is a reaction test game using entirely pygame!\nClick quit or X to return to terminal\nPress enter to start")
            cs(), reaction_game()
            cs()
        elif choice == 4: # To Do List Manager
            cs(), input("This is a todo list manager with checkboxes, and this saves using a text file!\n(Some advanced file saving ikr)\nPress enter to start")
            cs(), todolist_manager(todo)
            cs()
        elif choice == 5: # Word Counter 
            cs(), input("This lets you write text to a text file of your choice (input the relative path)\nKeeps track of the time and how many words are in the file too\nPress enter to start")
            cs(), word_counter()
            cs()
        elif choice == 6: # Movie Recommender
            cs(), input("Multiple movies that are in it and you can add movies manually to the csv\nSearch infinite amount of terms to narrow down movies!\nPress enter to start")
            cs(), movie_recommender()
            cs()
        elif choice == 7: # Exit
            cs(),print("Bye! Thanks for viewing my portfolio!"),exit()

main() # Running main function