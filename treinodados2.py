import matplotlib.pyplot as plt
#variaveis para gráficos de barras
x = [1,2,3,4,5]
y = [2,3,7,1,8]
#legendas
titulo = "Meu primeiro gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(x,y)
plt.show()