# File Handling for Pet Simulator 

import pandas as pd
from pet import pet

def save_pets_to_csv(pets, filename="PetSimulator/pets.csv"): # save to csv
    data = [{ # Saves the pet to the csv depending on each of the list
        "Name": pet.name,
        "Type": pet.type,
        "Age": round(pet.age, 2),
        "Health": pet.health,
        "Happiness": pet.happiness,
        "Energy": pet.energy,
        "Hunger": pet.hunger,
        "Cleanliness": pet.cleanliness
    } for pet in pets] # For pet it pets 
    df = pd.DataFrame(data) # Frames the data when saving
    df.to_csv(filename, index=False)
    print("Pets saved successfully!")

def load_pets_from_csv(filename="PetSimulator/pets.csv"): # load from csvssssssssssssss
    pets = []
    try:
        df = pd.read_csv(filename)
        for x, row in df.iterrows(): # Goes through the rows and makes pet lists then adds those to the main list
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
