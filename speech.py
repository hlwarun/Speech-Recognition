import pyttsx3
import speech_recognition as sr

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

def listening():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('Listening...')
        r.pause_threshold = 1
        sound = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print('Analyzing the input...')
            query = r.recognize_google(sound)
            print(f"Query:\t {query}")

        except Exception as e:
            speak("Sorry! I didn't get you. Please say again.")
            return 'none'
        return query


if __name__ == "__main__":
    listening()
