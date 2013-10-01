##################################
# fichier zones-de-couleurs-validation.py
# nom de l'exercice :  Zones de couleurs
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=15
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
nbrjoueur=int(input())
for i in range(nbrjoueur):
    jX=int(input())
    jY=int(input())

    if (jX<0 or jX>90)or (jY<0 or jY>70):
        print("En dehors de la feuille")
    elif (15<jX<45 and 60<jY<70)or(60<jX<85 and 60<jY<70):
        print("Dans une zone rouge")
    elif (10<jX<85 and 10<jY<55 )and not (25<jX<50 and 20<jY<45):
        print("Dans une zone bleue")
    else:
        print("Dans une zone jaune")
