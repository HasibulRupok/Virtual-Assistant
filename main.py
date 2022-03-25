import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takeInput():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            inputVoice = listener.listen(source)
            inputCommand = listener.recognize_google(inputVoice)
            inputCommand = inputCommand.lower()

            if "alexa" in inputCommand:
                inputCommand = inputCommand.replace("alexa", "")
            elif "hey alexa" in inputCommand:
                inputCommand = inputCommand.replace("hey alexa", "")

    except:
        pass

    return inputCommand


def run_alexa():
    input = takeInput()

    if "play" in input:
        song = input.replace('play', '')
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in input:
        time = datetime.datetime.now().strftime("%I:%M %p")  # %H for 24 hour formate, %I for 12 hr
        talk("it is " + time)
    elif "tell me about" in input:
        searchString = input.replace("tell me about", "")
        result = wikipedia.summary(searchString, 2)
        talk(result)
    elif "are you single" in input:
        talk("my creator did not give me the permission to get into a relationship so its complicated, never ask me "
             "about this")
    elif "tell me a joke" in input:
        talk(pyjokes.get_joke())
    elif "how are you" in input:
        talk("I am doing good, what about you?")
    else:
        talk("I can't get you, please say again")


while True:
    run_alexa()
