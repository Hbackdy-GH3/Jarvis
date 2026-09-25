import pywhatkit
from core.speech import speak


def play(command):
    song = command.replace("play", "", 1).strip()
    if not song:
        speak("what should I play?")
        return
    speak(f"playing {song}")
    pywhatkit.playonyt(song)