import random
from tabulate import tabulate
from pywikihow import search_wikihow
from pygame import mixer
import requests
import pygame
import pyttsx3
import pyautogui
from plyer import notification
import os
import smtplib
import webbrowser
import wikipedia
from pyttsx3.engine import Engine
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

pygame.init()

def speak(spt):
    engine.say(spt)
    engine.runAndWait()

def scrennshot():
    pyautogui.press(['win','prtsc'])
    speak('Ok screenshot take successfully')
def whish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning ")
        try:
            notification.notify(title='Hello',message=' Hi Good Mornig ', app_icon='ai.ico',timeout=3)
        except e:
            pass
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        try:
            notification.notify(title='Hello',message=' Hi Good Afternoon', app_icon='ai.ico',timeout=3)
        except e:
            pass
    else:
        speak("Good Evening")
        try:
            notification.notify(title='Hello',message=' Hi Good Evening', app_icon='ai.ico',timeout=3)
        except e:
            pass
    speak("Hi how can i help you please tell me")

def sendemail(to,cont):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail","yourpassword")
    server.sendmail('youremail',to,cont)
    server.close()
    
def takevr():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...!")
        query = r.recognize_google(audio,language='en-in')
        print("User Said :", query)
    except Exception as e:
        # print(query)
        # print("Say that again ...!")
        # speak('Say that again ...!')
        return "None"
    return query

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...!")
        query = r.recognize_google(audio,language='en-in')
        print("User Said :", query)
    except Exception as e:
        # print(query)
        print("Say that again ...!")
        speak('Say that again ...!')
        return "None"
    return query

clock = pygame.time.Clock()


if __name__ =='__main__':
    os.system('Turn Windows features on or of')
    whish()
    while True:
        clock.tick(60)
        query = take().lower()
        # query = 'song'
        if 'wikipedia' in query:
            speak("Serching in wikipedia")
            query = query.replace("wikipedia",'')
            resu = wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(resu)
            speak(resu)
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        elif 'shutdown' in query:
            speak('Ok Shutdowning your pc')
            os.system("shutdown /s /t 1")
        elif 'moive' in query:
            speak("Ok Playing star wars")
            os.system('telnet towel.blinkenlights.nl')
        elif 'google' in query:
            webbrowser.open('google.com')
        elif 'quit' in query:
            speak("ok bye bye see you soon")
            exit() 
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            speak(time)
        elif 'volume up' in query:
            pyautogui.press('volumeup')
        elif 'volume down' in query:
            pyautogui.press('volumedown')
        elif 'volume mute' in query:
            pyautogui.press('volumemute')
        elif 'volume unmute' in query:
            pyautogui.press('volumeunmute')
        elif 'notepad' in query:
            webbrowser.open('notepad.exe')
        elif 'what is your name' in query:
            speak('My Name Is Jarvis')
        elif 'what is your birth date' in query:
            pass # Complete Dhaval fgsduy
        elif 'scrennshot' in query:
            scrennshot()
        elif 'how to' in query:
            speak("Please say again")
            how = take()
            max_res = 1
            how_to = search_wikihow(how,max_res)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif 'what can you do' in query:
            speak('I can so the following things')
            mydata=[{'open youtube','youtube'},
                    {'open google','google'},
                    {'sending email','email'    },
                    {'opening notepad','notepad'},
                    {'volume + ', 'volume up'},
                    {'volume - ', 'volume down'},
                    {'volume mute','volume mute'},
                    {'serch in wikipedia','name + according to wikipedia'},
                    {'time','what is the time'}
                                                ]
            head=["To","Speak"]
            print(tabulate(mydata,headers=head,tablefmt='grid'))
        elif 'song' in query:
            mixer.init()
            mixer.music.load(random.choice(['song.mp3','song2.mp3','song3.mp3','song4.mp3']))
            mixer.music.play()
            

            
            # if query == 'pause':
            #     print('Working')
            #     pygame.mixer.music.pause()

            # elif query == 'stop':
            #     pygame.mixer.music.stop()
            # pygame.mixer.music.set_volume(1)

            
            # query()
        
        elif 'music' in query:
            mixer.init()
            mixer.music.load(random.choice(['song.mp3','song2.mp3','song3.mp3','song4.mp3']))
            mixer.music.play()

            # q2 = takevr().lower()

            # if q2 == 'pause':
            #     pygame.mixer.music.pause()

            # if q2 == 'stop':
                # pygame.mixer.music.stop() 
            # pygame.mixer.music.set_volume(1)


        elif 'ip address' in query:
            from requests import get
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")
            print(f"Your ip address is {ip}")
        elif 'folder' in query:
            try:
                path = 'c:\\'
                speak("What is folder name")
                txc = take()
                pathe = os.path.join(path,txc)
                os.mkdir(pathe)
                speak('folder created succesfully')
            except e:
                speak("Soory did not crete folder")

        elif 'email' in query:
            try:
                speak("What i can send")
                c2 = take()
                sendemail('sendermail',c2)
                speak("Email sent successfully")
                notification.notify(title='Email',message='Email Sent Successfully', app_icon='ai.ico',timeout=3)

            except Exception as e:
                speak("Sorry did not send email try again")