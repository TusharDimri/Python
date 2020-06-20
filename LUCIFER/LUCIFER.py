import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import json
import time
from plyer import notification
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning Mr Dimri!")
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon Mr Dimri!")
    else:
        speak("Good Evening Mr Dimri!")
    speak("Lucifer here. Sir please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 40
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"user said:{query} \n")

        except:
            print("Please say that again...")
            speak("Please say that again...")
            return "None"

        return query


def sendproperEmail(to, subject, message):  # This function sends gmail with subject
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = "tushar.dimri91@gmail.com"
    msg["To"] = to
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("tushar.dimri91@gmail.com", "8126840347")
    server.send_message(msg)
    server.quit()


def notify_me(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\User\\Downloads\\Coronavirus.ico",
        timeout=8
    )


def getData(url):
    r = requests.get(url)
    return r.text


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.login("tushar.dimri91@gmail.com", "8126840347")
    server.sendmail("tushar.dimri91@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    print("If the password is wrong I'll take your soul")
    speak("if the password is wrong i'll take your soul")
    password = input("Please enter your password:")
    if password == "iamyourmaster":
        wish_me()
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                try:
                    print("Searching Wikipedia...")
                    speak("Searching Wikipedia...")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    print("According to Wikipedia")
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    print(e)
                    print("Please speak that again")
                    speak("Please speak that again")

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/")
                print("Opening you tube for you sir, here it is")
                speak("Opening you tube for you sir, here it is")

            elif 'open google' in query:
                path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(path)
                print("Opening Google for you sir, here it is")
                speak("Opening Google for you sir, here it is")

            elif 'the time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M")
                print(f"The time is {current_time}")
                speak(f"The time is {current_time}")

            elif 'open  vs code' in query or 'vs code' in query:
                print("Opening VS code for you sir")
                speak("Opening VS code for you sir")
                codepath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
                os.startfile(codepath)
                print("Here it is sir")
                speak("Here it is sir")


            elif 'who are you' in query or 'are you' in query:
                print("I am Lucifer Mr. Dimri's private assistant and i want a soul")
                speak("I am Lucifer Mr. Dimri's private assistant and i want a soul")

            elif 'news' in query:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=in&'
                       'apiKey=f64e7fbdfeb74868865d4a85bb4a681f')
                response = requests.get(url)
                news = response.json()
                j = 1
                for i in news['articles']:
                    print(f'News {j}')
                    print(i['title'], "\n")
                    speak(f'News {j}')
                    speak(i['title'])
                    j = j + 1
                    time.sleep(1)

                else:
                    print("Thank you for listening to me patiently")
                    speak("Thank you for listening to me patiently")

            elif 'go to hell' in query:
                print("Sir i am the king of hell")
                speak("Sir i am the king of hell")

            elif 'f*** off' in query:
                print("No You Fuck Off")
                speak("No You Fuck Off")

            elif 'i want to practice guitar' in query:
                webbrowser.open("https://www.justinguitar.com/site-map-and-lesson-structure")
                print("Sir here is your favourite guitar tutorial site")
                speak("Sir here is your favourite guitar tutorial site")


            elif 'covid-19 india' in query or 'covid-19 cases' in query or '19 cases' in query or 'coronavirus cases in india' in query \
                    or 'coronavirus india' in query or 'coronavirus cases' in query:
                state = input("Enter the name of the state that you want the details about")
                myHTMLdata = getData("https://www.mohfw.gov.in/")
                soup = BeautifulSoup(myHTMLdata, 'html.parser')
                mystr = ""
                for table in soup.find_all('tbody'):
                    mystr += table.get_text()

                mystr = mystr[1:]
                itemlst = mystr.split("\n\n\n")
                td = -1

                for item in itemlst[0:33]:
                    data = item.split("\n")
                    if data[1] == state:
                        td = 1
                        break

                    elif data[2] == state:
                        td = 2
                        break

                if td == 1:
                    title1 = "Coronavirus Cases"
                    text = f"State: {data[1]}\nTotal Confirmed Cases: {data[2]}\nCured\Discharged: {data[3]}\nDeaths: {data[4]}"
                    notify_me(title1, text)
                    print(text)
                    speak(f"State: {data[1]}")
                    speak(f"Total Confirmed Cases: {data[2]}")
                    speak(f"Cured: {data[3]}")
                    speak(f"Deaths: {data[4]}")

                elif td == 2:
                    title2 = "Coronavirus Cases"
                    text = f"State: {data[2]}\nTotal Confirmed Cases: {data[3]}\nCured\Discharged: {data[4]}\nDeaths: {data[5]}"
                    notify_me(title2, text)
                    print(text)
                    speak(f"State: {data[2]}")
                    speak(f"Total Confirmed Cases: {data[3]}")
                    speak(f"Cured: {data[4]}")
                    speak(f"Deaths: {data[5]}")

                else:
                    print("Please Check your spelling.First letter of name should be capital.\nFor example:- 'Uttar Pradesh'")


            elif 'download music' in query or 'download songs' in query:
                webbrowser.open("https://realmusicpleer.com/")
                print("Sir here is your favourite music download site")
                speak("Sir here is your favourite music download site")


            elif 'bye' in query or 'see you lucifer' in query or 'to sleep' in query or 'go to sleep' in query or \
                    'see you later' in query:
                print("Bye Mr. Dimri, see you again")
                speak("Bye Mr. Dimri, see you again")

                break


            elif 'open pycharm' in query or 'pycharm' in query:
                speak("opening py charm for you sir")
                path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.4\\bin\\pycharm64.exe"
                os.startfile(path)
                speak("here it is, it may take some time though")

            elif 'send email' in query or 'send gmail' in query or 'send an email' in query or 'send a gmail' in query:
                speak(
                    "Sir, you can send email with a subject and a message or send  email with just a message. Press 's' for sending email with subject\n"
                    "and a message or type 'm' to send mail with only message ")
                inp = input(
                    "Sir, you can send email with a subject and a message or send  email with just a message. Press 's' for sending email with subject\n"
                    "and a message or type 'm' to send mail with only message ")
                if inp == 'M' or inp == 'm':
                    speak(
                        "Sir,do you want to type our mail or speak it verbally. Press 'w' to write it and 'v' to speak it verbally")
                    inp2 = input(
                        "Sir,do you want to type our mail or speak it verbally. Press 'w' to write it and 'v' to speak it verbally")
                    if inp2 == 'v' or inp2 == 'V':
                        try:
                            speak("Boss, please enter the gmail address of the person you want to send email to")
                            to = input("Boss, please enter the gmail address of the person you want to send email to")
                            speak("What should i say")
                            content = takeCommand()
                            sendEmail(to, content)
                            print("Email Successfully Sent")
                            speak("Email Successfully Sent")

                        except Exception as e:
                            print(e)
                            print("Sorry sir i coudn't send email")
                            speak("Sorry sir i coudn't send email")


                    elif inp2 == 'w' or inp2 == 'W':
                        try:
                            speak("Boss, please enter the gmail address of the person you want to send email to")
                            to = input("Boss, please enter the gmail address of the person you want to send email to")
                            speak("Please type your message")
                            content = input("Please type your message")
                            sendEmail(to, content)
                            print("Email Successfully Sent")
                            speak("Email Successfully Sent")

                        except Exception as e:
                            print(e)
                            print("Sorry sir i coudn't send email")
                            speak("Sorry sir i coudn't send email")


                    else:
                        print("Wrong Input")
                        speak("Wrong Input")



                elif inp == 's' or inp == 'S':
                    try:
                        speak("Boss, please enter the gmail address of the person you want to send email to")
                        to = input("Boss, please enter the gmail address of the person you want to send email to")
                        speak("Please type the subject of your message")
                        subject = input("Please type the subject of your message")
                        speak("Please type your message")
                        message = input("Please type your message")
                        sendproperEmail(to, subject, message)
                        speak("Email Successfully Sent")
                        print("Email Successfully Sent")

                    except Exception as e:
                        print(e)
                        speak("Sorry sir i coudn't send email")
                        print("Sorry sir i coudn't send email")

                else:
                    speak("Sir, Your input is wrong")

            elif 'open ms word' in query or 'open word' in query or 'ms word' in query:
                wpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007"
                print("Opening MS Word for you Sir")
                speak("Opening MS Word for you Sir")
                os.startfile(wpath)
                print("Sir, here it is")
                speak("Sir, here it is")


            elif 'i want to learn coding' in query or 'learn coding' in query or 'i want to learn to code' in query \
                    or 'learn to code' in query or 'i want to learn coding for free' in query or 'learn coding for free' in \
                    query or 'learn to code for free' in query:
                speak("Sir this is your favourite source to learn coding")
                webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww/playlists")
                speak("Happy Coding Mr. Dimri")

            elif 'what do you eat' in query or 'eat this' in query or 'what would you like to eat' in query or 'like to eat' in query \
                    or ' to eat' in query:
                speak("Sir, i only eat human souls")
                print("Sir, i only eat human souls")


            elif 'search google' in query or 'search in google' in query or 'google search' in query:
                speak("Press 's' to speak your query verbally and 'w' to write your query")
                ch = input("Press 's' to speak your query verbally and 'w' to write your query")
                if ch == 's' or ch =='S':
                    ser1 = takeCommand()
                    query1 = f"https://google.com/search?q={ser1}"
                    webbrowser.open(query)
                    speak("Sir, here is the output to your google search")
                    time.sleep(3)


                elif ch == 'w' or ch == 'W':
                    ser2 = input("Enter your query")
                    query2 = f"https://google.com/search?q={ser2}"
                    webbrowser.open(query2)
                    speak("Sir, here is the output to your google search")
                    time.sleep(3)

            elif 'learn japanese' in query or 'japanese class' in query:
                link = 'https://www.busuu.com/dashboard#/timeline'
                print("Accessing your japanese class")
                speak("Accessing your japanese class")
                webbrowser.open(link)
                print("Sir here is your japanese class, happy learning")
                speak("Sir here is your japanese class, happy learning")


            elif 'thanks' in query or 'thank you' in query:
                print("No problem, it's my pleasure to serve Mr. Dimri")
                speak("No problem, it's my pleasure to serve Mr. Dimri")

            elif 'introduce yourself' in query or 'say hi' in query or 'say hello' in query or 'greet' in query:
                print("Hii, i am Lucifer Mr. Dimri's personal assistant. Nice to meet you")
                speak("Hii, i am Lucifer Mr. Dimri's personal assistant. Nice to meet you")

        
    else:
        speak("Thanks for your soul you dumb mortal")
        print("Thanks for your soul you dumb mortal")








