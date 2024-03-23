from timer import *
from exercice import *
nombre_exercices = int(input("Entrer le nombre d'exercices : "))
number_of_serie=int(input("Entrer le nombre de serie  "))
exercises = []

for _ in range(nombre_exercices):
    nom = input("Entrer le nom de l'exercice : ")
    exercise = Exercise(nom)
    exercises.append(exercise)

time_exercise = int(input("Temps d'entraînement (en secondes) : "))
time_rest = int(input("Temps de repos entre exercices (en secondes) : "))
time_rest_series = int(input("Temps de repos entre séries (en secondes) : "))

timer = Timer(time_exercise, time_rest, time_rest_series)
timer.run_workout(exercises,number_of_serie)