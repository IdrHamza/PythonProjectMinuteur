from time import sleep
import winsound
from gtts import gTTS
import pygame
from gtts import gTTS
import pygame
import time


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
def serieStart(serie):
    text_to_speech(f"set number {serie}", "startserie.mp3")
    start_sound_serie = pygame.mixer.Sound("startserie.mp3")
    start_sound_serie.play()
    sleep(2)
def serierest(serie):
    text_to_speech(f"finish set number {serie}", "finishserie.mp3")
    finish_sound_serie = pygame.mixer.Sound("finishserie.mp3")
    finish_sound_serie.play()
    sleep(2)

def exercicestart(exercise):
    text_to_speech(f" {exercise.name}", "startexercice.mp3")
    start_sound_exercice = pygame.mixer.Sound("startexercice.mp3")

    start_sound_exercice.play()
    sleep(2)

    start_sound.play()

def exercicesrest():
    text_to_speech("rest exercice ", "rest.mp3")
    rest = pygame.mixer.Sound("rest.mp3")
    rest.play()
    sleep(2)
