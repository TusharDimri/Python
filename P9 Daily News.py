# News API.org used for content

import pywin32_system32
import requests
import json
import time

def speak(audio):
    from win32com.client import Dispatch
    speak  = Dispatch('SAPI.SpVoice')
    speak.Speak(audio)

url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=f64e7fbdfeb74868865d4a85bb4a681f')
response = requests.get(url)
news = response.json()
j = 1
for i in news['articles']:
    print(f'News {j}')
    print(i['title'],"\n")
    speak(f'News {j}')
    speak(i['title'])
    j = j+1
    time.sleep(1)
else:
    speak("Thank you for listening to me patiently")

