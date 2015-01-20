n,m = map(int,input().split())

def entre2(n,m):
    if n == m:
       print(n)
    else:
       print(n,end=' ')
       return entre2(n+1,m)

entre2(n,m)