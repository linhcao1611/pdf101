from PyPDF2 import PdfFileWriter, PdfFileReader 


inFilePath = input('Enter pdf file path: ')
inFile = PdfFileReader(open(inFilePath,'rb'))

print(inFile.getDocumentInfo())
print(inFile.getPageLayout())
print(inFile.getPageMode())
print(inFile.getOutlines())
print(inFile.getXmpMetadata())

for i in range(inFile.getNumPages()):
    p = inFile.getPage(i)
    outFile = PdfFileWriter()
    outFile.addPage(p)
    with open('page-%02d.pdf' % i, 'wb') as f:
        outFile.write(f)