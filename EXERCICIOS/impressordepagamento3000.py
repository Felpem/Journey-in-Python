horas= input('Escreva as horas trabalhadas:')
try:
    hs= float(horas)
except:
    print('Valor invalido, apenas numeros :)')
    quit()

valorphr= input('Escreva a valor das horas:')
try:
    vlhr= float(valorphr)
except:
    print('Valor invalido, apenas numeros :)')
    quit()

if hs <= 40:
    print(hs*vlhr)
elif hs > 40:
    print(40 * vlhr + ((1.5 * vlhr) * (hs - 40)))