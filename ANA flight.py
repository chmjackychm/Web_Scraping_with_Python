from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import csv
import numpy as np
import time
import math
import datetime
import pandas as pd

driver = webdriver.Firefox()
# driver.maximize_window()
driver.set_page_load_timeout(30)

home_page = 'https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:IAD,to:SHA,departure:11/01/2016TANYT&leg2=from:SHA,to:IAD,departure:11/14/2016TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&mode=search'
driver.get(home_page)
driver.implicitly_wait(5)
# choose only hotel

soup = BeautifulSoup(driver.page_source)

airline = soup.findAll("div", {"class": "secondary truncate"})
depature = soup.findAll("span", {"class": "departure-time departure-emphasis"})
arrive = soup.findAll("span", {"class": "arrival-time arrival-emphasis"})
next = soup.findAll("span", {"class": "next-day"})
flight_time = soup.findAll("div", {"class": "primary duration-emphasis"})
price = soup.findAll('div', {"class": "price-button-wrapper"})

carrier = [company.text.strip() for company in airline]
departure_time = [d.text.strip() for d in depature]
arrive_time = [a.text.strip() for a in arrive]
next_day = [n.text.strip() for n in next]
duration = [duration.text.strip() for duration in flight_time]
list_price = [p.find("", {"class": "visuallyhidden"}).text for p in price]

x = np.array([carrier, departure_time, arrive_time, next_day, duration, list_price], dtype=object)
d = list(map(list, zip(*x)))

# choose only ANA
p = pd.DataFrame(d)
p.columns = ['carrier', 'departure time', 'arrive time', 'Next day', 'flight_time', 'list_price']
ANA = p[p.carrier == "All Nippon Airways"]

writer = pd.ExcelWriter("C:/Users/jchen5/Downloads/ANA.xlsx")
ANA.to_excel(writer, "sheet1", index=False)
writer.save()
