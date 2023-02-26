from googlesearch import search
def misturar(x,y):
    lista=[]
    for i in x:
        for j in y:
            lista.append(str(i+j))
            lista.append(str(j+i))
    return lista
def nome_e_data(nome,data):
    lista=[]
    dicionario = {'01': 'janeiro', '02': 'fevereiro', '03': 'marco', '04': 'abril', '05': 'maio', '06': 'junho',
                  '07': 'julho', '08': 'agosto', '09': 'setembro', '11': 'novembro', '12': 'dezembro'}
    data=data.slipt('/')
    temp=[]
    temp.append(str(data[0] + dicionario[data[1]] + data[2]))
    temp.append(str(data[0] + dicionario[data[1]][0:3] + data[2]))
    temp.append(str(data[0] + dicionario[data[1]] + data[2][2:]))
    temp.append(str(data[0] + dicionario[data[1]][0:3] + data[2][2:]))
    temp.append(str(data[0] + data[1] + data[2]))
    lista+=misturar
    return lista
def inverte(palavra):
    nova_palavra=list(palavra)
    nova_palavra.reverse()
    return nova_palavra
def escrever(grandelista,nome):
    for i in grandelista:
     nomi = nome + '.txt'
     print(i)
     comando = 'echo ' + i + ' >> ' + nomi
    print('Escrito com sucesso')
def religiao():
    arq=open('dados.txt','r')
    lista=arq.readlines()
    return lista
def leet(frase):
    dic = {'a': '4', 'b': '8', 'g': '6', 'e': '3', 'i': '1', 'o': '0',
           'h': '8', 'q': '9', 't': '7', 's': '5', 'z': '2'}
    lista=''
    for letra in frase:
        try:
            lista+=dic([letra])
        except:
            lista+=(letra)
    return lista
def gerar_aleatorio_num():
    from random import randint
    lista=[]
    vezes=input('Quantos números você deseja:')
    while len(lista)<int(vezes):
        numero=''
        for i in range(randint(2,10)):
            numero+=str(randint(2,10))
        if numero not in lista:
            lista.append(numero)
    return lista
def modo_maconheiro():
    glp=[]
    arquivo_nome=str.lower(input('Qual o nome do arquivo a ser gerado'))
    arquivo=open(str(arquivo_nome+'.txt'),'w')
    arquivo.close()
    senhas=str.split(' ')
    for palavra in senhas:
        for outra in senhas:
            glp.append(str(palavra+outra))
    escrever(glp,arquivo_nome)
    return True


def modo_crackudo():  # gera a lista de palavras com mais "precisao"
    msg = '[*] Escrevendo {} [*]'
    temp = ''
    glp = []
    numeros_aleatorios = []
    arquivo_nome = str.lower(input('qual o nome do arquivo a ser gerado?\n>>>'))
    arquivo = open(str(arquivo_nome + '.txt'), 'w')
    arquivo.close()
    nome = str.lower(input('qual o nome do alvo?\n>>>'))
    idade = str.lower(input('qual a data de nascimento do alvo?(1/1/2019)\n>>>'))
    sobrenome = str.lower(input('qual os sobrenomes?\n>>>'))
    sobrenome = sobrenome.split(' ')
    conjuge = str.lower(input('qual o nome do conjuge?\n>>>'))
    casamento = str.lower(input('qual a data de casamento?\n>>>'))
    fe = str.lower(input('deseja incuir possivei senhas religiosas?(s/n)\n>>>'))
    empresa = str.lower(input('qual o nome da empresa alvo?\n>>>'))
    numFilhos = str.lower(input('qual o numero de filhos alvo?\n>>>'))

    if int(numFilhos) > 0:
        filhos = []
        for i in range(int(numFilhos)):
            filhos.append(str.lower(input('qual o nome do filho?\n>>>')))

    fut = str.lower(input('deseja incluir o time?(s/n)\n>>>'))

    if fut == 's':
        padraoTime = str.lower(input('deseja incluir combinacoes padrao de varios times?(s/n)\n>>>'))
        if padraoTime == 'n':
            combTimes = str.lower(input('digite as cominacoe separadas por espaco\n>>>'))

    leetPalavra = str.lower(input('se quiser adcionar palavras em leet digite separadas por espaco\n>>>'))
    aleatorias = str.lower(input('digite palavras que queira incrementar separada por espacos\n>>>'))
    numeros = str.lower(input('deseja adcionar numeros aleatorios?(s/n)\n>>>'))

    if 's' in numeros:
        numeros_aleatorios = gerar_aleatorio_num()

    if len(conjuge) > 0:  # aqui misturo eu checo se a pessoa tem algum conjuge e misturo os nomes

        if 's' in numeros:
            temp = str(nome + conjuge)
            glp.append(temp)
            glp += misturar(temp, numeros_aleatorios)
            temp = str(nome + 'e' + conjuge)
            print(temp)
            glp.append(temp)
            glp += misturar(temp, numeros_aleatorios)

        glp.append(inverte(str(nome + conjuge)))
        glp += misturar(inverte(str(nome + conjuge)), numeros_aleatorios)

    print(msg.format('senhas com o conjuge'))
    escrever(glp, arquivo_nome)  # aqui eu escrevo os dados gerados
    glp = []  # e zero a lista pra poupar espaço na memoria
    temp = []  # garanto que tenho uma variavel temporaria fazia pra alocar a lista de filhos
    print('glp \n\n\n', glp)
    if int(numFilhos) > 1:  # gero combinaçoes com os nomes dos filhos se tiverem mais que 1
        for i in filhos:
            for j in filhos:
                temp.append(str(i + j))
                temp.append(str(j + i))
        glp += misturar(temp, numeros_aleatorios)

        escrever(glp, arquivo_nome)
        glp = []

    return True
def pesquisa_avancada():
    nome=input('Digite aqui o nome completo da vítima:')
    for j in search(nome,tld="co.in",num=10,stop=10,pause=2):
        print(j)






