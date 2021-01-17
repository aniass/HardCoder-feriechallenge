
"""
Napisz program, który po uruchomieniu wyświetla w czytelnej formie aktualną datę, godzinę, dzień tygodnia i 
pogodę/temperaturę/ciśnienie w zadanym mieście (wykorzystaj np. https://rapidapi.com/commu.../api/open-weather-map/endpoints 
- pamiętaj o poprawnym przeliczeniu jednostek np. temperatura z kelwinów na stopnie) oraz losowy cytat 
(np. https://type.fit/api/quotes ). Wykorzystaj requests i datetime.
Propozycja rozszerzenia: Wyświetl również bieżący czas dla miast w różnych strefach czasowych (np. Pekin, Sydney, 
Waszyngton, Londyn) - wykorzystaj np. pytz: https://pypi.org/project/pytz/ oraz wyświetl listę osób obchodzących 
imieniny (poszukaj otwartej bazy danych lub wykorzystaj prosty web scrapping np. z wykorzystaniem: https://imienniczek.pl/widget/js ).

"""

import requests
import datetime
import random
from pytz import timezone
from bs4 import BeautifulSoup


city = input("Write your city: \n")  

def weather_api(query):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q":query,"lang":"eng"}

    headers = {
       'x-rapidapi-key': "Your API key",
       'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    description = data['weather'][0]['description']
    temperature = str(round(data['main']['temp'] - 273.15, 1)) + 'C'
    pressure = str(data['main']['pressure']) +'hPa'
    humidity = str(data['main']['humidity']) + '%'
    wind = str(data['wind']['speed']) + 'km/h'
    weather = {'description': description, 'temperature': temperature, 'pressure': pressure,
               'humidity': humidity, 'wind': wind}
    return weather


def time_and_data():
     today = datetime.datetime.today()
     print(f"""Today is {today.strftime('%A')}, {today.day}-{today.month}-{today.year} and time now is {today.hour}:{today.strftime('%M')}\n""")


def quote():
     url = "https://type.fit/api/quotes"
     response = requests.get(url).json()
     quote_res = random.choice(response)
     print(f'The random quote for today is:\n{quote_res["text"]}\nAuthor: {quote_res["author"]}\n') 


def time_in_world():
    time = '%d-%m-%Y %H:%M:%S'
    print("New York: {}".format(datetime.now(timezone("US/Eastern")).strftime(time)))
    print("London: {}".format(datetime.now(timezone("Europe/London")).strftime(time)))
    print("Beijng: {}".format(datetime.now(timezone("Asia/Shanghai")).strftime(time)))


def name_day():
    url = "https://imienniczek.pl/widget/js"
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, "html.parser")
    for day in soup.find_all("span"):
        print(day.text)


weather_info = weather_api(city)
print(f'The weather in {city} is {weather_info["description"]}.')
print(f'The details are: temperature is {weather_info["temperature"]}, pressure is {weather_info["pressure"]}, humidity is {weather_info["humidity"]} and wind is {weather_info["wind"]}.\n' )
time_and_data()
quote()
time_in_world()
name_day()