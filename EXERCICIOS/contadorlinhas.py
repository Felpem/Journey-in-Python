
pedido = input('Informe o nome do arquivo:')
try:
    arquivo = open(pedido)
except:
    print('O arquivo',pedido, 'não foi encontrado' )
    quit()
contador = 0
soma = 0
for linha in arquivo:
    if linha.startswith('X-DSPAM-Confidence:'):
        contador = contador + 1
        valor = float(linha.split(':')[1].strip())
        soma += valor
        media = soma / contador
    continue
print('Average spam confidence:', media)


