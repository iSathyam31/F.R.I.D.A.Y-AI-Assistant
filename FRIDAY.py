import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import os
import cv2
from requests import get
import smtplib
import psutil
import instaloader
import pyautogui
import PyPDF2
from bs4 import BeautifulSoup
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pywikihow import search_wikihow
import speedtest_cli
from pytube import YouTube
import qrcode


#### Using the pyttsx3 for the voice of the assistant ####
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #index '0' for 'David'(male) voice index '1' for 'zira'(female) voice


#### Setting up basic functions for F.R.I.D.A.Y ####


# 1. Clock
def Clock_time(query):
        print(query)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak("Current time is "+time)
        
        
# 2. Calander    
def Cal_day():
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week
    
    
# 3. Audio and the Greeting function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = Cal_day()
    print(t)
    if (hour >= 0) and (hour <= 12) and ('AM' in t):
        speak(f'Good morning Boss ! its {day} and the time is {t}')
    elif (hour >= 12) and (hour <= 16) and ('PM' in t):
        speak(f"Hope you had your brunch, good afternoon boss, its {day} and the time is {t}")
    else:
        speak(f"good evening boss, its {day} and the time is {t}")

    speak("How are you? I am your personel AI Assistant Jarvis! How can I be of service")
    
 
# 4. Command Function    
def command():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')  ##speech to text
        print(f"You said: {query}\n")

    except Exception as e:
          
        print("I could not get you, please speak again")  
        return "None"
    return query      


# 5. Intro
def Intro():
        while True:                
            permission = command()
            print(permission)
            if ("wake up" in permission) or ("get up" in permission):
                run_jarvis()
            elif ("goodbye" in permission) or ("get lost" in permission):
                speak("Thanks for using me boss, have a good day")
                sys.exit()          
                
                
######################################################################################
## SETTING UP ALL THE TASK FUNCTION ##
 
## Weather Forecasting

def temperature(query):
    IP_Address = get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
    geo_request = get(url)
    geo_data = geo_request.json()
    city = geo_data['city']
    search = f"temperature in {city}"
    url_1 = f"https://www.google.com/search?q={search}"
    r = get(url_1)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current {search} is {temp}")
    
    
## Internet speed

