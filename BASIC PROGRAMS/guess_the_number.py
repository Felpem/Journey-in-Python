from random import randint
print("========================")
print("| GUESS THE NUMBER 1.0 |")
print("========================")
placar = 0
tent = 0
while True:
	rdm = int(randint(1,100))
	print()
	dnv = input("Vamos Começar? [S]/[N] ")
	if dnv == "N" or dnv == "n":
		print("O seu placar foi", placar)
		print("Quem sabe mais tarde...Até :)")
		break
	else:
		while True:
			try:
				inpt = input("Digite um valor entre 1 e 100: ")
				num = int(inpt)
			except:
				print("ERRO! DIGITE UM VALOR NUMERICO.")
				continue
			if num < rdm:
				mensagem=print("Mais alto")
				tent = tent + 1
			elif num > rdm:
				mensagem=print("Mais baixo")
				tent = tent + 1
			elif num == rdm:
				mensagem1=print("Você acertou! Parabens e foi em", tent, "tentativas")
				placar = placar + 1
				tent = 0
				break