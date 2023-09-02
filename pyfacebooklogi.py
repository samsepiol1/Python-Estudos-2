from selenium import webdriver
browser=webdriver.Chrome('')
browser.get('http://www.facebook.com')
Searchbar1=browser.find_element_by_id('email')
Searchbar1.send_keys('')
Searchbar2=browser.find_element_by_id('pass')
Searchbar2.send_keys('')
Searchbar3=browser.find_element_by_id('u_0_0')
from selenium.webdriver.common.keys import Keys
Searchbar3.send_keys(Keys.ENTER)

