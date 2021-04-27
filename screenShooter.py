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
from model import counter
from PyPDF2 import PdfFileMerger

keyboard = kb.Controller()
# mouse = ms.Controller()
pdfmaker = FPDF()
path = '/Users/pawel.szalawinski/Pictures/Shoots/'

print("Keys:\n cmd - takes screenshot\n esc - end program\n shift - list all files")

path = input("provide path where operations should be made: ")
# TODO temporary - to delete
path = "/Users/pawel.szalawinski/Pictures/Shoots/"
sleeper.printDots()

licznik = counter.Counter(0, path)
print("Ready to taking shots!")

def keyShooter(x, y, button, pressed):
    screenshooter()

def addCounter(obj):
    licznik = obj.get_x()
    counter2 = licznik + 1
    obj.set_x(counter2)

def screenshooter(licznik):
    # t = time.localtime()
    # timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
    click = licznik.get_x()
    # /Users/pawel.szalawinski/Pictures/Shoots/
    file_name = (str(click) + ".png")
    path = licznik.get_y()
    savepath = path + file_name
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(savepath)
    addCounter(licznik)

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


def count_pictures(path):
    path, dirs, files = next(os.walk(path))
    file_count = len(files)
    return file_count


def createPdfFile(licznik):

    path = licznik.get_y()

    all_files = count_pictures(path)

    temp_dir = path + "tmp/"
    dest_dir = path + "tmpPDF/"

    os.mkdir(temp_dir)
    os.mkdir(dest_dir)
    merger = PdfFileMerger()

    i = 0
    j = 0
    while i < int(all_files) - 1:
        png_path = path + str(i) + ".png"
        jpg_filename = temp_dir + "jpeg" + str(i) + ".jpg"
        pdf_filename = "jpeg" + str(i) + ".pdf"
        pdf_temp_dir = temp_dir + pdf_filename
        im = Image.open(png_path)
        rgb_im = im.convert('RGB')
        rgb_im.save(jpg_filename)
        pdf = Image.open(jpg_filename)
        pdf.save(pdf_temp_dir)
        os.replace(pdf_temp_dir, dest_dir + pdf_filename)
        i += 1

    
    pdfs = []
    
    while j < int(all_files) - 1:
        pdf_filename = "jpeg" + str(j) + ".pdf"
        pdf_temp_dir = dest_dir + pdf_filename
        pdfs.append(pdf_temp_dir)
        j += 1

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(path + "result.pdf")
    merger.close()

    shutil.rmtree(temp_dir)
    shutil.rmtree(dest_dir)

    print("PDF file created")
    os._exit(0)

def on_press(key):
    if key == kb.Key.esc: os._exit(0)
    if key == kb.Key.cmd: screenshooter(licznik)
    if key == kb.Key.shift: createPdfFile(licznik)
    # if key == kb.Key.shift: listdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')
    if key == kb.Key.space: getlistdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
