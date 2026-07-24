import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

recognizer= sr.Recognizer()
engine = pyttsx3.init("sapi5")


def greet():
    hour=datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Good Morning!"

    elif 12 <= hour < 17:
        greeting = "Good Afternoon!"

    elif 17 <= hour < 21:
        greeting = "Good Evening!"

    else:
        greeting = "Good Night!"

    speak(f"{greeting}")


def listen():
   with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio=recognizer.listen(source,timeout=5,phrase_time_limit=6)
   try:
       print("Recognizing...")
       text=recognizer.recognize_google(audio)
       print("you said: ",text)
       return text
   
   except sr.UnknownValueError:
       print("Sorry , I did't Understand.")

   except sr.RequestError as e:
       print("Sorry ,There was an earror in retriving audio ",e)

   except sr.WaitTimeoutError:
       speak("ï didn't hear any thing")

   return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant said : ",text)

greet()
speak(f"Hello ,How may I assist you")

while True:
    command=listen().lower()

    if not command:
        speak("Please repeat.")
        continue

    if "hello" in command:
        speak(f"how may i help you ")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "time" in command:
        time=datetime.now().strftime("%I:%M %p")
        speak(f"current time is {time}")

    elif "date" in command:
        date=datetime.now().strftime("%d %B %Y")
        speak(f"current date is {date}")

    elif "search" in command:
        speak("what you want to search for ")
        query=listen()

        if query:
            speak(f"searching for {query}",)
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        else:
            speak("Sorry, I couldn't understand your search.")

    elif any(word in command for word in ['goodbye','good bye','bye',"éxit"]):
        speak("Good bye. have a nice day")
        break

    else:
        speak("Sorry, I don't know that command yet.")