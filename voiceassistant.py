import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand your request.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error connecting to the speech recognition service.")
        return ""

# Function to set a reminder
def set_reminder():
    speak("What task would you like to be reminded of?")
    task = listen()
    if task:
        speak("When should I remind you?")
        time = listen()
        try:
            # Convert time to a datetime object
            time = datetime.datetime.strptime(time, "%H:%M")
            now = datetime.datetime.now()

            # Calculate the time difference
            delta = time - now

            if delta.total_seconds() <= 0:
                speak("Sorry, that time has already passed.")
            else:
                speak(f"I will remind you to '{task}' in {delta.seconds // 3600} hours and {(delta.seconds // 60) % 60} minutes.")
        except ValueError:
            speak("Sorry, I couldn't understand the time.")

# Function to search the web
def search_web():
    speak("What would you like to search for?")
    query = listen()
    if query:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        speak(f"Here are the search results for '{query}'.")

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()

        if "reminder" in command:
            set_reminder()
        elif "search" in command:
            search_web()
        elif "exit" in command:
            speak("Goodbye!")
            break
