##################################
# fichier departement-de-chimie--melange-explosif-validation.py
# nom de l'exercice :  Département de chimie : mélange explosif
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=7
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
nbrMesures=int(input())
tempMin=int(input())
tempMax=int(input())
i=0
while i<nbrMesures:
    temperature=int(input())
    if tempMin<=temperature<=tempMax:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break
    i+=1

