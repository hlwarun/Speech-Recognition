import os
import datetime
import random
import speech_recognition as sr
from engines import *

def listening():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('Listening...')
        r.pause_threshold = 1
        sound = r.listen(source, timeout=None, phrase_time_limit=5)

        try:
            print('Analyzing the input...')
            query = r.recognize_google(sound)
            print(f"Query:\t {query}")

        except Exception as e:
            speak("Sorry! I didn't get you. Please say again.")
            return 'none'
        return query

def greetings():
    time = datetime.datetime.now().hour
    if time < 12:
        speak('Good morning sir!')
    elif time >= 12 and time < 17:
        speak('Good afternoon sir!')
    else:
        speak('Good evening sir!')
    speak('How can I help you?')

def current_time():
    timenow = datetime.datetime.now()
    timenow = datetime.datetime.strptime(f"{timenow.hour}:{timenow.minute}", "%H:%M")
    timenow = timenow.strftime("%I:%M %p")
    speak(f"The time now is {timenow} ")

def today_date():
    date_today = datetime.datetime.now().date()
    speak(f"You are living in {date_today} ")

def play_music():
    music_path = "C:\\Users\\ARUN\\Music"
    songs = os.listdir(music_path)
    choices = random.choice(songs)
    for song in songs:
        if song.endswith('.mp3'):
            os.startfile(os.path.join(music_path, choices))
