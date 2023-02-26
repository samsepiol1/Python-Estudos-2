import requests
import json
req=None
def requisicao(carta):
 try:
  req=requests.get('https://db.ygoprodeck.com/api/v2/cardinfo.php?name={}'.format(carta))
  lista_cartas=json.loads(req.text)
  return lista_cartas
 except Exception as erro:
    print('Problema na conexão')


    return None


def detalhes_cartas(detalhe):


  print('Nome:', (detalhe[0][0]['name']))
  print('Nível:',detalhe[0][0]['level'])
  print('Tipo:',detalhe[0][0]['type'])
  print('Descrição:',detalhe[0][0]['desc'])
  print('Ataque:',detalhe[0][0]['atk'])
  print('Defesa:',detalhe[0][0]['def'])
  print('')

sair=False
while not sair==True:
    escolher_carta=input('Digite o Nome da Carta ou SAIR:')
    if escolher_carta=='SAIR':
        sair=True
        print('Fechando Aplicação...')
    else:
        carta=requisicao(escolher_carta)
        if sair==False:
            detalhes_cartas(carta)
        elif carta['error']:
            print('A carta não existe no nosso banco de dados')
        else:
            detalhes_cartas(carta)
















