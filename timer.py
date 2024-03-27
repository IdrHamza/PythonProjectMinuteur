
from exercice_sound import *





class Timer:
    def __init__(self, time_exercise, time_rest, time_rest_series):
        self.time_exercise = time_exercise  
        self.time_rest = time_rest
        self.time_rest_series = time_rest_series

    def run_workout(self, exercises,series):
        for serie in range(1,series+1):
            serieStart(serie)
            for exercise in exercises:
                print(f"Exercice: {exercise.name}")
                exercicestart(exercise)
                for i in range(self.time_exercise):
                    sleep(1)
                    print(i)


                print("Repos entre exercices")
                exercicesrest()
                for i in range(self.time_rest):
                    sleep(1)
                    print(i)


            print("Repos entre séries")
            serierest(serie)

            for i in range(self.time_rest_series):
                sleep(1)
                print(i)
        finish_sound.play()