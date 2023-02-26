import pandas
dataSet = pandas.read_csv("https://github.com/Natalnet/GCiD/raw/master/Codes/Data/INMET-Dados_Diarios_PortoAlegre_1980-2017.csv",skiprows = 16, sep = ";")
print(dataSet.head())