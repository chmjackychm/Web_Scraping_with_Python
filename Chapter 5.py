# from urllib.request import urlopen
# from urllib.request import urlretrieve
# from bs4 import BeautifulSoup
# download image
# html = urlopen("http://www.pythonscraping.com")
# soup = BeautifulSoup(html)
# imageLocation = soup.find("a",{"id":"logo"}).find("img")["src"]
# urlretrieve(imageLocation,"logo.jpg")


# download image
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "C:/Users/jchen5/python/Web Scraping with Python/downloaded"
baseUrl = "http://pythonscraping.com"


def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))

# store data to csv
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
soup = BeautifulSoup(html)
table = soup.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('C:/Users/jchen5/python/Web Scraping with Python/editors.csv', 'wt')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()
