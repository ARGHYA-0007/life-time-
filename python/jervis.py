

import webbrowser
import urllib.parse
import time
import sys

try:
    import speech_recognition as sr
except Exception as e:
    print("Missing dependency: SpeechRecognition. Install with `pip install SpeechRecognition`.")
    raise

try:
    import pyttsx3
except Exception as e:
    print("Missing dependency: pyttsx3. Install with `pip install pyttsx3`.")
    raise

# Optional: play YouTube top result
try:
    import pywhatkit
    HAVE_PYWHATKIT = True
except Exception:
    HAVE_PYWHATKIT = False

engine = pyttsx3.init()
engine.setProperty("rate", 150)  # speaking rate

def speak(text):
    """Speak and print the text for feedback."""
    print("Jervis:", text)
    engine.say(text)
    engine.runAndWait()

def listen(timeout=6, phrase_time_limit=8):
    """Listen from the microphone and return recognized text (lowercased)."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.7)
        speak("Listening...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return ""
    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        speak("Sorry, speech service is unavailable.")
        print("Speech API error:", e)
        return ""

def google_search(query):
    q = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={q}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

def youtube_open():
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube")

def youtube_search(query):
    q = urllib.parse.quote_plus(query)
    url = f"https://www.youtube.com/results?search_query={q}"
    webbrowser.open(url)
    speak(f"Searching YouTube for {query}")

def play_on_youtube(query):
    if HAVE_PYWHATKIT:
        speak(f"Playing top YouTube result for {query}")
        try:
            pywhatkit.playonyt(query)  # opens top result in browser
        except Exception as e:
            speak("Couldn't play the video automatically. I'll open search results instead.")
            youtube_search(query)
            print("pywhatkit error:", e)
    else:
        speak("Auto-play isn't available because pywhatkit isn't installed. Opening search results instead.")
        youtube_search(query)

def parse_and_act(command):
    """Interpret the spoken command and act."""
    if not command:
        speak("I didn't catch that. Try again or say 'exit' to quit.")
        return True  # continue

    # common patterns
    if command.startswith("exit") or command.startswith("quit") or "stop jervis" in command:
        speak("Goodbye!")
        return False  # stop loop

    # Google search
    if command.startswith("search google for "):
        query = command.replace("search google for ", "", 1).strip()
        if query:
            google_search(query)
        else:
            speak("What should I search for on Google?")
        return True

    if command.startswith("google "):
        query = command.replace("google ", "", 1).strip()
        if query:
            google_search(query)
        else:
            speak("What should I search for on Google?")
        return True

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
        return True

    # YouTube
    if "open youtube" in command or command.strip() == "youtube":
        youtube_open()
        return True

    if command.startswith("search youtube for "):
        query = command.replace("search youtube for ", "", 1).strip()
        if query:
            youtube_search(query)
        else:
            speak("What should I search for on YouTube?")
        return True

    if command.startswith("youtube "):
        query = command.replace("youtube ", "", 1).strip()
        if query:
            youtube_search(query)
        else:
            youtube_open()
        return True

    # play on youtube
    if "play " in command and "on youtube" in command:
        # e.g. "play best guitar lesson on youtube"
        query = command.split("play",1)[1].split("on youtube",1)[0].strip()
        if query:
            play_on_youtube(query)
        else:
            speak("What should I play on YouTube?")
        return True

    if command.startswith("play "):
        # assume user wants YouTube if they say "play"
        query = command.replace("play ", "", 1).strip()
        if query:
            play_on_youtube(query)
        else:
            speak("What would you like me to play?")
        return True

    # fallback heuristics: if user just says a topic, ask whether they want Google or YouTube
    # We'll attempt Google by default
    speak(f"I'll search Google for: {command}")
    google_search(command)
    return True

def main_loop():
    speak("Hello — I'm Jervis. Say 'search google for ...', 'search youtube for ...', 'open youtube', or 'play ... on youtube'. Say 'exit' to quit.")
    running = True
    while running:
        command = listen()
        try:
            running = parse_and_act(command)
        except Exception as e:
            speak("Oops, something went wrong.")
            print("Error while handling command:", e)
            # continue loop

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        speak("Bye!")
        sys.exit(0)
