import sys

def operations(o):
    for i in range(o):
        pos, nbr = map(int,sys.stdin.readline().split())
        liste[pos-1] += nbr
    print(*liste)


p = int(sys.stdin.readline())
liste = list(map(int,sys.stdin.readline().split()))
o = int(sys.stdin.readline())
operations(o)
