# Jarvis — Voice Assistant

A modular, Python-based voice assistant that listens for a wake word, understands spoken commands, and responds with speech. Built as a learning project to explore speech recognition, text-to-speech, multithreading, and clean modular architecture.

## Features

- **Wake-word activation** — say "Jarvis" to start a session
- **Web search** — search Google by voice
- **Open websites** — open predefined sites by name
- **Play music** — play songs on YouTube via voice command
- **Tell the time** — ask what time it is
- **Notes** — write and read back notes
- **News headlines** — reads out the latest top headlines (via NewsAPI)
- **Interruptible speech** — say "stop" while Jarvis is talking to interrupt it immediately, powered by a background thread that listens in parallel with speaking

## Architecture

The project follows a layered, modular structure so new skills can be added without touching existing code:

```
Jarvis/
├── main.py           # entry point — wake-word loop and session handling
├── config.py         # all settings (mic index, timeouts, API keys) in one place
├── sites.py          # dictionary of website shortcuts for the "open" command
├── core/
│   ├── speech.py     # speech-to-text (listen) and text-to-speech (speak), with threading for interruption
│   └── router.py     # maps recognized trigger words to the right skill function
└── skills/
    ├── web.py        # search + open website
    ├── media.py      # play music
    ├── time.py       # tell the current time
    ├── notes.py      # write/read notes
    └── news.py       # fetch and read news headlines
```

**Import direction:** `main → router → skills → speech → config` — each layer only knows about the one below it, keeping the codebase easy to extend and debug.

## How interruptible speech works

Text-to-speech normally blocks the program while it talks, so the microphone can't listen at the same time. Jarvis solves this by running the TTS engine in a background thread, while the main thread keeps listening in short bursts for the word "stop." If it's heard, the engine is told to stop and a quick "OK!" confirms it.

## Setup

**1. Clone the repo and set up a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API keys**

Create a `.env` file in the project root (this file is git-ignored and never committed):
```
NEWS_API_KEY=your_newsapi_key_here
```
Get a free key at [newsapi.org](https://newsapi.org).

**4. Set your microphone index**

Run this to list available microphones and find your device index:
```python
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
```
Update `device_index` in `config.py` to match.

**5. Run it**
```bash
python main.py
```

## Usage

Say **"Jarvis"** to wake it up, then try:
- *"search python tutorials"*
- *"open youtube"*
- *"play believer imagine dragons"*
- *"what time is it"*
- *"write buy groceries tomorrow"*
- *"read notes"*
- *"news"* — say **"stop"** any time while it's talking to interrupt

## Tech stack

- `speech_recognition` — speech-to-text (Google Web Speech API)
- `pyttsx3` — offline text-to-speech
- `pywhatkit` — YouTube playback
- `requests` — NewsAPI integration
- `python-dotenv` — environment variable management
- `threading` — concurrent listen-while-speaking for interruption

## Future improvements

- Offline wake-word detection (openWakeWord) instead of full speech-to-text on every listen
- More accurate STT via Whisper
- Reminders and to-do list skill
- Smart home integration