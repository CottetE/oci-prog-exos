##################################
# fichier bonus--casernes-de-pompiers-validation.py
# nom de l'exercice :  Bonus : Casernes de pompiers
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=7
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
nbrpaires=int(input())
for i in range(nbrpaires):
    absmin1=int(input())
    absmax1=int(input())
    ordmin1=int(input())
    ordmax1=int(input())
    absmin2=int(input())
    absmax2=int(input())
    ordmin2=int(input())
    ordmax2=int(input())

    if absmax1<=absmin2 or absmax2<=absmin1:
        print("NON")
    elif absmin1>=absmax2 or absmin2>=absmax1:
        print("NON")
    elif ordmax1<=ordmin2 or ordmax2<=ordmin1:
        print("NON")
    elif ordmin1>=ordmax2 or ordmin2>=ordmax1:
        print("NON")
    else:
        print("OUI")
