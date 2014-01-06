
##################################
# fichier 04-fonction-min-obligatoire.py
# nom de l'exercice : Fonction min
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=7
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

#fonction mini et pas min car min et déjà utilisé par python !
def mini(entier1, entier2):
    """fonction qui prend 2 entiers en paramètre et
    renvoie le plus petit des deux."""

    if entier1 > entier2:
        return entier2
    else:
        return entier1

#coprs du programme
liste = [0,1,2,3,4,5,6,7,8,9]   #une liste de base "pseudo-quelconque"
for i in liste:
    liste[i] = int(input())     #actualisation de la liste
    
minimum = 1000  #minimum de base très grand pour éviter d'avoir un minim plus petit que le vrai minimum
for nbr in liste:
    var = mini(minimum,nbr)
    if var == minimum:
        minimum = var   #actualistation du minimum
    else:
        minimum = nbr   #actualistation du minimum
        
print(minimum)