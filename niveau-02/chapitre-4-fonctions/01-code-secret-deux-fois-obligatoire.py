
##################################
# fichier 01-code-secret-deux-fois-obligatoire.py
# nom de l'exercice : Code secret deux fois
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=1
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

# J'ai pas réellement fait ce qui est demandé mais ça marche aussi. ^^
def codeSecret():
   """Fonction qui demande un code secret, le lit et le retourne au
    programme."""
   
   codeS = int(input("Entrez le code :\n"))
   return codeS

#corps du programme
indice = 0 #indice de référence du nombre d'entrée(s) juste(s)
while 1:
    leCode = codeSecret()
    if leCode == 4242 and indice == 0:  #après une seule entrée juste
       print("Encore une fois.")
       indice = 1   #change l'indice de référence
    elif leCode == 4242 and indice == 1:    #avec la deuxième entrée juste
        print("Bravo.")
        break   #on sort de la boucle
   