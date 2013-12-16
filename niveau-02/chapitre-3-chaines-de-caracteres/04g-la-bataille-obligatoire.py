
##################################
# fichier 04g-la-bataille-obligatoire.py
# nom de l'exercice : La bataille
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=24
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

carteJoueur1 = input()
carteJoueur2 = input()
i = 0
while i < 52:
    if carteJoueur1[i] < carteJoueur2[i]:
        print(1)
        print(i)
        i = 52
    elif carteJoueur2[i] < carteJoueur1[i]:
        print(2)
        print(i)
        i = 52
    else:
        if len(carteJoueur1) - (i+1) == 0 or len(carteJoueur2) - (i+1) == 0:
            if len(carteJoueur1) == len(carteJoueur2):
                print('=')
                print(i + 1)
                i = 52
            elif len(carteJoueur1) > len(carteJoueur2):
                print(1)
                print(i + 1)
                i = 52
            elif len(carteJoueur1) < len(carteJoueur2):
                print(2)
                print(i + 1)
                i = 52
        else:
            i += 1