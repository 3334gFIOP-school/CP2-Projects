# Pet Simulator - Jackson Hauley

import random
from essentials import *
import csv
import pandas as pd
from file_handling import *
from pet import pet

def main(current_pet):
    print(current_pet)
    while True:
        cs()
        print("PET SIMULATOR")
        print(current_pet)
        print("1. Create Pet")
        print("2. Run Simulator")
        print("3. Switch Pet")
        print("4. Exit")
        choice = int_input("Enter your choice: ")
        if choice == 1:
            new_pet = create_pet()
            save_pets_to_csv(pets)
            if current_pet is None:
                current_pet = new_pet
                print(f"{current_pet.name} is now your selected pet.")
                input("Press enter to continue")
                print("No pet selected. Create or switch to a pet first.")
        elif choice == 2:
            length = int_input("How long do you want to run the simulator for? (in ticks): ")
            if current_pet is not None:
                for x in range(length):
                    current_pet.tick()
                    current_pet.event()
                if current_pet.health <= 0:
                    print(f"{current_pet.name} has died.")
                    input("Press enter to continue")
                    save_pets_to_csv(pets)
                    break
                else:
                    print(current_pet)
                    input("Press enter to continue")
                    save_pets_to_csv(pets)
            else:
                print("No pet selected. Create or switch to a pet first.")
                input("Press enter to continue")
        elif choice == 3: 
            current_pet = select_pet()
            if current_pet:
                print(f"Switched to {current_pet.name}.")
            save_pets_to_csv(pets)
        elif choice == 4:
            cs()
            print("Cya later!")
            save_pets_to_csv(pets)
            break
        else:
            print("Invalid choice!")


def create_pet():
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
    pets.append(new_pet)
    print(f"Pet {new_pet.name} has been created successfully!")
    return new_pet

def select_pet():
    while True:
        cs()
        print("Select a pet")
        if not pets:
            print("No pets available. Create a pet first.")
            input("Press enter to create a pet.")
            return create_pet()
        print("Available pets:")
        for x in range(len(pets)):
            print(f"{x + 1}. {pets[x].name}")
        pet_index = int_input("Enter the number of the pet to select: ") - 1
        if 0 <= pet_index < len(pets):
            return pets[pet_index]
        else:
            print("Invalid selection.")
            continue

pets = load_pets_from_csv()
input(pets)
current_pet = select_pet()
main(current_pet) # Runs main