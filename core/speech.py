import speech_recognition as sr
import pyttsx3 as pyt
import config

recognizer = sr.Recognizer()



def listen(timeout=None,phrase_time_limit=None):
    with sr.Microphone(device_index=2) as source:
        print("listening...")
        audio=recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
    print("recognizing...")
    return recognizer.recognize_google(audio)
    

def speak(whisper):
    t2s = pyt.init()
    print(whisper)
    t2s.say(whisper)
    t2s.runAndWait()