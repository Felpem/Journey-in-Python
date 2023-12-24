import os
texto = input('Insira o nome do arquivo:')
abrido = open(texto)

for linhas in abrido:
    linhas = linhas.upper()
    print(linhas.rstrip())