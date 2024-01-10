sexo= input('Você é homem ou mulher?\n')
h= input('Qual a sua altura?\nex: 1.80, 1.75\n')
try:
    ih= float(h)

except:
    print('INVALIDO!')
try:
    if sexo == 'homem':
        print((72.7*ih) - 58)

    elif sexo == 'mulher':
        print((62.1*ih) - 44.7)
    
except:
    print('INVALIDO')
    