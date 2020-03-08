import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am cammo tera swag Sir. How may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def readfile():
    hand=open('pas.txt')
    for line in hand:
        line=line.rstrip()
        if re.search('charan',line):
            return line

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    a=readfile()
    server.login('//your email id//', a)
    server.sendmail('//your email id//', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak(results)
        elif 'my computer' in query:
            speak("sir,please hold on a sec")
            os.startfile('..\\..\\')
        elif 'impressive'  in query:
            speak("thank u sir")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open chrome' in query:
            webbrowser.open("chrome.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open gmail' in query:
            speak("opening!,wait a sec")
            webbrowser.open("gmail.com")   
        elif 'play music' in query:
            #music_dir = 'C:\\Users\\Charanpreet\\Downloads\\music'
            #songs = os.listdir(music_dir)
            #print(songs)    
            #os.startfile(os.path.join(music_dir, songs[0]))
            webbrowser.open("https://gaana.com/playlist/gaana-dj-punjabi-top-50-1")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'hibernate' in query:  
            speak("ok sir")
            check = input("Want to shutdown your computer ? (y/n): ")
            if check == 'n':
                exit()
            else:
                speak("hibernating")
                os.system("shutdown //h //t 1")
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "//email id to which u want to send//"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")  
        elif 'how are you' in query:
            speak("I am fine,how are you sir")
            break