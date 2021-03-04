
"""
Napisz program liczący odległość liniową między dwoma dowolnymi punktami na mapie, wykorzystujący ich 
współrzędne geograficzne (długość i szerokość geograficzną). Wykorzystaj dowolny algorytm, 
np. https://pl.wikibooks.org/wiki/Astronomiczne_podstawy_geografii/Odleg%C5%82o%C5%9Bci?fbclid=IwAR3ONX2eqMWqbW6l_M9cNWxe-WgxQ_Z8jzcSldnCVv4whJtClBF--mMsbOE
Skorzystaj z API (np. https://rapidapi.com/trueway/api/trueway-geocoding), żeby obliczyć odległość pomiędzy 
twoim adresem, a charakterystycznymi punktami np. Wieżą Eiffla czy Tadź Mahal.
Propozycja rozszerzenia: zamiast podawać swój adres, użyj geolokalizacji.

"""

import requests
import geocoder
from math import sqrt, cos, pi


# give your rapidapi key
api_key = ""


def get_location(place):
    """Find coordinates of a given place."""
    
    url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
    querystring = {"address":place,"language":"pl"}
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    loc = response.json()['results'][0]['location']
    return loc['lat'], loc["lng"]


def get_distance(x1, x2, y1, y2):
    """
    Calculate linear distance between two geographic points.
    :return: float distance in kilometers.
    """
    dist = sqrt(pow((x2-x1), 2) + pow((cos((x1*pi)/180 ) * (y2-y1)), 2)) * (40075.704/360)
    return dist
    

def my_location():
    """Finds my location"""
    geo = geocoder.ip('me').latlng
    return geo


def main():
    place_one = "Eiffel Tower, Paris"
    place_two = "Taj Mahal, India"
    my_loc = my_location()
    loc_one = get_location(place_one)
    loc_two = get_location(place_two)
    distance = get_distance(my_loc[0], loc_one[0], my_loc[1], loc_one[1])
    distance_two = get_distance(loc_one[0], loc_two[0], loc_one[1], loc_two[1])
    print(f'The distance between me and {place_one} is {distance:.2f} km.')
    print(f'The distance between {place_one} and {place_two} is {distance_two:.2f} km.')


if __name__ == "__main__":
    main()