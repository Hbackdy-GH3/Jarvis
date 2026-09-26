import time
from core.speech import listen, speak, speak1
from core.router import route
import config
import speech_recognition as sr


def run():
    while True:
        try:
            text = listen()
            print(text)
            if config.wake_word in text.lower().split():
                speak1("Yes!, how can i help you")
                jarvis_active = time.time() + config.active

                while time.time() < jarvis_active:
                    try:
                        command = listen(
                            timeout=config.listening_timeout,
                            phrase_time_limit=config.phrase_time_limit
                        ).lower()
                        route(command)
                        jarvis_active = time.time() + config.active
                    except sr.WaitTimeoutError:
                        continue
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
                speak("Going to sleep")

        except Exception as e:
            print(f"Error: {e}")
        


if __name__ == "__main__":
    run()