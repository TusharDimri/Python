import smtplib
from email.message import EmailMessage
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content): # This function sends gmail without subject
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("tushar.dimri91@gmail.com","8126840347")
    server.sendmail("tushar.dimri91@gmail.com", to, content)
    server.close()

def sendproperEmail(to, subject, message): # This function sends gmail with subject
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = "tushar.dimri91@gmail.com"
    msg["To"] = to
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("tushar.dimri91@gmail.com", "8126840347")
    server.send_message(msg)
    server.quit()

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



if __name__ =='__main__':
    speak("Sir, you can send email with a subject and a message or send  email with just a message. Press 's' for sending email with subject\n"
          "and a message or type 'm' to send mail with only message ")
    inp = input("Sir, you can send email with a subject and a message or send  email with just a message. Press 's' for sending email with subject\n"
          "and a message or type 'm' to send mail with only message ")
    if inp == 'M' or inp == 'm':
        speak("Sir,do you want to type our mail or speak it verbally. Press 'w' to write it and 'v' to speak it verbally")
        inp2 = input("Sir,do you want to type our mail or speak it verbally. Press 'w' to write it and 'v' to speak it verbally")
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
                speak("Sorry sir i coudn't send email")
                print("Sorry sir i coudn't send email")

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
                speak("Sorry sir i coudn't send email")
                print("Sorry sir i coudn't send email")

        else:
            speak("Wrong Input")
            print("Wrong Input")


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