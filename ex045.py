import random
import time
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Jogo Jokenpô')
print('-=' * 20, '{}'.format(cores['limpa']))
print('''Escolha:
0 - Pedra
1 - Papel
2 - Tesoura
''')
jogador = int(input('Digite sua escolha: '))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(0,2)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PÔ')
time.sleep(1)
if jogador > 2:
    print('Escolha Inválida. Tente novamente!')
elif jogador == 0 and pc == 2:
    print('{}Você escolheu {} e o computador escolheu {}. Você venceu!{}'
          .format(cores['verde'], lista[jogador], lista[pc], cores['limpa']))
elif jogador == 1 and pc == 0:
    print('{}Você escolheu {} e o computador escolheu {}. Você venceu!{}'
          .format(cores['verde'], lista[jogador], lista[pc], cores['limpa']))
elif jogador == 2 and pc == 1:
    print('{}Você escolheu {} e o computador escolheu {}. Você venceu!{}'
          .format(cores['verde'], lista[jogador], lista[pc], cores['limpa']))
elif jogador == pc:
    print('{}Você escolheu {} o computador escolheu {}. Houve empate, tente novamente!{}'
          .format(cores['amarelo'], lista[jogador], lista[pc], cores['limpa']))
else:
    print('{}Você escolheu {} o computador escolheu {}. Você perdeu!{}'
          .format(cores['vermelho'], lista[jogador], lista[pc], cores['limpa']))
print('FIM')
