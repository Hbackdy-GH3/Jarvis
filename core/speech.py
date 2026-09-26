import speech_recognition as sr
import pyttsx3 as pyt
import config
import threading

recognizer = sr.Recognizer()



def listen(timeout=None,phrase_time_limit=None):
    with sr.Microphone(device_index=2) as source:
        print("listening...")
        audio=recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
    print("recognizing...")
    return recognizer.recognize_google(audio)

def listen_stop(timeout,phrase_time_limit):
    with sr.Microphone(device_index=2) as source:
        audio=recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
    return recognizer.recognize_google(audio)

def speak(whisper):
    
    print(whisper)

    box={}

    def run_speech():
        t2s = pyt.init()
        box["item"]=t2s
        t2s.say(whisper)
        t2s.runAndWait()
    
    speak_thread=threading.Thread(target=run_speech)
    speak_thread.start()

    while "item" not in box:
        pass

    t2s=box["item"]

    while speak_thread.is_alive():
        try:
            heard = listen_stop(timeout=1, phrase_time_limit=2)
            print(f"[DEBUG] heard: {heard}")
            if "stop" in heard.lower():
                t2s.stop()
                speak1("OK!")
                return True

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
    return False


def speak1(whisper):
    t2s=pyt.init()
    t2s.say(whisper)
    t2s.runAndWait()
    