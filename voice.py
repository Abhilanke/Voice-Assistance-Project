
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import ctypes
import pyjokes
import subprocess
import requests
from bs4 import BeautifulSoup
import wolframalpha
import textwrap

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    """
    12:00 - noon
    1:00 pm - morning / 13:00 - afternoon
    18:00 - evening 
    """
    if hour >=0 and hour<=12:
        speak("good morning  abhishek")
        print("good morning abhishek")
    elif hour >=12 and hour < 18:
        speak("good afternoon abhishek")
    else:
        speak(" good evening  abhishek")
    speak("let me know how can i help you,what are you looking for?")
    print("let me know how can i help you,what are you looking for?")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listning to you abhishek....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing your voice....")
        query = r.recognize_google(audio, language='en-in,')
        print(f"my dear frind you said : {query}\n")

    except Exception as e:
        print("abhishek say that again please.....")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lankeabhishek@gmail.com','oxhznxpecptzuxod')
    server.sendmail('lankeabhishek@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()

        if 'according to wikipedia' in query or 'information about'in query.lower():
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=1)
                print('\n'.join(textwrap.wrap(results, width=80)))

                speak(results)
            except wikipedia.exceptions.PageError:
                pass

        if 'open notepad' in query:
            npath ="c:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif'open paint'in query:
            npath ="C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)

        elif'open word'in query:
            os.system("start winword")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open whatsapp'in query:
            webbrowser.open("whatsapp.com")

        elif 'tell me the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"my dear friend,the time is{strTime}")
            print(f"my dear frind,the time is{strTime}")

        elif 'email to kunal1' in query:
            while True:
                try:
                    speak("What should I send?")
                    content = takecommand()
                    speak("You said: " + content + ". Is that correct?")
                    response = takecommand()
                    if 'yes' in response:
                        to = "kunalnikam0123@gmail.com"
                        sendEmail(to, content)
                        speak("Your email has been sent successfully")
                        print("Your email has been sent successfully")
                        break  # Exit the loop after the email is sent
                    else:
                        speak("Please provide the correct content for the email")
                except Exception as e:
                    print(e)
                    speak("My dear friend, I am unable to send the email. Please address the error")


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",  0)
            speak("Background changed successfully")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif'play music'in query:
            music_dir='F:\\song\\My Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "open wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "temperature" in query:
            search ="temperature in yeola"
            url = f"https://www.google.com/serch?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe")
            speak(f"current {search} is {temp}")
        elif "calculate" in query:

            app_id = "HTR4HT-PYA2R8R7QH"
            client = wolframalpha.Client("HTR4HT-PYA2R8R7QH")
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        elif 'search' in query or 'play' in query or 'what are' in query or 'who is' in query  or 'how' in query  or 'where' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            query = query.replace("what are", "")
            query = query.replace("who is", "")
            query = query.replace("how", "")
            query = query.replace("where", "")
            webbrowser.open(query)
        elif "what is" in query :
            client = wolframalpha.Client("HTR4HT-PYA2R8R7QH")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No result")

        elif 'email to priyanka' in query:
            while True:
                try:
                    speak("What should I send?")
                    content = takecommand()
                    speak("You said: " + content + ". Is that correct?")
                    response = takecommand()
                    if 'yes' in response:
                        to = "thakarepriyanka51@gmail.com"
                        sendEmail(to, content)
                        speak("Your email has been sent successfully")
                        print("Your email has been sent successfully")
                        break  # Exit the loop after the email is sent
                    else:
                        speak("Please provide the correct content for the email")
                except Exception as e:
                    print(e)
                    speak("My dear friend, I am unable to send the email. Please address the error")
        elif 'email to kunal' in query:
            while True:
                try:
                    speak("What should I send?")
                    content = takecommand()
                    speak("You said: " + content + ". Is that correct?")
                    response = takecommand()
                    if 'yes' in response:
                        to = "kunalnikam0123@gmail.com"
                        sendEmail(to, content)
                        speak("Your email has been sent successfully")
                        print("Your email has been sent successfully")
                        break  # Exit the loop after the email is sent
                    else:
                        speak("Please provide the correct content for the email")
                except Exception as e:
                    print(e)
                    speak("My dear friend, I am unable to send the email. Please address the error")

        elif 'send email' in query:
            while True:
                try:
                    speak("Whom should I send the email to?")
                    to = input("Please enter the recipient's email address: ")
                    speak("What should I send?")
                    content = takecommand()
                    speak("You said: " + content + ". Is that correct?")
                    response = takecommand()
                    if 'yes' in response:
                        sendEmail(to, content)
                        speak("Your email has been sent successfully")
                        print("Your email has been sent successfully")
                        break  # Exit the loop after the email is sent
                    else:
                        speak("Please provide the correct content for the email")
                except Exception as e:
                    print(e)
                    speak("My dear friend, I am unable to send the email. Please address the error")
"""
pyttsx3= puthon text to speech
smtplib= sending emails
speech_recognition= use to convert spoken word into text and work on api's
os= used to work/interact with operatng system
automate_wikipedia= used for automate webbrowser
datetime used to work with the date and time
Developed by Abhi
"""
















