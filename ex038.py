cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul'])*20)
print('Maior e Menor Número')
print('-='*20, '{}'.format(cores['limpa']))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('{}O número {} é o maior e o número {} é o menor!{}'
          .format(cores['verde'], num1, num2, cores['limpa']))
elif num1 < num2:
    print('{}O número {} é o maior e o número {} é o menor!{}'
          .format(cores['vermelho'], num2, num1, cores['limpa']))
else:
    print('{}Os dois número são iguais!{}'.format(cores['amarelo'], cores['limpa']))
