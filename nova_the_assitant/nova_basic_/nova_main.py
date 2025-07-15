import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import sounddevice as sd
import numpy as np
import sys
import winsound
import os
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import psutil
import threading
import time
import random

# Setup
user_name = "Yashwanth"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)
listening_enabled = True

# GUI Setup
root = tk.Tk()
root.title("NOVA-X Interface")
root.geometry("1280x800")
root.configure(bg="black")

# === Background ===
try:
    bg_img = Image.open("background.jpg")
    bg_img = bg_img.resize((1280, 800))
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Couldn't load background image:", e)

# === NOVA-X Logo ===
try:
    tronix_img = Image.open("nova_logo.png")
    tronix_img = tronix_img.resize((180, 180))
    tronix_photo = ImageTk.PhotoImage(tronix_img)
    logo_label = tk.Label(root, image=tronix_photo, bg="black")
    logo_label.image = tronix_photo
    logo_label.place(x=30, y=30)
except Exception as e:
    print("Couldn't load NOVA-X logo:", e)

# === GUI Labels ===
time_label = Label(root, text="", font=("Consolas", 20), fg="cyan", bg="black")
time_label.place(x=1000, y=20)

cpu_label = Label(root, text="", font=("Consolas", 16), fg="lime", bg="black")
cpu_label.place(x=1000, y=60)

status_label = Label(root, text="Waiting for wake word...", font=("Consolas", 16), fg="yellow", bg="black")
status_label.place(x=20, y=750)

# === Circle Beat Visualization ===
canvas = tk.Canvas(root, width=300, height=120, bg="black", highlightthickness=0)
canvas.place(x=500, y=680)
circle1 = canvas.create_oval(10, 30, 50, 70, outline="cyan", width=3)
circle2 = canvas.create_oval(60, 30, 100, 70, outline="cyan", width=3)
circle3 = canvas.create_oval(110, 25, 150, 75, outline="deepskyblue", width=4)

speaking = tk.BooleanVar(value=False)

# === Arc Reactor (center animation) with transparent background ===
try:
    arc_img = Image.open("arc_reactor.png")
    arc_img = arc_img.resize((500, 500))
    arc_img = ImageTk.PhotoImage(arc_img)
    arc_label = Label(root, image=arc_img, bg="black", bd=0)
    arc_label.image = arc_img
    arc_label.place(x=390, y=130)
except Exception as e:
    print("Couldn't load arc reactor image:", e)


def animate_arc(stop_event):
    while not stop_event.is_set():
        arc_label.config(highlightbackground=random.choice(["red", "deepskyblue", "blue", "aqua"]))
        time.sleep(0.05)


def beat_circles():
    canvas.delete(circle3)
    if speaking.get():
        canvas.create_oval(110, 20, 150, 80, outline="aqua", width=5)
    else:
        canvas.create_oval(110, 25, 150, 75, outline="deepskyblue", width=4)
    root.after(100, beat_circles)


def speak(text):
    def update_status():
        status_label.config(text=f"NOVA-X: {text}")
        status_label.update()

    root.after(0, update_status)
    print(f"NOVA-X: {text}")
    speaking.set(True)
    stop_event = threading.Event()
    t = threading.Thread(target=animate_arc, args=(stop_event,))
    t.start()
    engine.say(text)
    engine.runAndWait()
    stop_event.set()
    speaking.set(False)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="🎤 Listening...")
        status_label.update()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        status_label.config(text="🎵 Recognizing...")
        status_label.update()
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"{user_name}: {query}")
        status_label.config(text=f"You said: {query}")
        return query.lower()
    except:
        return ""


def greet():
    hour = datetime.datetime.now().hour
    part = "morning" if hour < 12 else "afternoon" if hour < 18 else "evening"
    speak(f"Hello Yashwanth, good {part}! How can I assist you?")


def handle_command(command):
    global listening_enabled
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"It's {current_time} now.")
    elif 'google' in command:
        topic = command.replace("google", "").strip()
        if topic:
            webbrowser.open(f"https://www.google.com/search?q={topic}")
            speak(f"Searching Google for {topic}.")
        else:
            speak("Tell me what to search.")
    elif 'close' in command:
        os.system("taskkill /im chrome.exe /f")
        speak("Closed the window.")
    elif 'play' in command:
        song = command.replace("play", "").strip()
        if song:
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)
            listening_enabled = False
            speak("I'll pause listening. Say 'nova' to continue or say 'terminate' to exit.")
            if wait_for_wake_word():
                listening_enabled = True
                greet()
            else:
                root.quit()
                sys.exit()
        else:
            speak("Which song?")
    elif 'notepad' in command:
        os.system("notepad")
        speak("Opening Notepad")
    elif 'exit' in command:
        speak("Goodbye Yashwanth.")
        root.quit()
        sys.exit()
    else:
        speak("I didn't understand that command.")


def wait_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Music Mode... Say 'Nova' to continue or 'terminate' to exit")
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
                query = recognizer.recognize_google(audio, language='en-in').lower()
                if 'nova' in query:
                    winsound.Beep(1000, 200)
                    return True
                elif 'terminate' in query:
                    speak("Terminating NOVA-X. Goodbye.")
                    root.quit()
                    sys.exit()
            except:
                continue


def update_system_info():
    while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p")
        root.after(0, lambda: time_label.config(text=now))
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        root.after(0, lambda: cpu_label.config(text=f"CPU: {cpu}%   MEM: {mem}%"))
        time.sleep(1)


def listen_loop():
    global listening_enabled
    while True:
        if not listening_enabled:
            time.sleep(1)
            continue
        query = listen()
        if 'nova' in query:
            winsound.Beep(1000, 200)
            greet()
            while True:
                if not listening_enabled:
                    break
                command = listen()
                if command:
                    handle_command(command)


def main():
    threading.Thread(target=update_system_info, daemon=True).start()
    beat_circles()
    speak("Say 'Nova' to start.")
    threading.Thread(target=listen_loop, daemon=True).start()
    root.mainloop()


if __name__ == "__main__":
    main()
