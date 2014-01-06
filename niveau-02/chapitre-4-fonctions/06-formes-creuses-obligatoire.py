
##################################
# fichier 06-formes-creuses-obligatoire.py
# nom de l'exercice : Formes creuses
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=13
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

def rectangle(ligne,colonne):
    """dessine un rectangle creux avec des '#'"""
    print('#'*colonne)
    if ligne == 1:
        print('\n')
        return
    if colonne == 1:
       for i in range(ligne-2):
          print('#')
    else:
       for i in range(ligne-2):
           print('#'+' '*(colonne-2)+'#')
    print('#'*colonne, end='\n\n')

def triangle(ligne):
    """dessine un triangle rectangle creux avec des '@'"""
    print('@')
    if ligne == 1:
        print('\n')
        return
    for i in range(ligne-2):
        print('@'+' ' * i +'@')
    print('@'*ligne, end='\n\n')

#corps du programme
ligne = int(input())        #ligne seule
rectangleL = int(input())   #ligne du rectangle
rectangleC = int(input())   #colonne du rectangle
triangleL = int(input())    #ligne triangle

print('X'*ligne, end='\n\n')
rectangle(rectangleL, rectangleC)
triangle(triangleL)