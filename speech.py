import os
from controllers import *

if __name__ == "__main__":
    greetings()
    if 1:
        query = listening().lower()
        if "notepad" in query:
            os.startfile("C:\\Windows\\System32\\notepad.exe")
        elif "command prompt" in query:
            os.system("start cmd")
        elif "time" in query:
            current_time()
        elif "date" in query:
            today_date()
        elif "music" in query or "song" in query  or "sing" in query or "songs" in query:
            play_music()
