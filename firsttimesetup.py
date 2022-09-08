import os
import sys

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

print("This Script will download all dependencies and install them.")

pipcommand = "pip"

if("--cmd" in sys.argv):
    pipcommand = input("Enter your pip command: ")



os.system(pipcommand + " install pyautogui")
os.system(pipcommand + " install win10toast")
os.system(pipcommand + " install keyboard")

print("Done!")