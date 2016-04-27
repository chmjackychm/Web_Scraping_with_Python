from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
soup = BeautifulSoup(html.read())
# for link in soup.findAll("a"):
#     if "href" in link.attrs:
#         print(link.attrs['href'])

# for link in soup.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$")):
#     if "href" in link.attrs:
#         print(link.attrs['href'])

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    soup = BeautifulSoup(html.read())
    return soup.find('div', {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

# find unique page
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

page = set()


def getLinks(pageUrl):
    global pages
    html = BeautifulSoup("http://en.wikipedia.org" + pageUrl)
    soup = BeautifulSoup(html)
    for link in soup.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
