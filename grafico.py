import matplotlib.pyplot as plt
import pandas
df = {'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]}
x=[1,2,3,4,5,6,7,8,9]
y=[11,12,13,14,15,16,17,18,19]
plt.savefig('nome_da_imagem2.png')
fig,ax=plt.subplots()
ax.plot(df['Aluno'],df['Prova'])
plt.show()


