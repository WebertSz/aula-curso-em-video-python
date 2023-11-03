from random import randint
cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'
         }
print('{}-='.format(cores['azul']) * 20)
print('JOGO ADIVINHE O NÚMERO')
print('-=' * 20, '{}'.format(cores['limpa']))
pc = randint(1, 100)
cont = 0
jogador = 0
while pc != jogador:
    jogador = int(input('Adivinhe o número que o computador escolheu: '))
    if jogador != pc:
        if jogador < pc:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
        cont += 1
print('Você acertou! Você precisou de {} tentativas para vencer!'.format(cont + 1))
