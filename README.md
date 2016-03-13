PDF-OCR-Zone
============

Renomme un fichier PDF en fonction du texte contenu dans une zone

Objectifs
---------
En fonction d'une zone contenue dans un fichier PDF renomme le fichier et enregistre le dans un répertoire

Liens que j'ai trouvé utiles
----------------------------
http://stackoverflow.com/questions/13984357/pythonmagick-cant-find-my-pdf-files
http://p-s.co.nz/wordpress/pdf-to-png-using-pythonmagick
http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python

Mécanismes
----------
Transforme un pdf en image 'png' isole une zone de l'image 'crop' et converti l'image en texte. Déplace et renomme le fichier pdf suivant le texte dans la zone de l'image. Affiche un rapport d'activité et efface les traces des fichiers inutiles

Répertoires de travail
----------------------
Le répertoire de base des fichiers PDF à taiter se trouve dans ".\pdf"
Le répertoire de destination des fichiers traités se trouve dans ".\pdf\fait"
