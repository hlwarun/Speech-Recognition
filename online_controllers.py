import requests
from engines import *

def my_ip_address():
    ip_address = requests.get("https://api.ipify.org").text
    speak(f"Your IP address is {ip_address}")
