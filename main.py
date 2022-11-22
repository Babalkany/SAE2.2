#################################################
# SAE 2.2 développement efficace                #
# software qt qui combine des images en .fits   #
# @author: Bastien BRUNEL & Tom LECLERCQ        #
# 22/11/2022                                    #
# V1.0 init affichage images                    #
#################################################

#import 
import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

def chargerAllImages(listImage):
    imageConcat = [fits.getdata(image) for image in listImage]
    
    # Version détaillé
    finalImage = np.zeros(shape=imageConcat[0].shape)

    for image in imageConcat:
        finalImage += image
        
    # Pour les fast learner
    #finalImage = np.sum(imageConcat, axis=0)
    
    image_hist = plt.hist(finalImage.flatten(), bins='auto')
    plt.show()
    
    plt.imshow(finalImage, cmap='gray', vmin=2E3, vmax=3E3)
    plt.colorbar()
    plt.show()


testt = ['C:/Users/SDO/Desktop/BUT1/Semestre_3/SAE3.02/fits_tests/M13_blue//M13_blue_0001.fits',
        'C:/Users/SDO/Desktop/BUT1/Semestre_3/SAE3.02/fits_tests/M13_blue//M13_blue_0002.fits',
        'C:/Users/SDO/Desktop/BUT1/Semestre_3/SAE3.02/fits_tests/M13_blue/M13_blue_0003.fits',
        'C:/Users/SDO/Desktop/BUT1/Semestre_3/SAE3.02/fits_tests/M13_blue/M13_blue_0004.fits',
        'C:/Users/SDO/Desktop/BUT1/Semestre_3/SAE3.02/fits_tests/M13_blue/M13_blue_0005.fits']

testb = ['C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0001.fits', 
        'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0002.fits', 
        'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0003.fits', 
        'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0004.fits', 
        'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0005.fits'
        ]

chargerAllImages(testb)