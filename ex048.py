cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Soma Números Ímpares de 1 a 500')
print('-=' * 20, '{}'.format(cores['limpa']))
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print('A soma de todos os valores é {}!'.format(s))
print('Fim')