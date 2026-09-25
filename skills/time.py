import time
from core.speech import speak

def time_now(command):
    local_time=time.localtime(time.time())
    format_time=time.strftime("%H:%M",local_time)
    speak(f"right now is {format_time}")