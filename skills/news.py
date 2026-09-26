from core.speech import speak, speak1
import requests
import config



def read_titles(command):
    response=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={config.news_api_key}")
    if response.status_code==200:
        data=response.json()

        articles=data.get("articles",[])

        for article in articles:
            stopped=speak(article['title'])
            if stopped:
                break
    else:
        speak("Sorry i couldn't found")