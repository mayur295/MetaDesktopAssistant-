#This a python project that focuses on development of basic desktop assistant 
#---**********************---


#import module pyttsx3 which is used for coversion of text into speech
# init function to get an engine instance for the speech synthesis (formation)
# sapi5 is API which allows the use of speech recognition(user asks) and speech synthesis (meta replys) within windows application 
# say method on the engine that passes the text input to be spoken
# run and wait method, it processes the voice commands. 

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  #to get the voice details  
# print(voices[1].id)  #0 and 1 are the voices available 0- male voice 1- female voice 
engine.setProperty('voice',voices[1].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.
    
def screenshot():
    pic=pyautogui.screenshot()
    pic.save('c:/User')

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<=16:
        speak("Good afternoon!")
    
    else:
        speak("Good evening!")
    
    speak("This is Meta, How may I help you?")

def takecommand():
    ''' it takes micrphone input from the user and returns string output
    '''
    # creating a recognizer instance 
    r = sr.Recognizer()

    # taking the audio input from microphone as source audio_data argument  
    with sr.Microphone() as source:
        print("listening...")

        r.pause_threshold = 0.8

        audio = r.listen(source)

    try:
        print("Recognizing...")
        # method of recognizer instance 
        query = r.recognize_google(audio, language = 'en-in')#Using google speech recognition api for voice recognition.
        # returns the audio in the string format 
        print(f"user said: {query}\n")
        
    except Exception as e:
        # print e
        print("sorry, i dont understand")

        # return none string when there is some problem 
        return"None"
    
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'your-password-here') #write 
    server.sendmail('receivermail@gmail.com', to, content) #write 
    server.close()
if __name__ == "__main__" :
    wishMe()
    while True:
        query = takecommand().lower()

        ## LOGIC for executing task based on query asked by the user 

        #To search something in wikipedia 
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        #To open youtube 
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
            
         elif 'open Linkedin' in query:
            webbrowser.open("Linkedin.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. Have A Good Day")
            exit()
            
            
        elif 'screenshot' in query:
            screenshot()
        #Know time by using datetime() function and storing the current
        #or live system into a variable called strTime.
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
            print(strTime)

        #To open visual studio code     
        elif 'open code' in query:
            codePath = "C:\\Users\\akanksha\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe" #mention the target location of app 
            os.startfile(codePath)

        #To send mail     
        elif 'mail to user' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "reveivermail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
                
                
     
