cores = {'limpa': '\033[m',
         'azul': '\033[1;34m', }
print('{}-='.format(cores['azul']) * 20)
print('FATORAÇÃO')
print('-=' * 20, '{}'.format(cores['limpa']))
num = int(input('Digite um número: '))
print('A fatoração de {}!'.format(num), end='')
fat = num
while num != 1:
       fat *= num - 1
       num -= 1
print(' é {}.'.format(fat))
print('FIM')
