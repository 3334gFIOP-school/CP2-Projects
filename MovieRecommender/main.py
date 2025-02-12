# Movie Recommender

import csv
import random

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
        choices = int_input("Movie Recommender\n\n1. Print Movie List\n2. Search Movies\n3. Exit\n\nWhich one do you want to do? (1-3): ")
    

# Reading and making the file a list of dictionaries

movies = [] # List of dictionaries of movies
with open("MovieRecommender\Movies list.csv") as file: # Reading the csv file
    reader = csv.reader(file) # reading the file
    next(reader) # Making it so you dont read the first line
    for row in reader: # Going through the list for every row
        movies.append({ # Adding this dictionary to the list
            "Title": row[0], # Title of the movie
            "Director": row[1], # Who directed the movie
            "Genre": row[2], # Genre of the movie
            "Rating": row[3], # The rating, like PG, PG-13
            "Runtime": int(row[4]),  # How many minutes it ran in an integer
            "Actors": row[5].split(", ") # Actor List (split into a list of all the actors)
            })
        
# Starting main functions

main() # Running the main function
