import os
import time
import socket
import threading
import random
import progressbar

print("""
   ____    ___                __         
/\  _`\ /\_ \    __        /\ \        
\ \ \L\ \//\ \  /\_\    ___\ \ \/'\    
 \ \  _ <'\ \ \ \/\ \  /'___\ \ , <    
  \ \ \L\ \\_\ \_\ \ \/\ \__/\ \ \\`\  
   \ \____//\____\\ \_\ \____\\ \_\ \_\
    \/___/ \/____/ \/_/\/____/ \/_/\/_/
""")

print("\033[97m----------------------------")
ip = str(input("\033[92m[\033[97m+\033[92m]IP Target : "))
print("\033[97m----------------------------")
port = int(input("\033[92m[\033[97m+\033[92m]Port : "))
print("\033[97m----------------------------")
packs = int(input("\033[92m[\033[97m+\033[92m]Packets : "))
print("\033[97m----------------------------")
thread = int(input("\033[92m[\033[97m+\033[92m]Threads : "))
print("\033[97m----------------------------")
  
  
def animated_marker():
    widgets = ['\033[94m[\033[97m#\033[94m]\033[97mLoading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
animated_marker()
