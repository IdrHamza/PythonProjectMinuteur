
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
                for i in range(1,self.time_exercise+1):
                    sleep(1)
                    print(i)


                print("Repos entre exercices")
                exercicesrest()
                for i in range(1,self.time_rest+1):
                    sleep(1)
                    print(i)



            if serie<series:
                print("Repos entre séries")
                serierest(serie)

                for i in range(1,self.time_rest_series +1):
                    sleep(1)
                    print(i)
        finish_sound.play()