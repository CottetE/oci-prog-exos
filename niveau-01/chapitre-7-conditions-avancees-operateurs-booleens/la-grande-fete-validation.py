##################################
# fichier la-grande-fete-validation.py
# nom de l'exercice :  La grande fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=11
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
datemin=int(input())
datemax=int(input())
nbrinvite=int(input())
a=0
for i in range(nbrinvite):
    date1=int(input())
    date2=int(input())
    if datemin<=date1<=datemax or datemin<=date2<=datemax:
        a+=1
    elif date1<=datemin<=date2 or date1<=datemax<=date2:
        a+=1
print(a)
