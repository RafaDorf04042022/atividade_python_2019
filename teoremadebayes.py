#esse algoritmo vai calcular quais vão ser a possibilidade de ocorrer um evento em relação ao evento anterior
#vai basear-se principalmente no teoremas de Bayes
#parte 1: Variaveis
#obs:
print('digite o valor como o valor da porcentagem dividido por 100')
#população
porcentagem_na_populacao=float(input('digite a porcentagem do evento em determinada população: '))
#ocorrência
porcentagem_em_a=float(input('digite a probabilidade do evento A ocorrer: '))
porcentagem_em_b=float(input('digite a probabilidade do evento B ocorrer: '))
teorema_de_bayes=float
#será determinado qual condição vai ser tomada como primeira condição dentro da população, se vai ser A ou B
condicional=bool(input('se A for o evento, digite True, se não, digite False: '))
#parte 2: Condições
#condição em que A é tido como primeira população
if condicional==True:
    teorema_de_bayes=((porcentagem_na_populacao*porcentagem_em_a)/porcentagem_em_b)*100
    print('essa é a probabilidade do evento ocorrer em relação ao anterior: ', teorema_de_bayes,'%')
#condição em que B é tido como primeira população
if condicional==False:
    teorema_de_bayes=((porcentagem_na_populacao*porcentagem_em_b)/porcentagem_em_a)*100
    print('essa é a probabilidade do evento ocorrer em relação ao anterior: ', teorema_de_bayes,'%')