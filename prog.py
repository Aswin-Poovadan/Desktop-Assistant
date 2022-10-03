import os
import sys
import pyttsx3
import random
import subprocess
import pyjokes
print("Hello User")
pyttsx3.speak("Hello User")
while True:
    pyttsx3.speak("How can I help you:")
    user=input("How can I help you:")

    # Remove any extra white spaces from user input.
    user = user.strip().lower()
    if(("run" in user) or ("launch" in user) or ("open" in user)) and (("chrome" in user)or ("browser" in user)):
        site=input("What you want to search:")
        site = site.strip()
        
        pyttsx3.speak('Request Initiated')
        print('Request Initiated')
        if sys.platform == "linux" or sys.platform == "linux2":
            q = "google-chrome " + f'www.google.com/search?q={site}'
            try:
                check = subprocess.Popen(q, stderr = subprocess.STDOUT, shell=True)
            except Exception as e:
                pyttsx3.speak("Sorry user . Check whether google chrome is installed or not in your system. If it installed check the requirements are satisfied..!")            #stdout,stderr = check.communicate()
        elif sys.platform == "darwin":
            q = 'open -a \"Google Chrome\"' + 'www.google.com/search?q=' + site   
            try:
                check = subprocess.Popen(q , stderr = subprocess.STDOUT, shell=True)
            except Exception as e:
                #s = check.stderr
                pyttsx3.speak("Sorry user . Check whether google chrome is installed or not in your system. If it installed check the requirements are satisfied..!")

        elif sys.platform == "win32":
            q = "start chrome " + 'www.google.com/search?q=' + site  
            try:
                check = subprocess.Popen(q , stderr = subprocess.STDOUT, shell=True)
            except Exception as e:
                #s = check.stderr
                pyttsx3.speak("Sorry user . Check whether google chrome is installed or not in your system. If it installed check the requirements are satisfied..!")

        # os.system('start chrome "www.google.com/search?q="'+site)
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
    elif (("tell" in user) or ("say" in user) or ("random" in user) or ("getting" in user)) and (("joke" in user)or("fun"in user) or ("bored" in user) or ("something" in user)):
        print("This might make you laugh")
        pyttsx3.speak("This might make you laugh")
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        print("Joke for you: ", My_joke)
        pyttsx3.speak(My_joke)

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
    elif(("run" in user) or ("launch" in user) or ("open" in user)) and (("calculator" in user)or ("calc" in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        ## to Make Plateform independent, Added additional code .
        if sys.platform == "linux" or sys.platform == "linux2":
           try:
               check = subprocess.Popen('gnome-calculator', shell=True)   # If any users other than gnome like KDE etc.. can update it for GUI calculator.
           except Exception as e:
               check = subprocess.Popen('bc', shell=True)
        elif sys.platform == 'win32':
            check = subprocess.Popen('calc', shell=True)
        elif sys.platform == 'darwin':
            pyttsx3.speak('Mac users please update this.!') # to update here mac users .
    elif(("close" in user) or ("kill" in user) or ("exit" in user)) and (("calculator" in user)or ("calc" in user)):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        try:
            os.system("taskkill /f /im calculator.exe")
        except:
            print("There is some error on your system")
    elif(("exit" in user)or("quit" in user)or ("terminate"in user))and("program"):
        b="Ok Bye,See You later"
        print(b)
        pyttsx3.speak(b)
        break
    else:
        print("Sorry,couldn't get that,please try another command")
        pyttsx3.speak("Sorry,couldn't get that,please try another command")

