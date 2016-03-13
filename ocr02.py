#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# Fait par Christophe SONNECK
# Le : 13/03/2016
#
# Objectifs  : En fonction d'une zone contenue dans un fichier PDF nomme le fichier et enregistre le dans un répertoire
# Mécanismes : Transforme un pdf en image 'png' isole une zone de l'image 'crop' et converti l'image en texte
#			   déplace et renomme le fichier pdf suivant le texte dans la zone de l'image. 
# 			   Affiche un rapport d'activité et efface les traces des fichiers inutiles
# -----------------------------------------------------------------------------------------------------
# Liens utiles
# http://stackoverflow.com/questions/13984357/pythonmagick-cant-find-my-pdf-files
# http://p-s.co.nz/wordpress/pdf-to-png-using-pythonmagick/
# http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python
# -----------------------------------------------------------------------------------------------------
#
import PythonMagick
import os 
from pytesseract import image_to_string
from PIL import Image

img = PythonMagick.Image() 
img.density("300") #Image à 300 dpi
chemin="C:\\Users\\CSONNECK\\Desktop\\python\\pdf\\" #Répertoire source
destination="C:\\Users\\CSONNECK\Desktop\\python\\pdf\\fait\\" #Répertoire de destination
for file in os.listdir(chemin): #Pour chaque fichier dans le répertoire chemin
    if file.endswith(".pdf"): #Si le fichier à l'extension pdf
		fileFrom = chemin+file #Nom du fichier avec son chemin
		toPng = file.replace(".pdf",".png") #Création du nom de sauvegarde de l'image extension pdf en png
		img.read(os.path.abspath(fileFrom)) #Lecture de l'image
		#img.crop("264x74+1209+377")
		img.crop("400x80+1937+337") #LargeurxHauteur+Coin Gauche+Coin Haut
		img.write(os.path.abspath(toPng)) #Conversion en Image
		image = Image.open(os.path.abspath(toPng))
		imageToText = image_to_string(image, lang='fra') #Applique l'OCR
		nom=destination+imageToText+".pdf" #Chemin des destination et Nom du fichier en extension PDF
		try: #Essai de sauvegarde avec rapport de réussite
			os.rename(os.path.abspath(fileFrom),os.path.abspath(nom)) #Renomme et déplace le fichier dans un autre répertoire
			print("OK : "+nom)
		except: #Echec de sauvegarde avec rapport
			print("Impossible : "+file)
		os.remove(os.path.abspath(toPng)) #Détruit le fichier image de travail pour l'OCR