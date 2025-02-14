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

def search_movies(): # Searching for movies function 
    cs() # Clears the screen
    term_amount = int_input("How many search terms do you want to search at once?: ")
    search_terms = []
    found_movie_num = []
    final_found_movie_num = []

    for x in range(term_amount): 
        search_terms.append(input(f"Search Term {x+1}: ")) # Search term list creation

    for x in range(len(movies)): # This is the main searching loop
        for i in range(term_amount):
            if str(search_terms[i]).strip().lower() in str(movies[x]["Title"]).strip().lower():
                found_movie_num.append(x) # Appends the movie dict index number if it finds any of these in it
            elif str(search_terms[i]).strip().lower() in str(movies[x]["Director"]).strip().lower():
                found_movie_num.append(x)
            elif str(search_terms[i]).strip().lower() in str(movies[x]["Genre"]).strip().lower():
                found_movie_num.append(x)
            elif str(search_terms[i]).strip().lower() in str(movies[x]["Rating"]).strip().lower():
                found_movie_num.append(x)
            elif str(search_terms[i]).strip().lower() in str(movies[x]["Actors"]).strip().lower():
                found_movie_num.append(x)
            try:
                int(search_terms[i])
                if int(search_terms[i])+10 > int(movies[x]["Runtime"]) > int(search_terms[x])-10:
                    found_movie_num.append(x)
            except ValueError:
                pass
            

    for i in range(len(search_terms)):
        num_count = found_movie_num.count(found_movie_num[i])
        if num_count == term_amount:
            final_found_movie_num.append(found_movie_num[i])

    for x in range(len(final_found_movie_num)): # Printing out the whole library
            print()
            print(f"Title: {movies[final_found_movie_num[x]]["Title"]}") # Indexing the dictionary in the dictionary for book/author
            print(f"Director: {movies[final_found_movie_num[x]]["Director"]}") # Director of the movie
            print(f"Genre: {movies[final_found_movie_num[x]]["Genre"]}") # Genre of the movie
            print(f"Rating: {movies[final_found_movie_num[x]]["Rating"]}") # Prints rating (PG, G)
            print(f"Runtime: {movies[final_found_movie_num[x]]["Runtime"]}") # Prints runtime in minutes
            print(f"Actors: {", ".join(movies[final_found_movie_num[x]]["Actors"])}\n") # Prints actors

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
