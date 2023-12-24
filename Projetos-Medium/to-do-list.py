lista = []

def add_tarefa():
    tarefa = input('Digite uma tarefa:')
    lista.append({'tarefa': tarefa, 'concluida': False})
    print('Tarefa adicionada com sucesso!')
add_tarefa()

def numerador():
    print('Sua Lista:')
    for i, tarefa in enumerate(lista, 1):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f'{i}. {status} {tarefa['tarefa']}')
numerador()

def chekador():
    numerador()
    numerotask = int(input('Digite o numero da tarefa concluida:'))
    if 1 <= len(lista):
        lista[numerotask - 1]['concluida'] = True
        print('Tarefa Completa!')
    else:
        print('Tarefa Invalida')

while True:
    print('\nEscolha uma opção:\n')
    print('Adicionar tarefa: Digite 1')
    print('Listar tarefas: Digite 2')
    print('Marcar tarefa como CONCLUIDA: Digite 3')
    print('Sair: Digite 4')

    option = input('Escolha uma Opção:')

    if option == '1':
        add_tarefa()
    elif option == '2':
        numerador()
    elif option == '3':
        chekador()
    elif option == '4':
        break