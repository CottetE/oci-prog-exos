def operation(n):
    for i in range(n):
        nbr, date = map(int,input().split())
        if nbr < 0:
           nbr = -nbr
        for j in range(nbr):
            if date == 0:
                del(pile[-1])
            else:
                pile.append(date)
                
    print(min(pile))       #merci à Simon

pile = []
n = int(input())
operation(n)

#si j'avais bien lui ce qui suit:

#Quand Gérard renouvelle son stock, il n'a en général pas beaucoup de temps et 
#place les nouveaux produits juste au dessus de ceux qui sont déjà en rayon.

#je n'aurais pas pris 3h pour cet exercice...