import speech_recognition as sr
import webbrowser
import os
import subprocess as sp
import pywhatkit
import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():

    time = datetime.datetime.now().strftime('%I:%M %p')
    speak('current Time' +time)

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning MT')
    elif hour>=12 and hour<18:
        speak('Good afternoon MT')
    else:
        speak('Good Evening MT')
    speak('welcome')
def takecommand():
    while True:
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening...')
                listener.pause_threshold = 0.5
                audio = listener.listen(source)
                print('Recognising...')
                query = listener.recognize_google(audio, language='en-in')
                query = query.lower()
                if 'hello' in query:
                    speak('hello mt')
                elif 'play' in query:
                    song = query.replace('play', '')
                    speak('opening youtube' +song)
                    pywhatkit.playonyt(song)

                elif 'wikipedia' in query:
                    speak('searching wikipedia')
                    query = query.replace('wikipedia', '')
                    result = wikipedia.summary(query, 3)
                    speak('according to wikipedia' +result)
                    print(wikipedia, +result)

                elif 'open google' in query:
                    speak('opening google')
                    webbrowser.open('google.com')

                elif 'open pycharm' in query:
                    query = query.replace('open pycharm', '')
                    speak(query)
                    os.startfile('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.1')

                elif 'microsoft edge' in query:
                    speak('opening microsoft edge')
                    sp.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

                elif 'text' in query:
                    speak('opening sublimetext')
                    sp.Popen("C:\\Program Files\\Sublime Text\\sublime_text.exe")

                elif 'oracle' in query:
                    speak('opening vbox')
                    sp.Popen("C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe")
               
                elif 'vscode' in query:
                    speak('opening code')
                    sp.Popen('# Enter the path where you have saved your vscode')
                    
# similarly you can give the path to any of them. here i have given mine you can give your saved path of application
# Here you can change the code if you need and can add any code.
# i have just made it as a project for my presentation if like it support me on github and thanks.
# I have not provided it any name , user can give it any name as per his/her need.        




        

        except:
            pass


if __name__ == '__main__':
    wishme()
    takecommand()












