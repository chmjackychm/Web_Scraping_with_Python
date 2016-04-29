# image processing
import os

os.chdir('C:/Users/jchen5/python/Web Scraping with Python/image')
from PIL import Image, ImageFilter

htt = Image.open('htt.jpg')
htt.show()
blurryhtt = htt.filter(ImageFilter.GaussianBlur)
blurryhtt.save('htt_blurred.jpg')
blurryhtt.show()
#
# #Scraping Text from Images on Websites  -- bug
# import time
# from urllib.request import urlopen, urlretrieve
# import subprocess
# from selenium import webdriver
# import os
# os.chdir('C:/Users/jchen5/python/Web Scraping with Python/image')
# path = 'C:/Users/jchen5/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe'
# driver = webdriver.PhantomJS(executable_path=path)
# driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
# time.sleep(2)
# driver.find_element_by_id('sitbLogoImg').click()
# imageList = set()
# time.sleep(5)
#
# #While the right arrow is available for clicking, turn through pages
# while "pointer" in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
#     driver.find_element_by_id('sitbReaderRightPageTurner').click()
#     time.sleep(2)
#     pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
#     for page in pages:
#         image = page.get_attribute('src')
#         imageList.add(image)
#
# driver.quit()
#
# #Start processing the images we've collected URLs for with Tesseract
# for image in sorted(imageList):
#     urlretrieve(image,'page.jpg')
#     p = subprocess.Popen(['tesseract','page.jpg','page'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#     p.wait()
#     f = open('page.txt','r')
#     print(f.read())


import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
req = session.get(url, headers=headers)
bsObj = BeautifulSoup(req.text)
print(bsObj.find("table", {"class": "table-striped"}).get_text)
