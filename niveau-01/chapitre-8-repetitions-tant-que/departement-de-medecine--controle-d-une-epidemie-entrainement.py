##################################
# fichier departement-de-medecine--controle-d-une-epidemie-entrainement.py
# nom de l'exercice :  Département de médecine : contrôle d'une épidémie
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=1
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
population=int(input())
malade=0
x=0
while malade<population:
    malade=3**x
    x+=1
print(x)

