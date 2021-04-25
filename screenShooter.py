import fnmatch
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog
import pynput.mouse    as ms
import pynput.keyboard as kb
import os
from os import listdir
import pyautogui

keyboard = kb.Controller()
mouse = ms.Controller()

print("Keys:\n cmd - takes screenshot\n esc - end program\n shift - list all files")

def keyShooter(x, y, button, pressed):
    screenshooter()
        

def screenshooter():
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
    file_name = ("screen-" + timestamp + ".png")
    path = r"/Users/pawel.szalawinski/Pictures/Shoots/"
    savepath = path + file_name
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(savepath)

def printDirectory():
    dirList = os.listdir('/Users/pawel.szalawinski/Pictures/Shoots/')
    print(dirList)

def on_press(key):
    if key == kb.Key.esc :os._exit(0) 
    if key == kb.Key.cmd: screenshooter()
    if key == kb.Key.shift: printDirectory()

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
