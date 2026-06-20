import os
import json
FILENAME = "movies.json"

def load():
    if not os.path.exists(FILENAME):
        return[]
    with open(FILENAME,"r", encoding="utf-8") as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILENAME,"w",encoding="utf-8") as f:
        json.dump(movies,f,indent=2)

def add_movies(movies):
    title = input("Eneter teh title for the movie: ").strip().lower()
    if any(movie['title'].lower() == title for movie in movies):
        print("Movie Already Exists")
    genre = input("Genre: ").strip().lower()
    try:
        rating= float(input("Enter a ratong: "))
        if not (0<=rating<=10):
            raise ValueError
    except ValueError:
        print("Please enter a valid number")
        return
    movies.append({"title":title,"genre":genre,"rating":rating})
    save_movies(movies)
    print("Movie Added Successfully")

def search_movies(movies):
    term= input("Enter the title or genre: ").lower().strip()

    results = [
        movie for movie in movies
        if term in movie['title'].lower() or term in movie['genre'].lower()
    ]
    if not results:
        print("No matching Results")
        return
    print(f"Found {len(results)} result(s)")
    for movie in results:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']} ")

def view_movies(movies):
    if not movies:
        print("No Movies in DB")
    print("-"*30)
    for movie in movies:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']} ")
    print("-"*30)

def run_movie_db():
    movies=load()

    while True:
        print("\nMy Movie DB")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit")

        choice=input("Choose an option between (1-4)").strip()
        match choice:
            case "1": add_movies(movies)
            case "2": view_movies(movies)
            case "3": search_movies(movies)
            case "4": break
            case _: print("Enter a valid choice")

if __name__ == "__main__":
    run_movie_db()