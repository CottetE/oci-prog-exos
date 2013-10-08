##################################
# fichier l-espion-est-demasque--validation.py
# nom de l'exercice :  L'espion est démasqué !
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=14
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
nbrPersonnes=int(input())
for i in range(nbrPersonnes):
    critere=0
    taille=int(input())
    age=int(input())
    masse=int(input())
    cheval=int(input())
    cheveux=int(input())
    if 178<=taille<=182:
        critere+=1
    if age>=34:
        critere+=1
    if masse<70:
        critere+=1
    if cheval==0:
        critere+=1
    if cheveux==1:
        critere+=1
    if critere==5:
        print("Très probable")
    elif 3<=critere<=4:
        print("Probable")
    elif critere==0:
        print("Impossible")
    else:
        print("Peu probable")

