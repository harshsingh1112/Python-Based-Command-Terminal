import os
import psutil 

def ps():
    print("📊 Process Information:")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)
