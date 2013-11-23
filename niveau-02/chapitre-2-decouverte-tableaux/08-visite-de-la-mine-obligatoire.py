
##################################
# fichier 08-visite-de-la-mine-obligatoire.py
# nom de l'exercice : Visite de la mine
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=11
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

nbrDepla=int(input())
liste=[]

for i in range(nbrDepla):
    liste= [int(input())] + liste
for i in liste:
    if i ==1:
        print(2)
    elif i ==2:
        print(1)
    elif i ==4:
        print(5)
    elif i ==5:
        print(4)
    else:
        print(3)
