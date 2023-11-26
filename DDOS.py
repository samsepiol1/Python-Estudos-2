import requests
import time
tempo=True
while not False:
 cabecalho={'User-Agent':'Mozila 5.0','Referer':'www.google.com'}
 cookies1={'Ultima visita':'20-20-1956','set-cookie':'1667353'}
 try:

    requisicao=requests.get('',headers=cabecalho,cookies=cookies1)
    time.sleep(1)
    status = requisicao.status_code
    print(status)

 except Exception as e:
    print('Requisição deu erro',e)




