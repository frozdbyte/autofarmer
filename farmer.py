import json
from multiprocessing.connection import wait
import os
import sys
import keyboard 
import time
from win10toast import ToastNotifier
import pyautogui;

print("""
       d8888888     88888888888888 .d88888b. 8888888888    d88888888888b. 888b     d88888888888888888888b. 
      d88888888     888    888    d88P" "Y88b888          d88888888   Y88b8888b   d8888888       888   Y88b
     d88P888888     888    888    888     888888         d88P888888    88888888b.d88888888       888    888
    d88P 888888     888    888    888     8888888888    d88P 888888   d88P888Y88888P8888888888   888   d88P
   d88P  888888     888    888    888     888888       d88P  8888888888P" 888 Y888P 888888       8888888P" 
  d88P   888888     888    888    888     888888      d88P   888888 T88b  888  Y8P  888888       888 T88b  
 d8888888888Y88b. .d88P    888    Y88b. .d88P888     d8888888888888  T88b 888   "   888888       888  T88b 
d88P     888 "Y88888P"     888     "Y88888P" 888    d88P     888888   T88b888       8888888888888888   T88b
      
      """)


# Set up environment
json_path = "./config.json"
toaster = ToastNotifier()

# Read config
try:
    with open(json_path, 'r') as f:
        config = json.loads(f.read())
except:
    print("No config found! Run findpositions!!")
    quit()

# Take input
print("""
  _____             __ _       
 / ____|           / _(_)      
| |     ___  _ __ | |_ _  __ _ 
| |    / _ \| '_ \|  _| |/ _` |
| |___| (_) | | | | | | | (_| |
 \_____\___/|_| |_|_| |_|\__, |
                          __/ |
                         |___/ 
""")
max = int(input("How many times do you want to farm? : "))
wait = int(input("How long does it take to farm one item? : "))
key = input("Whats the hotkey to farm? : ")
hotkey = input("What key do you want to your to start the process? : ")
mouse = True if input("Auto-Drag items? (y/n) : ") == "y" else False 
x = int(config["x1"])
y = int(config["y1"])
x2 = int(config["x2"])
y2 = int(config["y2"])
dl = int(config["dl"])

print("""
 _____                   _ 
|  __ \                 | |
| |  | | ___  _ __   ___| |
| |  | |/ _ \| '_ \ / _ \ |
| |__| | (_) | | | |  __/_|
|_____/ \___/|_| |_|\___(_)
""")
print("Press " + hotkey + " to start.")

def showbar(cur, mx):
    bar = "["
    for i in range(mx):
        if mx < 100:
            if i < cur:
                bar += "█"
            else:
                bar += "░"
    bar += "] " + str(cur) + "/" + str(max) + " "
    if mouse:
        sec = (max * wait + max * dl ) - (cur * wait + cur * dl)
    else:
        sec = (max * wait) - (cur * wait)
    if sec > 60:
        bar += "ca. " + str(round(sec/60)) + "m        "
    else:
        bar += "ca. " + str(sec) + "s        "
    
    sys.stdout.write("\r" + bar)
    sys.stdout.flush()

def clicker():
    while True: 
        try:  
            if keyboard.is_pressed(hotkey):  
                print('----- Starting Farming Session! -----')
                print("Farming " + str(max) + " times.")
                print("Every " + str(wait) + " seconds.")
                print("Completion in " + str(max * wait) + " seconds.")
                print("Hold " + hotkey + " to stop.")
                os.system('powershell -c (New-Object Media.SoundPlayer ".\sound\start.wav").PlaySync();')
                toaster.show_toast("Farming", "Started Farming Session!", duration=1)

                i = 0
                showbar(i, max)
                for i in range(max):
                    pyautogui.write(key)
                    time.sleep(wait)
                    if mouse:
                        pyautogui.moveTo(x, y)
                        pyautogui.dragTo(x2, y2, dl, button='left')
                    i+=1
                    showbar(i, max)
                    if keyboard.is_pressed(hotkey):
                        print("")
                        print("-- MANUAL STOP")
                        time.sleep(0.1)
                        break
                print("----- Farming Session Ended! -----")
                try:
                    os.system('powershell -c (New-Object Media.SoundPlayer ".\sound\end.wav").PlaySync();')
                except:
                    pass
                continue
        except KeyboardInterrupt:
            break

clicker();



