# Pet Simulator - Jackson Hauley

import random
from essentials import *
import csv
import pandas as pd

food_list = ["Animal Food","Animal Treats"]
pets = []


class pet:
    def __init__(self, name, type, age, health, happiness, energy, hunger, cleanliness):
        self.name = name
        self.type = type
        self.age = age
        self.health = health
        self.happiness = happiness
        self.energy = energy
        self.hunger = hunger
        self.cleanliness = cleanliness

    def __str__(self):
        return f"Name: {self.name}\nType: {self.type}\nAge: {self.age}\nHealth: {self.health}\nHappiness: {self.happiness}\nEnergy: {self.energy}\nHunger: {self.hunger}\nCleanliness: {self.cleanliness}\n"
    
    def feed(self, food):
        if food in food_list:
            self.hunger -= 10
            self.happiness += 5
            print(f"{self.name} has been fed!")
        else:
            print(f"{self.name} does not like {food}!")
        if self.hunger < 0:
            self.hunger = 0

    def tick(self): # Ticks the hunger and happiness and cleanliness
        self.hunger += 2
        self.cleanliness -= 2
        if self.cleanliness < 0:
            self.cleanliness = 0
        if self.hunger >= 80:
            self.happiness -= 5  #hungry
            self.energy -= 5  #tired
        elif self.hunger <= 20:
            self.happiness += 2  #fed
        if self.cleanliness <= 20:
            self.happiness -= 5  #dirty
            self.energy -= 5  #tired
        elif self.cleanliness >= 80:
            self.happiness += 2  #clean
        if self.happiness < 0:
            self.happiness = 0
        if self.cleanliness < 0:
            self.cleanliness = 0
        if self.energy < 0:
            self.energy = 0
        if self.hunger > 100:
            self.hunger = 100
        print(self)

    def event(self): # Runs an event for the pet
        eventnum = random.randint(1, 10)
        if eventnum == 1:
            print(f"{self.name} lays down to take a nap.")
            self.energy += 10
            self.happiness += 5
        elif eventnum == 2:
            print(f"{self.name} plays with a toy.")
            self.cleanliness -= 2
            self.happiness += 10
        elif eventnum == 3:
            print(f"{self.name} goes for a walk.")
            self.cleanliness -= 5
            self.happiness += 10
        elif eventnum == 4:
            print(f"{self.name} gets sick.")
            self.health -= 20
            self.happiness -= 10
        elif eventnum == 5:
            print(f"{self.name} goes to the vet for a checkup.")
            self.health += 20
            self.happiness -= 5
            self.cleanliness -= 5
    

        

pet("Scout", "Dog", 2, 100, 100, 100, 0, 100)

def main():
    current_pet = None
    while True:
        cs()
        print("PET SIMULATOR")
        print("1. Create Pet")
        print("2. Feed Pet")
        print("3. Event")
        print("4. Switch Pet")
        print("5. Exit")
        choice = int_input("Enter your choice: ")
        if choice == 1:
            new_pet = create_pet()
            pets.append(new_pet)
            save_pets_to_csv(pets)
            if current_pet is None:
                current_pet = new_pet
                print(f"{current_pet.name} is now your selected pet.")
        elif choice == 2:
            if current_pet:
                if not pets:
                    pets.extend(load_pets_from_csv())
                food = input("Enter food: ")
                save_pets_to_csv(pets)
                current_pet.feed(food)
            else:
                print("No pet selected. Create or switch to a pet first.")
        elif choice == 3:
            if current_pet:
                current_pet.event()
            else:
                print("No pet selected. Create or switch to a pet first.")
        elif choice == 4:
            if pets:
                print("Available pets:")
                for i, pet in enumerate(pets):
                    print(f"{i + 1}. {pet.name}")
                pet_index = int_input("Enter the number of the pet to switch to: ") - 1
                if 0 <= pet_index < len(pets):
                    current_pet = pets[pet_index]
                    print(f"Switched to {current_pet.name}.")
                else:
                    print("Invalid selection.")
            else:
                print("No pets available. Create a pet first.")
        elif choice == 5:
            cs()
            print("Cya later!")
            break
        else:
            print("Invalid choice!")


def save_pets_to_csv(pets, filename="pets.csv"):
    data = [{
        "Name": pet.name,
        "Type": pet.type,
        "Age": pet.age,
        "Health": pet.health,
        "Happiness": pet.happiness,
        "Energy": pet.energy,
        "Hunger": pet.hunger,
        "Cleanliness": pet.cleanliness
    } for pet in pets]
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print("Pets saved successfully!")

def load_pets_from_csv(filename="pets.csv"):
    pets = []
    try:
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            pets.append(pet(
                name=row["Name"],
                type=row["Type"],
                age=int(row["Age"]),
                health=int(row["Health"]),
                happiness=int(row["Happiness"]),
                energy=int(row["Energy"]),
                hunger=int(row["Hunger"]),
                cleanliness=int(row["Cleanliness"])
            ))
        print("Pets loaded successfully!")
    except FileNotFoundError:
        print("Error with loading pets from CSV file. File not found.")
    return pets

def create_pet():
    cs()
    print("Create a pet")
    name = input("Enter pet's name: ")
    type = input("Enter pet's type (e.g., Dog, Cat): ")
    age = int_input("Enter pet's age: ")
    health = int_input("Enter pet's health (0-100): ")
    happiness = int_input("Enter pet's happiness (0-100): ")
    energy = int_input("Enter pet's energy (0-100): ")
    hunger = int_input("Enter pet's hunger (0-100): ")
    cleanliness = int_input("Enter pet's cleanliness (0-100): ")
    new_pet = pet(name, type, age, health, happiness, energy, hunger, cleanliness)
    pets.append(new_pet)
    print(f"Pet {new_pet.name} has been created successfully!")
    return new_pet

main() # Runs main