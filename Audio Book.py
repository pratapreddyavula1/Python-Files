import pyttsx3
import PyPDF2
f=open("Python NumPy.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(f)
pages=pdfreader.numPages
speaker=pyttsx3.init()
page=pdfreader.getPage(6)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()


