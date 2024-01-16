"""CALCULADORA"""
import math

## FUNÇÃO PARA A SOMA / FUNCTION FOR SUM ##
def adicao():
    print("================")
    prim = input("Primeiro Valor: ")
    print("================")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    print("================")
    segun= int(segun)
    print("----------------------------")
    result = print("O resultado de", prim, '+', segun, 'é', prim+segun)
    print("----------------------------")
    return result

## FUNÇÃO PARA SUBTRAÇÃO / FUNCTION FOR SUBTRACTION ##
def subtracao():
    print("================")
    prim = input("Primeiro Valor: ")
    print("================")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    print("================")
    segun= int(segun)
    print("----------------------------")
    result = print("O resultado de", prim, '-', segun, 'é', prim-segun)
    print("----------------------------")
    return result

## FUNÇÃO PARA MULTIPLICAÇÃO / FUNCTION FOR MULTIPLICATION ##
def multiplicacao():
    print("================")
    prim = input("Primeiro Valor: ")
    print("================")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    print("================")
    segun= int(segun)
    print("----------------------------")
    result = print("O resultado de", prim, 'x', segun, 'é', prim * segun)
    print("----------------------------")
    return result

## FUNÇÃO PARA DIVISÃO / FUNCTION FOR DIVISION ##
def divisao():
    print("================")
    prim = input("Primeiro Valor: ")
    print("================")
    prim = int(prim)
    segun = input("Segundo Valor: ")
    print("================")
    segun= int(segun)
    print("----------------------------")
    result = print("O resultado de", prim, '÷', segun, 'é', prim/segun)
    print("----------------------------")
    return result

## FUNÇÃO PARA RAIZES / FUNCTION FOR ROOTS ##
def raizes():
    while True:
        print("========================")
        raiz = input("Digite o valor da Raiz: ")
        print("========================")
        raiz = int(raiz)
        if raiz < 0:
                 print("INVALÍDO! Digite numeros acima de 0")
                 quit()
        else:
                raizfinal = math.sqrt(raiz)
                print("----------------------------")
                result = print("O valor da Raiz de", raiz, "é igual a", raizfinal)
                print("----------------------------")
        return result     
         
## FUNÇÃO PARA POTÊNCIA / FUNCTION FOR POWER ##          
def potencia():
    print("================")
    base = input("Digite o valor da Base: ")
    print("================")
    base = int(base)
    expoente = input("Digite o valor do Expoente: ")
    print("================")
    expoente = int(expoente)
    print("----------------------------")
    result = print("O valor da potência de", base, "*",expoente, "é", base**expoente) 
    print("----------------------------")
    return result 


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
        print("Encerrado!! :)")
        break
