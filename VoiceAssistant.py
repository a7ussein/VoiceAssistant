# File: VoiceAssistant.py
# Author: Ahmed Hussein
# Date: 2022-02-20
# Description: A Python-based voice-controlled assistant that listens for voice commands,
# converts speech to text, and performs automated tasks.

# Input/Output
# Input: Voice commands
# Process: Activate voice assistant by saying "Hey Assistant" then start the command processing
# Output: Automated tasks performed

# Pseudocode: 
# 1. Initialize recognizer
# 2. Function listen()
# 3. Function process_command()
# 4. Function speak()

import pyjokes
import requests
import speech_recognition  # for speech to text
import pyttsx3  # for text to speech
import webbrowser  # for web search
import datetime
import time  # needed for sleep()

recognizer = speech_recognition.Recognizer()
speaker = pyttsx3.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def listen():
    with speech_recognition.Microphone() as mic:
        print("Say something...")
        audio = recognizer.listen(mic)
        try:
            return recognizer.recognize_google(audio).lower()
        except:
            speak("I didn't understand.")
            return ""

def getTime():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"It is {now}")

def search(query):
    webbrowser.open(f"https://google.com/search?q={query}")
    speak(f"Searching for {query}")

def tellJoke():
    joke = pyjokes.get_joke()
    speak(joke)

def getWeather():
    key = "" # gotta hide my api key hehe
    city = "Maine"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    try:
        res = requests.get(url)
        data = res.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        speak(f"It is {desc} with {temp} degrees Celsius in {city}.")
    except:
        speak("Sorry, I couldn't get the weather.")

def setTimer(seconds):
    speak(f"Timer set for {seconds} seconds")
    time.sleep(seconds)
    speak("Time's up!")

def handle(command):
    if "time" in command:
        getTime()
    elif "search for" in command:
        search(command.replace("search for", ""))
    elif "joke" in command:
        tellJoke()
    elif "weather" in command:
        getWeather()
    elif "set a timer for" in command:
        try:
            seconds = int(command.replace("set a timer for", "").strip())
            setTimer(seconds)
        except:
            speak("Please specify the time in seconds.")
    else:
        speak("Try a different command.")

def main():
    speak("Say 'hey assistant' to start.")
    while True:
        if "hey assistant" in listen():
            speak("What do you want?")
            handle(listen())

main()
