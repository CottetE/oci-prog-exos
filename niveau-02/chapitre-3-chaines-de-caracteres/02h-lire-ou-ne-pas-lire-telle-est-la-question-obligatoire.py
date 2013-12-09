
##################################
# fichier 02h-lire-ou-ne-pas-lire-telle-est-la-question-obligatoire.py
# nom de l'exercice : Lire ou ne pas lire, telle est la question
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=10
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

nbrLivre = int(input())
livreLu = ''

for i in range(nbrLivre):
    livre = input()
    if len(livre) > len(livreLu):
        print(livre)
        livreLu = livre