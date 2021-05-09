from PyPDF2 import PdfFileMerger
import os
from PIL import Image
import shutil


def count_pictures(path):
    path, dirs, files = next(os.walk(path))
    file_count = len(files)
    return file_count


def createPdfFile(licznik, pngPath):
    path = licznik.get_pth()

    all_files = count_pictures(pngPath)

    jpeg = path + "jpeg/"
    dest_dir = path + "tmpPDF/"

    print("making temp_dir for jpegs")
    os.mkdir(jpeg)
    print("making temp_dir for pdfs")
    os.mkdir(dest_dir)
    merger = PdfFileMerger()

    i = 0
    j = 0
    while i < int(all_files) - 1:
        png_path = pngPath + str(i) + ".png"
        jpg_filename = jpeg + "jpeg" + str(i) + ".jpg"
        pdf_filename = "jpeg" + str(i) + ".pdf"
        pdf_temp_dir = jpeg + pdf_filename
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

    print("Creating merged PDF file")
    merger.write(path + "merged.pdf")
    merger.close()

    print("Deleting pdf temporary directory")
    shutil.rmtree(dest_dir)
    print("PDF file created")

    answer = input("Do you want to keep jpg or png screenshots?"
                   "\n (j) keep jpgs, (p) keep pngs, (pj) keep jpegs and pngs, (a) remove all: \n")
    if answer == "j":
        shutil.rmtree(pngPath)
        print("Pngs deleted, jpegs kept")
    if answer == "p":
        shutil.rmtree(jpeg)
        print("Jpegs deleted, pngs kept")
    if answer == "a":
        shutil.rmtree(jpeg)
        shutil.rmtree(pngPath)
        print("All taken shoots removed")
    if answer == "pj":
        print("All shots taken saved")
    # TODO handle wrong answer

    # TODO add option to start again or exit
    os._exit(0)
