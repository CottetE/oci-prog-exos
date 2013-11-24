
##################################
# fichier 13-choix-des-emplacements-obligatoire.py
# nom de l'exercice : Choix des emplacements
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=18
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

nbrEmplace=int(input())
listeEmplace = nbrEmplace * ['0']

for i in range(nbrEmplace):
    numero=int(input())

    listeEmplace[numero]=i
    
for i in listeEmplace:
    print(i)