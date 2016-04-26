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

ANA_database = pd.DataFrame()

depart_list = ["12/01/2016", "12/02/2016", "12/03/2016", "12/04/2016", "12/05/2016", "12/06/2016", "12/07/2016"]
arrive_list = ["01/05/2017", "01/06/2017", "01/06/2017", "01/06/2017", "01/09/2017", "01/11/2017", "01/12/2017"]

for fill_depart, fill_arrive in zip(depart_list, arrive_list):
    carrier = []
    departure_time = []
    arrive_time = []
    next_day = []
    duration = []
    list_price = []
    driver = webdriver.Firefox()
    # driver.maximize_window()
    driver.set_page_load_timeout(50)
    home_page = "https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:IAD,to:SHA,departure:" + fill_depart + "TANYT&leg2=from:SHA,to:IAD,departure:" + fill_arrive + "TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&mode=search"
    driver.get(home_page)
    driver.implicitly_wait(50)
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

    depart_date = list()
    arrive_date = list()

    for i in range(len(carrier)):
        depart_date.append(fill_depart)
        arrive_date.append(fill_arrive)

    x = np.array([carrier, depart_date, arrive_date, departure_time, arrive_time, next_day, duration, list_price],
                 dtype=object)
    d = list(map(list, zip(*x)))

    # choose only ANA
    p = pd.DataFrame(d)
    p.columns = ['carrier', 'departure date', 'arrive date', 'departure time', 'arrive time', 'Next day', 'flight_time',
                 'list_price']
    ANA = p[p.carrier == "All Nippon Airways"]
    ANA_database = ANA_database.append(ANA)
    print(ANA_database)
    driver.close()


writer = pd.ExcelWriter("C:/Users/jchen5/Downloads/ANA.xlsx")
ANA_database.to_excel(writer, "sheet1", index=False)
writer.save()
