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
from pandas.tseries.offsets import BDay

flight_database = pd.DataFrame()

path = 'C:/Users/jchen5/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe'
# driver = webdriver.PhantomJS(executable_path=path)

for day in range(1, 32):
    for flexiable_date in range(6):
        fill_depart = datetime.date(2016, 12, day)
        fill_arrive = fill_depart + BDay(20 + flexiable_date)
        print(fill_depart.strftime("%m/%d/%Y"), "  ", fill_arrive.strftime("%m/%d/%Y"))
        # carrier = []
        # departure_time = []
        # arrive_time = []
        # next_day = []
        # duration = []
        # list_price = []
        try:
            # driver = webdriver.Firefox()
            driver = webdriver.PhantomJS(executable_path=path)
            # driver.maximize_window()
            driver.set_page_load_timeout(50)
            home_page = "https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:IAD,to:SHA,departure:" + fill_depart.strftime(
                "%m/%d/%Y") + "TANYT&leg2=from:SHA,to:IAD,departure:" + fill_arrive.strftime(
                "%m/%d/%Y") + "TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&mode=search"
            driver.get(home_page)
            driver.implicitly_wait(10)
            time.sleep(5)

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
                depart_date.append(fill_depart.strftime("%m/%d/%Y"))
                arrive_date.append(fill_arrive.strftime("%m/%d/%Y"))

            x = np.array(
                [carrier, depart_date, arrive_date, departure_time, arrive_time, next_day, duration, list_price],
                dtype=object)
            d = list(map(list, zip(*x)))

            p = pd.DataFrame(d)
            p.columns = ['carrier', 'departure date', 'arrive date', 'departure time', 'arrive time', 'Next day',
                         'flight_time',
                         'list_price']
            # choose only ANA
            # ANA = p[p.carrier == "All Nippon Airways"]
            print("Expedia found: " + str(len(p.index)) + " lines")
            flight_database = flight_database.append(p)
            # print(flight_database)
            driver.close()
        except:
            continue

for price in flight_database['list_price']:
    price = price.strip()
    price = price.replace("$", "")
    price = price.replace(",", "")
    price = float(price)

writer = pd.ExcelWriter("C:/Users/jchen5/Downloads/ANA.xlsx")
flight_database.to_excel(writer, "sheet1", index=False)
writer.save()
