from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np

html = urlopen(
    "http://www.compasslexecon.com/professionals/all?Name=&ExpertiseId=&WithTestifyingExperience=false&LocationId=&KeyWord=").read()
soup = BeautifulSoup(html)

professional = soup.findAll("div", {"class": "professionals-results-block clearfix"})

name_list = []
title_list = []
location_list = []
practice_list = []
link_list = []

for pro in professional:
    name = ''.join(pro.find("a", {"class": "pro-results-name"}).text)
    title = ''.join(pro.find('span').text)
    location = ''.join(pro.find("div", {"class": "pro-results-location"}).text)
    practice = ''.join(pro.find('div', {'class': 'pro-results-practice'}).text)
    link = 'http://www.compasslexecon.com' + pro.find('a', {'class': 'pro-results-name'}).get('href')

    name_list.append(name)
    title_list.append(title)
    location_list.append(location)
    practice_list.append(practice)
    link_list.append(link)

x = np.array([name_list, title_list, location_list, practice_list, link_list], dtype=object)
d = list(map(list, zip(*x)))
p = pd.DataFrame(d)
p.columns = ["Name", "Title", "Location", "Practice Area", 'Page']
writer = pd.ExcelWriter("C:/Users/jchen5/Downloads/CL List.xlsx")
p.to_excel(writer, "sheet1", index=False)
writer.save()
