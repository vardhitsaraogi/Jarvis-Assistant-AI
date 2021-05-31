#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time 

engine=pyttsx3.init()
wolframalpha_id='YLLGLW-9272PYHJWA'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak("Namaste Sir!")

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")#24 hour clock
    #Time=datetime.datetime.now().strftime("%I:%M:%S")#12 hour clock
    speak("The current time is")
    speak(Time)
    
#time_()

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak("The current day is")
    monname=""
    if(month==1):
        monname="January"
    elif(month==2):
        monname="February"
    elif(month==3):
        monname="March"
    elif(month==4):
        monname="April"
    elif(month==5):
        monname="May"
    elif(month==6):
        monname="June"
    elif(month==7):
        monname="July"
    elif(month==8):
        monname="August"
    elif(month==9):
        monname="September"
    elif(month==10):
        monname="October"
    elif(month==11):
        monname="November"
    elif(month==12):
        monname="December"
    speak(str(day)+" "+monname+" "+str(year))
    #speak(str(day)+" "+str(month)+" "+str(year))
    #speak(day)
    #speak(month)
    #speak(year)

#date_()

def wish():
    speak("Welcome back Sir!")
    #time_()
    #date_()
    
    hour=datetime.datetime.now().hour
    if(hour>=6 and hour<12):
        speak("Wishing you a very Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!")
    elif(hour>=18 and hour<24):
        speak("Good Evening!")
    else:
        speak("Good Night! Do sleep well!")
    
    speak("How can I be of your service today sir?")
    
#wish()

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-US')
        print("I recognised: ",end="")
        print(query)
        
    except Exception as e:
        print(e)
        print("Say again please")
        return "None"
    return query

