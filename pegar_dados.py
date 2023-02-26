import requests
from bs4 import BeautifulSoup
import re

url = 'https://covid.lais.ufrn.br/#parnamirim'

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

data_confirmados=soup.find(id='casos-confirmados---parnamirim').text

data_suspeitos = soup.find(id='casos-suspeitos---parnamirim').text

data_descartados = soup.find(id='casos-descartados---parnamirim').text

data_obitos = soup.find(id='óbitos---parnamirim').text

dados_comple = soup.find(id='lista-dos-bairos-2').text


filtro = re.compile('([0-9]+)')
resp = filtro.findall(data_confirmados)
conversao = resp
conversao2 = str(conversao)
conversao3 = conversao2.strip('[]')

url = 'https://covid.lais.ufrn.br/#parnamirim'

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

data_confirmados=soup.find(id='casos-confirmados---natal').text
print(data_confirmados)



