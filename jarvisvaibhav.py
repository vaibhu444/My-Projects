import pyttsx3
import pyaudio
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',200)
def Speak(audio):
    print("  ")
    print("  ")
    Assistant.say(audio)
    print(f":{audio}")
    Assistant.runAndWait()
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("recognizing...")
            query = command.recognize_google(audio , language='en-in')
            print(f"you said: {query}")

        except Exception as Error:
            return "None"

        return query.lower()
def music():
    Speak("tell me the name of music")
    music_name=takecommand()
    if 'play date ' in music_name:
        os.startfile('/snack 1\\ play_date.mp3')
    else:
        pywhatkit.playonyt(music_name)
def taskExe():
    while True:
        query = takecommand()
        if 'hello' in query:
            Speak("hello vaibhav sir how can i help you")
        elif 'who are you' in query:
            Speak("i am jarvis created by vaibhav")
        elif 'who is vaibhav' in query:
            Speak("vaibhav is programmer")
        elif 'do you know seed' in query:
            Speak("siddh  is vaibhav friend")
        elif 'jhil' in query:
            Speak("jeel is a character from mahabharat")
        elif 'youtube search' in query:
            Speak("ok vaibhav sir, I have found your result")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("done sir")
        elif 'google search' in query:
            Speak("this is i found")
            query=query.replace("jarvis", "")
            query=query.replace("google search", "")
            pywhatkit.search(query)
            Speak("done sir")
        elif 'website' in query:
            Speak("ok sir , launching")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            web1=query.replace("open","")
            web2='https://'+web1+'.com'
            webbrowser.open(web2)
            Speak("done sir")
        elif 'music' in query:
            music()
        elif 'exit' in query:
            break
        else:
            Speak("if you want to leave  speack exit")


taskExe()