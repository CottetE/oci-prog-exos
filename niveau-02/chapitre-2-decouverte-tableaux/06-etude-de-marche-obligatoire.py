
##################################
# fichier 06-etude-de-marche-obligatoire.py
# nom de l'exercice : Étude de marché
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=9
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

nbrProduit=int(input())
nbrPersonne=int(input())
liste=[0]*nbrProduit
for i in range(nbrPersonne):
    numero=int(input())
    liste[numero]+=1
for i in liste:
    print(i)
