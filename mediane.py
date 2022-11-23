#################################################
# SAE 2.2 développement efficace                #
# software qt qui combine des images en .fits   #
# @author: Bastien BRUNEL & Tom LECLERCQ        #
# 23/11/2022                                    #
# V1 Empilement par médiane                     #
#################################################



import numpy as np

import matplotlib.pyplot as plt

from astropy.io import fits

from astropy.utils.data import get_pkg_data_filename


def chargerAllImages(listImage):
    list_images = [fits.getdata(image) for image in listImage]
    new_image = []
    
    print(list_images)

    #copie de la structure de la premiere image
    for ligne in range(len(list_images[0])):
        new_image.append([])
        for pixel in list_images[0][ligne]:
            new_image[ligne].append([])


    for image in list_images:
        for ligne in range(len(image)):
            for pixel in range(len(image[ligne])):
                new_image[ligne][pixel].append(image[ligne][pixel])

    for ligne in new_image:
        for pixel in range(len(ligne)):
            # print(type(ligne[pixel]))
            ligne[pixel].sort()
            a = len(ligne[pixel])//2
            new_valeur = ligne[pixel][a]
            ligne[pixel] = new_valeur

    print(new_image)
    
test = ["C:/Users/SDO/Desktop/BUT1/Semestre_3/SAE3.02/fits_tests/mini/mini0.fits",
        "C:/Users/SDO/Desktop/BUT1/Semestre_3/SAE3.02/fits_tests/mini/mini1.fits",]

chargerAllImages(test)
