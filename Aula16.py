import oauth2
import json
import pprint
import urllib.parse
import re
consumer_key='IYAlo2Oa04EAukPH6SDRYhup0'
consumer_secret='2RwOEY5WYbauMLmH8rEjaGhqCFopYeaXsry0fJEw11jdvc8hOQ'
token_key='859529716180688896-nV8Yl0H6GDN0HqFd5zmsk9ClrM9So0J'
token_key_secret='LALH2etSH6DinyF3uStYoQQIU31VCUfK2mtkDJx0nd0pk'

consumer=oauth2.Consumer(consumer_key,consumer_secret)
token=oauth2.Token(token_key,token_key_secret)
cliente=oauth2.Client(consumer,token)
query=input('Digite o assunto que você quer pesquisar:')
query_codificada=urllib.parse.quote(query,safe='')
requisicao=cliente.request('https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query_codificada)+'&lang=pt')



decodificar=requisicao[1].decode()
objeto=json.loads(decodificar)
twittes=objeto['statuses']
contador=0
for twitter in twittes:
    print(twitter['user']['screen_name'])
    print(twitter['text'])
    print(twitter['user']['location'])
    print()
else:
    print('Palavra gotham não foi identificada nos Twittes')
contador2=0
for query_codificada in twitter['text']:
    contador2=contador2+1
    contador_resultado=contador2+0
for contador_resultado in range(0,contador_resultado,1):
    var = input('Desejar Exibir Quantas vezes essa palavra foi pesquisada?S/N')
    if var == 's'.lower():
        print('A palavra:{} aparece em {} Tweets'.format(query,contador2))
    else:
        print('Saindo da aplicação...')
        exit()










