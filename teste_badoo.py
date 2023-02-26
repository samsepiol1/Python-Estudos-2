import bs4 as bs
from bs4 import BeautifulSoup
import requests
sauce=requests.get('https://news.ycombinator.com/')
soup=BeautifulSoup(sauce.text,'lxml')
for tag in soup.find_all('title'):
    print()
nome=tag.text
if nome=='Hacker News':
    print('Script Funcionando')

else:
    print('Script não está funcionando')
nome2=tag.text




