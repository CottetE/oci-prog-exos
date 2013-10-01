##################################
# fichier personne-disparue-validation.py
# nom de l'exercice :  Personne disparue
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=9
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
chercher=int(input())
tailleliste=int(input())
a=[]
for i in range(tailleliste):
    nbr=int(input())
    a+=[nbr]
if chercher in a:
    print("Sorti de la ville")
else:
    print("Encore dans la ville")

