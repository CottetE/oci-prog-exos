##################################
# fichier maison-de-l-espion-validation.py
# nom de l'exercice :  Maison de l'espion
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=2
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
absmin=int(input())
absmax=int(input())
ordmin=int(input())
ordmax=int(input())
nbrM=int(input())
x=0
for i in range(nbrM):
    maisonx=int(input())
    maisony=int(input())
    if absmin<=maisonx<=absmax and ordmin<=maisony<=ordmax:
        x+=1
print(x)

