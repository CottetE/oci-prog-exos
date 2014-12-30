import sys

def operation(n):
    for i in range(n):
        nbr, date = map(int,sys.stdin.readline().split())
        if nbr < 0:
           nbr = -nbr
        for j in range(nbr):
            if date == 0:
                del(pile[0])    # la différence majeure avec 'date-de-peremption'
            else:
                pile.append(date)
                
    print(min(pile))

pile = []
n = int(sys.stdin.readline())
operation(n)

#c'est quand même bcp plus rapide avec sys !