def fonction(n,c):
    if c != 0:
        return fonction('[{}]'.format(n), c-1)
    else:
        print(n)

n, c = input().split()
fonction(n,int(c))
