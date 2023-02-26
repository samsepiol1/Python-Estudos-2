import re
import requests
requisicao=requests.get('https://www.uninassau.edu.br/enderecos')
padrao=re.findall(r'[2-9][0-9]{3}-[0-9]{4}',requisicao.text)
resultado_pesquisa=padrao[0]
for i in range(len(padrao)):
 resultado_pesquisa2=padrao[i]
 print(resultado_pesquisa2)



if padrao:
 print('Esses foram os números encontrados')


else:
    print('Telefone não encontrado. Digite outro site')
