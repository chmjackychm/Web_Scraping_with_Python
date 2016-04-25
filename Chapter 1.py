from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def gettitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.read())
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title
title = gettitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print("Title could not be found")
else:
    print(title)