#TakeCommand()

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)#gmail port
    server.ehlo()#identify esmt server
    server.starttls()#low security email
    server.login('user@gmail.com','pwd')
    server.sendmail('user@gmail.com',to,content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    
def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img=pyautogui.screenshot()
    img.save('C:/Users/Vardhit Saraogi/Desktop/Jarvis/SS.png')
    
if __name__ == "__main__":
    wish()
    while True:
        query=TakeCommand().lower()#lower case letters to recognize easily
        
        if 'time' in query:
            time_()
        
        elif 'date' in query:
            date_()
            
        elif 'wikipedia' in query:
            speak("Searching, just give me a moment")
            query=query.replace('wikipedia',' ')
            result=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia "+ result)
            print(result)
        
        elif 'send email' in query:
            try:
                speak("What should the mail contain?")
                content=TakeCommand()
                speak("Who should I send the mail to?")
                receiver=input("Enter email address: ")
                to=receiver
                sendmail(to,content)
                speak("So I am sending "+content+" ?")
                speak("Email has been sent")
                
            except Exception as e:
                print(e)
                speak("Sorry I was not able to send the email")
                
        elif 'search website' in query:
            speak("What should I search?")
            path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search=TakeCommand().lower()
            wb.get(path).open_new_tab(search+'.com')
            
        elif 'search youtube' in query:
            speak("What are you in the mood to watch?")
            term=TakeCommand().lower()
            speak("Taking you to youtube!")
            wb.open('https://www.youtube.com/results?search_query='+term)
            
        elif 'search google' in query:
            speak("What do I search for you?")
            term=TakeCommand().lower()
            speak("Finding results")
            wb.open('https://www.google.com/search?q='+term)
            
        elif 'cpu usage' in query:
            cpu()
            
        elif 'joke' in query:
            speak("Hahaha this one is funny, listen to this")
            joke()
        
        elif 'go offline' in query:
            speak("Going offline sir")
            quit()
            
        elif 'thank you' in query:
            speak("You are most welcome sir, glad I was able to help you, goodbye")
            quit()
        
        elif 'microsoft word' in query:
            speak("Opening MS word")
            #ms=r'C:/Office/Office/WINWORD.EXE'
            ms='C:/Users/Vardhit Saraogi/Desktop/Jarvis/Doc1.docx'
            os.startfile(ms)
            
        elif 'write a note' in query:
            speak("What do you want me to write?")
            notes=TakeCommand()
            file=open("Note.txt",'w')
            speak("Should I add date and time too?")
            ans=TakeCommand()
            if 'yes' in ans:
                tm=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(tm)
                file.write(':-')
                file.write(notes)
                speak("Done taking your notes sir")
            else:
                file.write(notes)
                speak("Done taking your notes sir")
                
        elif 'show note' in query:
            speak("Displaying your notes sir")
            file=open('Note.txt','r')
            print("Your note is: ",file.read())
            
        elif 'screenshot' in query:
            speak("Taking screenshot")
            screenshot()
            
        elif 'music' in query:
            #song='C:/Users/Vardhit Saraogi/Music'
            song='C:/Users/Vardhit Saraogi/Videos/Captures'
            music=os.listdir(song)
            speak("What should I play?")
            speak("There are {} songs to play. Choose a number".format(len(music)-1))
            ans=TakeCommand().lower()
            
            while('number' not in ans and 'any'!=ans and 'random'!=ans):
                speak("Sorry this option is not available, kindly try again")
                ans=TakeCommand().lower()
                
            if 'any' or 'random' in ans:
                num=random.randint(1,len(music)-1)
                st="Playing song number"+str(num)
                speak(st)
            else:                
                num=int(ans.replace('number',' '))
                st="Playing song number"+str(num)
                speak(st)
            os.startfile(os.path.join(song,music[num]))
            
        elif 'remember that' in query:
            speak("What should I remember for you?")
            memory=TakeCommand()
            speak("I will remember "+memory)
            remember=open('Mem.txt','w')
            remember.write(memory)
            remember.close()
            
        elif 'remind me' in query:
            remember=open('Mem.txt','r')
            speak('You had told me to remember '+remember.read())
            
        elif 'news' in query:
            try:
                jsObj=urlopen('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=33867656fe974b64bccc39b1259b4582')
                data=json.load(jsObj)#talks around 10
                i=1
                
                speak("Here is the news for today in regards of business")
                print("------------NEWS--------------"+'\n')
                for item in data['articles']:
                    print(str(i)+": "+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1
            
            except Exception as e:
                print(str(e))
            
        elif 'where is' in query:
            query=query.replace('where is',' ')
            location=query
            speak("Locating "+location)
            wb.open_new_tab('https://www.google.com/maps/place/'+location)
            
        elif 'calculate' in query:
            client=wolframalpha.Client(wolframalpha_id)
            ind=query.lower().split().index('calculate')
            query=query.split()[ind+1:]
            res=client.query(''.join(query))
            ans=next(res.results).text
            print('The answer to the question is: '+ans)
            speak('The answer to the question is: '+ans)

        elif 'what is' in query or 'who is' in query:
            client=wolframalpha.Client(wolframalpha_id)
            res=client.query(query)
            
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
                
            except StopIteration:
                print("No results")
                speak("Could not find results")
                
        elif 'take a break' in query or 'stop listening' in query:
            speak("For how long sir?")
            #ans=int(TakeCommand())
            ans=TakeCommand()
            while 'second' not in ans and 'minute' not in ans and 'hour' not in ans:
                speak('Please specify time')
                ans=TakeCommand()
            if 'second' in ans:
                ans=ans.replace('second','')
                ans=int(ans)
            elif 'minute' in ans:
                ans=ans.replace('minute','')
                ans=int(ans)
                ans=ans*60
            elif 'hour' in ans:
                ans=ans.replace('hour','')
                ans=int(ans)
                ans=ans*60*60
            time.sleep(ans)
            speak("My break is over sir")
            
        elif 'log out' in query:
            speak("Goodbye sir, logging you out")
            time.sleep(5)
            os.system('shutdown -l')
        
        elif 'restart' in query:
            speak("Restarting your pc sir")
            time.sleep(5)
            os.system('shutdown /r /t 1')
            
        elif 'shutdown' in query:
            speak("Goodbye sir, shutting down your system")
            time.sleep(5)
            os.system('shutdown /s /t 1')
            


# In[ ]:





# In[ ]:




