print("------------------------")
print("   Colégio PIKA molis   ")
print("------------------------")
quant = int(input("Digite a quantidade de alunos: "))
maiornt = 0

while quant >= 1:
    aluno = str(input("Nome Do Aluno: "))
    nota = int(input("Nota Do Aluno: "))
    print('----------------------')
    quant = quant - 1

    if nota > maiornt:
        maiornt = nota
        melhoraluno = aluno

print("O aluno com melhor aproveitamento foi", melhoraluno, 'com a nota', maiornt)
