from sklearn.datasets import load_breast_cancer
data=load_breast_cancer()
label_names=data['target_names']
labels=data['target']
feature_names=['feature-names']
features=data['data']
print(label_names)
print(labels[0])