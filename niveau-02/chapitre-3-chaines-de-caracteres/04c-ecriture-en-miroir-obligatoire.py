
##################################
# fichier 04c-ecriture-en-miroir-obligatoire.py
# nom de l'exercice : Écriture en miroir
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=20
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbrLignes = int(input())
for i in range(nbrLignes):
   chaine = input()
   chaineInverse = ""
   for i in chaine:
        chaineInverse = i + chaineInverse
   print(chaineInverse)