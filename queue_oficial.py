from collections import deque
class queue:
    def testing_2(ex):
        ex = deque([])
        u=int(input('digite a quantidade de itens: '))
        for i in range(u):
            i=input('digite o elemento que vamos adicionar na fila: ')
            ex.append(i)
            print(ex)
        for z in range(u):
            print('valor que foi removido do começo: ', ex.popleft())
            print(ex)