
##################################
# fichier 11-course-a-trois-jambes-obligatoire.py
# nom de l'exercice : Course à trois jambes
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=16
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

nbrPers=int(input())
liste=[]

for i in range(nbrPers):
    liste+=[int(input())]
liste.sort()
i=0
j=nbrPers -1
while i < nbrPers/2:
    print(liste[i], liste[j])
    i+=1
    j-=1