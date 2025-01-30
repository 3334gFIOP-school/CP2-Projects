# Jackson Hauley - Morse Code Translator

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
            print(f"\n{morse}") # Printing it in a readable format
            input("\nPress enter to continue")
        elif choice == 3:
            pass
        elif choice == 4: # Exittttinggg
            cs()
            print("Thanks for using Jacksons Morse Code Translator!")
            exit()
        else:
            print("Invalid Input (1-4), try again")
            input("Press enter to continue")

def eng_to_mor(): # English to morse code
    cs()
    english = input('Type in the sentence you want translated to morse code: ')
    englishlist = list(english) # Setting up the list

    for x in range(len(englishlist)):
        if englishlist[x] == " ": # Checking for spaces
            continue

        for i in range(len(alphabet)): # Replacing letters with morse code
            if alphabet[i] == englishlist[x].lower():
                englishlist.pop(x)
                englishlist.insert(x,morse_alphabet[i])
    return englishlist


def mor_to_eng():  # Morse code to English
    cs()
    morse = input('Type in the morse code you want translated to English: ')
    output = []
    words = morse.split('   ')  # split by triple space to separate words

    for x in words:
        letters = x.split()  # split by single space for letters
        word_output = []
        for i in letters: # Going through all the letters that it got by splitting a word

            if i in morse_alphabet:
                position = morse_alphabet.index(i) # indexing
                word_output.append(alphabet[position])
            else:
                print("There is non-morse code text in your input!")
                return  # exit if there is invalid Morse Code
        output.append(''.join(word_output))  # join the letters to form the word
    return ' '.join(output)  # return thing

# Running main code
main()