cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Números Pares de 1 a 50')
print('-=' * 20, '{}'.format(cores['limpa']))
for c in range(2, 51, 2):
    print(c)
print('Fim')