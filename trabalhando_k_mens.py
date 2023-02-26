#importando modulo
from sklearn.datasets import load_iris
from math import sqrt
import matplotlib.pyplot as plt
import random
#Instanciando Objetos
iris=load_iris()
data=iris.data #Dados para treinamento
labels=iris.target
labels_names=iris.target_names #Nome nos labels
#Calculo da distancia entre os centroides
def euclidian(v1,v2):
    #Armazena o quadrado da distancia
    dist=0.0
    for x in range(len(v1)):
        dist+=pow((v1[x]-v2[x]),2)
        #Extrai a Raiz
        eucli=sqrt(dist)
        return eucli

def Kcluster(data, distance=euclidian, k=3):
        # Determina o valor máximo e mínimo para cada atributo
        # Cria uma lista de tuplas que contem valores máximos e mínimos de cada atributo
        ranges = [(min([row[i] for row in data]),
                   max([row[i] for row in data]))
                  for i in range(len(data[0]))]

        # Cria K centroides aleatórias
        # Cria uma lista contendo os K centroides em posições aleatorias.
        # No nosso caso serão 3
        clusters = [[random.random() * (ranges[i][1] - ranges[i][0]) + ranges[i][0]
                     for i in range(len(data[0]))] for j in range(k)]

        lastmatches = None

        # O número de iterações será no máximo 100
        for t in range(100):
            bestmatches = [[] for i in range(k)]

            for j in range(len(data)):
                row=data[j]
                bestmatche=0
                for i in range(k):
                    d=distance(clusters[i],row)
                    if d== 0:
                        for rowid in bestmatches[i]:
                            for m in range(len(data[rowid])):
                                avgs=0
                                avgs[m]+=data[rowid][m]
                        for j in range(len(avgs)):
                            avgs[j]/=len(bestmatches[i])
                            clusters[i]=avgs
        return bestmatches
cluster=Kcluster(data,k=3)
c1 = data[cluster[0]]
c2 = data[cluster[1]]
c3 = data[cluster[2]]

#Plotar o gráfico
plots=[c1,c2,c3]
fig=plt.figure(236)
x=0
y=1
titles = ['sepal length x sepal width','sepal length x petal length',
          'sepal length x petal width','sepal width x petal length',
          'sepal width x petal width','petal length x petal width']

#gerar os gráficos
for h in range(1,7):
    fig.add_subplot(2,3,h)
    for plot, color in zip(plots,['r','g','b']):
     plt.scatter(plot[:, x], plot[:, y], c=color, alpha=0.7)
    if y ==3:
        x += 1
        y = x + 1
    plt.title(titles[h - 1])
    plt.xticks(())
    plt.yticks(())
    plt.show()









