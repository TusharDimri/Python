from pygame import mixer
import datetime
import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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


def reminder(audio, stop):
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()
    stopper = input(f"type \"{stop}\" to stop the music")
    while True:
        if audio == "Water.mp3":
            if stopper == "D" or stopper == 'd':
                w1 = open("Log.txt", "a")
                w1.write(f"User drank water at {str(datetime.datetime.now())} \n")
                mixer.music.stop()
                speak("Mr Dimri i hope you actually drank water")
                break
            else:
                print("Music will stop only if you type the given keyword")
                reminder("Water.mp3", "D")

        elif audio == "Eyes.mp3":
            if stopper == "E" or stopper == 'e':
                w1 = open("Log.txt", "a")
                w1.write(f"User did eye training at {str(datetime.datetime.now())} \n")
                mixer.music.stop()
                speak("Mr Dimri I'm sure you gave your eyes a break")
                break
            else:
                print("Music will stop only if you type the given keyword")
                reminder("Eyes.mp3", "E")

        elif audio == "Physical.mp3":
            if stopper == "P" or stopper == 'p':
                w3 = open("Log.txt", "a")
                w3.write(f"User did Physical Relaxation at {str(datetime.datetime.now())} \n")
                mixer.music.stop()
                speak("Mr Dimri i know you actually exercised")
                break
            else:
                reminder("Physical.mp3", "P")
                print("Music will stop only if you type the given keyword")
        break


if __name__ == '__main__':
    hour = int(datetime.datetime.now().hour)
    wish_me()
    speak("Mr Dimri, i hope you didn't forget about your skincare and workout routine")
    for hour in range(0, 25):
        time.sleep(1800)
        reminder("Water.mp3", "D")
        time.sleep(900)
        reminder("Eyes.mp3", "E")
        time.sleep(900)
        reminder("Physical.mp3", "P")

"""
This program  will play "Water.mp3" after every 30 minutes of its execution time,"Eyes.mp3" after every 45 minutes of its execution time and "Physical
.mp3" after every 1 hour of its execution time."Water.mp3" is to remind user to drink water ,"Eyes.mp3" to remind user to do eye workout and
"Physical.mp3" to remind user to do some physical workout.User is required to type "Drank" to stop water reminder,"Eydone" to stop eye workout
reminder and "Exdone" to stop physical workout reminder.User's activity will get logged in LOd.txt (text) file automatically with execution
time."STAY HEALTHY"
NOTE :- This program(P6 Healthy Programmer) is inside directory Music with three mp3 files because pygame module allows us loads mp3 files
only by using this method.In simple words this setup is for pygame module to work properly and for it to allow us to load mp3 files in our
python program as mp3 files should be in the same directory as the .py file containing this code for this code to work and I added mp3 files 
in a new directory "Music"(no particular reason) so i had to add this .py file in this directory too.
"""















