import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyautogui
driver=webdriver.Chrome('C:/Users/Deus/Downloads/chromedriver.exe')
driver.get('https://www.tecmundo.com.br/')
#teste=driver.find_element_by_class_name("nzn-mosaic-item")
html=driver.page_source
#for i in range(10):
    #teste=driver.find_elements_by_class_name("nzn-mosaic-item")
    #print()
teste=driver.find_element_by_xpath('//div[@id="nzn-js-mosaic1-wrapper"]').click()
time.sleep(5)
teste2=driver.find_element_by_class_name("nzn-news-info").click()
html2=driver.page_source
soup=BeautifulSoup(html2,'lxml')
print(pyautogui.position())
#harsh=soup.find('a',{"href": "Url", "title": "Title"}).text()
#print(harsh)