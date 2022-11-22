#################################################
# SAE 2.2 développement efficace                #
# software qt qui combine des images en .fits   #
# @author: Bastien BRUNEL & Tom LECLERCQ        #
# 22/11/2022                                    #
# V1.1 ajout gestion qt-astropy                 #
#################################################

#import qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QImage 

#import astropy
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

#var globales test
test = [['C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0001.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0002.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0003.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0004.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0005.fits']]

class App(QWidget):
    def __init__(self):
        super().__init__()
        
        # attribut liste des chemins d'images
        self.liste = []
        self.setWindowTitle('SAE 2.2')

        #chargement des fichiers
        self.openFileNamesDialog()

        self.chargerAllImages(self.liste[0])
        print(self.liste)

        #affichage
        self.show()

    def openFileNamesDialog(self):
        """
        méthode qui charge plusieurs fichiers et les ajoutes directement dans self.liste
        """
        #                          widget parent, label explication, chemin ou ouvrir la boite de dialogue, type de fichier a ouvrir
        files, _ = QFileDialog.getOpenFileNames(self,"Select one or more files to open", "","Images (*.fits)")
        if files:
            self.liste.append(files)
    
    def chargerAllImages(self, listImage):
        imageConcat = [fits.getdata(image) for image in listImage]
        
        # Version détaillé
        finalImage = np.zeros(shape=imageConcat[0].shape)  # type: ignore

        for image in imageConcat:
            finalImage += image  # type: ignore
            
        # Pour les fast learner
        #finalImage = np.sum(imageConcat, axis=0)
        
        image_hist = plt.hist(finalImage.flatten(), bins='auto')
        plt.show()
        
        plt.imshow(finalImage, cmap='gray', vmin=2E3, vmax=3E3)
        plt.colorbar()
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


