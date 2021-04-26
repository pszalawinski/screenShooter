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

keyboard = kb.Controller()
# mouse = ms.Controller()
pdfmaker = FPDF()
path = '/Users/pawel.szalawinski/Pictures/Shoots/'

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

def printDirectory(path):
    dirList = os.listdir(path)
    print(dirList)

def listdir_nohidden(path):
    print(glob.glob(os.path.join(path, '*')))

def getlistdir_nohidden(path):
    imageList = glob.glob(os.path.join(path, '*'))
    im_list = []
    for image in imageList:
        im_list.append(Image.open(image))

    pdf1_filename = "/Users/pawel.szalawinski/Pictures/Shoots/file.pdf"

    im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
    print("PDF file created")


def createPdfFile():
    temp_dir = "/Users/pawel.szalawinski/Pictures/Shoots/tmp/"
    dest_dir = "/Users/pawel.szalawinski/Pictures/Shoots/readyPDF/"

    os.mkdir(temp_dir)
    os.mkdir(dest_dir)

    counter = 1
    png_path = "/Users/pawel.szalawinski/Pictures/Shoots/screen-Apr-25-2021_141913.png"
    jpg_filename = temp_dir + "jpeg" + str(counter) + ".jpg"

    pdf_filename = "jpeg" + str(counter) + ".pdf"

    pdf_temp_dir = temp_dir + pdf_filename

    im = Image.open(png_path)
    rgb_im = im.convert('RGB')
    rgb_im.save(jpg_filename)

    pdf = Image.open(jpg_filename)
    pdf.save(pdf_temp_dir)

    os.replace(pdf_temp_dir, dest_dir + pdf_filename)
    shutil.rmtree(temp_dir)

    # im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
    print("PDF file created")

def on_press(key):
    if key == kb.Key.esc: os._exit(0)
    if key == kb.Key.cmd: screenshooter()
    if key == kb.Key.shift: createPdfFile()
    # if key == kb.Key.shift: listdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')
    if key == kb.Key.space: getlistdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
