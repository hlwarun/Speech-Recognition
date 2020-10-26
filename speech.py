import os
import sys
from device_controllers import *
from online_controllers import *

if __name__ == "__main__":
    greetings()
    while True:
        query = listening().lower()
        if "command prompt" in query:
            os.system("start cmd")
        elif "notepad" in query:
            os.startfile("C:\\Windows\\System32\\notepad.exe")
        elif "time" in query:
            current_time()
        elif "date" in query:
            today_date()
        elif "music" in query or "song" in query  or "sing" in query or "songs" in query:
            play_music()
        elif "ip address" in query:
            my_ip_address()
        elif "youtube" in query:
            youtube_search()
        elif "my website" in query:
            my_website()
        elif "google" in query:
            google_search()
        elif "wikipedia" in query:
            wikipedia_search(query)
        elif "exit" in query or "quit" in query or "sleep" in query:
            speak("It was fun working with you! See you soon.")
            sys.exit()
        elif "send email" in query:
            send_email()
        speak("Do you want me to go on, or should i quit?")
