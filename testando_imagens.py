import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome('C:/Users/Deus.DEUS.002/Documents/IF-Informática Para Internet/chromedriver.exe')
browser.get("https://suap.ifrn.edu.br/accounts/login/")
time.sleep(10)
username = browser.find_element_by_xpath("/html/body/div[1]/main/div[1]/form/div[1]/input")
password = browser.find_element_by_xpath("/html/body/div[1]/main/div[1]/form/div[2]/input[1]")
#ler senha e password atráves de um bloco de notas
username.send_keys("20201151210083")
password.send_keys("#Imac8824")
login_attempt = browser.find_element_by_xpath("/html/body/div[1]/main/div[1]/form/div[4]/input")
login_attempt.submit()
#tornar a geração do link aleatorio
browser.get("https://suap.ifrn.edu.br/djtools/profile_info/1000/")
soup = BeautifulSoup(browser.page_source,'lxml')
nome = soup.find_all('h4')[0].get_text()
#Arranjar uma forma de extrair o texto da imagem
for el in soup.find_all('img'):
        print (el)
print(nome)







