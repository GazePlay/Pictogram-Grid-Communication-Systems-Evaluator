'''
Code créé pour calculer la distance entre les pictogrammes d'une application de CAA
Prend en compte la difficulté du mouvement et la difficulté de la sélection 
'''

#!/usr/bin/env python
# -*- coding : utf-8 -*-

#Importation du module mathématiques
import math

#Fichier brut à traiter
rawFile=open("ProloquoBrut.csv","r",encoding="utf8")

#Fichier d'écriture des arcs
bowsFile=open("ArcsEtDistances.csv","w",encoding="utf8")

#Création de la liste des distances
disTab=[]

#Création de la liste des liens entre les répertoires
linksList=[]
linkCount=0

#Définition du poids du mouvement
m=1
#Définition du poids du temps de sélection
n=1

#Traitement du fichier source
for lines in rawFile :
	lines=lines.lower() 
	sentence=lines.strip()
	col=sentence.split("\t")

	#On gère le problème des lines semi vides créées par les liens entre les répertoires
	if len (col) > 4 :
		#Décraration des variables
		words=col[0]
		column=col[2]
		line=col[1]
		page=col[3]
		iden=col[4]

		#Récupération des coordonnées x,y
		x=int(line)
		y=int(column)

		#On stocke les coordonnées l'ID et x,y dans une liste
		disTab.append([iden,x,y,words,page])

	#On récupère les liens entre les répertoires
	elif len (col) > 1 : 
		headLink=col[0]
		pointedLink=col[1]

		#On stocke les liens entre les répertoires
		linksList.append([headLink,pointedLink])

#On parcours la liste créé plus haut
for i in range(0, len(disTab)):
	#On crée une variable qui prend comme valeur l'ID du mot d'indice i
	refID=disTab[i][0]
	#On crée une variable qui prend comme valeur le nom de la page actuelle 
	currentPage=disTab[i][4]
	#On créé une variable qui prend comme valeur le mot d'indice i
	mot=disTab[i][3]
	x1=disTab[i][1]
	y1=disTab[i][2]

	for j in range(i,len(disTab)):
		#On créé une nouvelle variable qui prend comme valeur l'ID du mot d'indice j
		ID=disTab[j][0]
		#On vérifie que l'on est toujours sur la bonne page
		currentPage2=disTab[j][4]
		x2=disTab[j][1]
		y2=disTab[j][2]

		if currentPage2==currentPage:
			#Si les deux IDs sont différents on récupère les coordonnées x et y de chacun
			if refID != ID :
				mot2=disTab[j][3] 

				#Calcul des distances Euclidiennes
				squaredDistance=(x1-x2)**2+(y1-y2)**2
				pictoDistance=math.sqrt(squaredDistance)

				#Ecriture du résultat dans un fichier
				bowsFile.write(mot+"\t"+refID+"\t"+ID+"\t"+str(pictoDistance*m+n)+"\n")
				bowsFile.write(mot2+"\t"+ID+"\t"+refID+"\t"+str(pictoDistance*m+n)+"\n")

	#On écrit le lien entre le pictogramme et la page
	if linkCount < len(linksList):

		#Ecriture du résultat dans un fichier
		bowsFile.write("Lien Picto Page"+"\t"+linksList[linkCount][0]+"\t"+linksList[linkCount][1]+"\t"+ str(n)+"\n")
		linkCount+=1

	#On écrit le lien entre la page et le pictogramme
	#On calcule la disantce entre le lien de la page et des pictogrammes à partir du pictogramme en haut à gauche avec x=1 et y=1 
	squaredDistance3=(1-x1)**2+(1-y1)**2
	pageToPicto=math.sqrt(squaredDistance3)

	#Ecriture du résultat dans un fichier
	bowsFile.write("Lien Page Picto"+"\t"+currentPage+"\t"+disTab[i][0]+"\t"+str(pageToPicto*m+n)+"\n")


bowsFile.close()
rawFile.close()
