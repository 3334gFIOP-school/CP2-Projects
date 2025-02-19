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

def main(): # Main function
    while True:
        cs()    
        choices = int_input("Movie Recommender\n\n1. Print Movie List\n2. Search Movies\n3. Exit\n\nWhich one do you want to do? (1-3): ")
        if choices == 1: # Print Movie List
            print_list() # Print list Function
        elif choices == 2: # Search Movie List
            search_movies() # Searching through movie list
        elif choices == 3: # Exit 
            cs() 
            print("Thanks for using jacksons movie recommender!")
            exit()
        else:
            print("Invalid Input! (1-3)")

def print_list(): # Print list Function
    cs()
    choice2 = int_input("Simple (1) or Complicated (2)? (1-2): ")
    if choice2 == 2:
        print(f"======= Movies =======\n") # Title of complicated list
        for x in range(len(movies)): # Printing out the whole library
            print(f"Title: {movies[x]["Title"]}") # Indexing the dictionary in the dictionary for book/author
            print(f"Director: {movies[x]["Director"]}") # Director of the movie
            print(f"Genre: {movies[x]["Genre"]}") # Genre of the movie
            print(f"Rating: {movies[x]["Rating"]}") # Prints rating (PG, G)
            print(f"Runtime: {movies[x]["Runtime"]}") # Prints runtime in minutes
            print(f"Actors: {", ".join(movies[x]["Actors"])}\n") # Prints actors
        input('Press enter to continue')# Press enter to continue
    elif choice2 == 1: # If simple/complicated you choose simple
        print(f"======= Simplefied Movies =======\n") # Title of simplefied notes
        for x in range(len(movies)): # Printing out the whole library
            print(f"Title: {movies[x]["Title"]}\n") # Indexing the dictionary in the dictionary for title
            print(f"Genre: {movies[x]["Genre"]}\n") # Indexing the genre
        input('Press enter to continue') # Press enter to continue

def search_movies():  # Searching for movies function
    cs()  # Clears the screen
    term_amount = int_input("How many search terms do you want to search at once?: ")
    search_terms = [input(f"Search Term {x+1}: ").strip().lower() for x in range(term_amount)]
    final_found_movie_num = []
    for index, movie in enumerate(movies):  # Iterate through movie list (I had to look up enumerate tbh but I figured it out its just another x or i)
        count = 0
        for term in search_terms:
            term_found = term in movie["Title"].strip().lower() or term in movie["Director"].strip().lower() or term in movie["Genre"].strip().lower() or term in movie["Rating"].strip().lower() or term in movie["Actors"][0].strip().lower() or term in movie["Actors"][1].strip().lower()# TRUE if it finds anything
            if not term_found: # This is if its a number
                try:
                    term_as_int = int(term)
                    if term_as_int + 10 > int(movie["Runtime"]) > term_as_int - 10:
                        term_found = True
                except ValueError:
                    continue
            else:
                count += 1 # This is to fix what you had a problem with
        if count == term_amount:
            final_found_movie_num.append(index)
    if final_found_movie_num:
        for index in final_found_movie_num:
            print()
            print(f"Title: {movies[index]['Title']}")
            print(f"Director: {movies[index]['Director']}")
            print(f"Genre: {movies[index]['Genre']}")
            print(f"Rating: {movies[index]['Rating']}")
            print(f"Runtime: {movies[index]['Runtime']}")
            print(f"Actors: {', '.join(movies[index]['Actors'])}\n")

    else:
        print("No Movies Found!")
    input("Press enter to continue")
        
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
            }) # End dictionary
        
# Starting main functions

main() # Running the main function
