# Pet Simulator - Jackson Hauley

import random
from essentials import *
import csv
import pandas as pd
from file_handling import *
from pet import pet

def main(current_pet): # Main Functions 
    while True:
        cs() # Clear Screen
        print("PET SIMULATOR") # Title and optins
        print(current_pet)
        print("1. Create Pet")
        print("2. Run Simulator")
        print("3. Switch Pet")
        print("5. Exit")
        choice = int_input("Enter your choice: ")
        if choice == 1:
            new_pet = create_pet() # Create a pet if you need to and/or want to
            save_pets_to_csv(pets)
            if current_pet is None:
                current_pet = new_pet
                print(f"{current_pet.name} is now your selected pet.") # Tells them what pet they got
                input("Press enter to continue")
                print("No pet selected. Create or switch to a pet first.")
        elif choice == 2:
            length = int_input("How long do you want to run the simulator for? (in ticks): ") # Length of simulating the pet
            if current_pet is not None:
                for x in range(length):
                    current_pet.tick() # Ticking, this is basically time checking
                    current_pet.event() # This is the event that it does
                if current_pet.health <= 0:
                    print(f"{current_pet.name} has died.") # If the pet dies, it will tell you
                    print("You can revive pet by making it sleep and eat and play a bunch ngl")
                    input("Press enter to continue")
                    save_pets_to_csv(pets)
                else:
                    print(current_pet) # Shows the final stats of the pet
                    input("Press enter to continue")
                    save_pets_to_csv(pets)
            else:
                print("No pet selected. Create or switch to a pet first.")
                input("Press enter to continue")
        elif choice == 3: 
            current_pet = select_pet() # Pet Selection
            if current_pet:
                print(f"Switched to {current_pet.name}.")
            save_pets_to_csv(pets)
        elif choice == 4: # manually do stuff for your pet
            cs()
            choice2 = int_input("Choose what to do with your pet:\n1. Feed\n2. Clean\n3. Play\n4. Sleep\n5. Exit\nEnter your choice: ")
            if choice2 == 1:
                current_pet.feed() # Feed Pet
            elif choice2 == 2:
                current_pet.clean() # Clean Pet
            elif choice2 == 3:
                current_pet.play() # Play with Pet
            elif choice2 == 4:
                current_pet.sleep() # Sleep Pet
            elif choice2 == 5:
                pass
            save_pets_to_csv(pets) # Saves Pets
        elif choice == 5:
            cs()
            print("Cya later!")
            save_pets_to_csv(pets) # Saves pets after leaving
            break
        else:
            print("Invalid choice!")


def create_pet(): # Pet creation screen
    cs()
    print("Create a pet")
    name = input("Enter pet's name: ")
    type = input("Enter pet's type (e.g., Dog, Cat): ")
    age = 0
    health = 100
    happiness = 100
    energy = 100
    hunger = 0
    cleanliness = 100
    new_pet = pet(name, type, age, health, happiness, energy, hunger, cleanliness)
    pets.append(new_pet) # Adds a new pet here
    print(f"Pet {new_pet.name} has been created successfully!")
    return new_pet

def select_pet(): # Pet selection functon
    while True:
        cs()
        print("Select a pet")
        if not pets:
            print("No pets available. Create a pet first.") # Select pet
            input("Press enter to create a pet.")
            return create_pet() # Lets you create a pet if you have none
        print("Available pets:")
        for x in range(len(pets)):
            print(f"{x + 1}. {pets[x].name}") # Crap that shows you the list
        print(f"{len(pets) + 1}. Create a new pet")
        pet_index = int_input("Enter the number of the pet to select: ") - 1
        if 0 <= pet_index < len(pets):
            return pets[pet_index]
        elif pet_index == len(pets):
            return create_pet() # If you want to create a new pet create one
        else:
            print("Invalid selection.")
            continue

pets = load_pets_from_csv()
current_pet = select_pet()
main(current_pet) # Runs main