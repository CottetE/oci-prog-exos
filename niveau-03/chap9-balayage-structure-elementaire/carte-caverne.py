# carte de la caverne frioi par Emerald

class Carte():
    def __init__(self):
        self.nbr = 0
        self.elements = []

    def vide(self):
        return self.nbr == 0 #return True si = 0 !

    def empiler(self,k):
        self.elements.append(k)
        self.nbr += 1

    def depiler(self):
        del self.elements[-1]
        self.nbr -= 1

caverne = Carte()
nbChar = int(input())
plan = input()

def check():
    for i in plan:    
        if i =='(':
            caverne.empiler(0) #le 0 est arbitraire
        elif i == ')':
            try:
                caverne.depiler()
            except:
                return False
        else:
            continue

    if caverne.vide():
        return True
    else:
        return False
   
if check():
    print(1)
else:
    print(0)



# Ca marche !!!!!!!!!!!!!!!

