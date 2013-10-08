##################################
# fichier departement-de-pedagogie--le-c-est-plus-c-est-moins--entrainement.py
# nom de l'exercice :  Département de pédagogie : le c'est plus, c'est moins !
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=5
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici
nbr=int(input())
essais=0
while 1:
    proposition=int(input())
    if proposition==nbr:
        essais+=1
        break
    elif proposition<nbr:
        print("c'est plus")
        essais+=1
    else:
        print("c'est moins")
        essais+=1
print("Nombre d'essais nécessaires :")
print(essais)

