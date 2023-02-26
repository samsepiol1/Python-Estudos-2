import matplotlib.pyplot as plt
x1 = [1,3,5,7,9]
y1 = [2,3,7,1,0]
z = [200,500,100,330,100]


#legendas
titulo = "Meu primeiro gráfico de Scatter Plot"
eixox = "Eixo X"
eixoy = "Eixo Y"

#gráfico
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.scatter(x1,y1,label="Meus Pontos",color="red",marker=".",s=z)
plt.legend()
plt.plot(x1,y1,color="k",linestyle=":")
plt.show()
