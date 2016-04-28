from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen('https://zh.wikipedia.org/wiki/SNH48%E7%AC%AC%E4%BA%8C%E5%B1%86%E7%B8%BD%E9%81%B8%E8%88%89')
soup = BeautifulSoup(html)

table = soup.findAll('table', {'class': 'wikitable sortable'})[0]
rows = table.findAll('tr')

csvFile = open('C:/Users/jchen5/python/Web Scraping with Python/snh.csv', 'wt', encoding='utf-8-sig')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['th', 'td']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()

from selenium import webdriver
import time

path = 'C:/Users/jchen5/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe'
driver = webdriver.PhantomJS(executable_path=path)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(1)
print(driver.find_element_by_id('content').text)

time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()

# driver.find_element_by_css_selector("#content")
# driver.find_elements_by_css_selector("#content")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = 'C:/Users/jchen5/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe'
driver = webdriver.PhantomJS(executable_path=path)
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.ID, 'loadedButton'))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()
