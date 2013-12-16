
##################################
# fichier 04f-ngms-sns-vlls-obligatoire.py
# nom de l'exercice : ngms sns vlls
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=23
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

titre = input()
nom = input()
consonneTitre = ''
consonneNom = ''
for i in titre:
   if i not in 'AEIOUY ':
      consonneTitre += i
print(consonneTitre)
for i in nom:
   if i not in 'AEIOUY ':
      consonneNom += i
print(consonneNom)