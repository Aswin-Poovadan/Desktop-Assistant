import os, sys, pyttsx3, random, subprocess

run_commands = {"run", "launch", "open"}
close_commands = {"close", "kill", "exit"}
exit_program_keywords = {"terminate", 'quit', "exit"}
camera_keywords = {"camera", "selfie", "photo"}
linux = {"linux", 'linux2'}

def main():
    while True:
        pyttsx3.speak("How can I help you:")
        user=input("How can I help you:")

        user = user.strip().lower()
        cmd = user.split(' ')[0]

        if cmd in run_commands:
            if "chrome" in user or "browser" in user:

                site=input("What you want to search:")
                site = site.replace(' ', '+')

                pyttsx3.speak('Request Initiated')
                print('Request Initiated')
                if sys.platform in linux:
                    q = "google-chrome " + f'www.google.com/search?q={site}'
                elif sys.platform == "darwin":
                    q = 'open -a \"Google Chrome\"' + 'www.google.com/search?q=' + site   
                elif sys.platform == "win32":
                    q = "start chrome " + 'www.google.com/search?q=' + site  
                try:
                    subprocess.Popen(q, stderr = subprocess.STDOUT, shell=True)
                except Exception as e:
                    pyttsx3.speak("Sorry user . Check whether google chrome is installed or not in your system. If it installed check the requirements are satisfied..!")            #stdout,stderr = check.communicate()
                finally:
                    continue
            
            if 'editor' in user or 'notepad' in user:
                pyttsx3.speak("Request Initiated")
                print("Request Initiated!!")
                os.system('start notepad')
                continue
            
            if 'paint' in user or 'draw' in user:
                pyttsx3.speak("Request Initiated")
                print("Request Initiated!!")
                os.system('start mspaint')
                continue

            if 'calculator' in user or 'calc' in user:
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
                continue

        if cmd in close_commands:
            if "chrome" in user or 'browser' in user:
                pyttsx3.speak("Request Initiated")
                print("Request Initiated!!")
                os.system("taskkill /f /im chrome.exe")
                continue
                
            if 'notepad' in user or 'editor' in user:
                pyttsx3.speak("Request Initiated")
                print("Request Initiated!!")
                os.system("taskkill /f /im notepad.exe")
                continue
            
            if 'paint' in user or 'draw' in user:
                pyttsx3.speak("Request Initiated")
                print("Request Initiated!!")
                os.system("taskkill /f /im mspaint.exe")
                continue
            
            if 'calculator' in user or 'calc' in user:
                pyttsx3.speak("Request Initiated")
                print("Request Initiated!!")
                try:
                    os.system("taskkill /f /im calculator.exe")
                except:
                    print("There is some error on your system")
                finally:
                    continue
        
        if cmd in exit_program_keywords:
            b="Ok Bye,See You later"
            print(b)
            pyttsx3.speak(b)
            exit()

        if (("take" in user) or ("launch" in user) or ("open" in user)) and (user in camera_keywords):
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
            a="Write an essay on cricket the teacher told the class, Chintu finishes his work in five minutes, \
                The teacher is impressed,she asks Chintu to read his essay aloud for everyone.Chintu reads \
                'The cricket match is cancelled because of rain :D'"
            print(a)
            pyttsx3.speak(a)
        elif (("play" in user)or ("boring" in user)) and (("game"in user)or ("coin" in user)or("heads"in user)or("tails" in user)):
            print("Lets Play Heads or Tails")
            pyttsx3.speak("Lets Play Head or Tail")
            coins=["Heads","Tails"]
            while True:
                try:
                    toss=input("Heads or Tails:")

                    if not toss or toss not in coins:
                        raise ValueError() 

                    pyttsx3.speak(toss)
                    com=random.choice(coins)
                    if toss==com:
                        print("Bot:",com)
                        print("Aha you are good at this!")
                        pyttsx3.speak("Wow you are good at this")
                        continue
                    print(com)
                    print("  Haha  Not this time")
                    pyttsx3.speak("Haha  Not this time")
                except KeyboardInterrupt:
                    break
                except ValueError:
                    print("[-] Error: Invalid value. Try again.")
                    continue
                except Exception as e:
                    print(f"[-] Error: {e}")
                    break
        else:
            print("Sorry,couldn't get that,please try another command")
            pyttsx3.speak("Sorry,couldn't get that,please try another command")

if __name__ == "__main__":
    print("Hello User")
    pyttsx3.speak("Hello User")
    main()
