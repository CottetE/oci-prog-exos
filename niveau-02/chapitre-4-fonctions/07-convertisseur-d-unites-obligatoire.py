
##################################
# fichier 07-convertisseur-d-unites-obligatoire.py
# nom de l'exercice : Convertisseur d'unités
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=14
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

def degre(nbr):
    """converti nbr celsius en farenheit"""
    return str(32 + 1.8 * nbr)+' f'

def gramme(nbr):
    """converti nbr gramme en livres"""
    return str(nbr * 0.002205)+' l'

def metre(nbr):
    """converti nbr mètre en pied"""
    return str(nbr / 0.3048)+' p'

#corps du programme
nbrValeur = int(input())
for i  in range(nbrValeur):
    valeur = input().split()
    if valeur[1] == 'm':        #si on a des mètres
        print(metre(float(valeur[0])))
    elif valeur[1] == 'g':      #si on a des grammes
        print(gramme(float(valeur[0])))
    else:                       #si on a des degrés celsius
        print(degre(float(valeur[0])))
