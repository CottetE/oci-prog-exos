{"filter":false,"title":"carte-caverne.py","tooltip":"/niveau-03/chap9-balayage-structure-elementaire/carte-caverne.py","undoManager":{"mark":15,"position":15,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["# carte de la caverne frioi...","","class Carte():","    def __init__(self):","        self.nbr = 0","        self.elements = []","","    def vide(self):","        return self.nbr == 0 #return True si = 0 !","","    def empiler(self,k):","        self.elements.append(k)","        self.nbr += 1","","    def depiler(self):","        del self.elements[-1]","        self.nbr -= 1","","caverne = Carte()","nbChar = int(input())","plan = input()","","def check():","    for i in plan:    ","        if i =='(':","            caverne.empiler(0) #le 0 est arbitraire","        elif i == ')':","            try:","                caverne.depiler()","            except:","                return False","        else:","            continue","","    if caverne.vide():","        return True","    else:","        return False","   ","if check():","    print(1)","else:","    print(0)","","","","# Ca marche !!!!!!!!!!!!!!!","",""]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"remove","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"remove","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["d"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":39},"end":{"row":0,"column":39},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1421793340505,"hash":"934e8d445c07fa339e4ea190b0f1712c6f4dbd4e"}