import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
data = pd.read_excel('animals-weight.xlsx')

print(data.corr())

figure = plt.figure(figsize=(9,6))
plt.scatter(np.log(data['Body Weight']), np.log(data['Brain Weight']))
plt.xlabel('Body Weight')
plt.ylabel('Brain Weight')
plt.show()

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data.drop('Animals', axis=1))
col = ['Body Weight', 'Brain Weight']
new_data = pd.DataFrame(data_scaled, columns=col)

print(new_data.head())