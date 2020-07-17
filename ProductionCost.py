# -*- coding: utf-8 -*-

# networkx package pour le graphe
import networkx as nx
from networkx import *

#matplotlib package et pyplot pour la visualisation
import matplotlib.pyplot as plt


text= open("phrasesEntrée.txt", "r" , encoding="utf8")

end= open("Resultat.txt", "w" , encoding="utf8")

class WeightedPath:

	def __init__(self):
		self.path = []
		self.weight=0


#Fonction qui établit le noeud à partir duquel il faut commencer à calculer un arc
'''
text = texte d'entrée
nodeList = liste de tous les noeuds du graphe
edgeList = tableau associatif de tous les arcs avec en clé le noeud tête et en valeurs le noeud pointé et le poids de l'arc
'''
def initialNode (text, nodeList, edgeList):
	startNode="home"
	stock=[]
	totalWeight=0
	#On parcours le fichier texte
	for line in text : 
		line=line.lower()
		line=line.strip()
		#On évite les lignes vides
		if line != "":
			#On récupère le plus court chemin
			words=shortestPath(startNode, line, nodeList, edgeList)
			path=words.path
			#On récupère le dernier élément de la liste 
			startNode=path[-1]
			#On ajoute le poids
			totalWeight+=words.weight

		finalPath=[]
		#On ajoute le premier élément de la liste au chemin final
		finalPath.append(path[0])
		#On parcours le chemin
		for i in range(1, len(path)):
			#Si on toruve deux mots qui se suivent différents
			if path[i-1] != path[i]:
				#on ajoute l'elt au chemin final
				finalPath.append(path[i])
		#On stocke dans une liste le chemin et le poids total
		stock.append(str(finalPath)+" "+str(totalWeight))

	return stock


#Fonction qui prend en entrée un mot de la phrase et en fait une liste de noeuds possibles
'''
nodeList = liste de tous les noeuds du graphe
word = chaque word de la phrase d'entrée 
'''
def textToNodes(word, nodeList):
	candidatesNode=[]
	#on parcours la liste des noeuds
	for i in range (0, len (nodeList)):
		#on découpe au '@' pour récupérer le mot d'origine au lieu de l'identifiant complet
		wordNode=nodeList[i].split("@")
		#Si le mot d'origine est égal au word de la phrase
		if wordNode[0]==word:
			#on l'ajoute à la liste des noeuds canidats potentiels
			candidatesNode.append(nodeList[i])
	return candidatesNode


#Fonction de calcul du plus court path
'''
initialNode = point de départ de la recherche dans le graphe
sentance = phrase d'entrée pour laquelle il faut calculer le cout de production
nodeList = liste de tous les noeuds du graphe
edgeList = tableau associatif de tous les arcs avec en clé le noeud tête et en valeurs le noeud pointé et le weight de l'arc
'''
def shortestPath(initialNode, sentance, nodeList, edgeList):
	initialNodes=[]
	words=sentance.split(" ")
	shortestPath=[]
	#Initialisation du poids total
	totalWeight=0
	initialNodes.append(initialNode)

	#On créé la variable du chemin final
	finalPath=[]
	pathList=[]

	#On céé un nouveau graphe avec la liste des candidats 
	coupleGraphe=nx.DiGraph()
	coupleGraphe.add_node("end")

	index=0
	#On parcours la phrase 
	for word in words :
		minWeight=10000
		#On stocke dans une variable les mots "candidats" pour créer le plus court chemin
		candidates=textToNodes(word, nodeList)
		#Pour chaque candidat
		for candidate in candidates :
			#On ajoute les candidats comme noeuds du souso graphe
			coupleGraphe.add_node(candidate)

			#Quand on arrive à l fin d ela phrase 
			if index==len(words)-1:
				#On créé un arc "end" de poids 0
				coupleGraphe.add_edge(candidate,"end",weight=0)

			#On parcours la liste des noeuds initiaux
			for firstNode in initialNodes :
				#On extrait le plus court chemin entre le premier noeud et le candidat avec la fonctionn "shortest_path "fonction Networkx
				path=nx.shortest_path(G,source=firstNode, target=candidate)

				#On initialise le poids
				weight=0
				#On parcours le chemin
				for i in range(1, len(path)):
					edgePrevNode = edgeList[path[i-1]]
					for edge in edgePrevNode :
						#On vérifie que le premier elt de la variable arc = shortest path de i
						if edge[0]==path[i]:
							weight+=edge[1]

				#Si le poids est inférieur au poids minimum
				if weight<minWeight :
					#Le poids min prend la valeur du poids
					minWeight=weight

				pathList.append(path)

				coupleGraphe.add_edge(path[0],path[-1],weight=weight)
		#On modifie le point de départ de la fonction
		initialNodes=candidates
		index=index+1
		
		#On calcule la somme des poids entre les arcs
		totalWeight+=minWeight

	#On applique à nouveau une recherche du plus court chemin dans le sous graphe
	shortestpath=nx.shortest_path(coupleGraphe,source="home", target="end")


	#On céé le chemin final 
	wordIndex=0
	#On parcours la liste des chemins
	for path in pathList:
		if (shortestpath[wordIndex]==path[0]) & (shortestpath[wordIndex+1]==path[-1]):
			for words in path:
				finalPath.append(words)
			wordIndex=wordIndex+1

	#On créé un objet
	weightedPath=WeightedPath()
	weightedPath.path=finalPath
	weightedPath.weight=totalWeight

	return weightedPath



#On créé le graph G
G=nx.DiGraph()

#On ouvre le fichier contenant la liste des pictogrammes
f=open("ArcsEtDistances.csv", "r", encoding ="utf8")

edgeList={}

# ~ On parcours le fichier pour déterminer les noeuds, les arcs et les poids
for line in f:
	line=line.strip()
	col = line.split('\t')

	#création de la liste des noeuds
	G.add_node(col[1])
	nodeList=list(G.nodes())

	# Création des arcs avec leurs poids
	G.add_edge(col[1],col[2],weight=col[3])

	#Création d'un tableau associatif qui comprendra les noeuds et les poids 
	if col[1] in edgeList.keys():
		edgeList[col[1]].append((col[2],float(col[3])))
	else :
		edgeList[col[1]]=[(col[2],float(col[3]))]

result=initialNode(text, nodeList, edgeList)

#Ecriture du résultat dans un fichier 
for elt in result :
	end.write(elt+"\n")

#On choisi le type d'algorithme qui gère la disposition des noeuds dans l'espace
pos=nx.spring_layout(G)

f.close()
text.close()
