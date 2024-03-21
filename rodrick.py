import wikipedia
import pyttsx3
import speech_recognition as sr
import pyaudio

def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',100)
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def take_commmand():
    command = ""
    try:
       with sr.Microphone() as source:
           print("Listening...")
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower
           print(command)
           if "jacob" in command:
               command = command.replace("jacob", "")
               print(command)
           if 'old' in command:
               talk("I am 20 years old")
           if 'live' in command:
               talk("I live in Zamboanga City")
           if 'peter' in command:
               talk("We are siblings")
           else:
               talk("Please say my name")

    except:
        pass
    command ="no mic"
    print(command)

    take_commmand()
