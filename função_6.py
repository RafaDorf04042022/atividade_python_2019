def func_6(matriz, arquivo):
    variavel_controle=0
    arquivo=open('lista_de_compras.txt','w')
    while variavel_controle<len(matriz):
        variavel_controle_elemento=0
        while variavel_controle_elemento<3:
            variavel_elemento=matriz[variavel_controle]
            arquivo.write(str(variavel_elemento[variavel_controle_elemento]))
            variavel_controle_elemento+=1
        variavel_controle+=1