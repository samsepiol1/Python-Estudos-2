lista_impar=[]
lista_par=[]
lista_primo=[]
for i in range(1,101,2):
    lista_impar.append(i)
print(lista_impar)
for p in range(2,101,2):
    lista_par.append(p)
print(lista_par)
for pri in range(2,101):
    cont=0
    for y in range(1,pri+1):
        if pri%y==0:
            cont=cont+1
    if cont <=2:
            lista_primo.append(pri)
print(lista_primo)













