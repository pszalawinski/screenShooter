from PyPDF2 import PdfFileMerger
import os
from PIL import Image
import shutil


def count_pictures(path):
    path, dirs, files = next(os.walk(path))
    file_count = len(files)
    return file_count


def createPdfFile(licznik):
    path = licznik.get_pth()

    all_files = count_pictures(path)

    temp_dir = path + "tmp/"
    dest_dir = path + "tmpPDF/"

    print("making temp_dir for jpegs")
    os.mkdir(temp_dir)
    print("making temp_dir for pdfs")
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

    print("Creating merged PDF file")
    merger.write(path + "merged.pdf")
    merger.close()

    print("deleting temp_dirs")
    shutil.rmtree(temp_dir)
    shutil.rmtree(dest_dir)

    print("PDF file created")
    os._exit(0)
