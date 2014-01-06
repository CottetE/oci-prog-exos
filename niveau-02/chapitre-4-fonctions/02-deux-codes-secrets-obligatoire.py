
##################################
# fichier 02-deux-codes-secrets-obligatoire.py
# nom de l'exercice : Deux codes secrets
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=3
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

# J'ai repris le code du premier de franceIOI pour partir 
# sur de bonnes bases.
def lireCode(indice):
    tentative = indice #indice = 0 au pour le premier code et 1 pour le deuxième code
    codeS = 0
    if tentative == 0:
        while codeS != 4242: #boucle pour le premier code
            print("Entrez le code :")
            codeS = int(input())
    elif tentative == 1:    #boucle pour le second code
        while codeS != 2121:
            print("Entrez le code :")
            codeS = int(input())
       
lireCode(0)
print("Premier code bon.")
lireCode(1)
print("Bravo.")