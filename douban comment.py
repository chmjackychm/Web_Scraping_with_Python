# coding: utf-8

from selenium import webdriver
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time

path = 'C:/Users/jchen5/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe'
driver = webdriver.PhantomJS(executable_path=path)


def get_comment():
    topic_id = input("What's your topic id? ")
    base = "https://wap.douban.com/group/topic/" + str(topic_id) + "/comments?page="
    print("...Give me a second...\n")
    driver.get(base)
    page_range = driver.find_element_by_class_name("paginator").text.split("|")[-1]
    print("OK, the topic has " + page_range.split("/")[1] + " pages")

    start_page = input("Which page you want to start?")
    end_page = input("Which page you want to stop?")
    name = input("Is there any specific author you want to look? Just type in name: ")
    length = int(end_page) - int(start_page)

    driver.get(base + start_page)
    print("\n...Scraping now...\n")
    for i in range(length + 1):
        time.sleep(1)
        print(int(start_page) + i)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        list = soup.find('div', {'class': 'list'})
        reply = list.findAll("div", {"class": "item"})
        author = [r.find('span').text.split()[0] for r in reply]
        comment = [r.find('p').text for r in reply]
        for i, v in enumerate(author):
            if v == name:
                print(v, '\n\n', comment[i], '\n-------\n')
        driver.find_element_by_link_text("下一页").click()


get_comment()
