import PyPDF2
file=open("Python NumPy.pdf","rb")
reader=PyPDF2.PdfFileReader(file)
writer=PyPDF2.PdfFileWriter()

pages=reader.numPages
page=reader.getPage(3)
writer.addPage(page)
writer.encrypt(user_pwd="Avula@321",owner_pwd="None",use_128bit=True)
newfile=open("New file.pdf","wb")
writer.write(newfile)
newfile.close()
file.close()