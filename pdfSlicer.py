# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Tue Mar 23 17:35:52 2021

@author: Johan
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdfSlice(start,stop,inputName,outputName):

    inputpdf = PdfFileReader(open(str(inputName), "rb"))
    output = PdfFileWriter()
    
    for i in range(int(start), int(stop) + 1):
        try:
            output.addPage(inputpdf.getPage(i))
        except IndexError:
            print("Start or stop index is inproper.")
        
    with open(str(outputName), "wb") as outputStream:
        output.write(outputStream)
        
    return("Done!")
        
start = input("Enter start: ")
stop = input("Enter stop: ")
inputFil = input("Enter name of inputfile(ex. job.pdf): ")
outputFil = input("Enter name of outputfile(ex. newjob.pdf): ")
    
pdfSlice(start,stop,inputFil,outputFil)
