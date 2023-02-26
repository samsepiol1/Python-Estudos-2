import bs4 as bs
import urllib.request
import requests
import json
from bs4 import BeautifulSoup
sauce=urllib.request.urlopen('https://www.tecmundo.com.br/').read()
soup=bs.BeautifulSoup(sauce,'lxml')
paragrafos=soup.find('article')
testes=paragrafos.find("div",class_="nzn-mosaic-news").find_all('h3',class_='nzn-news-info')
testes2=soup.find("a",itemprop='url')
testes3=soup.find_all("a"[0])
testes4=soup.find_all("title",attr='Title')
testes5=soup.find_all('a',class_='nzn-main-item')
testes6=soup.find("div",class_="nzn-mosaic-wrapper uk-clearfix")
testes7=testes6.find("h3",class_="nzn-news-info")
testes8=testes7.find("a")
print(testes8)
for teses in soup.find_all('a',class_='nzn-main-item'):
    var_noticias=[teses][0]['title']


