import numpy as np
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2hsv,hsv2rgb

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch
import seaborn

import pandas as pd

import webcolors

seaborn.set()
current_image=imread("./maurilio.jpg")
current_image=resize(current_image,(256,256),mode="reflect",anti_aliasing=True)
current_image_hsv=rgb2hsv(current_image)
pixel_list=current_image_hsv.reshape(-1,3)
print(pd.DataFrame(current_image.reshape(-1,3),columns=["R","G","B"]).head())
inertia=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,random_state=1234)
    kmeans.fit(pixel_list)
    inertia.append((i,kmeans.inertia_))
plt.plot([w[0] for w in inertia],[w[1] for w in inertia],marker="X")
plt.xlabel("Numeros de clusters")
plt.ylabel("Inercia")

kmeans=KMeans(n_clusters=3,init='k-means++',n_init=10,random_state=1234)
kmeans.fit(pixel_list)
cluster_list=kmeans.labels_
cluester_mask=cluster_list.reshape(256,256)

cmap = ListedColormap(hsv2rgb(kmeans.cluster_centers_.reshape(1,3,3)).reshape(3,3))
bounds=[0,1,2]
norm=BoundaryNorm(bounds,cmap.N)

plt.imshow(cluester_mask,cmap=cmap)
patches =[Patch(color=c, label="Cluster {}".format(i)) for i,c in enumerate(cmap.colors)]
plt.legend(handles=patches,loc=4,frameon=True)
plt.grid(False)
plt.show()