def InternetSpeed(query):
        speak("Wait a few seconds boss, checking your internet speed")
        st = speedtest_cli.Speedtest()
        dl = st.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        print(dl,up)
        speak(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")
     
     
## Search for processes how to

def How(query):
        speak("How to do mode is is activated")
        while True:
            speak("Please tell me what you want to know")
            how = self.take_query()
            try:
                if ("exit" in how) or("close" in how):
                    speak("Ok sir how to mode is closed")
                    break
                else:
                    max_result=1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
            except Exception as e:
                speak("Sorry sir, I am not able to find this")
                
                
## Communication commands

def comum(query):
        print(query)
        if ('hi'in query) or('hai'in query) or ('hey'in query) or ('hello' in query) :
            speak("Hello boss what can I help for u")
        else :
            self.No_result_found()
            
            
## Fun commands to interact with Friday

def Fun(query):
        print(query)
        if 'what is your name' in query:
            speak("My name is friday")
        elif 'what is my name' in query:
            speak("your name is Sathyam")
        elif 'what is my university name' in query:
            speak("you are studing in Indian Institute of Information Technology Sri City, with bachelors in Computer Science") 
        elif 'what can you do' in query:
            speak("I talk with you until you want to stop Boss, please consider me as your best friend")
        elif 'what is your age' in query:
            speak("I am very young that u")
        elif 'let us go for a date' in query:
            speak('Sure Boss, I would love to')
        elif 'are you single' in query:
            speak('No, I am in a relationship with you')
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
        elif 'are you there' in query:
            speak('Yes boss I am here')
        elif 'tell me something' in query:
            speak('boss, I don\'t have much to say, you only tell me someting i will give you the company')
        elif 'thank you' in query:
            speak('boss, I am here to help you..., your welcome')
        elif 'in your free time' in query:
            speak('boss, I will be listening to all your words')
        elif 'i love you' in query:
            speak('Aww, that is so sweet of you Boss...,I love you too')
        elif 'can you hear me' in query:
            speak('Yes Boss, I can hear you')
        elif 'do you ever get tired' in query:
            speak('It would be impossible to tire of our conversation')
        else :
            self.No_result_found()                                            
            
#Web camera
    #NOTE to exit from the web camera press "ESC" key 
def webCam(self):    
        speak('Opening camera')
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('web camera',img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()     
     
            
## Social media accounts

def social(query):
        print(query)
        if 'facebook' in query:
            speak('opening your facebook')
            webbrowser.open('https://www.facebook.com/')
        elif 'whatsapp' in query:
            speak('opening your whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        elif 'instagram' in query:
            speak('opening your instagram')
            webbrowser.open('https://www.instagram.com/iSathyam31')
        elif 'twitter' in query:
            speak('opening your twitter')
            webbrowser.open('https://twitter.com/')
        elif 'discord' in query:
            speak('opening your discord')
            webbrowser.open('https://discord.com/')
        else :
            self.No_result_found()
            
            
## Browser search command

def B_S(query):
        print(query)
        try:
            # ('what is meant by' in query) or ('tell me about' in query) or ('who the heck is' in query)
            if ('wikipedia' in query):
                target1 = query.replace('search for','')
                target1 = target1.replace('in wikipedia','')
            elif('what is meant by' in query):
                target1 = query.replace("what is meant by"," ")
            elif('tell me about' in query):
                target1 = query.replace("tell me about"," ")
            elif('who the heck is' in query):
                target1 = query.replace("who the heck is"," ")
            print("searching....")
            info = wikipedia.summary(target1,5)
            print(info)
            speak("according to wikipedia "+info)
        except :
            self.No_result_found()
            
            
## Browser

def brows(query):
        print(query)
        if 'google' in query:
            speak("Boss, what should I search on google..")
            S = self.take_query()#taking query for what to search in google
            webbrowser.open(f"{S}")
        elif 'edge' in query:
            speak('opening your Miscrosoft edge')
            os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\ApplicationMicrosoftEdge.exe')#path for your edge browser application
        else :
            self.No_result_found()
            
            
## Google Application selection

def Google_Apps(query):
        print(query)
        if 'gmail' in query:
            speak('opening your google gmail')
            webbrowser.open('https://mail.google.com/mail/')
        elif 'maps' in query:
            speak('opening google maps')
            webbrowser.open('https://www.google.co.in/maps/')
        elif 'news' in query:
            speak('opening google news')
            webbrowser.open('https://news.google.com/')
        elif 'calender' in query:
            speak('opening google calender')
            webbrowser.open('https://calendar.google.com/calendar/')
        elif 'photos' in query:
            speak('opening your google photos')
            webbrowser.open('https://photos.google.com/')
        elif 'documents' in query:
            speak('opening your google documents')
            webbrowser.open('https://docs.google.com/document/')
        elif 'spreadsheet' in query:
            speak('opening your google spreadsheet')
            webbrowser.open('https://docs.google.com/spreadsheets/')
        else :
            self.No_result_found()
            
            
## Youtube

def yt(query):
        print(query)
        if 'play' in query:
            speak("Boss can you please say the name of the song")
            song = self.take_query()
            if "play" in song:
                song = song.replace("play","")
            speak('playing '+song)
            print(f'playing {song}')
            pywhatkit.playonyt(song)
            print('playing')
        elif "download" in query:
            speak("Boss please enter the youtube video link which you want to download")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            speak(f"Boss downloaded {yt.title} from the link you given into the main folder")
        elif 'youtube' in query:
            speak('opening your youtube')
            webbrowser.open('https://www.youtube.com/')
        else :
            self.No_result_found()
            
            
## Open source accounts

def open_source(query):
        print(query)
        if 'github' in query:
            speak('opening your github')
            webbrowser.open('https://github.com/iSathyam31')
        elif 'gitlab' in query:
            speak('opening your gitlab')
            webbrowser.open('https://gitlab.com/-/profile')
        else :
            self.No_result_found()
            
            
## OTT

def OTT(query):
        print(query)
        if 'hotstar' in query:
            speak('opening your disney plus hotstar')
            webbrowser.open('https://www.hotstar.com/in')
        elif 'prime' in query:
            speak('opening your amazon prime videos')
            webbrowser.open('https://www.primevideo.com/')
        elif 'netflix' in query:
            speak('opening Netflix videos')
            webbrowser.open('https://www.netflix.com/')
        else :
            self.No_result_found()
            
            
## Opening local application

def OpenApp(query):
        print(query)
        if ('calculator'in query) :
            speak('Opening calculator')
            os.startfile('C:\\Windows\\System32\\calc.exe')
        elif ('paint'in query) :
            speak('Opening msPaint')
            os.startfile('c:\\Windows\\System32\\mspaint.exe')
        elif ('notepad'in query) :
            speak('Opening notepad')
            os.startfile('c:\\Windows\\System32\\notepad.exe')
        elif ('discord'in query) :
            speak('Opening discord')
            os.startfile('..\\..\\Discord.exe')
        elif ('editor'in query) :
            speak('Opening your Visual studio code')
            os.startfile('..\\..\\Code.exe')
        elif ('spotify'in query) :
            speak('Opening spotify')
            os.startfile('..\\..\\Spotify.exe')
        else :
            self.No_result_found()
            
            
## Closing a local application

def CloseApp(query):
        print(query)
        if ('calculator'in query) :
            speak("okay boss, closeing caliculator")
            os.system("taskkill /f /im calc.exe")
        elif ('paint'in query) :
            speak("okay boss, closeing mspaint")
            os.system("taskkill /f /im mspaint.exe")
        elif ('notepad'in query) :
            speak("okay boss, closeing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif ('discord'in query) :
            speak("okay boss, closeing discord")
            os.system("taskkill /f /im Discord.exe")
        elif ('editor'in query) :
            speak("okay boss, closeing vs code")
            os.system("taskkill /f /im Code.exe")
        elif ('spotify'in query) :
            speak("okay boss, closeing spotify")
            os.system("taskkill /f /im Spotify.exe")
        else :
            self.No_result_found()
            
            
## Shopping Links

def shopping(query):
        print(query)
        if 'flipkart' in query:
            speak('Opening flipkart online shopping website')
            webbrowser.open("https://www.flipkart.com/")
        elif 'amazon' in query:
            speak('Opening amazon online shopping website')
            webbrowser.open("https://www.amazon.in/")
        else :
            self.No_result_found()
            
            
## PDF Reader

def pdf_reader(query):
        speak("Boss enter the name of the book which you want to read")
        n = input("Enter the book name: ")
        n = n.strip()+".pdf"
        book_n = open(n,'rb')
        pdfReader = PyPDF2.PdfFileReader(book_n)
        pages = pdfReader.numPages
        speak(f"Boss there are total of {pages} in this book")
        speak("plsase enter the page number Which I nedd to read")
        num = int(input("Enter the page number: "))
        page = pdfReader.getPage(num)
        text = page.extractText()
        print(text)
        speak(text)
        
        
## Time calculating algorithm

def silenceTime(query):
        print(query)
        x=0
        #caliculating the given time to seconds from the speech commnd string
        if ('10' in query) or ('ten' in query):x=600
        elif '1' in query or ('one' in query):x=60
        elif '2' in query or ('two' in query):x=120
        elif '3' in query or ('three' in query):x=180
        elif '4' in query or ('four' in query):x=240
        elif '5' in query or ('five' in query):x=300
        elif '6' in query or ('six' in query):x=360
        elif '7' in query or ('seven' in query):x=420
        elif '8' in query or ('eight' in query):x=480
        elif '9' in query or ('nine' in query):x=540
        silence(x)
        
        
## Silence

def silence(query,k):
        t = k
        s = "Ok boss I will be silent for "+str(t/60)+" minutes"
        speak(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        speak("Boss "+str(k/60)+" minutes over")



## Mail verification

def verifyMail(query):
        try:
            speak("what should I say?")
            content = self.take_query()
            speak("To whom do u want to send the email?")
            to = self.take_query()
            self.SendEmail(to,content)
            speak("Email has been sent to "+str(to))
        except Exception as e:
            print(e)
            speak("Sorry sir I am not not able to send this email")
            
            
## Mail sender

def SendEmail(query,to,content):
        print(content)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("YOUR_MAIL_ID","PASWORD")
        server.sendmail("YOUR_MAIL_ID",to,content)
        server.close()
        
        
## Location

def locaiton(query):
        speak("Wait boss, let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
            speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            speak("Sorry boss, due to network issue i am not able to find where we are.")
            pass
        
        
## Screenshot

def scshot(query):
        speak("Boss, please tell me the name for this screenshot file")
        name = self.take_query()
        speak("Please boss hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("I am done boss, the screenshot is saved in main folder.")
        
        
## System condition

def condition(query):
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage + " percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    speak(f"Boss our system have {percentage} percentage Battery")
    if percentage >= 75:
        speak(f"Boss we could have enough charging to continue our work")
    elif percentage >= 40 and percentage <= 75:
        speak(f"Boss we should connect out system to charging point to charge our battery")
    elif percentage >= 15 and percentage <= 30:
        speak(f"Boss we don't have enough power to work, please connect to charging")
    else:
        speak(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")

# no result found
def No_result_found(self):
    speak('Boss I couldn\'t understand, could you please say it again.')
    
    



#### MAIN FUNCTION ####

class Friday():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            query = self.recognizer.recognize_google(audio).lower()
            print("You:", query)
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Can you repeat?")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

    def run(self):
        while True:
            query = self.listen()

            # Logic for executing tasks based on query
            if ('play a song' in query) or ('youtube' in query) or ("download a song" in query) or ("download song" in query): 
                # commands for opening youtube, playing a song in youtube, and download a song in youtube
                yt(query) # function is from line 555
            
            # Interaction commands with FRIDAY
            elif ('what is your age' in query) or ('are you single' in query) or ('are you there' in query) or ('tell me something' in query) or ('thank you' in query) or ('in your free time' in query) or ('i love you' in query) or ('can you hear me' in query) or ('do you ever get tired' in query):
                Fun(query)
            
            elif 'time' in query: 
                Clock_time(query)
            
            elif (('hi' in query) and len(query)==2) or ((('hai' in query) or ('hey' in query)) and len(query)==3) or (('hello' in query) and len(query)==5):
                comum(query)
            
            elif ('what can you do' in query) or ('your name' in query) or ('my name' in query) or ('university name' in query):
                Fun(query)
            
            elif ('tell me joke' in query) or ('let us go for a date' in query):
                Fun(query)
            
            # It will tell the day Eg : Today is Wednesday
            elif ("today" in query):
                day = self.Cal_day()
                speak("Today is "+day)
            
            # command if you don't want FRIDAY to speak until for a certain time
            # Note: FRIDAY can be silent for a max of 10 mins
            # Eg: FRIDAY keep quiet for 5 minutes 
            elif ('silence' in query) or ('silent' in query) or ('keep quiet' in query) or ('wait for' in query):
                silenceTime(query)
            
            # Command for opening your social media accounts in browser
            # Eg: FRIDAY open facebook (or) FRIDAY open social media facebook 
            elif ('facebook' in query) or ('whatsapp' in query) or ('instagram' in query) or ('twitter' in query) or ('discord' in query) or ('social media' in query):
                social(query)
            
            # command for opening your OTT platform accounts
            # Eg: open hotstart
            elif ('hotstar' in query) or ('prime' in query) or ('netflix' in query):
                OTT(query)
            
            # command to search for something in wikipedia
            # Eg: what is meant by python in wikipedia (or) search for "_something_" in wikipedia
            elif ('wikipedia' in query) or ('what is meant by' in query) or ('tell me about' in query) or ('who the heck is' in query):
                B_S(query)
            
            # command for opening your browsers and search for information in google
            elif ('open google' in query) or ('open edge' in query):
                brows(query)
            
            # command to open your google applications
            elif ('open gmail' in query) or ('open maps' in query) or ('open calender' in query) or ('open documents' in query) or ('open spredsheet' in query) or ('open images' in query) or ('open drive' in query) or ('open news' in query):
                Google_Apps(query)
            
            # command to open your open-source accounts
            # you can add other if you have
            elif ('open github' in query) or ('open gitlab' in query):
                open_source(query)
            
            # Command to open desktop applications
            # It can open: calculator, notepad, paint, teams(aka online classes), discord, spotify, ltspice, vscode(aka editor), steam, VLC media player
            elif ('open calculator' in query) or ('open notepad' in query) or ('open paint' in query) or ('open discord' in query) or ('open spotify' in query):
                OpenApp(query)
            
            # Command to close desktop applications
            # It can close: calculator, notepad, paint, discord, spotify, ltspice, vscode(aka editor), steam, VLC media player
            elif ('close calculator' in query) or ('close notepad' in query) or ('close paint' in query) or ('close discord' in query) or ('close ltspice' in query) or ('close editor' in query) or ('close spotify' in query) or ('close steam' in query) or ('close media player' in query):
                CloseApp(query)
                
            #command for opening your webcamera
            #Eg: jarvis open webcamera
            elif ('web cam'in query) :
                webCam()
    
            
            # command for opening shopping websites 
            # NOTE: you can add as many websites
            elif ('flipkart' in query) or ('amazon' in query):
                shopping(query)
            
            # command for asking your current location
            elif ('where i am' in query) or ('where we are' in query):
                locaiton()
            
            # command for opening command prompt 
            # Eg: FRIDAY open command prompt
            elif ('command prompt' in query):
                speak('Opening command prompt')
                os.system('start cmd')
            
            # Command for opening taking screenshot
            # Eg: FRIDAY take a screenshot
            elif ('take screenshot' in query) or ('screenshot' in query) or ("take a screenshot" in query):
                scshot()
            
            # Command for reading PDF
            # EG: FRIDAY read pdf
            elif ("read pdf" in query) or ("pdf" in query):
                pdf_reader()
            
            # command for searching for a procedure how to do something
            # Eg: FRIDAY activate mod
            #     FRIDAY How to make a cake (or) FRIDAY how to convert int to string in programming 
            elif "activate mod" in query:
                How()
            
            # command for increasing the volume in the system
            # Eg: FRIDAY increase volume
            elif ("volume up" in query) or ("increase volume" in query):
                pyautogui.press("volumeup")
                speak('volume increased')
            
            # command for decreaseing the volume in the system
            # Eg: FRIDAY decrease volume
            elif ("volume down" in query) or ("decrease volume" in query):
                pyautogui.press("volumedown")
                speak('volume decreased')
            
            # Command to mute the system sound
            # Eg: FRIDAY mute the sound
            elif ("volume mute" in query) or ("mute the sound" in query):
                pyautogui.press("volumemute")
                speak('volume muted')
            
            # command for playing a downloaded mp3 song which is present in your system
            # Eg: FRIDAY play music
            elif 'music' in query:
                try:
                    music_dir = 'E:\\music' # change the song path directory if you have songs in other directory
                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))
                except:
                    speak("Boss an unexpected error occurred")
            
            # command for knowing your system IP address
            # Eg: FRIDAY check my ip address
            elif 'ip address' in query:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                speak(f"your IP address is {ip}")
            
            # command for sending an email 
            # Eg: FRIDAY send email
            elif 'send email' in query:
                verifyMail()
            
            # command for checking the temperature in surroundings
            # FRIDAY check the surroundings temperature
            elif "temperature" in query:
                temperature()
            
            # command for checking internet speed
            # Eg: FRIDAY check my internet speed
            elif "internet speed" in query:
                InternetSpeed()
            
            # command to make FRIDAY sleep
            # Eg: FRIDAY you can sleep now
            elif ("you can sleep" in query) or ("sleep now" in query):
                speak("Okay boss, I am going to sleep you can call me anytime.")

            
            # command for waking FRIDAY from sleep
            # FRIDAY wake up
            elif ("wake up" in query) or ("get up" in query):
                speak("boss, I am not sleeping, I am online, what can I do for u")
            
            # command for exiting FRIDAY from the program
            # Eg: FRIDAY goodbye
            elif ("goodbye" in query) or ("get lost" in query):
                speak("Thanks for using me boss, have a good day")
                sys.exit()
            
            # command for knowing about your system condition
            # Eg: FRIDAY what is the system condition
            elif ('system condition' in query) or ('condition of the system' in query):
                speak("checking the system condition")
                condition()
            
            # command for shutting down the system
            # Eg: FRIDAY shutdown the system
            elif ('shutdown the system' in query) or ('down the system' in query):
                speak("Boss shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")
            
            # command for restarting the system
            # Eg: FRIDAY restart the system
            elif 'restart the system' in query:
                speak("Boss restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")
            
            # command for making the system sleep
            # Eg: FRIDAY sleep the system
            elif 'sleep the system' in query:
                speak("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
                
                               
if __name__ == "__main__":
    assistant = Friday()
    assistant.run()                                                                                                                                                            
                                                            