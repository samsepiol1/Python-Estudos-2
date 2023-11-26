import time
from selenium import webdriver

driver = webdriver.Chrome('')
driver.get('')
Searchbar1 = driver.find_element_by_id('Enter user name')
time.sleep(0.5)
Searchbar1.send_keys('')
Searchbar2 = driver.find_element_by_id('passwd')
Searchbar2.send_keys('')
Searchbar3 = driver.find_element_by_id('Log_On')
Searchbar3.click()



