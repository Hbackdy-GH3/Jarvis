from skills.web import search, open_site
from skills.media import play
from core.speech import speak
from skills.time import time_now
from skills.notes import add_note, read_note
from skills.news import read_titles

TRIGGERS = {
    "search": search,
    "open": open_site,
    "play": play,
    "time": time_now,
    "write":add_note,
    "read":read_note,
    "news": read_titles
    
}


def find_trigger_word(command):
    for word in command.split():
        if word in TRIGGERS:
            return word
    return None


def route(command):
    word = find_trigger_word(command)
    if word:
        TRIGGERS[word](command)
    else:
        speak("sorry, yet we have not programmed!")