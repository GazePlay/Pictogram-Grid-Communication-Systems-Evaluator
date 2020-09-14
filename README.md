# Picrogtam-Grid-Communication-Systems-Evaluator

The aim of this project is to provide a means of evaluating, by means of a computer system, the pictogram grids used in the carding of Alternative and Augmented Communication tools. Thanks to a complete description of a pictogram grid, the system will estimate the difficulty of producing a sentence in natural language in the application. This difficulty is calculated according to the user's motor fluency by adding variables representing the difficulty of the action of moving from one pictogram to another and the difficulty of selecting a pictogram. 

Prerequisite
-

To start the project you will first need a file listing the pictograms of the AAC application you wish to test. This must be formed in the same way as the "ProloquoBrut.csv" file with 5 columns: 1) Word, 2) Line, 3) Column, 4) Page, 5) Identifier. Attention, if your application contains pictograms allowing you to move from one page to another, each link between pages must be identified in your listing file. Below each pictogram description allowing the user to move from one page to another each time a line must be added, leave columns 1 (Word), 2 (Line) and 3 (Column) empty and fill column 4 (Page) with the identifier of the pictogram to be clicked on and in column 5 (Identifier) the identifier of the page to which the pictogram redirects the user. Without a correct description of the application the system will not work. 

Required facilities
-

Pour que ce système fonctionne il faudra diposer:
 * Une version récente du logiciel Python (7 ou 8)
 * Le package Networkx ("NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks") https://networkx.github.io/
 * La 

Listing des fichiers
-


--> 2 Corpus 
--> 2 codes 
--> 1 Sortie 

Etapes d'utilisation
-


--> 1 corpus 
--> 2 Distance
--> 3 Arcset D
--> 4 prodCost
--> 5 fichier sortie 

Versions
-

Dernière version le : 01/08/2020

Auteurs 
-

Lucie, Sébastien

Liens bibliographiques
-

--> Mettre le lien de l'article 
