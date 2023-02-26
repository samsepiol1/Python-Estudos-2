import json
import googlesearch
import requests
sua_localizacao=input('Digite seu Bairro, Cidade ou Estado')
file=open('perfis.txt','rb')
data=file.readlines()
dicionario=data[4].decode()
localizacao=dicionario[15:]
print(localizacao)














