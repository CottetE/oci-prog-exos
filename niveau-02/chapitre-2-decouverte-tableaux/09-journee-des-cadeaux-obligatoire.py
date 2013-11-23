
##################################
# fichier 09-journee-des-cadeaux-obligatoire.py
# nom de l'exercice : Journée des cadeaux
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=14
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbrHabit=int(input())
fortune=[]

for i in range(nbrHabit):
    fortune+=[int(input())]
fortune.sort()

if nbrHabit%2 != 0:
    print(int(fortune[int(nbrHabit/2)]))
else:
    valeur=(fortune[int(nbrHabit/2)-1]+fortune[int(nbrHabit/2)])/2
    print(valeur)
