# To Do List - Jackson Hauley

todo = []

with open("ToDoList/list.txt", "r") as file:
    for line in file:
        split_line = line.strip()
        todo.append(split_line)

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

def print_list(): # Prints the whole to do list
    cs()
    print("To Do List\n")
    for x in todo:
        split = x.split("//") # splits it with double slashes
        print(f"[{split[0]}] {split[1]}")
    input("\nPress enter to continue")

def add_item(todo): # Adds an item to the text file
    cs()
    print("Add Item to List\n")
    adding = input("What item would you like to add?: ")

    todo.append(f"O//{adding}")

    with open("ToDoList/list.txt", "w") as file:
        for x in todo:
            file.write(f"{x}\n")
                       
    print("Item added!")

    input("\nPress enter to continue")

def remove_item(todo):  # Removes an item from the text file
    cs()
    item_removed = False
    print("Removing Item from List\n")
    removing = input("What item would you like to remove?: ").strip().lower()

    for x in todo:
        strip_x = x.split("//")[1].strip().lower()  
        if removing == strip_x:  # Compare with input
            todo.remove(x) 
            item_removed = True

    with open("ToDoList/list.txt", "w") as file:
        for x in todo:
            file.write(f"{x}\n")

    if item_removed:
        print("Item Removed!")
    else:
        print("Item not found!")

    input("\nPress enter to continue")

def mark_item(todo): # Marking an item with an X or an O
    cs()
    switched = False
    print("Marking Item in List\n")
    marking = input("What item would you like to mark/unmark?: ").strip().lower()

    for x in todo:
        strip_x = x.split("//")[1].strip().lower()  
        if marking == strip_x:  # Compare with input
            switched = True
            todo.remove(x)
            if x.split("//")[0] == "X": # Switching around the marking
                todo.append(f"O//{x[1].strip().lower()}")
                print(f"[X] {x.split("//")[1].strip().lower()} is now [O] {x.split("//")[1].strip().lower()}!") # Marking stuff
            elif x.split("//")[0] == "O":
                todo.append(f"X//{x[1].strip().lower()}")
                print(f"[O] {x.split("//")[1].strip().lower()} is now [X] {x.split("//")[1].strip().lower()}!")
    
    with open("ToDoList/list.txt", "w") as file:
        for x in todo:
            file.write(f"{x}\n")

    if switched:
        print("Item Changed!")
    else:
        print("Item not found!")

    input("\nPress enter to continue")
        

def main(todo): # Main function that runs everything inside of it

    while True:
        cs()
        choice = int_input("To Do List Manager\n\n1. View List\n2. Add Item\n3. Remove Item\n4. Mark Item\n5. Exit\n\nWhat would you like to do? (1-5): ")
        if choice == 1: # View List
            print_list()
        elif choice == 2: # Add Item
            add_item(todo)
        elif choice == 3: # Remove Item
            remove_item(todo)
        elif choice == 4: # Mark Item
            mark_item(todo)
        elif choice == 5: # Exit
            cs()
            print("Thanks for using Jacksons Amazing To Do List Manager!")
            exit()
        else:
            input("Invalid Input!\nPress enter to continue")


main(todo)