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

# Navigating Trees
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html)

for child in soup.find("table", {"id": "giftList"}).children:
    print(child)
# children are always exactly one tag below a parent, whereas descendants can be at any level in
# the tree below a parent.

# This code prints out the list of product rows in the giftList table. If you were to
# write it using the descendants() function instead of the children() function, about
# two dozen tags would be found within the table and printed, including img tags, span
# tags, and individual td tags.

for descendant in soup.find("table", {"id": "giftList"}).descendants:
    print(descendant)

# for sibling in soup.find("table",{'id':'giftList'}).tr.next_siblings:
#     print(sibling)

print(soup.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
