import webbrowser
from urllib.parse import quote_plus
from sites import sites
from core.speech import speak, listen
import speech_recognition as sr


def search(command):
    while True:
        try:
            search_query = listen(timeout=20).replace("search", "", 1).strip().capitalize()
            speak(f"searching {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={quote_plus(search_query)}")
            break
        except sr.WaitTimeoutError:
            speak("do you want to go back?")
            if "go back" in listen().lower():
                speak("Going back")
                break


def open_site(command):
    website = command.split()
    for site in sites:
        if site in website:
            speak(f"opening {site}")
            webbrowser.open(sites.get(site))
            return
    speak("I couldn't find that site")