import pyttsx3

engine = pyttsx3.init('sapi5')

rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(sound):
    engine.say(sound)
    engine.runAndWait()




if __name__ == "__main__":
    speak('hello there')
