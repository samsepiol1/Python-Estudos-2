import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

planets=pd.read_csv('planets.csv',sep=',')
sns.set(style='ticks')

#Inicializando a figura por meio de um logaritmo
f,ax=plt.subplots(figsize=(7,6))
ax.set_xscale('log')

#Carregando exemplos dos Dataset's

