import pandas
import matplotlib.pyplot as plt
from datetime import datetime
#Transformando data em variável do tipo datetime
dataSet=pandas.read_csv("https://raw.githubusercontent.com/Natalnet/GCiD/master/Codes/Data/INMET-Dados_Mensais_Natal_1968-2018.csv", sep=";")
print(type(dataSet))
dataSet["Data"] = pandas.to_datetime(dataSet["Data"], format = "%d/%m/%Y")


plt.plot(dataSet["Data"], dataSet["PrecipitacaoTotal"])
plt.title("Precipitação ao longo dos anos")
plt.xlabel("Data")
plt.ylabel("Precipitação")
plt.show()