from mendeleev import element
from googletrans import Translator
import time
time.sleep(0.1)
inicio  = time.time()
tradutor = Translator()


nome_elemento = str(input('Digite a sigla do elemento:'))
tamanho_palavra = len(nome_elemento)
if  tamanho_palavra== 2:
    nome_elemento = nome_elemento[0].upper()+nome_elemento[1]
    o = element(nome_elemento)
    pegando_nome = o.name
    pegando_valencia = o.group.symbol
    traducao = tradutor.translate(pegando_nome, dest='pt')
    print('Nome do elemento: {}'.format(traducao.text))
    print('Numero Atomico {}'.format(o.atomic_number))
    if pegando_valencia == 'IA':
        print('O elemento possui um eletron na camada de valência')
    if pegando_valencia == 'IIA':
        print('O elemento possui dois eletrons na camada de valencia')
    if pegando_valencia == 'IIIA':
        print('O elemento possui três eletrons na camada de valência')
    if pegando_valencia =='IVA':
        print('O elemento possui quatro eletrons na camada de valência')
    if pegando_valencia =='VA':
        print('O elemento possui cinco eletrons na camada de valencia')
    if pegando_valencia =='VIA':
        print('O elemento possui seis eletrons na camada de valência')
    if pegando_valencia =='VIIA':
        print('O elemento possui sete eltrons na camada de valencia')
    if pegando_valencia =='VIIIA':
        print('O elemento possui oito eletrons na camada de valencia')



else:

    o = element(nome_elemento.upper())
    pegando_nome = o.name
    pegando_valencia = o.group.symbol
    traducao = tradutor.translate(pegando_nome, dest='pt')
    print('Nome do elemento: {}'.format(traducao.text))
    print('Numero Atomico: {}'.format(o.atomic_number))
    if pegando_valencia == 'IA':
        print('O elemento possui um eletron na camada de valência')
    if pegando_valencia == 'IIA':
        print('O elemento possui dois eletrons na camada de valencia')
    if pegando_valencia == 'IIIA':
        print('O elemento possui três eletrons na camada de valência')
    if pegando_valencia =='IVA':
        print('O elemento possui quatro eletrons na camada de valência')
    if pegando_valencia =='VA':
        print('O elemento possui cinco eletrons na camada de valencia')
    if pegando_valencia =='VIA':
        print('O elemento possui seis eletrons na camada de valência')
    if pegando_valencia =='VIIA':
        print('O elemento possui sete eltrons na camada de valencia')
    if pegando_valencia =='VIIIA':
        print('O elemento possui oito eletrons na camada de valencia')
fim =time.time()
diferenca = fim - inicio
print("%.2f"%diferenca)





