
##################################
# fichier 03d-analyse-de-frequence-obligatoire.py
# nom de l'exercice : Analyse de fréquence
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=16
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules

#oui mon code est très très moooooooche !!!!!! ;)

# mettre votre code ici

nbrLigne, nbrMot = map(int, input().split())
listeMots = []
listeLongueurMot = []

for i in range(nbrLigne):
    ligne = input().split()
    for i in ligne:
        listeMots += [i]
    
for i in listeMots:
    listeLongueurMot += [len(i)]
    
listeLongueurMot.append(110) #ajout d'une valeur max pour la bon fonctionnement de la fin
listeLongueurMot.sort()

indice = listeLongueurMot[0]
for i in listeLongueurMot:
     if indice == 110:
        indice = 1000
     if i > indice:
        print("{} : {}".format(indice, listeLongueurMot.count(indice)))
        indice = i