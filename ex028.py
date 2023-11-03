import random
import time

nome = (input('Entre com seu nome: ')).upper().strip()
print('Bem vindo ao Jogo da Adivinhação!')
print('Computador pense em um número de 0 a 5: ')
print('Computador pensando...')
numpc : int = random.randint(0,5)
time.sleep(2)
num = int(input('{} adivinhe o número que o computador escolheu de 0 a 5: '.format(nome)))
if num == numpc:
    print('Resultado...')
    time.sleep(3)
    print('Parabéns {}! O número que o computador escolheu foi {} e você acertou!'.format(nome, numpc))
else:
    print('Resultado...')
    time.sleep(3)
    print('{} você errou, o número que o computador escolheu foi {}. Tente novamente!'.format(nome, numpc))
print('Fim do Jogo da Adivinhação!')
