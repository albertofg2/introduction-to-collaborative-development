import matplotlib.pyplot as plt
import scipy


def splitter():
    # Cargar la imagen al programa
    img =  scipy.datasets.face()

    # Separar los canales en diferentes colores
    for i in range(len(img)):
        for j in range(len(img[0])):
            img_roja = img[i,j][0]
            img_verde = img[i,j][1]
            img_azul = img[i,j][2]




    """
    img_roja = img[:,:,0]
    img_verde = img[:,:,1]
    img_azul = img[:,:,2]
    """

    # Union de las tres arrays en una sola lista
    imagenes=[img_roja, img_verde, img_azul]


    return imagenes
