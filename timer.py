from time import sleep
import winsound
from gtts import gTTS
import pygame
from gtts import gTTS
import pygame
import time

# Initialize the Pygame mixer
pygame.mixer.init()

# Text to speech conversion function
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# Generate audio files for "start" and "finish"
text_to_speech("start set", "start.mp3")
text_to_speech("finish exercice", "finish.mp3")

# Load the audio files
start_sound = pygame.mixer.Sound("start.mp3")
finish_sound = pygame.mixer.Sound("finish.mp3")



class Timer:
    def __init__(self, time_exercise, time_rest, time_rest_series):
        self.time_exercise = time_exercise  
        self.time_rest = time_rest
        self.time_rest_series = time_rest_series

    def run_workout(self, exercises,series):
        for serie in range(1,series+1):
            text_to_speech(f"set number {serie}", "startserie.mp3")
            start_sound_serie = pygame.mixer.Sound("startserie.mp3")
            start_sound_serie.play()
            sleep(2)

            for exercise in exercises:
                print(f"Exercice: {exercise.name}")
                text_to_speech(f" {exercise.name}", "startexercice.mp3")
                start_sound_exercice = pygame.mixer.Sound("startexercice.mp3")

                start_sound_exercice.play()
                sleep(2)


                winsound.Beep(1500,1000)
                sleep(1)
                winsound.Beep(1500, 1000)
                sleep(1)
                start_sound.play()

                for i in range(self.time_exercise):
                    sleep(1)
                    print(i)


                print("Repos entre exercices")
                text_to_speech("rest exercice ", "rest.mp3")
                rest= pygame.mixer.Sound("rest.mp3")
                rest.play()
                sleep(2)
                for i in range(self.time_rest):
                    sleep(1)
                    print(i)


            print("Repos entre séries")
            text_to_speech(f"finish set number {serie}", "finishserie.mp3")
            finish_sound_serie = pygame.mixer.Sound("finishserie.mp3")
            finish_sound_serie.play()
            sleep(2)

            for i in range(self.time_rest_series):
                sleep(1)
                print(i)
        finish_sound.play()