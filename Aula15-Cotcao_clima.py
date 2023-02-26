import requests
import json
from googletrans import Translator

def conversao(k):

    resultado_conversao=k-273
    return resultado_conversao
cidade=input('Escreva o nome da sua cidade:')
requisicao=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=7a633c858c513314c8776d892171f9ba')
clima=json.loads(requisicao.text)
try:
 tradutor2 = Translator()
 tradutor3=(tradutor2.translate(clima['weather'][0]['main'],dest='pt'))
 print('Estado do Clima: {}'.format(tradutor3.text))
 print('Temperatura:{:.2f}'.format(conversao(clima['main']['temp'])))

except Exception as KeyError:
    print('Cidade não localizada')






















