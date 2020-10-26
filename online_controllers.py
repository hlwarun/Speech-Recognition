import requests
import wikipedia
import webbrowser
from engines import *

def my_ip_address():
    ip_address = requests.get("https://api.ipify.org").text
    speak(f"Your IP address is {ip_address}")

def wikipedia_search(query):
    speak("Keep patience, we are searching...")
    query = query.replace('wikipedia', "")
    result = wikipedia.summary(query, sentences=3)
    speak(f"According to wikipedia, {result}.")

def my_website():
    speak("Keep patience, we are connecting...")
    webbrowser.open("ghimirearun.com.np")
