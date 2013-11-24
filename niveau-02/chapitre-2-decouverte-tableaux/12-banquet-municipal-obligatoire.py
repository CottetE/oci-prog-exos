
##################################
# fichier 12-banquet-municipal-obligatoire.py
# nom de l'exercice : Banquet municipal
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=17
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbrPosition=int(input())
nbrChange=int(input())
listePosition=[]
listeChange=[]

for i in range(nbrPosition):
    listePosition+=[int(input())]
for i in range(nbrChange):
    premier=int(input())
    deuxieme=int(input())

    listePosition[premier],listePosition[deuxieme]=listePosition[deuxieme],listePosition[premier]
for i in listePosition:
    print(i)