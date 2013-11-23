
##################################
# fichier 05-grand-inventaire-obligatoire.py
# nom de l'exercice : Grand inventaire
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=7
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

nbrope=int(input())
liste = [0]*10
for i in range(nbrope):
    numero=int(input())-1
    quantite=int(input())
    liste[numero]+=quantite
for i in liste:
    print(i)
