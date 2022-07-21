#aqui eu importo a função que executa o print da variavel
from função_print import testing
#aqui eu importo a fila 
from queue_oficial import queue
#declaração de variaveis:
i=float(input('digite um numero: '))
t=str('desculpe, passou o limite de vezes em que podemos repetir tal processo')
#aqui será repetido a váriavel até ela alcançar o 10
while i<10:
    i+=1
    #aqui é a função print
    testing.local(i)
    #aqui é a fila
    queue.testing_2(None)
#aqui vai ser tratado as vezes em que i>=10
else:
    testing.local(t)