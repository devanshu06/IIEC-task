import pyttsx3
import os
import speech_recognition as sr
import webbrowser

print("#####################################  WELCOME  ##########################################")
pyttsx3.speak("welcome to your personal voice assistant ")
print()

while True:
    x = print("what you want me to do")

    r = sr.Recognizer()  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("start say..")
        audio = r.listen(source)
        print("speech done ..")
        p = r.recognize_google(audio)
        print(p)

        if "Linux" in p and "open" in p :
             pyttsx3.speak("Linux command line page will open in a second")
             webbrowser.open("http://192.168.43.219/iiectask2commandline.html")
        elif "docker" in p and "open" in p :
            pyttsx3.speak("Dockerpage will open in a second")
            webbrowser.open("http://192.168.43.219/iiectask2docker.html")
