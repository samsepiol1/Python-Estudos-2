import requests
cabecalho={'User-agent': 'Windows 12','Referer':'https:google.com','CF_IPcountry':'US'}
meus_cookies={'Ultima visita':'10-10-2020'}
dados={'username':'admin','password':'guigui123'}
try:
  requisicao=requests.post('http://www.unirn.edu.br/2016/users/login', headers=cabecalho,cookies=meus_cookies,data=dados)

  texto=requisicao.text
except Exception as e:
    print("Requisiçaõ deu erro:",e)
print(texto)





