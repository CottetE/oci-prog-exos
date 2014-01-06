
##################################
# fichier 03-deux-rectangles-obligatoire.py
# nom de l'exercice : Deux rectangles
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=5
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

def rectangle(forme,ligne,colonne):
    """fonction qui construit un rectangle avec
    la forme qui apparait nbr colonnes par nbr lignes.
    forme -> str / ligne -> int / colonne -> int """

    forme = forme
    ligne = ligne
    colonne = colonne
    for i in range(ligne):
        print(forme * colonne)

#corps du programme
rectangle('X',4,10)
rectangle('O',6,5)