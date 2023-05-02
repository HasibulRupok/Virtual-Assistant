# Virtual_Assistant


This virtual assistant, created in Python, uses speech recognition and text-to-speech capabilities to interact with the user. Here's a brief description of how your virtual assistant works:

1. Importing necessary modules: The code begins by importing the required modules, including `pyttsx3` for text-to-speech conversion, `speech_recognition` for speech recognition, `pywhatkit` for playing songs on YouTube, `datetime` for retrieving the current time, `wikipedia` for fetching information from Wikipedia, and `pyjokes` for generating jokes.

2. Initializing the speech synthesis engine: The speech synthesis engine is initialized using `pyttsx3`. The voice is set to the second voice in the available voices.

3. Defining the `talk` function: This function takes a text input and uses the speech synthesis engine to convert it into speech. The speech is then spoken out by the virtual assistant using the `runAndWait()` method.

4. Defining the `takeInput` function: This function listens to the user's voice input through the microphone. It utilizes the `speech_recognition` module to recognize the speech and convert it into text. The recognized text is then returned as the user's command.

5. Implementing the `run_alexa` function: This function is the core logic of your virtual assistant. It calls the `takeInput` function to get the user's command. It then processes the command using various `if` statements to perform different actions:
   - If the command contains "play," it extracts the song name and plays it on YouTube using `pywhatkit.playonyt`.
   - If the command contains "time," it retrieves the current time using `datetime` and speaks it out.
   - If the command contains "tell me about," it extracts the search query and fetches a summary from Wikipedia using `wikipedia.summary`. The summary is then spoken out.
   - If the command contains "are you single," it responds with a predefined answer about the assistant's relationship status.
   - If the command contains "tell me a joke," it generates a random joke using `pyjokes` and speaks it out.
   - If the command contains "how are you," it responds with a predefined answer about the assistant's well-being.
   - If none of the above conditions are met, it responds with a generic message indicating it didn't understand the user's command.

6. Running the virtual assistant: The code enters an infinite loop and repeatedly calls the `run_alexa` function to continuously listen for and respond to user commands.

The virtual assistant uses speech recognition to understand user commands, performs actions based on those commands (such as playing songs, retrieving information, telling jokes, etc.), and utilizes text-to-speech conversion to provide responses.

## Packages:
    SpeechRecognition
    pyttsx3
    PyAudio
    pywhatkit
    datetime
    wikipedia
    pyjokes

## to run this code install this packages by this command:
    pip install SpeechRecognition
    pip install pyttsx3
    pip install PyAudio
    pip install pywhatkit
    pip install wikipedia
    pip install pyjokes

*** Make sure you install all the packages to run the code

*** You can download the full project from =>
                https://drive.google.com/file/d/18YGgbL1t1ZwjNT6D3562K2NP5UH1MbIC/view?usp=sharing

You can watch the project demo on Youtube => https://youtu.be/ViZtKUgJHMQ
