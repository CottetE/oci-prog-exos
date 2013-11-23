
##################################
# fichier 07-repartition-du-poids-obligatoire.py
# nom de l'exercice : Répartition du poids
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=10
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

nbrChar=int(input())
mTotale=0
char=[]
for i in range(nbrChar):
    newChar=float(input())
    mTotale+=newChar
    char+=[newChar]

indice=mTotale/nbrChar
for i in char:
    change=-(i-indice)
    print(change)