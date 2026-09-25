from core.speech import speak
import os

def add_note(command):
    notes=command.replace("write","",1).strip().capitalize()
    with open("notes.txt","a") as note:
        note.write(f"{notes}\n")
    speak("Notes saved!")

def read_note(command):
    if "notes" in command.lower():
        if os.path.exists("notes.txt"):
            if os.path.exists("notes.txt")!=0:
                with open("notes.txt","r") as note:
                    speak(note.read())
            else: speak("file is empty")
        else: speak("file does not empty")
    else:
        speak("i couldn't understand")