cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Tabuada')
print('-=' * 20, '{}'.format(cores['limpa']))
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{:2} * {:2} = {:2}'.format(num, c, num * c))
print('Fim')