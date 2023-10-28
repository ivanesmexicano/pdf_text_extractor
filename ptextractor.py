# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:50:05 2023

@author: cochigordo
"""


#TODO:
#Select from a folder several pdfs
#Chose one pdf or several
#Loop on the pages and extract the text on each
#Save the text in a json format
#Save the text in a csv format
#print a summary of text found

#perhaps some text cloud or any visualization tool, bar charts for example
#create more analyttics perhaps even animations




import os

osenv=os.environ.items()
print(os.path)


#%%
print("osenv")
print(osenv)
#%%
dir=os.listdir('.')
#%%

for x in dir:
    if ".pdf" in x:
        extract_text(x)
        print(type(x))
        print(x)
        



#%%

import PyPDF2
#%%

def extract_text(name_pdf):
    # Open the PDF file
    pdf_file = open(name_pdf, "rb")
    
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)
    
    # Extract text from all pages in the PDF file
    text = ""
    for i in range(num_pages):
        page = pdf_reader.pages[i]
        text += page.extract_text()
    
    # Close the PDF file
    pdf_file.close()
    
    # Save the extracted text to a file
    with open("extracted_text.txt", "w") as f:
        f.write(text)
        print("Saved text extracted from:")
        print(name_pdf)
        
