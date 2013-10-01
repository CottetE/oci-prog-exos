##################################
# fichier espion-etranger-validation.py
# nom de l'exercice :  Espion étranger
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=1
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
dateavant=int(input())
dateapres=int(input())
nbrspy=int(input())
x=0
for i in range(nbrspy):
    spy=int(input())
    if dateavant<=spy<=dateapres:
        x+=1
print(x)
