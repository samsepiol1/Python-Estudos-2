idade=0
soma=1
cont=0
media=1
while idade!=-1:
    idade=int (input('Digite aqui a sua idade:'))
    cont=cont+1
    cont_final=cont-1
    soma=soma+idade
media=soma/cont_final
if (media>=0) and (media<=25):
    print('Turma Jovem')
elif(media>=26) and (media<=60):
    print('Turma Adulta')
elif(media>60):
    print('Turma idosa')
print(media)








