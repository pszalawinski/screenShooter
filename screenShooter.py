import fnmatch
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog
import pynput.keyboard as kb
from os import listdir
import pyautogui
from fpdf import FPDF
import glob
from PIL import Image
from utils import sleeper, merger
from model import counter

import logging



from pynput import mouse

class MyException(Exception):pass


keyboard = kb.Controller()

print("Keys:\n cmd - takes screenshot\n esc - end program\n Shift - creates pdf from taken shots")

path = input("provide path where operations should be made: ")
#  TODO temporary - to delete
path = "/Users/pawel.szalawinski/Pictures/Shoots/"
print(">>Path recorded")
print(">>Provide coordinates:")

NumberOfMouseClicks = 0
coordinates = list()
def on_click(x, y, button, pressed):
    global NumberOfMouseClicks
    print(x, y)
    coordinates.append(x)
    coordinates.append(y)

    NumberOfMouseClicks += 1
    if (NumberOfMouseClicks==4):
        raise MyException(button)

with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except MyException as e:
        pass

# print("=>Coordinates provided: \ntop left: " +str(top_left) + "\ntop right: " + str(top_right) + "\nbottom left: " + str(bottom_left) + "\nbottom right: " + str(bottom_right) )
print("Coordinates: " + str(coordinates))
sleeper.printDots()

licznik = counter.Counter(0, path, coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5], coordinates[6], coordinates[7])

print(licznik.__dict__)

print("Ready to taking shots!")

def keyShooter(x, y, button, pressed):
    screenshooter()

def addCounter(obj):
    licznik = obj.get_licz()
    counter2 = licznik + 1
    obj.set_licz(counter2)

def screenshooter(licznik):
    # t = time.localtime()
    # timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
    click = licznik.get_licz()
    # /Users/pawel.szalawinski/Pictures/Shoots/
    file_name = (str(click) + ".png")
    print("Shot taken: " + file_name)
    path = licznik.get_pth()
    savepath = path + file_name
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(savepath)
    addCounter(licznik)

def exit():
    print("Bye bye")
    time.sleep(0.3)
    os._exit(0)

def on_press(key):
    if key == kb.Key.esc: exit()
    if key == kb.Key.cmd: screenshooter(licznik)
    if key == kb.Key.shift: merger.createPdfFile(licznik)
    # if key == kb.Key.shift: listdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
