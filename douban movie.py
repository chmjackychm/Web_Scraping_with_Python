# coding: utf-8

# In[98]:

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup
import time
import datetime

# In[99]:

today = datetime.datetime.today()

# In[100]:

ps = 'C:/Users/jchen5/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe'

# In[101]:

driver = webdriver.PhantomJS(executable_path=ps)

# In[102]:

url = 'https://movie.douban.com/'

# In[103]:

wait = ui.WebDriverWait(driver, 15)


# In[113]:

def get_movie():
    # search filter
    print(driver.current_url)
    num = int(input("how many you want to see? "))
    print("--------------------------------------------------------------------------")
    kind = input(
        "1-Hot\n2-Douban Guess\n3-Newest\n4-Classics\n5-Playable\n6-High Scores\n7-Wonderful but not popular\n8-Chinese film\n9-Hollywood\n10-Korea\n11-Japan\n12-Action movies\n13-Comedy\n14-Love story\n15-Science fiction\n16-Thriller\n17-Horror film\n18-Cartoon\nplease select:")
    print("--------------------------------------------------------------------------")
    sort = input("How do you want to sort it?\n1-Hot\n2-Time\n3-Rate\n")
    print("--------------------------------------------------------------------------")
    print('\n')
    print(today.strftime("Data is scraped at: %A %d/%B/%Y"))
    print('\n...crawling now...')
    driver.get(url)
    # click kind
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="gaia_frm"]/div[1]/div[1]/label[%s]' % kind))
    driver.find_element_by_xpath('//*[@id="gaia_frm"]/div[1]/div[1]/label[%s]' % kind).click()
    # click sort
    wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="gaia_frm"]/div[3]/div[1]/label[%s]' % sort))
    driver.find_element_by_xpath('//*[@id="gaia_frm"]/div[3]/div[1]/label[%s]' % sort).click()

    # scroll down
    page = num // 20
    for i in range(page):
        # print(i)
        wait.until(lambda driver: driver.find_element_by_class_name('more'))
        driver.find_element_by_class_name('more').click()
        time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    movie = driver.find_elements_by_class_name('item')
    item = [m.text for m in movie]
    name = [t.split()[0] for t in item]
    score = [t.split()[1] for t in item]
    link = [m.get_attribute('href') for m in movie]

    for i, j in enumerate(name):
        if i <= num - 1:
            print(i + 1, j, score[i], link[i])


# In[114]:

get_movie()
