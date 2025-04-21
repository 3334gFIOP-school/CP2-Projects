# Pet Class

from essentials import *
import random
import time

class pet: # PET CLASS
    def __init__(self, name, type, age, health, happiness, energy, hunger, cleanliness):
        self.name = name # Initializing variables for the class
        self.type = type
        self.age = age
        self.health = health
        self.happiness = happiness
        self.energy = energy
        self.hunger = hunger
        self.cleanliness = cleanliness

    def __str__(self):
        return f"\nName: {self.name}\nType: {self.type}\nAge: {self.age}\nHealth: {self.health}\nHappiness: {self.happiness}\nEnergy: {self.energy}\nHunger: {self.hunger}\nCleanliness: {self.cleanliness}\n"
    
    def event(self): # Runs an event for the pet
        eventnum = random.randint(1, 10) # Random Event
        if eventnum == 6:
            eventnum = random.randint(1, 10)
            if eventnum == 6:
                eventnum = random.randint(1, 10)
        cs()
        if eventnum == 1:
            print(f"{self.name} lays down to take a nap.") # nap
            self.energy += 10
            print("Energy + 10")
            self.happiness += 5
            print("Happiness + 5")
        elif eventnum == 2:
            print(f"{self.name} plays with a toy.") # toy
            self.cleanliness -= 2
            print("Cleanliness - 2")
            self.happiness += 10
            print("Happiness + 10")
        elif eventnum == 3:
            print(f"{self.name} goes for a walk.") # walk
            self.cleanliness -= 5
            print("Cleanliness - 5")
            self.happiness += 10
            print("Happiness + 10")
        elif eventnum == 4:
            print(f"{self.name} gets sick.") # sick ness
            self.health -= 20
            print("Health - 20")
            self.happiness -= 10
            print("Happiness - 10")
        elif eventnum == 5:
            print(f"{self.name} goes to the vet for a checkup.") # vet
            self.health += 20
            print("Health + 20")
            self.happiness -= 5
            print("Happiness - 5")
            self.cleanliness -= 5
            print("Cleanliness - 5")
        elif eventnum == 6:
            print(f"{self.name} DIES") # death
            self.health = 0
            self.happiness = 0
            self.cleanliness = 0
            self.energy = 0
            print("Your pet is now dead! You can revive it by bringing its stats back up") # dead
        elif eventnum == 7:
            print(f"{self.name} eats some food.") # food
            self.hunger -= 10
            print("Hunger - 10")
            self.happiness += 5
            print("Happiness + 5")
        elif eventnum == 8:
            print(f"{self.name} plays with you.") # playtime
            self.cleanliness -= 5
            print("Cleanliness - 5")
            self.happiness += 30
            print("Happiness + 30")
        elif eventnum == 9:
            print(f"{self.name} spontaneously combusts.") # combustion
            self.cleanliness -= 20
            print("Cleanliness - 20")
            self.happiness -= 20
            print("Happiness - 20")
            self.energy -= 20
            print("Energy - 20")
        elif eventnum == 10:
            print(f"{self.name} is bored.") # boredom
            self.happiness -= 5
            print("Happiness - 5")
            self.cleanliness += 10
            print("Cleanliness + 10")
        self.energy -= 1
        print("Energy - 1")
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
        self.age = round(self.age, 2) #rounds the age to 2 decimal places
        self.age += 0.01
        print(self)

    def feed(self): # Feeds the pet
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed")
        input("Press enter to continue")

    def clean(self): # Cleans the pet
        self.cleanliness += 10
        if self.cleanliness > 100:
            self.cleanliness = 100
        print(f"{self.name} has been cleaned")
        input("Press enter to continue")

    def play(self): # plays with pet
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} has been played with")
        input("Press enter to continue")

    def sleep(self): # sleeps
        self.energy += 50
        if self.energy > 100:
            self.energy = 100
        for x in range(5):
            time.sleep(1)
            print(f"{self.name} is sleeping... {5-x}")
        print(f"{self.name} has slept")
        input("Press enter to continue")