from random import sample
def repeticoes(numero):
    repitacoes=1
    valores=[]
    numero=list(str(numero))
    for k in numero:
        if numero.count(k)>1 and k not in valores:
            number=numero.count(k)
            repitacoes*= fatorial(number)
            valores.append(k)
        return repitacoes
def fatorial(numero):
    calc=1
    for i in range(numero):
        calc*=numero
        numero-=1
    return calc
def anagrama(numero,df=""):
    qnt_numeros, permutacoes, listaNumero = len(str(numero)), [], list(str(numero))

    totalPermutacoes = fatorial(qnt_numeros) / repeticoes(numero)

    while len(permutacoes) != totalPermutacoes:

        permutacao = ''

        gerarAnagrama = sample(str(numero), qnt_numeros)

        for k in gerarAnagrama:
            permutacao += k

        if permutacao not in permutacoes:
            permutacoes.append(permutacao)

    if df is 'max': return int(max(permutacoes))
    if df is 'min': return int(min(permutacoes))
    if df is '': return permutacoes