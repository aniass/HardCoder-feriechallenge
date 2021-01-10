"""
Napisz program, który na podstawie masy [kg] i wzrostu [cm] wylicza wskaźnik BMI 
(https://en.wikipedia.org/wiki/Body_mass_index) oraz informuje użytkownika, w jakim jest zakresie. Zakresy można wpisać 
“z palca” (ale może nieco mądrzej niż ciągiem if-elif-else dla każdego zakresu! 😉 ) albo odczytać z dowolnego API, np. 
https://rapidapi.com/navii/api/bmi-calculator?fbclid=IwAR1aTsYVMzd3lYZ7EhSeW7zFd1JOBDiF6crz3HhchBnxf_vq56WBxoYH26o
Następnie program losuje jedną z aktywności fizycznych oraz czas jej 
wykonania, np. bieganie przez 30 minut. Czas nie może być dłuższy niż podany przez użytkownika (maksymalny czas, który 
można poświęcić na ćwiczenia). Zadbaj o to, aby czas aktywności był jakoś uzależniony od BMI (na przykład osoba z 
niedowagą nie powinna ćwiczyć mniej niż osoba o wadze normalnej - ustal pewien minimalny czas; ale już osoba z nadwagą 
powinna ćwiczyć dłużej - ustal odpowiedni nieliniowy mnożnik, tak aby nie przekroczyć maksimum). Utwórz w ten sposób 
plan treningowy na 7 następnych dni, wyniki zapisując do pliku .txt.
Propozycja rozszerzenia: przygotuj urozmaicony plan treningowy uwzględniający maksymalny czas wpisany przez użytkownika 
- kilka aktywności fizycznych ma wypełniać całą dzienną ilość czasu, mają zajmować jakąs ustaloną minimalną długość 
(np. 10 minut) oraz nie mogą się powtarzać jednego dnia.

"""
import random


bmi_categories = {0: "very severely underweight ",
                 15: "severely underweight",
                 16: "underweight",
                 18.5: "normal (healthy weight)",
                 25: "overweight",
                 30: "obese Class I (Moderately obese)",
                 35: "obese Class II (Severely obese)",
                 40: "obese Class III (Very severely obese)"}


def calc_bmi(mass,height):
    bmi = mass/((height / 100) **2)
    
    for key, names in bmi_categories.items():
        if bmi >= key:
            bmi_names = names
        else:
            break
    print(f'Your BMI value is: {bmi:.2f} and you have {bmi_names}.')
    return bmi


def exercise_time(bmi):
    if bmi <= 16:
        time = random.randint(1, max_time)
    elif bmi <= 25:
        time = random.randint(10, max_time)
    elif bmi <= 30:
        time = random.randint(20, max_time)
    elif bmi <= 35:
        time = random.randint(30, max_time)
    else:
        time = random.randint(30, max_time)
    return time
    

def training_plan():
    activities_list = ['running', 'aerobic', 'swimming', 'dance', 'walking', 'cycling']
    with open("training plan .txt", "w", encoding="UTF-8") as file:
        for num_day in range(1,8):
            sports = random.choice(activities_list)
            file.write(f'Your training for day {num_day} your exercise is "{sports}" for {get_activities} minutes.\n')
        file.close()
        print("This is your training plan for the next week. Check your txt fie.")


height = int(input('Write your height in centimeters:\n'))
mass = int(input('Write your weight in kilograms:\n'))
bmi = calc_bmi(mass, height)
max_time = int(input("Write your minimum time that you can do exercise, minimum is 10 minutes: "))
get_activities = exercise_time(bmi)
training_plan()
    