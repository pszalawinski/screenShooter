import fnmatch
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog
import pynput.keyboard as kb
import os
import pyautogui

keyboard = kb.Controller()

def screenshooter():
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
    file_name = ("screen-" + timestamp + ".png")
    path = r"/Users/pawel.szalawinski/Pictures/Shoots/"
    savepath = path + file_name

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(savepath)

def on_press(key):
    if key == kb.Key.shift :os._exit(0) 
    if key == kb.Key.cmd: screenshooter()

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
