#Modulos importados
from skimage.measure import _structural_similarity as ssim
import cv2
import matplotlib.pyplot as plt
import numpy as np
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err
def compare_images(imageA,imageB,title):
    #Comparando as imagens usando o SKLEARN e o método criado mse
    m=mse(imageA,imageB)
    s=ssim(imageA,imageB)

    #Configurando a imagem

    fig=plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    #Mostrando a primeira imagem
    ax=fig.add_subplot(1,2,1)
    plt.imshow(imageB,cmap=plt.cm.gray)
    plt.axis("off")

    #Mostrar as imagens
    plt.show()




