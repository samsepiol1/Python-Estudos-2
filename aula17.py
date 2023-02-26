from Twitter import Twitter
import time
consumer_key='IYAlo2Oa04EAukPH6SDRYhup0'

consumer_key2='2RwOEY5WYbauMLmH8rEjaGhqCFopYeaXsry0fJEw11jdvc8hOQ'

acess_token='859529716180688896-nV8Yl0H6GDN0HqFd5zmsk9ClrM9So0J'

acess_token_secret='LALH2etSH6DinyF3uStYoQQIU31VCUfK2mtkDJx0nd0pk'

twitter=Twitter(consumer_key,consumer_key2,acess_token,acess_token_secret)

#resp= twitter.tweet('Vamos testar nossa lib')
pesquisa=twitter.search('solyd','pt')
print(pesquisa)



