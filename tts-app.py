import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
print("""
████████╗████████╗░██████╗░░░░░░░█████╗░██████╗░██████╗░
╚══██╔══╝╚══██╔══╝██╔════╝░░░░░░██╔══██╗██╔══██╗██╔══██╗
░░░██║░░░░░░██║░░░╚█████╗░█████╗███████║██████╔╝██████╔╝
░░░██║░░░░░░██║░░░░╚═══██╗╚════╝██╔══██║██╔═══╝░██╔═══╝░
░░░██║░░░░░░██║░░░██████╔╝░░░░░░██║░░██║██║░░░░░██║░░░░░
░░░╚═╝░░░░░░╚═╝░░░╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░
""")
print("")
i = input("Enter File Name(.mp3)\n")
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = i
    tts.save(filename)
    playsound.playsound(filename)
t = input("Enter Text\n")
speak(t)