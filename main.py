import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'chintu' in command:
                command = command.replace('chintu','')
                print(command)
    except:
        pass
    return command

def run_chintu():
    command = take_command()

    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('chintu here,the time is ' + time)
    elif 'wikipedia'in command:
        answer = command.replace('wikipedia says','')
        info = wikipedia.summary(answer, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('HELLO ....its chintu')
        talk('how may i help you?')
    else:
        talk('errrrrrrrrrr... please say the command again')

while True:
    run_chintu()