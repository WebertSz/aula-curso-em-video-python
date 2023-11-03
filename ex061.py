cores = {'limpa': '\033[m',
         'azul': '\033[1;34m', }
print('{}-='.format(cores['azul']) * 20)
print('PROGRESSÃO ARITMÉTICA ex061 E P.A MELHORADA ex062')
print('-=' * 20, '{}'.format(cores['limpa']))
termo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))
cont = 0
cont2 = 1
while cont2 != 0:
    while cont < 10:
        print('{}... '.format(termo), end='')
        termo += razão
        cont += 1
        if cont == 10:
            print('Pausa')
            cont2 = int(input('\nQuer mostrar mais quantos termos? '))
            cont -= cont2
print('Fim')
