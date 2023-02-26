import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataSet=pd.read_csv("https://raw.githubusercontent.com/Natalnet/GCiD/master/Codes/Data/INMET-Dados_Mensais_Natal_1968-2018.csv",sep=';')

"""print(dataSet.head()) Exibindo cabeçalho"""

"""print(dataSet.describe()) descrição mais detalhadada"""
#Transformando a data em uma variável do tipo dataTime
dataSet["Data"]=pd.to_datetime(dataSet["Data"],format="%d/%m/%Y")

#Declarando variáveis para ajudar na analise de dados
diaInicial=pd.to_datetime("01/01/2008",format="%d/%m/%Y")
diaFinal=pd.to_datetime("31/12/2018",format="%d/%m/%Y")

#Retornando o dataSet
dataSetPrec=dataSet[(dataSet["Data"] >= diaInicial) & (dataSet["Data"] <= diaFinal)]
# Visualizando os dados do cabeçalho
print(dataSetPrec.head())
#Visualizando os dados do DataSet de forma resumida
print(dataSetPrec.describe())

#Trabalhando com as variáveis
dataSetPrec = dataSetPrec[["NumDiasPrecipitacao","PrecipitacaoTotal"]].dropna().reset_index(drop = True)

#Visualizar os dados






