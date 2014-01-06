
##################################
# fichier 05-distance-obligatoire.py
# nom de l'exercice : Distance
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=9
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules
from math import sqrt

# mettre votre code ici

def distanceE(x1,y1,x2,y2):
    """fonction qui prend les coordonées de deux points et
    retourne la distance euclidienne des deux.La distance
    euclidienne = racine carré de ((x2-x1)^2 + (y2-y1)^2)
    """

    return sqrt((x2-x1)**2 + (y2-y1)**2)
    
#corps du programme
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distanceE(x1,x2,y1,y2))