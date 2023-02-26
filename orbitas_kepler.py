import pandas as pd
import math
#Leitura da planinha que contém os dados
x=pd.read_excel('C:/Users/Deus.DEUS.002/Desktop/Relatorio_unirn/dados_orbitas.xlsx',sep=r'\s*,\s*',
                           header=0, encoding='ascii',engine='xlrd')
#Exibição dos dados
print(x)
print()
print("MENOR RAIO MÉDIO ENTRE PLANETAS DO SISTEMA SOLAR")
print()
print(x['Planetas '][0])
print(x['Raio Médio'].min())
print()
print("MAIOR RAIO MÉDIO ENTRE PLANETAS DO SISTEMA SOLAR")
print()
print(x['Planetas '][7])
print(x['Raio Médio'].max())
print()
print("MENOR PERÍODO DE REVOLUÇÃO")
print(x['Planetas '][0])
print(x['Período Em anos Terrestres'].min())
print()
print("MAIOR PERÍODO DE REVOLUÇÃO")
print(x['Planetas '][7])
print(x["Período Em anos Terrestres"].max())
print()
#Agora vamos ao cálculo das constantes baseado no raio médio fornecido
#Usando a formula de Kepler para definir a constante
constante_kepler=(x['Raio Médio'].max()**3)/(x["Período Em anos Terrestres"].max()**2)
print("CONSTANTE DO MAIOR PLANETA")
print(round(constante_kepler))
print()
print("CONSTANTE DO MENOR PLANETA")
constante_kepler2=(x['Raio Médio'].min()**3)/(x["Período Em  anos Terrestres"].min()**2)
print(round(constante_kepler2))









