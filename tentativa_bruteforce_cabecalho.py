import requests
cabecalho={'User-agent': 'Windows 12','Referer':'https:google.com','CF_IPcountry':'US'}
meus_cookies={'Ultima visita':'10-10-2020'}
nome = 'Lucas'
arquivo = open('cara.txt','r')
conteudo = arquivo.readlines()
dados={'username':'pohpo','password':conteudo[0]}
try:
    requisicao = requests.post('https://autenticacao.ufrn.br/sso-server/login?service=https%3A%2F%2Fsigaa.ufrn.br%2Fsigaa%2Flogin%2Fcas', headers=cabecalho, cookies=meus_cookies,data=dados)
    texto = requisicao.text
except Exception as e:
    print('A requisição falhou',e)
print(dados)








