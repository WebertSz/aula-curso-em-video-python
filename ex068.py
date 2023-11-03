from random import randint
from time import sleep

cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m'}
print(f'{cores["azul"]}-=' * 20)
print('JOGO PAR OU ÍMPAR - BREAK')
print('-=' * 20, f'{cores["limpa"]}')
cont = 0
while True:
    while True:
        print('[1]PAR\n[2]ÍMPAR')
        escolha = int(input('Escolha: '))
        if escolha == 1:
            print('Você escolheu PAR, o computador é ÍMPAR.')
            break
        elif escolha == 2:
            print('Você escolheu ÍMPAR e o computador é PAR.')
            break
        else:
            print(f'{cores["vermelho"]}Inválido. Escolha novamente.{cores["limpa"]}')
    num = int(input('escolha um número de 0 à 10: '))
    print(f'Você escolheu {num}')
    pc = randint(0, 10)
    print('O computador está escolhendo...')
    sleep(1)
    print(f'O computador escolheu {pc}')
    soma = num + pc
    if escolha == 1 and soma % 2 == 0:
        print(f'{soma} é PAR. Você venceu!')
        cont += 1
    elif escolha == 1 and soma % 2 != 0:
        print(f'{soma} é ÍMPAR. Você perdeu!')
        break
    elif escolha == 2 and soma % 2 != 0:
        print(f'{soma} é ÍMPAR. Você venceu!')
        cont += 1
    else:
        print(f'{soma} é PAR. Você perdeu!')
        break
if cont == 0:
    print('Você não venceu nenhuma vez!')
else:
    print(f'Você venceu {cont} seguida(s)!')
print('Tente novamente!')
