# To Do List - Jackson Hauley

todo = []

with open("ToDoList/list.txt", "r") as file:
    for line in file:
        split_line = line.strip()
        print(split_line)
        todo.append(line.strip())

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

def print_list():
    cs()
    print("To Do List\n")
    for x in todo:
        x.split("//")
        print(f"[{x[0]}] {x[1]}")
    input("\nPress enter to continue")

def main():
    while True:
        cs()
        choice = int_input("To Do List Manager\n\n1. View List\n2. Add Item\n3. Remove Item\n4. Mark Item\n5. Exit\n\nWhat would you like to do? (1-5): ")
        if choice == 1: # View List
            print_list()
        elif choice == 2: # Add Item
            pass
        elif choice == 3: # Remove Item
            pass
        elif choice == 4: # Mark Item
            pass
        elif choice == 5: # Exit
            cs()
            print("Thanks for using Jacksons Amazing To Do List Manager!")
            exit()
        else:
            input("Invalid Input!\nPress enter to continue")


main()