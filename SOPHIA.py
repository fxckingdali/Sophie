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
import webbrowser 
import webbrowser as wb
import subprocess
import pygame
import psutil
import pywhatkit as kit




from Features.custom_voice import speak
from Features.play_songs import play_songs
from Features.weather import get_weather_data, get_recommendation







engine = pyttsx3.init()
voices = engine.getProperty('voices')
voicespeed = 170
engine.setProperty


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!, sir, How may I assist you today?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!, sir. How may I assist you today?")

    else:
        speak("Good Evening!, sir. How may I assist you today?")

def get_weather_data(json_data):
    description_of_weather = json_data['weather'][0]['description']
    temperature = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    weather_details = "The weather is {} with a temperature of {}°C, humidity at {}%, and wind speed of {} m/s.".format(
        description_of_weather, temperature, humidity, wind_speed)
    return weather_details

def get_recommendation(weather_data):
    recommendation = ""
    if "rain" in weather_data.lower():
        recommendation = "Don't forget to take an umbrella with you sir."
    elif "snow" in weather_data.lower():
        recommendation = "Bundle up and wear warm clothing sir."
    elif "sun" in weather_data.lower():
        recommendation = "It's going to be a sunny day. Don't forget to apply sunscreen sir."
    else:
        recommendation = "Enjoy your day, sir!"

    return recommendation

def weather(city):
    api_key = "2d86172af916bbaef8e46e2f84dc3739"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",
        "appid": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        json_data = response.json()
        if json_data["cod"] == 200:
            weather_details = get_weather_data(json_data)
            recommendation = get_recommendation(weather_details)
            print(weather_details)
            print(recommendation)
            speak(weather_details)
            speak(recommendation)
        else:
            print("Unable to retrieve weather information.")
            speak("Sorry, I couldn't fetch the weather information sir.")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        speak("Sorry, an error occurred while fetching the weather information sir.")    

def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery:
        percentage = battery.percent
        speak(f"The current battery percentage is {percentage} percent.")
        if percentage < 20:
            speak("Warning! Low battery level sir.")


def introduce():
    speak("Hello! I am Sophia, Mr. John's personal assistant, my name stands for Smart Operational Program for Hyperintelligent and Ingenious Assistance, and Im here to fulfill all of your needs and desires.")




def mute():
    global is_muted
    is_muted = True
    engine.stop()


def resume():
    global is_muted
    is_muted = False


def stop():
    engine.stop()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print(e)
        return "---"
    return query

def track_location():
    api_key = "65542d4a605aa298432fa7e3a1a3168a"  # Replace with your actual API key

    response = requests.get(f"http://api.ipstack.com/check?access_key={api_key}")
    data = json.loads(response.text)

    if "city" in data:
        city = data["city"]
        region = data["region_name"]
        country = data["country_name"]

        speak(f"You are currently in {city}, {region}, {country}.")
    else:
        speak("I'm sorry, but I couldn't determine your current location.")


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=1644de86aa5e471d8a613689ea8814be"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    for ar in articles:
        head.append(ar["title"])

    for i in range(len(day)):
        speak(f"Today's {day[i]} news is: {head[i]}")


    



def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is " + time)
    print("The current time is " + time)


def date():
    now = datetime.datetime.now()
    day = now.day
    month = now.strftime("%B")  # Get the month name
    year = now.year

    speak("Today is")
    speak(month)
    speak(str(day))  # Convert day to string for better speech synthesis
    speak("and the year is")
    speak(str(year))  # Convert year to string for better speech synthesis



        
# Open chrome/website
def open_chrome():
    url = "https://www.google.co.in/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)


