# Picrogtam-Grid-Communication-Systems-Evaluator

The aim of this project is to provide a means of evaluating, by means of a computer system, the pictogram grids used in the carding of Alternative and Augmented Communication tools. Thanks to a complete description of a pictogram grid, the system will estimate the difficulty of producing a sentence in natural language in the application. This difficulty is calculated according to the user's motor fluency by adding variables representing the difficulty of the action of moving from one pictogram to another and the difficulty of selecting a pictogram. 

Prerequisite
-

To start the project you will first need a file listing the pictograms of the AAC application you wish to test. This must be formed in the same way as the "**ProloquoBrut.csv**" file with 5 columns: 1) Word, 2) Line, 3) Column, 4) Page, 5) Identifier. Attention, if your application contains pictograms allowing you to move from one page to another, each link between pages must be identified in your listing file. Below each pictogram description allowing the user to move from one page to another each time a line must be added, leave columns 1 (Word), 2 (Line) and 3 (Column) empty and fill column 4 (Page) with the identifier of the pictogram to be clicked on and in column 5 (Identifier) the identifier of the page to which the pictogram redirects the user. Without a correct description of the application the system will not work. 

Required facilities
-

In order for this system to work, it will be necessary to dipose:
 * A recent version of Python software (7 or 8)
 * The Networkx package ("NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks"): https://networkx.github.io/
 * The matplotlib library: https://matplotlib.org/

Listing of files
-

On the Github you will find at your disposal :

 * Two Python files: 
 
  1. "**distanceCalculation.py**", which creates a graph from the pictogram file. To create the graph, it will create the arcs necessary to represent the passage from one pictogram to another. The weight of each arc will depend on the nature of the pitcograms, the distance between the pictograms, the difficulty of movement and the difficulty of selection. Five different calculations are therefore made: 
 * Pictogram to pictogram : C=D(P1,P2)m+n
 * Pictogram to pictogram that links to a page : C=D(P1,P2)m
 * Pictogram that links to a page to page : C=n
 * Page to pictogram : C=D(P(1,1),P2)m+n
 * Page to pictogram that links to a page : C=D(P(1,1),P2)m
 
  2. "**ProductionCost.py**" which calculates the production cost of a sentence in the application.

 
 * Two .csv files: "**ProloquoBrut.csv**" which corresponds to our list of pictograms and "ArcsEtdistances.csv" which corresponds to our list of arcs created from the first .csv file.
 * One .txt file: "**phraseEnter.txt**" which contains the phrase or the corpus of phrase for which we want to know the production cost.
 * One .odt file: "**ProloquoCanadien.odt**" which contains the unformatted description of our pictogram list.
 
Steps of use
-

* Step 1: Create the graph corresponding to the possible navigations in the application
 Run the script "**distanceCalculation.py**" to update the file "**ArcsAndDistances.csv**".

* Step 2: Extract the production cost of a sentence
 Insert in the text file "**phraseEnter.txt**" the phrases for which you want to know the cost.
 Run the script "**ProductionCost.py**" and save the result.

Versions
-

Last version on: 2020/09/18

Auteurs 
-

Lucie Chasseur : https://github.com/LucieChasseur

Sébastien Riou : https://github.com/kuhlkrein

Liens bibliographiques
-

This work is inspired by the article :

Lucie Chasseur, Marion Dohen, Benjamin Lecouteux, Sébastien Riou, Amélie Rochet-Capellan, et al..Evaluation of the acceptability and usability of augmentative and alternative communication (AAC)tools: the example of pictogram grid communication systems with voice output. ACM SIGACCESS Conference on Computers and Accessibility, 2020, Athènes, Greece. 10.1145. hal-02896668 https://hal.univ-grenoble-alpes.fr/hal-02896668
