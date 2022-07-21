def fatorial(n):
    if n==1:
        return n
    else:
        return fatorial(n-1)*n
i=int(input('digite um numero: '))
print(fatorial(i))