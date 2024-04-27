from PyQt5.QtWidgets import QApplication, QFileDialog
from PyPDF2 import PdfWriter, PdfReader
import sys

def get_PdfFilePath():
    app = QApplication(sys.argv)
    file_path, _ = QFileDialog.getOpenFileName(None, "Select PDF file", "", "PDF Files (*.pdf);;All Files (*)")
    if file_path:
        print("PDF file selected:", file_path)
    QApplication.instance().exit()
    return file_path

def get_PdfFilesPath(): 
    app = QApplication(sys.argv)
    file_paths, _ = QFileDialog.getOpenFileNames(None, "Select PDF files", "", "PDF Files (*.pdf);;All Files (*)")
    if file_paths:
        print("PDF files selected:", file_paths)
    QApplication.instance().exit()
    return file_paths

def reverse_PdfFile(src, dst = 0):
    if dst == 0:
        dst = src.replace('.pdf', '_modified.pdf')

    input_pdf = PdfReader(src)
    total_pages = len(input_pdf.pages)

    output_pdf = PdfWriter()
    # This loop will iterate over each page and add it to the writer
    for page in range(total_pages - 1, -1, -1):
        # Adding a custom page label (number)
        output_pdf.add_page(input_pdf.pages[page])

    with open(dst, 'wb') as f:
        output_pdf.write(f)

def merge_PdfFiles(src= [], dst = 0):
    if len(src) == 0:
        return
    if dst == 0:
        dst = src[0].replace('.pdf', '_merged.pdf')

    ## loop src list
    input_pdf = []
    total_pages = []
    for i in range(len(src)):
        input_pdf.append(PdfReader(src[i]))
        total_pages.append(len(input_pdf[i].pages))

    output_pdf = PdfWriter()
    # This loop will iterate over each page and add it to the writer
    for i in range(len(src)):
        for page in range(total_pages[i]):
            output_pdf.add_page(input_pdf[i].pages[page])

    with open(dst, 'wb') as f:
        output_pdf.write(f)

def rotate_PdfPage(src, pageNums = []):
    input_pdf = PdfReader(src)
    total_pages = len(input_pdf.pages)

    pageNums = list(map(lambda x: x - 1, pageNums))

    output_pdf = PdfWriter()
    # This loop will iterate over each page and add it to the writer
    for page in range(total_pages):
        if page in pageNums:
            output_pdf.add_page(input_pdf.pages[page].rotate(180))
        else:
            output_pdf.add_page(input_pdf.pages[page])

    with open(src, 'wb') as f:
        output_pdf.write(f)

