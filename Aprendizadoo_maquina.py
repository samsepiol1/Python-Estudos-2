import pandas
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
#Leitura de dados
dataSet=pandas.read_csv("https://github.com/Natalnet/GCiD/raw/master/Codes/Data/INMET-Dados_Diarios_PortoAlegre_1980-2017.csv",skiprows = 16, sep = ";")
dataSet.head()
print(dataSet['Estacao'])
#Transformando a data em um variavel do tipo datetime
dataSet["Data"] = pandas.to_datetime(dataSet["Data"], format = "%d/%m/%Y")
#Atribuir data como indices
dataSet=dataSet.set_index("Data")
#Eliminando as colunas
dataSet = dataSet.drop(columns = ["Unnamed: 11","Estacao"])
#Descrevendo base de dados
dataSet.describe()

#Separando as horas
dataSet00,dataSet12=[dataSet[dataSet["Hora"]==0],dataSet[dataSet["Hora"]==1200]]
#Verficando os dados a essa hora
dataSet00.describe()
#Excluir Colunas que não servem
ataSet00 = dataSet00.drop(columns = ["Hora","Precipitacao","TempMinima"])
dataSet12 = dataSet12.drop(columns = ["Hora","TempMaxima","Insolacao","Evaporacao Piche","Temp Comp Media","Umidade Relativa Media","Velocidade do Vento Media"])
dataSet12.head()
#Criando um intervalo entre as datas
dataInicial='1980-01-01'
dataFinal='2017-12-31'
tempo=pandas.date_range(dataInicial, dataFinal)
#Atribuindo este intervalo de tempo á dataSet provisório
dataSetProv=pandas.DataFrame()
dataSetProv["Dat"]=tempo
#Visualizando o DataSet provisorio
print(dataSetProv.head())
#Atribuindo Indice
dataSet=dataSet.set_index("Data")
#Mesclando os dois resultados
dataSetProv=dataSetProv.join(dataSet00).join(dataSet12)
dataSet = dataSetProv
dataSet=dataSet.dropna()

#Chuva x Temperatura
plt.scatter(dataSet.index, dataSet["Precipitacao"])

data = load_breast_cancer()






