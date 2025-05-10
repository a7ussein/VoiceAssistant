# VoiceAssistant.py

A simple Python-based voice-controlled assistant developed by **Ahmed Hussein**. The assistant listens for simple voice commands, converts speech to text, and performs automated tasks such as telling the time, searching the web, telling jokes, reporting the weather, and setting timers.

---

## Features

- Voice-activated using **“Hey Assistant”**
- Understands and executes five commands:
  - **"What time is it?"** – Speaks the current system time
  - **"Search for [query]"** – Opens a browser search for the query
  - **"Tell me a joke."** – Tells a random joke using `pyjokes`
  - **"What’s the weather like?"** – Retrieves current weather using OpenWeatherMap API
  - **"Set a timer for [X] seconds."** – Sets a countdown timer and alerts when done

---

## Requirements

Install the required Python packages:

```bash
pip install pyjokes requests SpeechRecognition pyttsx3
pip install pyaudio 
