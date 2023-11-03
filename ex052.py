cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Número Primo')
print('-=' * 20, '{}'.format(cores['limpa']))
num = int(input('Digite um número: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        div += 1
if div == 2:
    print('O número {} é primo!'.format(num))
else:
    print('O número {} não é primo!'.format(num))
print('Fim')