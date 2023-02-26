import pymysql
import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request
sauce=urllib.request.urlopen('https://www.tecmundo.com.br').read()
soup=bs.BeautifulSoup(sauce,'lxml')
paragrafos=soup.find('article')
coleta=soup.find("a",itemprop='url')
coleta2=soup.find_all("a"[0])
coleta3=soup.find_all("title",attr='Title')
coleta5=soup.find_all('a',class_='nzn-main-item')
coleta6=soup.find("div",class_="nzn-mosaic-wrapper uk-clearfix")
coleta7=coleta6.find("h3",class_="nzn-news-info")
testes8=coleta7.find("a")
print(testes8)
for coletas in soup.find_all('a',class_='nzn-main-item'):
    var_noticias=[coletas][0]['title']



# Alocar o bando poral_noticias.db na memória
not_2=var_noticias
conn = pymysql.connect(host='localhost',user='root',password='',db='portal_noticias')
# Criando Cursor, para orientar os comandos
cursor = conn.cursor()
cursor.execute("INSERT INTO noticias (titulo) VALUES (%s)"),(not_2)
cursor=cursor.execute('show tables')
# inserindo dados na tabela
print("Tabela Criada com Sucesso!")
# desconectando...
conn.close()
