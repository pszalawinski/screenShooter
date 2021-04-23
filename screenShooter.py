import fnmatch
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog
from pynput.mouse import Button, Controller, Listener
import os

import pyautogui

# root = tk.Tk()

# canvas1 = tk.Canvas(root, width=200, height=50)
# canvas1.pack()
mouse = Controller()


def on_click(x, y, button, pressed):
    screenshooter()

def on_scroll(x, y, dx, dy):
    os._exit(0)

# def takeScreenshot():
#     while True:
#     screenshooter()

def screenshooter():
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
    file_name = ("screen-" + timestamp + ".png")
    path = r"C:\Users\Szau\Pictures\\Screen"
    savepath = path + file_name

    myScreenshot = pyautogui.screenshot()
    #file_path = filedialog.SaveAs(defaultextension='.jpg')
    #file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(savepath)
    # time.sleep(1.5)


# myButton = tk.Button(text='Take Screenshot',
#                      command=takeScreenshot, bg='green', fg='white', font=10)
# canvas1.create_window(100, 25, window=myButton)
# root.mainloop()

with Listener(
    on_click=on_click,
    on_scroll=on_scroll
) as listener:
    listener.join()
