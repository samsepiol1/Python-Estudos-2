import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Deus.DEUS.002/Documents/site_final/img/chromedriver.exe')
driver.get('https://waha.teleperformance.com.br/vpn/index.html')
Searchbar1 = driver.find_element_by_id('Enter user name')
time.sleep(0.5)
Searchbar1.send_keys('silva.16955')
Searchbar2 = driver.find_element_by_id('passwd')
Searchbar2.send_keys('mudar@123')
Searchbar3 = driver.find_element_by_id('Log_On')
Searchbar3.click()



