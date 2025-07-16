import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import tkinter as tk
import threading
import cv2
from PIL import Image, ImageTk
import sys
import vlc
import time
import multiprocessing


contacts = {"papa": "verma.vijay1092@gmail.com",
            "arpit": "vermaarpit627@gmail.com",
            "devansh": "devanshkumar1103@gmail.com"
            }  # Example contacts, replace with actual emails

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)  # Max volume

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak the given audio
def speak(audio):
    print("Speaking:", audio)
    engine.say(audio)
    engine.runAndWait()

# Greeting according to time
def greetme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")

def takecommand():
    # It takes voice input and returns it as a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        speak("Sorry, speak again!")
        return None


#to send email

def sendEmail(to, content):
    # Replace with your email credentials
    your_email = "vermaarpit627@gmail.com"
    your_password = "aark eucp vnha pkbt"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your mail server if not Gmail
        server.ehlo()
        server.starttls()
        server.login(your_email, your_password)
        server.sendmail(your_email, to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        print(e)
        speak("Sorry sir, I was not able to send the email.")

# Add VLC directory to the system path
os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")


# Function to play Jarvis video using VLC
import subprocess
import os

def play_jarvis_overlay():
    video_path = r"C:\Users\Arpit\Desktop\Arpit Python\python in vs code\jarvis_video.mp4.mp4"

    if not os.path.exists(video_path):
        print("❌ Video not found.")
        return

    subprocess.Popen([
        r"C:\Program Files\VideoLAN\VLC\vlc.exe",
        video_path,
        "--fullscreen",
        "--no-video-title-show",
        "--no-video-deco",
        "--no-qt-fs-controller",
        "--video-on-top",
        "--loop",
        "--qt-start-minimized",
        "--quiet",
        "--no-qt-privacy-ask"
    ])

    
# Main program execution
if __name__ == "__main__":
    greetme()
    video_process = None 
    while True:
        query = takecommand()


        if query and 'wikipedia' in query.lower(): 
            speak("Searching Wikipedia...")
            query = query.lower().replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")
                

        elif query and 'open youtube' in query.lower():
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif query and 'open stackoverflow' in query.lower():
            speak("Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")

        elif query and 'open google' in query.lower():
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif query and 'open linkedin' in query.lower():
            speak("Opening LinkedIn...")
            webbrowser.open("https://www.linkedin.com")

        elif query and 'open github' in query.lower():
            speak("Opening GitHub...")
            webbrowser.open("https://www.github.com")

        elif query and 'play music' in query.lower():
            music_dir = {
                "Arpit": "C:\\Users\\Arpit\\Desktop\\Arpit Python\\python in vs code\\Music\\Arpit",
                "Arijit Singh": "C:\\Users\\Arpit\\Desktop\\Arpit Python\\python in vs code\\Music\\Arijit singh",
                "Radhe Radhe": "C:\\Users\\Arpit\\Desktop\\Arpit Python\\python in vs code\\Music\\Radhey Radhey",
                "Kishore Kumar": "C:\\Users\\Arpit\\Desktop\\Arpit Python\\python in vs code\\Music\\Kishore kumar"
                }  # Add your music directories here

            speak("Which music do you want to play? You can say Kishore Kumar, Arijit Singh, Radhe Radhe, or Arpit.")
            artist = takecommand()
            print("Recognized:", artist)

            if artist:
                artist = artist.strip().lower()
                found = None
                for key in music_dir:
                    print(f"Checking if '{key.lower()}' in '{artist}'")
                    if key.lower() in artist:
                        found = key
                        break

                if found:
                    songs = os.listdir(music_dir[found])
                    if songs:
                        song = random.choice(songs)
                        os.startfile(os.path.join(music_dir[found], song))
                        speak(f"Playing {song} by {found}.")
                    else:
                        speak("The folder is empty.")
                else:
                    speak("Sorry, I don't have that music.")
            else:
                speak("Sorry, I didn't catch the artist name.")

        elif query and "the time" in query.lower():
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strtime}")
            speak(f"Sir, the time is {strtime}")

        elif query and "the date" in query.lower():
            strdate = datetime.datetime.now().strftime("%d %B %Y")
            print(f"Sir, the date is {strdate}")
            speak(f"Sir, the date is {strdate}")

        elif query and 'open notepad' in query.lower():
            speak("Opening Notepad...")
            notepad_path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepad_path)

        elif query and 'open calculator' in query.lower():
            speak("Opening Calculator...")
            calculator_path = "C:\\Windows\\System32\\calc.exe"
            os.startfile(calculator_path)

        elif query and 'send email' in query.lower():
            try:
                speak("To whom should I send the email?")
                name = takecommand()
                if name:
                    name = name.lower()
                    if name in contacts:
                        to = contacts[name]
                        speak(f"Email will be sent to {name} at {to}.")

                        speak("What should I say?")
                        content = takecommand()

                        if content:
                            sendEmail(to, content.strip())
                        else:
                            speak("Sorry, I didn't catch the message.")
                    else:
                        speak("Sorry, I don't have an email saved for that name.")
                else:
                    speak("Sorry, I didn't catch the name.")
            except Exception as e:
                print(e)
                speak("Sorry sir, I was not able to send the email.")

        if query and 'hello jarvis' in query.lower():
            speak("Hello sir, Jarvis is activated!")
            play_jarvis_overlay()

        elif query and 'exit' in query.lower():
            speak("Goodbye sir, have a nice day!")
            break
        elif query and 'stop' in query.lower():
            speak("Goodbye sir, have a nice day!")
            break
        elif query and 'bye' in query.lower():
            speak("Goodbye sir, have a nice day!")
            break
        elif query and 'thank you' in query.lower():
            speak("You are welcome sir, have a nice day!")
            break




