import oauth2
import json
import pprint
import urllib.parse
consumer_key='IYAlo2Oa04EAukPH6SDRYhup0'
consumer_secret='2RwOEY5WYbauMLmH8rEjaGhqCFopYeaXsry0fJEw11jdvc8hOQ'
token_key='859529716180688896-nV8Yl0H6GDN0HqFd5zmsk9ClrM9So0J'
token_key_secret='LALH2etSH6DinyF3uStYoQQIU31VCUfK2mtkDJx0nd0pk'

consumer=oauth2.Consumer(consumer_key,consumer_secret)
token=oauth2.Token(token_key,token_key_secret)
cliente=oauth2.Client(consumer,token)
query=input('Publicar Tweet:')
query_codificada=urllib.parse.quote(query,safe='')
requisicao=cliente.request('https://api.twitter.com/1.1/statuses/update.json?status={}'.format(query_codificada),method='POST')



decodificar=requisicao[1].decode()
objeto=json.loads(decodificar)
print(objeto)
