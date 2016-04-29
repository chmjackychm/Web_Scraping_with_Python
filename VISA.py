from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=EAC1614153626')
soup = BeautifulSoup(html)

status = soup.find('div', {'class': 'rows text-center'}).find('h1')
# text = soup.find('div',{'class':'rows text-center'}).find('p')
print(status.text)
# print(text.text)
