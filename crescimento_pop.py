#Crescimento da População Brasileiro 1980 - 2016
#DataSus

import matplotlib.pyplot as plt


dados = open("populacao_brasileira.csv").readlines()
x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))
plt.bar(x,y,color="#e4e4e4")
plt.plot(x,y,color="k",linestyle="--")

plt.title("Crescimento da População Brasileira")
plt.xlabel("Ano")
plt.ylabel("População x10000")
plt.show()

