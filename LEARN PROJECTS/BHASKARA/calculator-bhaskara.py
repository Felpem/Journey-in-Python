import math
print('Calculadora de Bhaskara')
print('--------------------')
valorA = input('Digite o Valor de A: ')
valorB = input('Digite o Valor de B: ')
valorC = input('Digite o Valor de C: ')

a = int(valorA)
b = int(valorB)
c = int(valorC)

delta = (b**2) - 4 * a * c
delta = float(delta)
if delta < 0:
    print("--------------------")
    print('Numero negativo não tem Raiz:', '\nDelta igual a:', delta)
    quit('Programa Encerrado')
raiz1 = -(b) + math.sqrt(delta)
raiz2 = -(b) - math.sqrt(delta)
bhaskara1 = raiz1 / (2 * a)
bhaskara2 = raiz2 / (2 * a)
print("--------------------")
print('O valor de Delta é:', delta, '\nX¹ é:', bhaskara1, '\nX² é:', bhaskara2 )
print("--------------------")
