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
from fpdf import FPDF
import glob
from PIL import Image
import shutil
from utils import sleeper

keyboard = kb.Controller()
# mouse = ms.Controller()
pdfmaker = FPDF()
path = '/Users/pawel.szalawinski/Pictures/Shoots/'

print("Keys:\n cmd - takes screenshot\n esc - end program\n shift - list all files")

path = input("provide path where operations should be made: ")
sleeper.printDots()

class Counter:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

counter = Counter(0, path)
print("Ready to taking shots!")

def keyShooter(x, y, button, pressed):
    screenshooter()

def addCounter(obj):
    counter = obj.get_x()
    counter2 = counter + 1
    obj.set_x(counter2)

def screenshooter(counter):
    # t = time.localtime()
    # timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
    click = counter.get_x()
    # /Users/pawel.szalawinski/Pictures/Shoots/
    file_name = (str(click) + ".png")
    path = counter.get_y()
    savepath = path + file_name
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(savepath)
    addCounter(counter)

def printDirectory(path):
    dirList = os.listdir(path)
    print(dirList)

def getlistdir_nohidden(path):
    imageList = glob.glob(os.path.join(path, '*'))
    im_list = []
    for image in imageList:
        im_list.append(Image.open(image))

    pdf1_filename = "/Users/pawel.szalawinski/Pictures/Shoots/file.pdf"

    im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
    print("PDF file created")


def createPdfFile(counter):

    path = counter.get_y()

    temp_dir = path + "tmp/"
    dest_dir = path + "readyPDF/"

    os.mkdir(temp_dir)
    os.mkdir(dest_dir)

    file_number = 1
    png_path = path + str(file_number) + ".png"
    jpg_filename = temp_dir + "jpeg" + str(file_number) + ".jpg"

    pdf_filename = "jpeg" + str(file_number) + ".pdf"

    pdf_temp_dir = temp_dir + pdf_filename

    im = Image.open(png_path)
    rgb_im = im.convert('RGB')
    rgb_im.save(jpg_filename)

    pdf = Image.open(jpg_filename)
    pdf.save(pdf_temp_dir)

    os.replace(pdf_temp_dir, dest_dir + pdf_filename)
    shutil.rmtree(temp_dir)

    print("PDF file created")

def on_press(key):
    if key == kb.Key.esc: os._exit(0)
    if key == kb.Key.cmd: screenshooter(counter)
    if key == kb.Key.shift: createPdfFile(counter)
    # if key == kb.Key.shift: listdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')
    if key == kb.Key.space: getlistdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
