cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Soma de Números Pares')
print('-=' * 20, '{}'.format(cores['limpa']))
s = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
print('A soma de todos os números pares foi {}'.format(s))
print('Fim')