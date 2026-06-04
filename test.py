import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import smtplib
import tkinter as tk
from tkinter import messagebox
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir! I am Friday. Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        try:
            print("Listening....")
            audio = r.listen(source, phrase_time_limit=5)
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-IN')
            print(f"user said: {query}\n")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I could not understand what you said!")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def play_music():
    os.system("start spotify:")
    speak("Playing music")

def tell_date_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    speak(f"The current date and time is {date_time}")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("manas.sri07@gmail.com", "jzzt kctw zabd qhue")  # Replace with your email and password
    server.sendmail("manas.sri07@gmail.com", to, content)
    server.close()

def on_listen():
    query = takecommand()
    if query:
        query = query.lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.open("facebook.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")
        elif 'play music' in query:
            play_music()
        elif ' time' in query:
            tell_date_time()
        elif 'send email to manas' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "manassrivastava094@gmail.com"  # Replace with your email
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email. Please try again.")
        elif 'send email to kishan' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "kishanpandey2151@gmail.com",
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend kishan. I am not able to send this email. Please try again.")
        elif 'send email to saksham' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "rrdx83250@gmail.com",
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend saksham. I am not able to send this email. Please try again.")
        elif 'send email to yuvraj' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "raj.yuvi2004@gmail.com",
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend saksham. I am not able to send this email. Please try again.")

# Create the main window for the GUI
root = tk.Tk()
root.title("Friday Assistant")
root.geometry("400x200")

# Create a label
label = tk.Label(root, text="Click below to activate listening", font=("Arial", 14))
label.pack(pady=10)

# Create the wish me button
wishme_button = tk.Button(root, text="Wish Me", font=("Arial", 12), command=wishMe, height=2, width=15)
wishme_button.pack(pady=5)


# Create the listen button
listen_button = tk.Button(root, text="Listen", font=("Arial", 12), command=on_listen, height=2, width=15)
listen_button.pack(pady=5)

# Start the GUI main loop
root.mainloop()
