maior= None
menor= None
looping= True

while looping:
    numero= input("Digite um numero ou 'pronto' para finalizar:")
    if numero == "done":
        break
    else:
        try:
            numeros= int(numero)
            if maior is None or numeros > maior:
                maior = numeros
            if menor is None or numeros < menor:
                menor = numeros
        except:
            print('ENTRADAS INVALIDAS, DIGITE "DONE" OU UM NUMERO.')

print('Concluído')
print('Maximum:', maior)
print('Minimum:', menor)