# Classes and Objects in Python

class subject:
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

    def __str__(self): # Every method in a class has to have self as the first parameter
        return f"Name: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}\nRoom: {self.room}"

first = subject("CS Principles", 1, "LaRose", 200)
second = subject("CP2", 2, "LaRose", 200)
print(first.content) # Printing a part of the object from the class
print(second.content)


class pokemon:
    def __init__(self, name, species, hp, dmg): # This is self, it is called when you create an object
        self.name = name # You have to put all the variables in self that are going to be used in the class
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"Name: {self.name} is a {self.species} with {self.hp} HP and does {self.dmg} damage in battle"
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            print(f"{self.name} attacks {opponent.name} for {self.dmg} damage")
            opponent.hp -= self.dmg
            print(f"{opponent.name} has {opponent.hp} HP left")
            if opponent.hp <= 0:
                print(f"{opponent.name} has been knocked out!")
            else:
                print(f"{opponent.name} attacks {self.name} for {opponent.dmg} damage")
                self.hp -= opponent.dmg
                print(f"{self.name} has {self.hp} HP left")
                if self.hp <= 0:
                    print(f"{self.name} has been knocked out!")





fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spiky = pokemon("Spiky", "Jolteon", 150, 100)


fluffy.battle(spiky)
spiky.HP

slimy.battle(spiky)

#What is a class in python?
    # A blueprint for creating objects

#What is an object in python?
    # A variable that is contained within the class, the specific instance, you can have multiple objects of the same class

#How do python classes relate to python objects?
    # Classes are blueprints for creating objects

#How do you create a python class?
    # Using class (name): then having def __init__(self): and so on

#What are methods?
    # Functions that exist for a specific class

#How do you create a python object?
    # Using the class name and putting the variables in the parentheses

#How to you call a method for an object?
    # Using the object name and then the method name with parentheses

#Why do we use python classes?
    # To create objects that have properties and methods with organization