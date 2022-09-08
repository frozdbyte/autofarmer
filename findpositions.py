import sys
import keyboard 
import pyautogui
import json
import time

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


x1 = 0
y1 = 0
x2 = 0
y2 = 0

def save():
    j  = json.loads("{\"x1\":\"" + str(x1) + "\",\"y1\":\"" + str(y1) + "\",\"x2\":\"" + str(x2) + "\",\"y2\":\"" + str(y2) + "\",\"dl\":\"1\"}")

    with open('config.json', 'w') as f:
        json.dump(j, f)


if("--skip" in sys.argv):
    save()
    print("Done! Config created with 0 values!")
    input("Press enter to exit.")
    quit()

print("Move your mouse to the items position and press -.")
while True:  
    if keyboard.is_pressed("-"):
        x1 = pyautogui.position()[0]
        y1 = pyautogui.position()[1]
        break

print("Move your mouse to your Inventories position and press -.")
time.sleep(1)
while True:  
    if keyboard.is_pressed("-"):
        x2 = pyautogui.position()[0]
        y2 = pyautogui.position()[1]
        break
   
save()
    
print("Done! Config saved!")
input("Press enter to exit.")
quit()