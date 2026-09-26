from dotenv import load_dotenv
import os

load_dotenv()

device_index = 2
wake_word = "jarvis"
active = 300
listening_timeout = 15
phrase_time_limit = 10
wake_word="jarvis"
wake_word_threshold=0.5
news_api_key = os.environ.get("NEWS_API_KEY") 
