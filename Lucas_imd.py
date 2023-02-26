""""import PyPDF2
from PyPDF2 import PdfFileReader
f=open('IMD CERIMONIA DE CERTIFICAÇÃO 2019.pdf','rb')
pdf=PyPDF2.PdfFileReader(f)
print('Quantidade de páginas',pdf.getNumPages())
print(pdf())"""

arquivo=open('IMD CERIMONIA DE CERTIFICAÇÃO 2019.txt','rb')
print(arquivo.read())





