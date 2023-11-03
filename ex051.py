cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Progressão Aritmética')
print('-=' * 20, '{}'.format(cores['limpa']))
termo = int(input('Digite o 1º termo da Progressão Aritmética: '))
r = int(input('Digite a razão da Progressão Aritmética: '))
for c in range(1, 11):
    print(termo)
    termo += + r
print('Fim')