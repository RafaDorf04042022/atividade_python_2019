
def delta(a,b,c):
  return  (b**2)-4*a*c


def baskara(a,b,c):
  if a == 0 or delta(a,b,c) < 0:
    print(delta(a,b,c))
    print('Impossivel calcular.')
  else:
    x1 = (-b + (delta(a,b,c)**0.5)) / (2 * a)
    x2 = (-b - (delta(a,b,c)**0.5)) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')


a=float(input('Digite o valor de a: '))
b=float(input('Digite o valor de b: '))
c=float(input('Digite o valor de c: '))

baskara(a,b,c)