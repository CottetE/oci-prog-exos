##################################
# fichier amitie-entre-gardes-validation.py
# nom de l'exercice :  Amitié entre gardes
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=5
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
soldat1=int(input())
soldat2=int(input())
soldat3=int(input())
soldat4=int(input())
if soldat1<=soldat3<=soldat2 or soldat3<=soldat2<=soldat4 or soldat1<=soldat4<=soldat2 or soldat3<=soldat1<=soldat4:
    print("Amis")
else:
    print("Pas amis")