if __name__ == "__main__":

    wishme()
    weather("Vitoria-Gasteiz")
    


    try:

        while True:
            query = takeCommand().lower()
            print(query)
            

            if "good morning" in query:
                speak("good morning sir")

            elif "time" in query:
                time()

            elif "date" in query:
                date()

            # open chrome
            elif "open chrome" in query:
                open_chrome()

            # Wikipedia search
            elif "wikipedia" in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
                print(result)

            # Chrome search
            elif "search website" in query:
                speak("what should i search?")
                chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search + ".com")

            # Random jokes
            elif "joke" in query:
                speak(pyjokes.get_jokes())

            elif "introduce yourself" in query:
                speak("Hi, I am Sophia and I'm Mr. John's personal virtual assistant. Nice to meet you")

            

            

           
           
            
            
            elif "who's the best" in query:
                speak("You are, sir. No doubt about it.")

            elif "how are you" in query:
                speak("I'm functioning optimally, ready to assist you.")

            elif "open fl studio" in query:
                speak("Opening FL Studio.")
                os.startfile("C:\Program Files\Image-Line\FL Studio 20\FL64.exe")

            elif "open Chrome" in query:
                speak("Opening Chrome.")
                os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            
            elif "play" in query:
                query = query.replace('play', '')
                speak('Playing' + query)
                pywhatkit.playonyt(query)
            
            elif "where i am" in query or "where are we" in query:
                track_location()
            
            elif "close the app" in query:
                pyautogui.hotkey('alt', 'f4')


            elif "hidden menu" in query:
            # Win+X: Open the hidden menu
               pyautogui.hotkey('winleft', 'x')

            elif "task manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
               pyautogui.hotkey('ctrl', 'shift', 'esc')
            
            elif "mute device" in query:
               pyautogui.hotkey ('f6')

            

            elif "task view" in query:
            # Win+Tab: Open the Task view
               pyautogui.hotkey('winleft', 'tab')
            
            elif "drop my needle" in query:
               play_songs()
            
            elif "open instagram" in query:
                webbrowser.open("instagram.com")

            elif "open tiktok" in query:
                webbrowser.open("tiktok.com")

            elif "open my tv series" in query:
                speak("Opening Brokie Netflix sir.")
                os.startfile("C:/Users/Dani/OneDrive/Escritorio/InkaPelis.lnk")
            
            elif "weather of a city" in query:
                speak("Sure, please provide the city name.")
                city = takeCommand().lower()
                weather(city)

            elif "weather" in query:
                weather("Vitoria-Gasteiz")
            
            elif "open gmail" in query:
                speak("Opening Gmail sir.")
                os.startfile("C:/Users/Dani/OneDrive/Escritorio/Gmail.lnk")

            elif "open sports" in query:
                speak("Opening Brokie Sports channel sir.")
                os.startfile("C:/Users/Dani/OneDrive/Escritorio/Futemax.lnk")

            elif "open Blender" in query:
                speak("Opening Blender sir.")
                os.startfile("C:/Users/Dani/OneDrive/Escritorio/Blender 3.5.lnk")
            
            elif "open SketchUp" in query:
                speak("Opening sketchup sir.")
                os.startfile("C:/Users/Dani/OneDrive/Escritorio/SketchUp Web.lnk")
            
            elif "open YouTube" in query:
                speak("Opening YouTube sir.")
                os.startfile("C:/Users/Dani/OneDrive/Escritorio/YouTube.lnk")
            
            elif "open google" in query:
                speak("sir, what should I search on Google?")
                cm = takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif "listen to Mozart" in query:
                pywhatkit.playonyt("requiem")
                speak("playing your favourite classic sir")

            elif "tell me the news" in query:
                speak("please wait sir, fetching the latest news")
                news()
            
            elif "thanks" in query or "thank you" in query:
                speak("You're welcome, sir. It's my pleasure to assist you.")

            elif "hey" in query:
                speak("Hello, sir. How may I assist you today?")

            elif "how am I looking today" in query or "how am I" in query:
                speak("You are looking extremely attractive today. As always, sir.")

            elif "open my movies" in query:
   
                website = "https://ridomovies.tv"
                webbrowser.open(website)

            




        


            

    except Exception:
        print("something went wrong!")