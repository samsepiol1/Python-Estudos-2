from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/Users/Deus.DEUS.002/Documents/IF-Informática Para Internet/chromedriver.exe')
driver.get('https://autenticacao.ufrn.br/sso-server/login?service=https%3A%2F%2Fsigaa.ufrn.br%2Fsigaa%2Flogin%2Fcas')
Searchbar1=driver.find_element_by_id('username')
time.sleep(0.5)
Searchbar1.send_keys('steve.jkl5@gmail.com')
Searchbar2=driver.find_element_by_id('password')
time.sleep(1)
Searchbar2.send_keys('imac88246948')
time.sleep(2)
Searchbar3=driver.find_element_by_class_name('btn-login')
Searchbar3.send_keys(Keys.ENTER)




