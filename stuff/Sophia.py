import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import json
import os
import time
import pyautogui
import webbrowser as wb

listener = sr.Recognizer()
engine = pyttsx3.init()
r = sr.Recognizer()
keywords = [("jarvis", 1), ("hey jarvis", 1), ] # setting up our 'wake' words
source = sr.Microphone() #setting up which mic we are using

def takeCommand():
   rate = 200 #Sets the default rate of speech
   engine = pyttsx3.init() #Initialises the speech engine
   voices = engine.getProperty('voices') #sets the properties for speech
   engine.setProperty('voice', voices[1].id) #Gender and type of voice
   engine.setProperty('rate', rate+50) #Adjusts the rate of speech
   engine.runAndWait() #waits for speech to finish and then continues with program

def Speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning!, sir")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon!, sir")

    else:
        Speak("Good Evening!, sir")

    Speak("I am Sophia. How may I assist you today?")

def track_location():
    api_key = "YOUR_IPSTACK_API_KEY"  # Replace with your actual API key

    response = requests.get(f"http://api.ipstack.com/check?access_key={api_key}")
    data = json.loads(response.text)

    if "city" in data:
        city = data["city"]
        region = data["region_name"]
        country = data["country_name"]

        Speak(f"You are currently in {city}, {region}, {country}.")
    else:
        Speak("I'm sorry, but I couldn't determine your current location.")

def process_query(query):
    if "sophia" in query:
        if "what's your name" in query or "Sophia" in query:
            Speak("My name is Sophia. I'm an AI assistant here to assist you.")

        elif "how attractive am I today" in query:
            Speak("You are looking extremely attractive today.")

        elif "who's the best" in query:
            Speak("You are, sir. No doubt about it.")

        elif "how are you" in query:
            Speak("I'm functioning optimally, ready to assist you.")

    

    elif "monitor and announce malfunctions" in query:
        Speak("Monitoring for malfunctions. I will announce any detected issues.")

    elif "direct a route to" in query:
        destination = query.split("direct a route to")[1].strip()
        # Code to calculate and direct the route

    elif "calculate the distance between" in query:
        locations = query.split("calculate the distance between")[1].strip()
        location_1, location_2 = locations.split("and")
        # Code to calculate the distance between the two locations
        # Code to handle the chronometer or timer functionality

        
    elif "open fl studio" in query:
        Speak("Opening FL Studio.")
        os.startfile("C:\Program Files\Image-Line\FL Studio 20\FL64.exe")

    elif "open Chrome" in query:
        Speak("Opening Chrome.")
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")


    elif "open" in query:
        Speak("Opening.")
        os.startfile()

    elif "play" in query:
        query = query.replace('play', '')
        Speak('Playing' + query)
        pywhatkit.playonyt(query)

    elif "hidden menu" in query:
            # Win+X: Open the hidden menu
            pyautogui.hotkey('winleft', 'x')

    elif "task manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

    elif "task view" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

    elif "take screenshot" in query:
            # win+perscr
            pyautogui.hotkey('winleft', 'prtscr')
            Speak("done")

    elif "close the app" in query:
            pyautogui.hotkey('alt', 'f4')


    # Add the rest of the elif conditions for the queries you provided

    else:
        Speak("Sorry, I didn't catch that. Could you please repeat?")
    
    
def set_alarm(alarm_time):
    current_time = datetime.datetime.now().strftime("%H:%M")
    
    while current_time != alarm_time:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("21:30")


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    Speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    Speak("The current date is")
    print(day, month, year)
    Speak(day)
    Speak(month)
    Speak(year)







# Main program
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand()
        process_query(query)





       
















