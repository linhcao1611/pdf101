from PyPDF2 import PdfFileWriter, PdfFileReader 
import os.path
import sys

inFilePath = input('Enter pdf file path: ')
if not os.path.isfile(inFilePath):
	sys.exit("No file exist!!")
pdfReader = PdfFileReader(open(inFilePath,'rb'))

print(pdfReader.getPageLayout())
print(pdfReader.getPageMode())
print(pdfReader.getOutlines())
print(pdfReader.getXmpMetadata())

dotIndex = inFilePath.find(".")
beginIndex = inFilePath.find("/")
if beginIndex == -1:
	beginIndex = 0
	fileName = ''
else:
	fileName = inFilePath[beginIndex+1:dotIndex]
print('filename: '+fileName)
print(inFilePath[:beginIndex])

for i in range(pdfReader.getNumPages()):
    p = pdfReader.getPage(i)
    outFile = PdfFileWriter()
    outFile.addPage(p)
    with open(inFilePath[:beginIndex+1]+ fileName+'-%04d.pdf' % (i+1), 'wb') as f:
        outFile.write(f)