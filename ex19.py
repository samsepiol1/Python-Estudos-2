nome_jogador=input('Insira o nome aqui')
quant_partidas=int(input('Quantidade de Partidas Jogadas'))
total_gols=[]
dicionario_dados={}
contador=0
for c in range(quant_partidas):
    gols =input('Quantidade gols{}'.format(c))
    testador=int(gols)
    contador=testador+0
    total_gols.append(contador)
    soma_gols=sum(total_gols)
    dicionario_dados={'Nome':nome_jogador,'Gols':total_gols,'Total de gols':soma_gols}
print(dicionario_dados)



