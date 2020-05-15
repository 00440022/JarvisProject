import pyttsx3
import datetime
import speech_recognition as sr
from tkinter import messagebox
import tkinter as tk
import gtts
import random
import os
import wikipedia
import webbrowser

#----------- documentation ---------------------

# first we have to open the terminal from below options
# then we have to type this commands in the same order one by one

#----------- commands ---------------------------

# pip install wikipedia
# pip install pywin32
# pip install pipwin
# pipwin install pyaudio

# ------------------------------------------------

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio, toBeSaved=False):
    if(toBeSaved):
        rand = random.randrange(1, 100000)
        tts = gtts.gTTS(audio)
        tts.save("{}{}.mp3".format(str(audio).replace(" ", "_"), rand))
        os.startfile("{}{}.mp3".format(str(audio).replace(" ", "_"), rand))
    else:
        engine.say(audio)
        engine.runAndWait()

def reply(queryFromResult):
    query = str(queryFromResult).lower()
    if ("how are you" in query):
        speak("I am fine, Nice to meet you")
    elif ("wikipedia" in query):
        query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
    elif ("open google" in query):
        speak("opening google")
        webbrowser.open("google.com")
    elif ("open youtube" in query):
        speak("opening youtube")
        webbrowser.open("youtube.com")
    elif ("open facebook" in query):
        speak("opening facebook")
        webbrowser.open("facebook.com")




def onStart():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        engine.say("Good morning")
        engine.runAndWait()
    elif(hour>12 and hour<=16):
        engine.say("Good afternoon")
        engine.runAndWait()
    elif(hour>16 and hour<=19):
        engine.say("Good evening")
        engine.runAndWait()
    else:
        engine.say("Hope, your day was great!")
        engine.runAndWait()

    engine.say("How can I help you?")
    engine.runAndWait()
#
notClickedListen = True

def listenToUser(btn):
    global notClickedListen
    if(notClickedListen):
        onStart()
        notClickedListen = False

    btn.configure(background="#2b18d8")
    btn.configure(text="Listening.......")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.energy_threshold = 200
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-IN")
        reply(query)
        btn.configure(background="#d8d106")
        btn.configure(text="Listen")
    except Exception as e:
        print(e)
        btn.configure(background="#d8d106")
        btn.configure(text="Listen")
        messagebox.showerror(
            title="Error",
            message='''Some error occurred,\n
                    please try gain later'''
        )

#
# speak("Hi, How are you")

top = tk.Tk()

        
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font10 = "-family {Segoe UI} -size 13 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font9 = "-family {Courier New} -size 15 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"

top.geometry("553x180")
top.title("Jarvis")
top.configure(background="#add2d6")

Entry1 = tk.Entry(top)
Entry1.place(relx=0.054, rely=0.111,height=34, relwidth=0.893)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font=font9)
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")
Entry1.configure(width=494)

Button1 = tk.Button(top, command = lambda:speak(Entry1.get(), False))
Button1.place(relx=0.054, rely=0.389, height=33, width=236)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#ccd829")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Speak''')
Button1.configure(width=236)


menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
top.configure(menu = menubar)

Button1_1 = tk.Button(top, command = lambda:speak(Entry1.get(), True))
Button1_1.place(relx=0.506, rely=0.389, height=33, width=246)
Button1_1.configure(activebackground="#ececec")
Button1_1.configure(activeforeground="#000000")
Button1_1.configure(background="#ccd829")
Button1_1.configure(disabledforeground="#a3a3a3")
Button1_1.configure(foreground="#000000")
Button1_1.configure(highlightbackground="#d9d9d9")
Button1_1.configure(highlightcolor="black")
Button1_1.configure(pady="0")
Button1_1.configure(text='''Save and play''')
Button1_1.configure(width=246)

Button2 = tk.Button(top, command = lambda: listenToUser(Button2))
Button2.place(relx=0.054, rely=0.667, height=33, width=496)
Button2.configure(activebackground="#ececec")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#d8d106")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(font=font10)
Button2.configure(foreground="#fff")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Listen''')
Button2.configure(width=496)

top.mainloop()



