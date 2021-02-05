import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    speak("Current time is")
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)


def date():
    speak("current date is")
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)





def wishme():
    speak("Welcome Back Team ")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening Sir")
    else:
        speak("Good Night Sir")

    speak("I am Reable  your personal voice assistant at your service tell me  how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please ....")
        return "None"

    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail,com', 5874)
    server.ehlo()
    server.starttls()
    server.login('krsri1998@gmail.com', 'Karan1998#')
    server.sendmail('snehbhat100@gmail.com', to, content)
    server.close()


def said():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening Sir")
    else:
        speak("Good Night Sir")




def talk(que):
    speak("I am karan personal talking assistant i will be his voice ")
    said()
    while True:
        a = input()
        if "quit" in a:
            break
        else:
            speak(a)
        que = takeCommand().lower()


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'offline' in query:
            quit()
        elif 'wikipedia' in query:
            speak("Searching ...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendemail(to, content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("unable to sent email")
        elif 'search in chrome' in query:
            speak("what should i search")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'play songs' in query:
            songs_dir = 'D:\\music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("what should i remember")
            data = takeCommand()
            speak("you said me to remember " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'joke' in query:
            jokes()

        elif 'talk' in query:
            talk(query)