#################################################
# SAE 2.2 développement efficace                #
# software qt qui combine des images en .fits   #
# @author: Bastien BRUNEL & Tom LECLERCQ        #
# 15/12/2022                                    #
# V1.5 ajout du calcul des outlers              #
#################################################

#import qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QCheckBox, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#import astropy
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.stats import sigma_clip, mad_std
from scipy import stats

#var globales test
test = [['C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0001.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0002.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0003.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0004.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0005.fits']]

class App(QWidget):
    def __init__(self):
        super().__init__()
        
        #label
        self.label = QLabel("Choisir une méthode de calcul")


        # attribut liste des chemins d'images
        self.liste = []
        self.setWindowTitle('SAE 2.2')
        self.figure = plt.figure()

        # jointure plt/qt
        self.canvas = FigureCanvas(self.figure)

        # création d'un petit layout rapide
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # création boutons 
        self.btnAvg = QPushButton("Moyenne")
        self.btnMed = QPushButton("Médiane")
        self.check = QCheckBox("éliminer les ouliers ?")
        

        # création connexions bouton/méthode
        self.btnMed.clicked.connect(self.btnMedClicked)
        self.btnAvg.clicked.connect(self.btnAvgClicked)

        # layout 2 le retour
        layout.addWidget(self.check)
        layout.addWidget(self.btnAvg)
        layout.addWidget(self.btnMed)

        # appel fichieres
        self.openFileNamesDialog()

        #affichage
        self.show()

    def btnAvgClicked(self):
        """
        méthode qui calcule l'image composée des pixels moyens de tous les fichiers présent dans self.liste
        """
        self.chargerAllImages(self.liste[0], option = 1) 

    def btnMedClicked(self):
        """
        méthode qui calcule l'image composée des pixels médians de tous les fichiers présent dans self.liste
        """
        self.chargerAllImages(self.liste[0], option = 2)

    def openFileNamesDialog(self):
        """
        méthode qui charge plusieurs fichiers et les ajoutes directement dans self.liste
        """
        #                          widget parent, label explication, chemin ou ouvrir la boite de dialogue, type de fichier a ouvrir
        files, _ = QFileDialog.getOpenFileNames(self,"Select one or more files to open", "","Images (*.fits / *.fit)")
        if files:
            self.liste.append(files)
            
    # def calculIncoherence(self, ListPixel):
    #     liste = []
    #     m = np.mean(ListPixel)
    #     for i in ListPixel:
    #         if i < m+3*np.std(ListPixel) and i > m-3*np.std(ListPixel):
    #             liste.append(i)
    #     return liste
                
    def chargerAllImages(self, listImage, option=1):
        imageConcat = [fits.getdata(image) for image in listImage]
        self.figure.clear()

        if option == 1:
            copieImage = np.mean(imageConcat, axis=0)
            if self.check.isChecked():
                copieImage = sigma_clip(copieImage, sigma=3, maxiters=1, stdfunc=mad_std)
                self.label.setText("Empilement par moyenne avec rejet des outliers")
            else:
                self.label.setText("Empilement par moyenne simple")

        #médiane
        elif option == 2:
            copieImage = np.median(imageConcat, axis=0)
            if self.check.isChecked():
                copieImage =  sigma_clip(copieImage, sigma=3, maxiters=1, stdfunc=mad_std)
                self.label.setText("Empilement par médiane avec rejet des outliers")
            else:
                self.label.setText("Empilement par médiane simple")

        plt.imshow(copieImage, cmap='gray')
        plt.colorbar()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
