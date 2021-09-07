from typing import Text
import pyttsx3
import PyPDF2

book = open('file_path','rb') #make sure the path or the file_path is in the same directory
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
engine = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(1)
    Text = page.extractText()   
    engine.say(Text)
    engine.runAndWait()