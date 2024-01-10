mensagem= input('Escolha um numero entre 0.0 e 1.0, use o .(ponto):')
nota= float(mensagem)

if nota > 1:
    print('nota invalida')

elif nota >= 0.9:
    print('nota: A')

elif nota >= 0.8:
    print('nota: B')

elif nota >= 0.7:
    print('nota: C')

elif nota >= 0.6:   
    print('nota: D')

elif nota < 0.6:
    print('nota: F')


