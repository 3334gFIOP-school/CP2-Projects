# Pet Class

from essentials import *
import random

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
    
    def event(self): # Runs an event for the pet
        eventnum = random.randint(1, 10)
        cs()
        if eventnum == 1:
            print(f"{self.name} lays down to take a nap.")
            self.energy += 10
            print("Energy + 10")
            self.happiness += 5
            print("Happiness + 5")
        elif eventnum == 2:
            print(f"{self.name} plays with a toy.")
            self.cleanliness -= 2
            print("Cleanliness - 2")
            self.happiness += 10
            print("Happiness + 10")
        elif eventnum == 3:
            print(f"{self.name} goes for a walk.")
            self.cleanliness -= 5
            print("Cleanliness - 5")
            self.happiness += 10
            print("Happiness + 10")
        elif eventnum == 4:
            print(f"{self.name} gets sick.")
            self.health -= 20
            print("Health - 20")
            self.happiness -= 10
            print("Happiness - 10")
        elif eventnum == 5:
            print(f"{self.name} goes to the vet for a checkup.")
            self.health += 20
            print("Health + 20")
            self.happiness -= 5
            print("Happiness - 5")
            self.cleanliness -= 5
            print("Cleanliness - 5")
        elif eventnum == 6:
            print(f"{self.name} DIES")
            self.health = 0
            self.happiness = 0
            self.cleanliness = 0
            print("Your pet is now dead! You can revive it by bringing its stats back up")
        input("Press enter to continue")

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
        self.age += 0.01
        print(self)
