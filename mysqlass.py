import http.client
import json
from urllib.parse import quote_plus
base= '/maps/api/geocode/json'

def geocode(address):
    path='{}?={}&sensor=false'.format(base,quote_plus(address))
    conexao=http.client.HTTPConnection('maps.google.com')
    conexao.request('GET',path)
    rawreply=conexao.getresponse().read()
    reply=json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])
nome=geocode("Brandenburg Gate, Berlin")
print(nome)
