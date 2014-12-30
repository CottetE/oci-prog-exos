def toto(a, n):
    if n != 0:
        return toto('({0} + {0})'.format(a), n-1)
    else:
        print(a)


n = int(input())
a = '0'
print('0 = ',end='')
toto(a, n)
