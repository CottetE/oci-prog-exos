##################################
# fichier nombre-de-personnes-a-la-fete-validation.py
# nom de l'exercice :  Nombre de personnes à la fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=6
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
nbrpersonne=int(input())
x=[]
k=0
for i in range(nbrpersonne*2):
    gars=int(input())
    if gars>0:
        x+=[gars]
        if len(x)>k:
            k=len(x)
    else:
        x.remove(-gars)
print(k)

