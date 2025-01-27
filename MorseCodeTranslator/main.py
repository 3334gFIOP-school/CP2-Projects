# Jackson Hauley - Morse Code Translator

# Instructions

'''
[X] Create two lists (one of the alphabet letters in English, and other for the corresponding Morse Code Symbols) 
[X] Create a function to translate English into Morse Code
[X] Create a function to translate Morse Code into English
[X] Create a main loop where users can choose to translate English to Morse Code, Morse Code to English, or Exit
Project needs to:
[O] Use string manipulation to control the appearance of the output 
[O] Use basic error handling (for characters not in Morse Code)
[X] Use good naming for functions and variables
[O] Use pseudocode comments to explain what the program is doing
[O] Use white space to make sure code is easy to read
'''

# Initializing Lists

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z') # Alphabet Tuple
morse_alphabet = ( # Morse Code Tuple
    '.-',   # A
    '-...', # B
    '-.-.', # C
    '-..',  # D
    '.',    # E
    '..-.', # F
    '--.',  # G
    '....', # H
    '..',   # I
    '.---', # J
    '-.-',  # K
    '.-..', # L
    '--',   # M
    '-.',   # N
    '---',  # O
    '.--.', # P
    '--.-', # Q
    '.-.',  # R
    '...',  # S
    '-',    # T
    '..-',  # U
    '...-', # V
    '.--',  # W
    '-..-', # X
    '-.--', # Y
    '--..', # Z
)

# Defining Functions

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

def main():
    while True:
        cs()
        choice = int_input("Morse code translator\n\n1. English to Morse Code\n2. Morse Code to English\n3. View Morse Code to English Table\n4. Exit\n\nWhat do you want to do? (1-4): ") # Seleciton Menu
        if choice == 1: # English to Morse Code
            english = eng_to_mor() # English to morse code code
            print()
            print(" ".join(english)) # Printing it in a readable format
            input("\nPress enter to continue")
        elif choice == 2: # Morse code to english
            morse = mor_to_eng() # Morse code to english code
            print()
            print("".join(morse)) # Printing it in a readable format
            input("\nPress enter to continue")
        elif choice == 3:
            pass
        elif choice == 4:
            cs()
            print("Thanks for using Jacksons Morse Code Translator!")
            exit()
        else:
            print("Invalid Input (1-3), try again")
            input("Press enter to continue")

def eng_to_mor(): # English to morse code
    cs()
    english = input('Type in the sentence you want translated to morse code: ')
    englishlist = list(english) # Setting up the list
    for x in range(len(englishlist)):
        if x == " ": # Checking for spaces
            continue
        for i in range(len(alphabet)): # Replacing letters with morse code
            if alphabet[i] == englishlist[x].lower():
                englishlist.pop(x)
                englishlist.insert(x,morse_alphabet[i])
    return englishlist


def mor_to_eng(): # Morse code to english
    cs()
    morse = input('Type in the morse code you want translated to english: ')
    morselist = list(morse) # Setting up the list
    for x in range(len(morselist)):
        if x == " ": # Checking for spaces
            continue
        for i in range(len(morse_alphabet)): # Replacing letters with english
            if morse_alphabet[i] == morselist[x].lower():
                morselist.pop(x)
                morselist.insert(x,alphabet[i])
    return morselist


main()