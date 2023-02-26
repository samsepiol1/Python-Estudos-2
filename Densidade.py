import pandas
import matplotlib.pyplot as plt
subs={'Agua':[1,0],'Benzeno':[0,90],'Cloriformio':[1,53]}
print(subs['Agua'])
subs_org=pandas.Series([1.0,0.90,1.53],index=["Agua","Benzeno","Cloriformio"])
print('Nivel de Densidade das Substâncias:')
fig,ax=plt.subplots()
ax.plot(subs_org)
plt.show()
