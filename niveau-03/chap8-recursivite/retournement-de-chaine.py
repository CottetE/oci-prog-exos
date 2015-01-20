texte = input()

def alenvers(t):
    print(t[0],end='')
    try:
        return alenvers(t[1:])
    except:
        return None

alenvers(texte[::-1])


#utiliser try et except c'est cool ! :D
#faire texte[::-1] c'est très flemmard par contre ^^