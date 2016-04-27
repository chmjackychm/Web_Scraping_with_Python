# from urllib.request import urlopen
# textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
# print(textPage.read())

from urllib.request import urlopen

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(textPage.read(), 'utf-8')

# read CSV online -- use csv.reader
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
    print("The album \"" + row[0] + "\" was released in " + str(row[1]))

# read CSV online -- use csv.Dictreader: handle variable name (take longer time)
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)
print(dictReader)

for row in dictReader:
    print(row)

# read PDF -- bug: io.UnsupportedOperation: seek
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import StringIO
# from io import open
#
# def convert_pdf_to_txt(path, codec='utf-8'):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = urlopen(path)
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()
#
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)
#
#     text = retstr.getvalue()
#
#     fp.close()
#     device.close()
#     retstr.close()
#     return text
#
# path = "http://pythonscraping.com/pages/warandpeace/chapter1.pdf"
# #path = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf").read()
# outputString = convert_pdf_to_txt(path)
