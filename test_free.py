i=int(input("Digite um numero: "))
n='#'*i
s=len(n)
while i!=-1:
    semente=''+n[s-i:]
    print(semente)
    i-=1