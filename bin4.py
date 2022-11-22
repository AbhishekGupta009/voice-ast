from ast import main
from msilib import MSIMODIFY_VALIDATE_NEW
from multiprocessing.spawn import _main
from tkinter.tix import MAIN
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import folium
import winshell
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak ("Good evening")
    speak("Hello i am assistant of abhishek gupta ,how may i help you ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        print("Say that agin please...")
        return"None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open  youtube' in query:
            webbrowser.open("youtube.com")
         #   os.startfile(codePath)
        elif 'play music' in query:
            music_dir = 'F:\\Audio songs\\punjabi'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        #     speak("my name is abhishek gupta");
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'where am i' in query:
                speak('wait ! i am fatching')
                time.sleep(3)
                india = folium.Map(location = ['26.90173', '80.97416']).save("india1.html")
                webbrowser.open("india1.html")    
        elif  'bin' in query:
                try:

                    speak("i am trying to clear recycle bin")
                    time.sleep(3)
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    speak("Sucessfully clear recycle bin")
                except :
                    speak("Sorry! nothing in recycle bin")
            