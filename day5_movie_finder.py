
"""
#MOVIE #FINDER
Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części filmu zadanego w wyszukiwaniu (np. Rambo, Scary Movie, Shrek). 
Można przyjąć założenie, że wszystkie filmy “z serii” muszą zawierać szukany ciąg - czasem zdarzają się błędne wyniki 
wyszukiwania z baz, można je spróbować odfiltrować. Wyświetl dla każdego podstawowe informacje np. rok, długość, ocena, 
spis aktorów (pierwszych 5 z listy).
"""

import requests


def movie_search(title):
    
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q": title}
    
    headers = {
        'x-rapidapi-key': "your API key",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    movies = response.json()
    return movies


def movie_info(data):
    for i in range(0, 5):
        try:
            title = data["d"][i]["l"]
            year = data["d"][i]["y"]
            cast = data["d"][i]["s"]
            rating = data["d"][i]["rank"]
            print(f"Movie: {title}\nYear of production: {year}\nMain cast: {cast}\nRating is {rating}.")
        except Exception as e:
            print(f"No found {e}")
    
    
films = movie_search(input('Type the title of the movie: '))
movie_info(films)

