import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)  # Max volume

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

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
    speak("I am Jarvis, how can I help you today?")

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

# Main program execution
if __name__ == "__main__":
    greetme()
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

#to open web browsers

#Youtube
        elif query and 'open youtube' in query.lower():
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

# Stack Overflow
        elif query and 'open stackoverflow' in query.lower():
            speak("Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")

# Google
        elif query and 'open google' in query.lower():
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

#linkedIn
        elif query and 'open linkedin' in query.lower():
            speak("Opening LinkedIn...")
            webbrowser.open("https://www.linkedin.com")

# GitHub
        elif query and 'open github' in query.lower():
            speak("Opening GitHub...")
            webbrowser.open("https://www.github.com")

#to play music

        music_dir = {
            "Kishore Kumar": "C:\\Users\\Arpit\\Desktop\\musics\\Arijit singh",
            "Arijit Singh": "C:\\Users\\Arpit\\Desktop\\musics\\Arpit",
            "Radhe Radhe": "C:\\Users\\Arpit\\Desktop\\musics\\Radhe Radhe",
            "Arpit": "C:\\Users\\Arpit\\Desktop\\musics\\Kishore Kumar"}
        if query and 'play music' in query.lower():
            speak("Which music do you want to play? You can say Kishore Kumar, Arijit Singh, Radhe Radhe, or Arpit.")
            artist = takecommand()
            print("Recognized:", artist)
        if artist:
            artist = artist.strip().lower()
            found = None
            for key in music_dir:
                if artist in key.lower():
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

#time and date 
        elif query and "the time" in query.lower():
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strtime}")
            speak(f"Sir, the time is {strtime}")
        elif query and "the date" in query.lower():
            strdate = datetime.datetime.now().strftime("%d %B %Y")
            print(f"Sir, the date is {strdate}")
            speak(f"Sir, the date is {strdate}")

#to open applications

        elif query and 'open code' in query.lower():
            speak("Opening Visual Studio Code...")
            code_path = "C:\\Users\\Arpit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif query and 'open notepad' in query.lower():
            speak("Opening Notepad...")
            notepad_path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepad_path)

        elif query and 'open calculator' in query.lower():
            speak("Opening Calculator...")
            calculator_path = "C:\\Windows\\System32\\calc.exe"
            os.startfile(calculator_path)

#for exiting the program
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
            speak("You're welcome, sir!")

                    
       
