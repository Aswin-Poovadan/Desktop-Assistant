import os
import sys
import pyttsx3
import random
import subprocess
print("Hello User")
pyttsx3.speak("Hello User")
while True:
    pyttsx3.speak("How can I help you:")
    user=input("How can I help you:")
    if(("run" in user) or ("launch" in user) or ("open" in user)) and (("chrome" in user)or ("browser" in user)):
        site=input("What you want to search:")
        if sys.platform == "linux" or sys.platform == "linux2":
            q = "ls /usr/bin/ | grep google-chrome".split(" ")
            check = subprocess.Popen(q , stdout=subprocess.PIPE , stderr=subprocess.STDOUT)
            stdout,stderr = check.communicate()
            check = subprocess.Popen(stdout[0] , stdout=subprocess.PIPE , stderr = subprocess.STDOUT)
            stdout,stderr = check.communicate()
        # elif sys.platform == "darwin":

        # elif sys.platform == "win32":

        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start chrome "www.google.com/search?q="'+site)
    elif(("close" in user) or ("kill" in user) or ("exit" in user)) and (("chrome" in user)or ("browser"in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system("taskkill /f /im chrome.exe")
    elif (("run" in user) or ("launch" in user) or ("open" in user)) and (("editor" in user) or ("notepad" in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start notepad')
    elif(("close" in user) or ("kill" in user) or ("exit" in user)) and (("notepad" in user)or("editor" in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system("taskkill /f /im notepad.exe")
    elif (("run" in user) or ("launch" in user) or ("open" in user)) and (("paint" in user) or ("draw" in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start mspaint')
    elif(("close" in user) or ("kill" in user) or ("exit" in user)) and (("paint" in user)or("draw" in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system("taskkill /f /im mspaint.exe")
    elif (("take" in user) or ("launch" in user) or ("open" in user)) and (("photo" in user) or ("camera" in user)or("selfie" in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start microsoft.windows.camera:')
    elif (("run" in user) or ("what" in user) or ("open" in user)) and ("date" in user):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start date')
    elif (("run" in user) or ("what" in user) or ("open" in user)) and ("time" in user):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start time')
    elif (("tell" in user) or ("say" in user) or ("random" in user)) and (("joke" in user)or("fun"in user)):
        print("This might make you laugh")
        pyttsx3.speak("This might make you laugh")
        a="  Write an essay on cricket the teacher told the class, Chintu finishes his work in five minutes, The teacher is impressed,she asks Chintu to read his essay aloud for everyone.Chintu reads 'The cricket match is cancelled because of rain :D'"
        print(a)
        pyttsx3.speak(a)
    elif (("play" in user)or ("boring" in user))and (("game"in user)or ("coin" in user)or("heads"in user)or("tails" in user)):
        print("Lets Play Heads or Tails")
        pyttsx3.speak("Lets Play Head or Tail")
        toss=input("Heads or Tails:")
        pyttsx3.speak(toss)
        coins=["Heads","Tails"]
        com=random.choice(coins)
        if toss==com:
            print("Bot:",com)
            print("Aha you are good at this!")
            pyttsx3.speak("Wow you are good at this")
        else:
            print(com)
            print("  Haha  Not this time")
            pyttsx3.speak("Haha  Not this time")
    elif(("exit" in user)or("quit" in user)or ("terminate"in user))and("program"):
        b="Ok Bye,See You later"
        print(b)
        pyttsx3.speak(b)
        break
    else:
        print("Sorry,couldn't get that,please try another command")
        pyttsx3.speak("Sorry,couldn't get that,please try another command")


    

 