"""CALCULADORA"""

import math

def adicao():
    prim = input("Primeiro Valor: ")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    segun= int(segun)
    result = print("O resultado de", prim, '+', segun, 'é', prim+segun)
    return result
def subtracao():
    prim = input("Primeiro Valor: ")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    segun= int(segun)
    result = print("O resultado de", prim, '-', segun, 'é', prim-segun)
    return result
def multiplicacao():
    prim = input("Primeiro Valor: ")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    segun= int(segun)
    result = print("O resultado de", prim, 'x', segun, 'é', prim * segun)
    return result
def divisao():
    prim = input("Primeiro Valor: ")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    segun= int(segun)
    result = print("O resultado de", prim, '÷', segun, 'é', prim/segun)
    return result
def raizes():
    while True:
        raiz = input("Digite o valor da Raiz: ")
        raiz = int(raiz)
        if raiz < 0:
                 print("INVALÍDO! Digite numeros acima de 0")
                 quit()
        else:
                raizfinal = math.sqrt(raiz)
                result = print("O valor da Raiz de", raiz, "é igual a", raizfinal)
        return result     

            
            
def potencia():
    base = input("Digite o valor da Base: ")
    base = int(base)
    expoente = input("Digite o valor do Expoente: ")
    expoente = int(expoente)
    result = print("O valor da potência de", base, "*",expoente, "é", base**expoente)  


while True:
    print("============================")
    print("|    SUPER CALCULADORA     |")
    print("============================")

    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Raiz Quadrada")
    print("[6] Potênciação")
    print("[7] SAIR")
    print('----------------------------')
    opcao = input("Escolha uma operação para fazer: ")
    
    if opcao == "1":
        adicao()
    elif opcao == '2':
        subtracao()
    elif opcao == '3':
        multiplicacao()
    elif opcao == '4':
        divisao()
    elif opcao == "5":
        raizes()
    elif opcao == "6":
        potencia()
    elif opcao == "7":
        break