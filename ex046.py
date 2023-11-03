from time import sleep

cores = {'limpa': '\033[m',
         'azul': '\033[1;34m'}
print('{}-='.format(cores['azul']) * 20)
print('Contagem Regressiva')
print('-=' * 20, '{}'.format(cores['limpa']))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOM! BOOM! POOW! Feliz ano novo!')
