import requests
import wikipedia
import webbrowser
import smtplib
from engines import *
from device_controllers import listening

def my_ip_address():
    ip_address = requests.get("https://api.ipify.org").text
    speak(f"Your IP address is {ip_address}")

def youtube_search():
    speak("Keep patience, we are connecting...")
    webbrowser.open("youtube.com")

def my_website():
    speak("Keep patience, we are connecting...")
    webbrowser.open("ghimirearun.com.np")

def google_search():
    speak("What do you want me to search on google?")
    search_query = listening().lower()
    if "nothing" in search_query or "none" in search_query:
        webbrowser.open("google.com")
    else:
        # For this to work the default search engine of your browser should be set to google.com
        webbrowser.open(f'{search_query}')

def send_email():
    try:
        speak("Please type the email address of the receiver!")
        send_to = input("Email address of the receiver: ")
        speak("What should I say to the receiver?")
        email_body = listening().lower()

        # Enabling and logging to gmail server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("YOUR EMAIL ADDRESS", "YOUR EMAIL PASSWORD")
        server.sendmail("YOUR EMAIL ADDRESS", send_to, email_body)
        server.close()

        speak("Email has been sent!")
    except Exception as e:
        speak("Sorry! Email could not be sent.")

def wikipedia_search(query):
    speak("Keep patience, we are searching...")
    query = query.replace('wikipedia', "")
    result = wikipedia.summary(query, sentences=3)
    speak(f"According to wikipedia, {result}.")
