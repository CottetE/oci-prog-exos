##################################
# fichier nombre-de-jours-dans-le-mois-validation.py
# nom de l'exercice :  Nombre de jours dans le mois
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=4
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici
mois=int(input())
if 1<=mois<=3 or 7<=mois<=9:
    print(30)
elif mois==11:
    print(29)
else:
    print(31)

