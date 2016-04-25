from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html.read())

namelist = soup.findAll('span',{"class":"green"})
for name in namelist:
    print(name.get_text())

# .get_text() strips all tags from the document you are working
# with and returns a string containing the text only. For example, if
# you are working with a large block of text that contains many
# hyperlinks, paragraphs, and other tags, all those will be stripped
# away and you’ll be left with a tagless block of text.
# Keep in mind that it’s much easier to find what you’re looking for
# in a BeautifulSoup object than in a block of text. Calling
# .get_text() should always be the last thing you do, immediately
# before you print, store, or manipulate your final data. In
# general, you should try to preserve the tag structure of a document
# as long as possible.

namelist2 = soup.findAll(text= "the prince")
print (len(namelist2))

#The keyword argument
alltext = soup.findAll(id='text')
print(alltext[0].get_text())

#caveat
soup.findAll("",{"class":"green"})






